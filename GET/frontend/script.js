async function chamarApi(endpoint) {
    const resposta = await fetch(endpoint);
    const dados = await resposta.json();
    document.getElementById("resultado").textContent = JSON.stringify(dados, null, 4);
}
