from fastapi import FastAPI
from fastapi.responses import FileResponse # Entregar o html para o navegador
from fastapi.staticfiles import StaticFiles


app = FastAPI()
app.mount("/frontend", StaticFiles(directory="frontend"), name="frontend")

@app.get("/")
def home():
    return FileResponse("frontend/index.html")

@app.get("/status")
def status():
    return {"status": "online"}

@app.get("/versao")
def versao():
    return {
        "api": "FastAPI Aula 1",
        "versao": "1.0"
    }

@app.get("/indicadores/vendas")
def vendas():
    return {
        "faturamento_total": 125000.50,
        "quantidade_pedidos": 320,
        "ticket_medio": 390.63,
        "periodo": "Maio/2026"
    }

@app.get("/clientes/inativos")
def lista_clientes():
    return [
        {
            "nome": "Supermercado Central",
            "dias_sem_compra": 120,
            "ultima_compra": "2026-01-10"
        },
        {
            "nome": "Farmacia Vida",
            "dias_sem_compra": 95,
            "ultima_compra": "2026-02-04"
        },
        {
            "nome": "Loja Horizonte",
            "dias_sem_compra": 180,
            "ultima_compra": "2025-11-15"
        },
    ]









































