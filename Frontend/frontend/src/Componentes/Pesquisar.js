import React, { useState, useEffect } from 'react';

export default function Pesquisar() {

    const [nomeCNPJ, setNomeCNPJ] = useState([]);

    const handleSubmitForm = (event) => {
        event.preventDefault();

        const cnpjValue = event.target.elements.cnpjInput.value;

        fetch(`http://localhost:5000/clientes/${cnpjValue}`)
        .then(response => response.json())
        .then(nomeCNPJ => setNomeCNPJ(nomeCNPJ))
        
        
    };

    const handleFlipStatus = (event) => {
    event.preventDefault();
        
    fetch(`http://localhost:5000/clientes/flipStatus/${inputValue}`, {
        method: 'PUT'
        })
    };

        const handleExcluir = (event) => {
    event.preventDefault();
        
    fetch(`http://localhost:5000/clientes/delete/${inputValue}`, {
        method: 'DELETE'
        })
    };

    const [inputValue, setInputValue] = useState('');
    const handleInputChange = (event) => {
        // Update the state with the latest input value whenever it changes
        setInputValue(event.target.value);
      };

    return(
        <div class="table">
            <label>Consultar cliente:</label>
            <label>{inputValue}</label>
            <form onSubmit={handleSubmitForm}>
              <input type="text" name="cnpjInput" onChange={handleInputChange} placeholder="Nome ou CNPJ" class="colunas"/>
              <input type="submit" value="Pesquisar" class="colunas"/>
            </form>
            <div>
              <input type="text" name="cli" placeholder="Nome do cliente" value={nomeCNPJ}class="colunas"></input>
              <button class="colunas" onClick={handleFlipStatus}>Alterar status</button>
              <button class="colunas" onClick={handleExcluir} >Excluir</button>

            </div>
        </div>
      )
}