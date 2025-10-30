"use client";
import { SignedIn, SignedOut, useAuth } from "@clerk/nextjs";
import { useEffect, useState } from "react";

export default function Dashboard() {
  return (
    <main className="bg-black min-h-screen text-white">
      <SignedIn>
        <DashboardContent />
      </SignedIn>
      <SignedOut>
        <div className="flex flex-col items-center justify-center min-h-screen px-4">
          <h1 className="text-white text-4xl font-bold mb-6">Please sign in to access the dashboard.</h1>
        </div>
      </SignedOut>
    </main>
  );
}

function DashboardContent() {
  const { getToken } = useAuth();
  const [data, setData] = useState(null);

  useEffect(() => {
    async function fetchData() {
      const token = await getToken({ template: "default" });
      const res = await fetch("http://localhost:8000/protected", {
        headers: { Authorization: `Bearer ${token}` },
      });
      const result = await res.json();
      setData(result);
    }
    fetchData();
  }, [getToken]);

  return (
    <div className="p-8">
      <h1 className="text-2xl font-bold mb-4">Dashboard</h1>
      {data ? <pre>{JSON.stringify(data, null, 2)}</pre> : <p>Loading...</p>}
    </div>
  );
}
