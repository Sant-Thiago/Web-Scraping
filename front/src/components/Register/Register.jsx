import React, { useState } from 'react';
import Input from '../Input/Input';
import $ from 'jquery';

import Input from '../Input/Input'
import './Register.css'

function Register() {

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
        $.ajax({
            url: "http://127.0.0.1:5000/create/wsdata?collection=User",
            type: "POST",
            contentType: "application/json",
            data: JSON.stringify({
                nome: inputForm.nome,
                email: inputForm.email,
                cpf: inputForm.cpf
            }),
            success: response => {
                console.log('[SUCESS]:: '+ JSON.stringify(response));
                <Input/>
            },
            error: (xhr, status, error) => {
                console.log('xhr aqui ==> '+ JSON.stringify(xhr));
                console.log('status aqui ==> '+ status);
                // console.log('Erro aqui ==> '+ error);
            }
        });
    };
    
    return (
        <div className='registerContainer'>
            <form onSubmit={handleSubmit} method="POST" className='regiterForm'>
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