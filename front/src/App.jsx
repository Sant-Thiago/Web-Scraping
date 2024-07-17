import React, { useState } from 'react';
import { Routes, Route, BrowserRouter } from "react-router-dom";
import './App.css';
import Register from './components/Register/Register';
import Login from './components/Login/Login';

function App() {

  const [type, setType] = useState('');

  
  return (
    <div className='containerApp'>
      <h1>Web Scraping {type}</h1>
      <div className="divisor"></div>
      <BrowserRouter>
        <Routes>
          <Route 
            path='/' 
            element={<Register setType={() => setType('| Cadastro')} />} 
            exact 
          ></Route>
          <Route 
            path='/login' 
            element={<Login setType={() => setType('| Autenticação')} />} 
          ></Route>
          <Route 
            path='/product'
            element={ null } 
          ></Route>

        </Routes>
      </BrowserRouter>
      <div id='result'></div>
    </div>
  );
}

export default App;
