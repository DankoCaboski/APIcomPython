import React, { useState, useEffect } from 'react';
import '../App.css';

export default function Pesquisar() {

    const [nomeCNPJ, setNomeCNPJ] = useState([]);
    const [data, setData] = useState([]);


    const handleSubmitForm = (event) => {
        event.preventDefault();

        const cnpjValue = event.target.elements.cnpjInput.value;

        fetch(`http://localhost:5000/clientes/${cnpjValue}`)
        .then(response => response.json())
        .then(nomeCNPJ => setNomeCNPJ(nomeCNPJ))

        fetch(`http://localhost:5000/clientes/contatos/${inputValue}`)
          .then(response => response.json())
          .then(data => setData(data));
        
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
            <div class="table">
                <label className='bar'>Lista de contatos</label>
                <table>                
                    <thead>
                    <tr className="contatos">
                        <th className="colunas">Nome</th>
                        <th className="colunas">Telefone</th>
                        <th className="colunas">Email</th>
                    </tr>
                    </thead>
                    <tbody className="contatos">
                    {data.map((item, index) => (
                        <tr key={index}>
                        <td className="colunas">{item[2]}</td>
                        <td className="colunas">{item[4]}</td>
                        <td className="colunas">{item[4]}</td>
                        </tr>
                    ))}
                    </tbody>
                </table>
            </div>
        </div>
      )
}