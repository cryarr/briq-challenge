import React from 'react';
import logo from './logo.svg';
import './App.css';

//this input display should be working, but its not getting the form input from the quote display
function App() {
  return (
    <div className="App">
      <header className="App-header">
        <p>
	  		briq challenge
        </p>
      </header>
	  <main>
	  	<quoteDisplay>
	  	<input starinput={stars}/>
	  </main>
    </div>
  );
}

export default App;
