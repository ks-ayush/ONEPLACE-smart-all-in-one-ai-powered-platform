from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from sentence_transformers import SentenceTransformer
from qdrant_client import QdrantClient
import requests
import cohere
import os
from dotenv import load_dotenv

load_dotenv()

router = APIRouter()

QDRANT_URL = os.getenv("QDRANT_URL")
QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")
HF_API_KEY = os.getenv("HF_API_KEY")
co = cohere.Client(os.getenv("COHERE_API_KEY"))

COLLECTION = "products"
MODEL_NAME = "microsoft/phi-3-mini-4k-instruct"
# MODEL_NAME = "tiiuae/falcon-7b-instruct"  
# MODEL_NAME = "HuggingFaceH4/zephyr-7b-beta"
# MODEL_NAME = "mistralai/Mistral-7B-Instruct-v0.2"


client = QdrantClient(url=QDRANT_URL, api_key=QDRANT_API_KEY)
model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')


class SearchRequest(BaseModel):
    query: str


def generate_ai_message(user_query, products):
    """Generate a natural text response using Cohere Chat API (no markdown)."""
    if not products:
        return "No matching products found."

    context = "\n".join([
        f"{p['title']} ({p['store']}) - ₹{p['price_inr']}: {p['description']}. "
        for p in products
    ])

    prompt = f"""
You are a helpful online shopping assistant.

User asked: "{user_query}"

Here are the available products:
{context}

Write a short, conversational reply suggesting one or two top options.
Do not use markdown, bullet points, or emojis. Include product links directly in the text.
"""

    try:
        response = co.chat(
            model="command-r-plus-08-2024",  
            message=prompt,
            temperature=0.6,
            max_tokens=200,
        )
        return response.text.strip()
    except Exception as e:
        print("Cohere API error:", e)
        return "Sorry, I couldn’t generate a response right now."




@router.post("/search")
async def semantic_search(request: SearchRequest):
    query_vector = model.encode(request.query).tolist()

    try:
        results = client.search(
            collection_name=COLLECTION,
            query_vector=query_vector,
            limit=3,
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Search failed: {str(e)}")

    products = []
    for res in results:
        payload = res.payload
        products.append({
            "title": payload.get("title"),
            "brand": payload.get("brand"),
            "category": payload.get("category"),
            "price_inr": payload.get("price_inr"),
            "description": payload.get("description"),
            # "image_urls": payload.get("image_urls"),
            "image_url": (payload.get("image_urls") or [None])[0],
            "store": payload.get("store"),
            "product_url": payload.get("product_url")
        })

    ai_message = generate_ai_message(request.query, products)

    return {
        "query": request.query,
        "results": products,
        "ai_message": ai_message
    }
