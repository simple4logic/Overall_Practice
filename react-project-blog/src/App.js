import React, {useState} from 'react';
import logo from './logo.svg';
import './App.css';

function App() {

  let posts = "comment"; 

  return ( //JSX Language in the function of the js
    <div className="App">
      <div className="black-nav">
        developer blog
      </div>
      <img src = {logo}></img>
      <h4>
        {posts}
      </h4>
    </div>
  );
}

export default App;
