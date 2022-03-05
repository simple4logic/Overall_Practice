/* eslint-disable */

import React, {useState} from 'react';
import logo from './logo.svg';
import './App.css';

function App() {
  let [title, fix] = useState(['제목1','제목2','제목3','제목4']);

  return (

    <div className="App">
      <div className="black-nav">
        <div>developing blog</div>  
      </div>
      <div className="lists">
        <h3>{ title[0] } <span>b</span>0 </h3>
        <p>3월 1일 발행</p>
        <hr/>  
      </div>
      <div className="lists">
        <h3>{ title[1] }</h3>
        <p>3월 2일 발행</p>
        <hr/>  
      </div>
      <div className="lists">
        <h3>{ title[2] }</h3>
        <p>3월 3일 발행</p>
        <hr/>  
      </div>
      <div className="lists">
        <h3>{ title[3] }</h3>
        <p>3월 4일 발행</p>
        <hr/>  
      </div>
    </div>
  );
}

export default App;
