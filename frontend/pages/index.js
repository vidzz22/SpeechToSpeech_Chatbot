import React from 'react';
import Head from 'next/head';
import '../public/styles.css';

export default function Home() {
  return (
    <div className="container">
      <Head>
        <title>Speech-to-Speech Chatbot</title>
        <meta name="description" content="Chatbot interface" />
      </Head>
      <header>
        <img src="/logo.png" alt="Platform Logo" className="logo" />
        <h1>Speech-to-Speech Chatbot</h1>
      </header>
      <main>
        <p>Chat interface goes here.</p>
      </main>
    </div>
  );
}
