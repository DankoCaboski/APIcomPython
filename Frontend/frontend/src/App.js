import React, { useEffect, useState } from 'react';
import './App.css';
import Tabela from './Componentes/Tabela';
import Pesquisar from './Componentes/Pesquisar';


function App() {
  let [exibirClientes, setExibirClientes] = useState(true);
  
  const handleButtonClick = () => {
    setExibirClientes(!exibirClientes);
  };

  return (
    <div className="App">
      <header className="App-header">
        <div>
          <p className="bar">Clientes</p>
        </div>
        {exibirClientes ? ( <Tabela/> ) : ( <Pesquisar/> )}
        {exibirClientes ? (
        <button onClick={handleButtonClick} class="bt">Editar cliente</button>
        ):(
          <button onClick={handleButtonClick} class="bt">Consultar clientes</button>
        )}
      </header>
    </div>
  );
}

export default App;
