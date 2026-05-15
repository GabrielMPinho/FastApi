const botao_atualizar = document.getElementById("atualizar");
const tabela = document.getElementById("leads-tabela");
const botao_adicionar = document.getElementById("cadastro");
const nome_input = document.getElementById("nome");
const origem_input = document.getElementById("origem");
const score_input = document.getElementById("score");

botao_atualizar.addEventListener("click", async () => {
    const resposta = await fetch("/leads");
    const dados = await resposta.json();
    tabela.innerHTML = "";

    if (dados.leads.length === 0) {
        tabela.innerHTML = '<tr><td colspan="4" class="empty-row">Nenhum lead cadastrado ainda.</td></tr>';
        return;
    }

    dados.leads.forEach((lead) => {
        tabela.innerHTML += `
            <tr>
                <td>${lead.nome}</td>
                <td>${lead.origem}</td>
                <td>${lead.score}</td>
                <td>${lead.hora_cadastro}</td>
            </tr>
        `;
    });
});

botao_adicionar.addEventListener("click", async () => {
    const nome = nome_input.value;
    const origem = origem_input.value;
    const score = Number(score_input.value);

    const resposta = await fetch("/leads", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            "nome": nome,
            "origem": origem,
            "score": score
        })
    });

    if (!resposta.ok) {
        const erro = await resposta.json();
        console.log(erro);
        alert(erro.detail || "Erro no cadastro");
        return;
    }

    const dados = await resposta.json();
    console.log(dados);
    alert("Dados enviados com sucesso!");

    nome_input.value = "";
    origem_input.value = "";
    score_input.value = "";
});
