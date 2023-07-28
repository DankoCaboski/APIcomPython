import React, { useState, useEffect } from 'react';

export default function Tabela() {
  const [data, setData] = useState([]);

  useEffect(() => {
    fetch('http://localhost:5000/clientes')
      .then(response => response.json())
      .then(data => setData(data));
  }, []);

    return(
        <table>
            <thead>
              <tr>
                <th className="colunas">Nome</th>
                <th className="colunas">CNPJ</th>
                <th className="colunas">Status</th>
              </tr>
            </thead>
            <tbody>
              {data.map((item, index) => (
                <tr key={index}>
                  <td className="colunas">{item[0]}</td>
                  <td className="colunas">{item[1]}</td>
                  <td className="colunas">{item[2]}</td>
                </tr>
              ))}
            </tbody>
          </table>
    )
}