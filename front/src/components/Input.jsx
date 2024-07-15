import React, { useState } from "react";
import './Input.css'

function Input() {
    const [valor, setValor] = useState('');

    return (
        <div className="inputContainer">
            <input 
                type="text" 
                value={valor}
                onChange={(e) => setValor(e.target.value)}
                className="inputField"
            />
            <button 
                type="submit"
                className="inputButton"
                onClick={() => {setValor('')}}
            >Enviar</button>
        </div>
    )
}

export default Input;