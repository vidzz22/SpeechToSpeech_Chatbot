import React from 'react';
import Head from 'next/head';

export default function Dashboard() {
  return (
    <div className="container">
      <Head>
        <title>User Dashboard</title>
        <meta name="description" content="User dashboard with credits and profile" />
        <link rel="stylesheet" href="/styles.css" />
      </Head>
      <header>
        <img src="/logo.png" alt="Platform Logo" className="logo" />
        <h1>User Dashboard</h1>
      </header>
      <main>
        <p>Credits, profile details, and other user information will be displayed here.</p>
      </main>
    </div>
  );
}
