import React, { useState, useEffect } from 'react';
import { useNavigate } from "react-router-dom";
import $ from 'jquery';

import Input from '../Input/Input';
import './Register.css'

function Register({ setType }) {

    const navigate = useNavigate();

    const [inputForm, setInputForm] = useState({
        nome: '',
        email: '', 
        cpf: ''
    });

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
        // $.ajax({
        //     url: "http://127.0.0.1:5000/create/wsdata?collection=User",
        //     type: "POST",
        //     contentType: "application/json",
        //     data: JSON.stringify({
        //         nome: inputForm.nome,
        //         email: inputForm.email,
        //         cpf: inputForm.cpf
        //     }),
        //     success: response => {
        //         console.log('[SUCESS]:: '+ JSON.stringify(response));
        //     },
        //     error: (xhr, status, error) => {
        //         console.log('xhr aqui ==> '+ JSON.stringify(xhr));
        //         console.log('status aqui ==> '+ status);
        //         // console.log('Erro aqui ==> '+ error);
        //     }
        // });
        alert("TUDO CERTO")
        setTimeout(() => {
            navigate("/login")
        })

    };
    
    return (
        <div className='registerContainer'>
            <form onSubmit={handleSubmit} method="POST" className='registerForm'>
                {Object.keys(inputForm).map((key, index) => ( 
                    <Input 
                        key={index} 
                        name={key} 
                        value={inputForm[key].field} 
                        event={handleInputValue} 
                    />
                ))}
                <button 
                    type='submit'
                    className='registerButton'
                >
                    Cadastrar
                </button>
            </form>
        </div>
    )
}

export default Register;