const botao = document.getElementById("atualizar");
const resultado = document.getElementById("leads-tabela");
botao.addEventListener('click', async () => {
    const resposta = await fetch("/leads");
    const dados = await resposta.json();
    console.log("Apertou"); 
    resultado.textContent = JSON.stringify(dados);
});


