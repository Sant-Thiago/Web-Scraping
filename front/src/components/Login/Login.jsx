import React, { useState, useEffect } from 'react';

import Input from '../Input/Input';
import './Login.css'

function Login({ setType }) {

    useEffect(() => {
        setType();
      }, [setType]);

    return (
        <div className='loginContainer'>
            <h1>BEM VINDO</h1>
            <Input
                hasButton={true}
            />
        </div>
    )
}

export default Login;
