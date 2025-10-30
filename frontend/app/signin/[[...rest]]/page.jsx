"use client";

import { SignIn, SignedIn, SignedOut, UserButton } from "@clerk/nextjs";

export default function SignInPage() {
  return (
    <div className="flex justify-center items-center min-h-screen bg-gray-100">
      
      <SignedOut>
        <SignIn
          path="/signin"
          routing="path"
          signUpUrl="/signup"
          
        />
      </SignedOut>

      
      <SignedIn>
        <div className="text-center">
          <h1 className="text-3xl font-bold mb-4 text-gray-800">
            You are already signed in 
          </h1>
          <p className="text-gray-600 mb-6">
            Manage the account from below.
          </p>

          
          <div className="flex justify-center">
            <UserButton afterSignOutUrl="/signin" />
          </div>
        </div>
      </SignedIn>
    </div>
  );
}
