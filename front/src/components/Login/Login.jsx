import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import Input from '../Input/Input';
import $ from 'jquery';

import './Login.css';
import Title from '../Title/Title';

function Login() {
    
    const [inputForm, setInputForm] = useState({ cpf: '' });
    const navigate = useNavigate();

    const handleInputValue = (event) => {
        const { name, value } = event.target;
        setInputForm({
            ...inputForm,
            [name]: value
        });
    };

    const handleSubmit = (event) => {
        // Chamado para evitar que o formulário seja enviado de forma tradicional (recarregando a página)
        event.preventDefault();
        $.ajax({
            url: `http://127.0.0.1:5000/select/wsdata/by?collection=User&cpf=${inputForm.cpf}`,
            type: "GET",
            dataType: "json",
            success: response => {

                if (response.error) {
                    alert(response.error)
                    setTimeout(() => {
                        navigate("/register")
                    })
                } else {
                    setTimeout(() => {
                        navigate("/search")
                    })
                }
            },
            error: (xhr, status, error) => {
                console.log('xhr aqui ==> '+ JSON.stringify(xhr));
                console.log('status aqui ==> '+ status);
                // console.log('Erro aqui ==> '+ error);
            }
        })
    }

    return (
        <div className='loginContainer'>
            <Title 
                type={'| Autenticação'}
            />
            <form onSubmit={handleSubmit} method="POST" className='loginForm'>
                {Object.keys(inputForm).map((key, index) => (
                    <Input 
                        key={index} 
                        name={key}
                        hasButton={true} 
                        value={inputForm[key]} 
                        event={handleInputValue} 
                    />
                ))}
            </form>
        </div>
    )
}

export default Login;
