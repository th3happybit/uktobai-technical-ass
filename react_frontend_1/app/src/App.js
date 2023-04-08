import React, { useState } from 'react';
import './App.css';

function App() {
  const [inputString, setInputString] = useState('');
  const [inputNumber, setInputNumber] = useState('');
  const [result, setResult] = useState('');
  const [error, setError] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    // input validation
    if (!inputString || inputString.trim() === '' || isNaN(inputNumber) || inputNumber < 1) {
      setError('Please enter a valid string and a positive number.');
      setResult('');
    } else {
      setError('');
      setResult(inputString.repeat(inputNumber));
    }
  };

  return (
    <div className="App">
      <h1>Repeat String</h1>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          placeholder="Enter a string"
          value={inputString}
          onChange={(e) => setInputString(e.target.value)}
        />
        <input
          type="number"
          placeholder="Enter a number"
          value={inputNumber}
          onChange={(e) => setInputNumber(parseInt(e.target.value, 10))}
        />
        <button type="submit">Submit</button>
      </form>
      {error && <p className="error">{error}</p>}
      {result && <p>{result}</p>}
    </div>
  );
}

export default App;
