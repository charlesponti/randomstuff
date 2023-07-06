'use client';

import React, {useState} from 'react';

const LandingPage: React.FC = () => {
  const [isDarkMode, setIsDarkMode] = useState(false);
  const [responseValue, setResponseValue] = useState('');
  const [inputValue, setInputValue] = useState('');
  const [error, setError] = useState(null);

  const toggleDarkMode = () => {
    setIsDarkMode(!isDarkMode);
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();

    try {
      // Make a POST request to the API route
      const response = await fetch('/api/openai', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({
          prompt: inputValue,
        }),
      });
      const data = await response.json();

      if (response.status !== 200) {
        setError(data.message);
      } else {
        setResponseValue(data.response);
      }
    } catch (error) {
      console.error(error);
      setError(error.message);
    }
  };

  return (
    <div className={isDarkMode ? 'dark' : ''}>
      <header className="py-8 px-4">
        <div className="container mx-auto flex justify-between items-center">
          <h1 className="text-4xl font-bold">Startup</h1>
          <button
            className="px-4 py-2 rounded text-white bg-blue-500 hover:bg-blue-600"
            onClick={toggleDarkMode}
          >
            {isDarkMode ? 'Light Mode' : 'Dark Mode'}
          </button>
        </div>
      </header>
      <main className="container mx-auto py-16 px-4">
        <h2 className="text-2xl font-bold mb-8">Welcome to Our Startup</h2>
        <form onSubmit={handleSubmit}>
          <div>
            {error && (
              <div className="bg-red-500 text-white p-4 mb-4 rounded">
                {error}
              </div>
            )}
          </div>
          <input
            type="text"
            value={inputValue}
            onChange={e => setInputValue(e.target.value)}
            placeholder="Enter your value"
            className="p-2 mb-4 w-full border border-gray-300 focus:outline-none"
          />
          <button className="px-4 py-2 rounded text-white bg-blue-500 hover:bg-blue-600">
            Submit
          </button>
        </form>
        <div>
          {responseValue && (
            <div className="mt-8">
              <h3 className="text-xl font-bold mb-4">Response</h3>
              <p>{responseValue}</p>
            </div>
          )}
        </div>
      </main>
      <footer className="py-4 px-4 bg-gray-200 dark:bg-gray-800">
        <div className="container mx-auto text-center">
          &copy; 2023 Startup. All rights reserved.
        </div>
      </footer>
    </div>
  );
};

export default LandingPage;
