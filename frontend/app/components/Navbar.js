import React from 'react'
import Link from 'next/link'

const Navbar = () => {
  return (
    <main>
        <nav className='bg-black flex justify-between items-center border-b border-gray-800'>
            <div className='py-3 px-4'>
                <h1 className='text-white text-3xl font-bold'>ONEPLACE</h1>
            </div>
            <div className='gap-4'>
                <ul className='flex'>
                    <Link href={"/"}><li className='text-white px-4 py-3 hover:underline cursor-pointer'>Home</li></Link>
                    <Link href={"/signin"}><li className='text-white px-4 py-3 hover:underline cursor-pointer'>Signin</li></Link>
                    <Link href={"/signup"}><li className='text-white px-4 py-3 hover:underline cursor-pointer'>Signup</li></Link>
                   
                </ul>
            </div>
        </nav>
    </main>
  )
}

export default Navbar
