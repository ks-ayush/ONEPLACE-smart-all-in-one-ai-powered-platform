from sentence_transformers import SentenceTransformer
from qdrant_client import QdrantClient
from qdrant_client.http.models import VectorParams, PointStruct
from dotenv import load_dotenv
import os


load_dotenv()
QDRANT_URL = os.getenv("QDRANT_URL")
QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")
COLLECTION = "products"

print("Products data preparation started...")

if not QDRANT_URL or not QDRANT_API_KEY:
    raise ValueError("Missing QDRANT_URL or QDRANT_API_KEY in .env file")

client = QdrantClient(url=QDRANT_URL, api_key=QDRANT_API_KEY)


model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

client.recreate_collection(
    collection_name=COLLECTION,
    vectors_config=VectorParams(size=384, distance="Cosine"),
)

products = [
    {
    "product_id": "P_001",
    "title": "Nike Air Zoom Pegasus 39 Running Shoes",
    "brand": "Nike",
    "category": "Shoes",
    "price_inr": 7000,
    "description": "Lightweight, breathable running shoes offering superior comfort and bounce for everyday runs.",
    "image_urls": ["https://assets.myntassets.com/w_412,q_30,dpr_3,fl_progressive,f_webp/assets/images/2025/JUNE/9/GEicOIwo_91c4e1a17e63482a8309a616034b4d44.jpg"],
    "store": "myntra",
    "product_url": ["https://www.myntra.com/sports-shoes/nike/nike-pegasus-39-mens-lace-ups-road-running-shoes/34806269/buy"]
  },
  {
    "product_id": "P_002",
    "title": "Adidas Classic White Sneakers",
    "brand": "Adidas",
    "category": "Shoes",
    "price_inr": 2599,
    "description": "Stylish and durable white sneakers that go well with jeans or joggers for daily casual wear.",
    "image_urls": ["https://assets.adidas.com/images/w_383,h_383,f_auto,q_auto,fl_lossy,c_fill,g_auto/e4f8e3b37bd34d63815e159088d6b61e_9366/samba-og-shoes.jpg"],
    "store": "myntra",
    "product_url": ["https://www.myntra.com/adidas-white-shoes"]
  },
  {
    "product_id": "P_003",
    "title": "HRX by Hrithik Roshan Cotton T-Shirt",
    "brand": "HRX",
    "category": "T-Shirts",
    "price_inr": 799,
    "description": "Soft, sweat-wicking cotton T-shirt designed for comfort and performance.",
    "image_urls": ["https://assets.myntassets.com/w_412,q_30,dpr_3,fl_progressive,f_webp/assets/images/26666878/2023/12/29/54159f6f-a596-4ec4-bd8b-581f1f332fe21703829981990-HRX-by-Hrithik-Roshan-White-HRX-FIGHTER-Lifestyle-Tshirts-86-1.jpg"],
    "store": "myntra",
    "product_url": ["https://www.myntra.com/hrx-tshirts"]
  },
  {
    "product_id": "P_004",
    "title": "Levi's Regular Fit Blue Jeans",
    "brand": "Levi's",
    "category": "Jeans",
    "price_inr": 2899,
    "description": "Classic mid-rise blue denim jeans with durable stretch fabric and a modern fit.",
    "image_urls": ["https://lsco.scene7.com/is/image/lsco/005054834-detail1-pdp?fmt=jpeg&qlt=70&resMode=sharp2&fit=crop,1&op_usm=0.6,0.6,8&wid=2000&hei=2500"],
    "store": "myntra",
    "product_url": ["https://www.myntra.com/levis-regular-fit-jeans"]
  },
  {
    "product_id": "P_005",
    "title": "Allen Solly Formal Shirt",
    "brand": "Allen Solly",
    "category": "Shirts",
    "price_inr": 1799,
    "description": "Premium cotton blend shirt suitable for office and formal occasions.",
    "image_urls": ["https://imagescdn.allensolly.com/img/app/product/3/39627790-12958323.jpg?auto=format&w=390"],
    "store": "myntra",
    "product_url": ["https://www.myntra.com/allen-solly-shirts"]
  },
  {
    "product_id": "P_006",
    "title": "Woodland Leather Boots",
    "brand": "Woodland",
    "category": "Shoes",
    "price_inr": 3499,
    "description": "Tough, rugged leather boots designed for adventure and outdoor terrain.",
    "image_urls": ["https://rukminim2.flixcart.com/image/480/640/xif0q/shoe/e/h/i/-original-imagudcfzrnffqnm.jpeg?q=90"],
    "store": "Flipkart",
    "product_url": ["https://www.flipkart.com/mens-footwear/casual-shoes/~woodland-boots/pr?sid=osp,cil,e1f"]
  },
  {
    "product_id": "P_007",
    "title": "Puma Black Sports Jacket",
    "brand": "Puma",
    "category": "Jackets",
    "price_inr": 2599,
    "description": "Lightweight, full-sleeve sports jacket with breathable fabric for workouts and outdoor wear.",
    "image_urls": ["https://assets.myntassets.com/dpr_1.5,q_60,w_400,c_limit,fl_progressive/assets/images/productimage/2020/10/18/afd335a2-420b-4546-9373-3b61e0e091361602981396051-1.jpg"],
    "store": "myntra",
    "product_url": ["https://www.myntra.com/puma-jackets"]
  },
  {
    "product_id": "P_008",
    "title": "Peter England Formal Trousers",
    "brand": "Peter England",
    "category": "Trousers",
    "price_inr": 1999,
    "description": "Slim-fit trousers made of high-quality fabric ideal for formal office wear.",
    "image_urls": ["https://imagescdn.peterengland.com/img/app/product/9/954422-12341823.jpg?auto=format&w=390"],
    "store": "Flipkart",
    "product_url": ["https://www.flipkart.com/mens-trousers/peter-england~brand/pr?sid=clo,vua,mle,lhk"]
  },
  {
    "product_id": "P_009",
    "title": "H&M Casual Hoodie",
    "brand": "H&M",
    "category": "Hoodies",
    "price_inr": 2199,
    "description": "Comfortable cotton-blend hoodie with kangaroo pocket and modern design.",
    "image_urls": ["https://assets.myntassets.com/w_412,q_30,dpr_3,fl_progressive,f_webp/assets/images/2025/SEPTEMBER/9/6O8bVKNB_20214c9b3cd8463dbf65648fa270c0ca.jpg"],
    "store": "myntra",
    "product_url": ["https://www.myntra.com/h-and-m-sweatshirts"]
  },
  {
    "product_id": "P_010",
    "title": "Casio Analog Men's Watch",
    "brand": "Casio",
    "category": "Watches",
    "price_inr": 1499,
    "description": "Classic analog watch with stainless steel strap and 3-year battery life.",
    "image_urls": ["https://rukminim2.flixcart.com/image/480/640/xif0q/watch/r/r/a/-original-imahftqfbf7rp9sy.jpeg?q=90"],
    "store": "Flipkart",
    "product_url": ["https://www.flipkart.com/watches/casio~brand/pr?sid=r18"]
  },
  {
    "product_id": "P_011",
    "title": "Boat Rockerz 450 Bluetooth Headphones",
    "brand": "Boat",
    "category": "Headphones",
    "price_inr": 1799,
    "description": "Wireless on-ear headphones with 15 hours playback and immersive sound.",
    "image_urls": ["https://rukminim2.flixcart.com/image/480/640/ksw4ccw0/headphone/e/b/0/rockerz-450-boat-original-imag6cqpa23frzap.jpeg?q=90"],
    "store": "Flipkart",
    "product_url": ["https://www.flipkart.com/boat-rockerz-450-upto-15-hours-playback-bluetooth-headset/p/itm077a566bd128b"]
  },
  {
    "product_id": "P_012",
    "title": "Samsung Galaxy M14 5G",
    "brand": "Samsung",
    "category": "Mobiles",
    "price_inr": 11000,
    "description": "Powerful 5G smartphone with 6000mAh battery and Exynos 1330 processor.",
    "image_urls": ["https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQVFnoEPVwMkrA6YuIiGQw7TSU6NCyeBG2akMqAWoE_HOhXbWbQ0-XEc0EzhfL05MmscBY&usqp=CAU"],
    "store": "Flipkart",
    "product_url": ["https://www.flipkart.com/samsung-galaxy-m14-5g-smoky-teal-128-gb/p/itmb2e6db6c62f07"]
  },
  {
    "product_id": "P_013",
    "title": "Fossil Gen 5 Smartwatch",
    "brand": "Fossil",
    "category": "Smartwatches",
    "price_inr": 9999,
    "description": "Stylish WearOS smartwatch with fitness tracking, heart rate, and voice control.",
    "image_urls": ["https://zoneofdeals.com/wp-content/uploads/2024/07/FOSSIL-GEN-5-5-carlyle-hr.jpg"],
    "store": "Flipkart",
    "product_url": ["https://www.flipkart.com/q/fossil-gen-5"]
  },
  {
    "product_id": "P_014",
    "title": "Noise ColorFit Pro 4",
    "brand": "Noise",
    "category": "Smartwatches",
    "price_inr": 2999,
    "description": "Feature-packed smartwatch with AMOLED display, sports modes, and health sensors.",
    "image_urls": ["https://rukminim2.flixcart.com/image/480/640/l4ln8nk0/smartwatch/x/m/c/45-72-wrb-sw-colorfitpro4max-std-rgld-pnk-android-ios-noise-yes-original-imagfgr4eysszsjg.jpeg?q=20"],
    "store": "Flipkart",
    "product_url": ["https://www.flipkart.com/noise-colorfit-pro4-bluetooth-calling-1-72-truview-display-functional-crown-smartwatch/p/itmee78ed5df4c2d"]
  },
  {
    "product_id": "P_015",
    "title": "Wildcraft 35L Laptop Backpack",
    "brand": "Wildcraft",
    "category": "Backpacks",
    "price_inr": 1799,
    "description": "Spacious water-resistant backpack with laptop sleeve and multiple compartments.",
    "image_urls": ["https://rukminim2.flixcart.com/image/832/832/xif0q/backpack/s/c/m/-original-imah9a2guwhseuz6.jpeg?q=70&crop=false"],
    "store": "Flipkart",
    "product_url": ["https://www.flipkart.com/backpacks/wildcraft~brand/pr?sid=reh%2C4d7%2Cak9&p%5B%5D=facets.rating%255B%255D%3D4%25E2%2598%2585%2B%2526%2Babove"]
  },
  {
    "product_id": "P_016",
    "title": "Puma Men's Classic Hoodie",
    "brand": "Puma",
    "category": "Hoodies",
    "price_inr": 2299,
    "description": "Warm cotton-blend hoodie with adjustable hood and ribbed hem for a sporty style.",
    "image_urls": ["https://m.media-amazon.com/images/I/51fMdddYg2L._SX679_.jpg"],
    "store": "Amazon",
    "product_url": ["https://www.amazon.in/Mens-Hoodies-PUMA-Sweatshirts/s?rh=n%3A1968075031%2Cp_89%3APUMA"]
  },
  {
    "product_id": "P_017",
    "title": "Allen Solly Men's Regular Fit Formal Shirt",
    "brand": "Allen Solly",
    "category": "Shirts",
    "price_inr": 1799,
    "description": "Cotton formal shirt ideal for office wear with a soft texture and premium finish.",
    "image_urls": ["https://m.media-amazon.com/images/I/71tRrNX-a3L._SY879_.jpg"],
    "store": "Amazon",
    "product_url": ["https://www.amazon.in/Allen-Solly-Solid-Regular-ALSFACUFQ58287_Pink/dp/B0DXTFLQDR/ref=sr_1_6?adgrpid=169869581197&dib=eyJ2IjoiMSJ9.IMDMj0Caer_9zldZQUL8i0Z-v3AexBPZglmVk0_Wu7K4kkPzDF6gMGKsqaSAvFMEN1Tw7xboXkfhaa3LNM_zyXniU7pTeVTDlY151Z71h9GZNQwjhT4m6lx4DSl8CdT9KVdAzEhYgc2e0-Kp7dinqpoLuVmQ126jcKskJycKoYnvLq00dwB09p3SiI0rpkBs0B300AKASX8z8ww28b9AzeLiRCJZodDz0mtDMgeiXoRbjJ5jE_Nc6fLL0mVESp0X-B1HcUQsTemvh3CwAnCNhYVBhclcfVFoIk2PomRewSg.rrH9zeRrNwRUQaTN3TNqNaGfVb0MGA1VG9WksX05R9Y&dib_tag=se&gad_source=1&hvadid=763291322599&hvdev=c&hvlocphy=9300940&hvnetw=g&hvqmt=e&hvrand=9523352189472534391&hvtargid=kwd-2244286028540&hydadcr=19600_2389668&keywords=allen%2Bsolly%2Bshirts%2Bfor%2Bmen%2Bamazon&mcid=c4057e6e26543e2fa12b777354ac11cf&qid=1761580490&sr=8-6&th=1&psc=1"]
  },
  {
    "product_id": "P_018",
    "title": "Levi's Men's 511 Slim Fit Jeans",
    "brand": "Levi's",
    "category": "Jeans",
    "price_inr": 2499,
    "description": "Slim fit stretch denim offering comfort and modern style, perfect for casual and semi-formal looks.",
    "image_urls": ["https://m.media-amazon.com/images/I/51NskDjU02L._SX679_.jpg"],
    "store": "Amazon",
    "product_url": ["https://www.amazon.in/s?k=levi%27s+men%27s+511+slim+fit+jeans&adgrpid=136990852020&hvadid=595889975482&hvdev=c&hvlocphy=9300940&hvnetw=g&hvqmt=e&hvrand=562913030838380612&hvtargid=kwd-300171231048&hydadcr=23458_1935856&mcid=c13b1476526c322a88765ae1083848db&tag=googinhydr1-21&ref=pd_sl_4ypq7jj00f_e"]
  }
]


points = []

for idx, product in enumerate(products):
   
    text = (
        f"{product['title']} | {product['brand']} | {product['category']} | "
        f"{product['description']} | Price: ₹{product['price_inr']} | Store: {product['store']}"
    )

    vector = model.encode(text).tolist()

    product["product_url"] = (
        product["product_url"][0] if isinstance(product["product_url"], list) else product["product_url"]
    )


    points.append(
        PointStruct(
            id=idx + 1,
            vector=vector,
            payload=product,
        )
    )


client.upsert(collection_name=COLLECTION, points=points)
print("Products embedded and uploaded to Qdrant successfully!")
