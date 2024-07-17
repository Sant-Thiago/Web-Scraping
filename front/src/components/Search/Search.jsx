import React, { useEffect, useState } from 'react'
import { handleInputValueOne } from '../../Utils/Utils.jsx'
import $ from 'jquery';

import Input from '../Input/Input';
import Title from '../Title/Title';

import './Search.css'

function Search() {
    const [suggest] = useState(['Pesquise.....', 'Iphone 15', 'Jaqueta Faya', 'Fone Wireless'])
    const [currentIndex, setCurrentIndex] = useState(0)
    const [placeholder, setPlaceholder] = useState(suggest[currentIndex])
    
    const [search, setSearch] = useState('')
    const [products, setProducts] = useState([])

    useEffect(() => {
        const interval = setInterval(() => {
            setCurrentIndex(prevIndex => (prevIndex + 1) % suggest.length)
            setPlaceholder(suggest[currentIndex])
        }, 4200)

        // Limpa o interval quando o componente for desmontado
        return () => clearInterval(interval)
    // [currentIndex] Instrui o React a executar o useEffect toda vez que o 'currentIndex' for alterado, criando esse loop 
    }, [currentIndex])

    

    const handleSubmit = (event) => {
        event.preventDefault();

        const params = {
            'q': search,
            'limit': 7
        };
        
        // Construindo a URL da API
        const baseUrl = 'https://api.mercadolibre.com/sites/MLB/search';
        const url = new URL(baseUrl);
        url.search = new URLSearchParams(params).toString();

        $.ajax({
            url: url,
            type: "GET",
            dataType: "json",
            success: response => {
                const results = response.results
                setProducts(results);
                return response;
            },
            error: (xhr, status, error) => {
                console.log('xhr aqui ==> '+ JSON.stringify(xhr));
                console.log('status aqui ==> '+ status);
                // console.log('Erro aqui ==> '+ error);
            }
        })
    }

    return (
        <div className='searchContainer'>
            <Title />
            <form onSubmit={handleSubmit} method="POST" className='searchForm'>
                <Input 
                    hasButton={true} 
                    value={search} 
                    placeholder={placeholder}
                    event={(event) => handleInputValueOne(event, setSearch)}
                />
            </form>
            {
                products.length > 0 ? ( 
                    products.map(product => (
                        <div className='divResult' key={product.id}>
                            <a href={product.permalink} target='blank' >{product.title} - R${product.price}</a>
                        </div>
                ))) : null
            }
        </div>
    )
}

export default Search;
