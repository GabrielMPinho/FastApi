const botao = document.getElementById("atualizar");
const resultado = document.getElementById("leads-tabela");
botao.addEventListener('click', async () => {
    const resposta = await fetch("/leads");
    const dados = await resposta.json();
    resultado.innerHTML = "";
    if (dados.leads.length === 0) {
        resultado.innerHTML = '<tr><td colspan="4" class="empty-row">Nenhum lead cadastrado ainda.</td></tr>';
        return;
    }
    dados.leads.forEach((lead) => {
        resultado.innerHTML += `
            <tr>
                <td>${lead.nome}</td>
                <td>${lead.origem}</td>
                <td>${lead.score}</td>
                <td>${lead.hora_cadastro}</td>
            </tr>
        `;
    });
});

