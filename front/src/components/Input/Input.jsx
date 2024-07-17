import React, { useState } from "react";
import './Input.css'

function Input({value, hasButton, name, type, inputMode, placeholder, event}) {

    return (
        <div className="inputContainer">
            <input 
                type={type ? type : 'text'} 
                value={value}
                name={name}
                placeholder={placeholder ? placeholder : name}
                inputMode={inputMode}
                onChange={event}
                className="inputField"
            />
            {
                hasButton ? (
                    <button 
                        type="submit" 
                        className="inputButton" 
                    >
                        Enviar
                    </button>
                ) : null

            }
            
        </div>
    )
}

export default Input;