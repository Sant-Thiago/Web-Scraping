import React, { useState } from 'react';
import { Routes, Route, BrowserRouter } from "react-router-dom";
import './App.css';
import Register from './components/Register/Register';

function App() {

  const [type, setType] = useState('');

  return (
    <div className='containerApp'>
      <h1>Web Scraping {type}</h1>
      <div className="divisor"></div>
      <BrowserRouter>
        <Routes>
          <Route 
            Component={() => <Register setType={setType('| Cadastro')} />} 
            path='/' 
            exact 
          ></Route>
          <Route 
            Component={() => <Register setType={setType('| Cadastro')} />} 
            path='/julia' 
            exact 
          ></Route>

        </Routes>
        {/* <Route Component={ product } path='/product'></Route> */}
      </BrowserRouter>
      <div id='result'></div>
    </div>
  );
}

export default App;
