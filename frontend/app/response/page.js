"use client";
import React, { useState } from "react";
import axios from "axios";

const ResponsePage = () => {
    const [query, setQuery] = useState("");
    const [products, setProducts] = useState([]);
    const [aiResponse, setAiResponse] = useState("");
    const [loading, setLoading] = useState(false);

    

    const handleSearch = async () => {
        if (!query.trim()) return;
        setLoading(true);
        try {
            const res = await axios.post("http://127.0.0.1:8000/api/search", { query });
            setProducts(res.data.results || []);
            setAiResponse(res.data.ai_message || "No ONEPLACE AI suggestions found.");
        } catch (err) {
            console.error(err);
            setAiResponse("Error fetching data.");
        } finally {
            setLoading(false);
        }
    };


    return (
        <main className="bg-black min-h-screen text-white px-6 py-8">
            <h1 className="text-3xl font-bold mb-6 text-center">Smart Product Search</h1>

            <div className="flex flex-col sm:flex-row justify-center mb-8 gap-2">
                <input
                    type="text"
                    value={query}
                    onChange={(e) => setQuery(e.target.value)}
                    placeholder="Search for products like 'budget hoodies'..."
                    className="w-full sm:w-1/2 p-2 rounded-lg text-black bg-amber-50 outline-none"
                />
                <button
                    onClick={handleSearch}
                    className="w-full sm:w-auto bg-blue-600 px-4 py-2 rounded-lg hover:bg-blue-700"
                >
                    Search
                </button>
            </div>

            {loading && <p className="text-center text-gray-400">Loading...</p>}

            {aiResponse && (
                <section className="bg-gray-800 p-4 rounded-lg mb-6">
                    <h2 className="text-xl font-semibold mb-2">ONEPLACE AI Suggestion</h2>
                    <p className="text-gray-300">{aiResponse}</p>
                </section>
            )}

            <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-6">
                {products.map((p, index) => (
                    <div
                        key={index}
                        className="bg-gray-900 p-4 rounded-xl shadow-lg hover:shadow-blue-500/20 transition"
                    >
                        <img
                            src={p.image_url}
                            alt={p.title}
                            className="w-full h-48 sm:h-56 md:h-48 lg:h-56 object-cover rounded-lg mb-3"
                        />
                        <h3 className="text-lg font-semibold">{p.title}</h3>
                        <p className="text-sm text-gray-400">{p.store}</p>
                        <p className="text-blue-400 font-bold mt-1">₹{p.price_inr}</p>
                        <p className="text-gray-300 text-sm mt-2">{p.description}</p>
                        <a
                            href={p.product_url}
                            target="_blank"
                            rel="noopener noreferrer"
                            className="block text-center bg-blue-700 mt-4 py-2 rounded-lg hover:bg-blue-800"
                        >
                            View Product
                        </a>
                    </div>
                ))}
            </div>
        </main>
    );
};

export default ResponsePage;
