"use client";
import Image from "next/image";
import React from "react";
import { toast } from "react-toastify";
import Router from "next/router";
import Particles from "./components/particles";
import Link from "next/link";
import { SignedIn, SignedOut } from "@clerk/nextjs";

export default function Home() {

  return (

    <main className="relative w-full h-screen bg-black overflow-hidden">

      <div className="absolute inset-0 z-0">
        <Particles
          particleColors={["#ffffff", "#ffffff"]}
          particleCount={100}
          particleSpread={5}
          speed={0.1}
          particleBaseSize={100}
          moveParticlesOnHover={true}
          alphaParticles={true}
          disableRotation={false}
        />
      </div>


      <section className="absolute inset-0 z-10 flex flex-col items-center justify-center text-center px-4">


        <h1 className="text-white text-5xl font-bold mb-6">Welcome to ONEPLACE</h1>
        <p className="text-gray-300 text-lg mb-8 max-w-2xl">
          ONEPLACE brings products from multiple stores and online shopping sites together in one smart search.
          You can find anything — shoes, gadgets, clothes, and more — all in one place.
          Just type a simple prompt like watches under ₹4000 and get instant results.
          Powered by AI-based semantic search, ONEPLACE understands what you mean, not just what you type.
          Fast, accurate, and easy — making online shopping simpler than ever.
        </p>

        {/* <div>
          <div className="flex space-x-4 justify-center">
            <Link href={"/response"}>
            <button
              className="bg-blue-600 hover:bg-blue-700 text-white font-semibold py-3 px-6 rounded"
              
            >
              Get Started
            </button>
            </Link>
            
          </div>
          
        </div> */}

        <div className="flex justify-center">
          <SignedIn>
            <Link href="/response">
              <button className="bg-blue-600 hover:bg-blue-700 text-white font-semibold py-3 px-6 rounded">
                Get Started
              </button>
            </Link>
          </SignedIn>

          <SignedOut>
            <Link href="/signin">
              <button className="bg-gray-600 hover:bg-gray-700 text-white font-semibold py-3 px-6 rounded">
                Sign In to Get Started
              </button>
            </Link>
          </SignedOut>
        </div>
      </section>
    </main>




  );
}
