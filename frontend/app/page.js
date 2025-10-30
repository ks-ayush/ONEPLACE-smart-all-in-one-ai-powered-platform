"use client";
import Image from "next/image";
import React from "react";
import { toast } from "react-toastify";
import Router from "next/router";
import Particles from "./components/particles";
import Link from "next/link";
 
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
        
        <div>
          {/* <form className="text-white flex flex-col gap-6">
            <input
              type="text"
              placeholder="red Nike shoes under ₹4000"
              className="px-4 py-2 rounded-l-md border w-96 border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500"
            />
            <button
              type="submit"
              className="bg-blue-600 hover:bg-blue-700 text-white font-semibold px-4 py-2 rounded-r-md"
            >
              Search
            </button>
            
          </form> */
          }
          <div className="flex space-x-4 justify-center">
            <Link href={"/response"}>
            <button
              className="bg-blue-600 hover:bg-blue-700 text-white font-semibold py-3 px-6 rounded"
              
            >
              Get Started
            </button>
            </Link>
            
          </div>
          
        </div>
      </section>
    </main>

    // <main style={{ width: '100%', height: '600px', position: 'relative' }} className="bg-black min-h-screen">
    //   <Particles
    //     particleColors={['#ffffff', '#ffffff']}
    //     particleCount={200}
    //     particleSpread={10}
    //     speed={0.1}
    //     particleBaseSize={100}
    //     moveParticlesOnHover={true}
    //     alphaParticles={false}
    //     disableRotation={false}
    //   />

    //   <section>
    //     <div className="flex flex-col items-center justify-center text-center pt-40 px-4">
    //       <h1 className="text-white text-5xl font-bold mb-6">Welcome to ONEPLACE</h1>
    //       <p className="text-gray-300 text-lg mb-8 max-w-2xl">
    //         Your unified platform for all your needs. Discover, connect, and manage everything in one place.
    //       </p>
    //       <div className="flex space-x-4">
    //         <button
    //           className="bg-blue-600 hover:bg-blue-700 text-white font-semibold py-3 px-6 rounded"
    //           onClick={() => toast.success("Get Started clicked!")}
    //         >
    //           Get Started
    //         </button>
    //         <button
    //           className="bg-gray-600 hover:bg-gray-700 text-white font-semibold py-3 px-6 rounded"
    //           onClick={() => toast.info("Learn More clicked!")}
    //         >
    //           Learn More
    //         </button>
    //       </div>
    //     </div>
    //   </section>

    // </main>



  );
}
