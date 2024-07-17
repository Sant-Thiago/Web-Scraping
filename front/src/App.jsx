import React, { useState } from 'react';
import { Routes, Route, BrowserRouter } from "react-router-dom";
import './App.css';
import Register from './components/Register/Register';
import Login from './components/Login/Login';
import Search from './components/Search/Search';

function App() {

  const [type, setType] = useState('');

  
  return (
    <div className='containerApp'>
      <BrowserRouter>
        <Routes>
          <Route 
            path='/' 
            element={<Login />} 
            exact 
          ></Route>
          <Route 
            path='/register' 
            element={<Register />} 
          ></Route>
          <Route 
            path='/search'
            element={ <Search /> } 
          ></Route>
        </Routes>
      </BrowserRouter>
      <div id='result'></div>
    </div>
  );
}

export default App;
