from fastapi import FastAPI
from fastapi.responses import FileResponse # Entregar o html para o navegador
from fastapi.staticfiles import StaticFiles # Entrega outros arquivos 

# ======================================= AULA 1 =======================================
app = FastAPI()
app.mount("/frontend", StaticFiles(directory="frontend"), name="frontend") # Entrega arquivos css e js da pasta frontend. É possível acessar eles na url /frontend/nome_arquivo 

@app.get("/") # Na url padrão
def home(): # A função home entrega o arquivo html com o path padrão
    return FileResponse("./frontend/index.html")

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

@app.get("/logistica/lead-time")
def lead_time():
    return {
        "rota": "SP-RJ",
        "lead_time_medio_dias": 3.5,
        "entregas_realizadas": 84,
        "periodo": "Maio/2026"
    }

@app.get("/producao/resumo")
def prod_resumo():
    return  {
        "unidade": "Fabrica SP",
        "volume_produzido": 15420,
        "volume_refugado": 320,
        "eficiencia_percentual": 97.92, 
        "periodo": "Maio/2026"
    }

@app.get("/financeiro/resumo")
def finan_resumo():
    return  {
        "receita_total": 250000.00,
        "despesas_total": 175000.00,
        "lucro_liquido": 75000.00,
        "margem_percentual": 30.0, 
        "periodo": "Maio/2026"
    }
# ======================================================================================

# ======================================= AULA 2 =======================================

# 1. Variáveis na api; Path Parameter
@app.get("/clientes/{cliente_id}")
def buscar_cliente(cliente_id: int):
    return {
        "cliente_id": cliente_id,
        "nome": "Cliente Exemplo",
        "status": "ativo"
    }

@app.get("/produtos/{produto_id}")
def buscar_produto(produto_id: int):
    return {
        "produto_id": produto_id,
        "nome": "Produto Corporativo",
        "categoria": "Dados",
        "status": "ativo"
    }
#---------------------------------------

# 2. Parâmetros; Query Parameter
# A única diferença é que a gente chama a api com ?variavel=x&variavel2=y
@app.get("/vendas") # /vendas?periodo=maio&unidade=sp
def listar_vendas(periodo: str, unidade: str):
    return {
        "periodo": periodo,
        "unidade": unidade,
        "faturamento_total": 100000        
    }

@app.get("/pedidos")
def listar_pedidos(status: str, unidade: str):
    return {
        "status": status,
        "unidade": unidade,
        "quantidade_pedidos": 42
    }
#---------------------------------------

# 3. Combinando 1 e 2
@app.get("/clientes/{cliente_id}/pedidos") # Não esta ligado com a de cima
def pedidos_cliente(cliente_id: int, status: str): # http://localhost:8000/clientes/123/pedidos?status=ativo
    return {
        "cliente_id": cliente_id, 
        "status": status,
        "quantidade_pedidos": 5
    }

@app.get("/vendedores/{vendedor_id}/vendas")
def vendas_vendedor(vendedor_id: int, periodo: str):
    return {
        "vendedor_id": vendedor_id,
        "periodo": periodo,
        "total_vendas": 87500.75,
        "quantidade_pedidos": 64
    }
#---------------------------------------

# 4. Query Parameter opcional
@app.get("/clientes")
def listar_clientes(status: str | None = None): # Recebe status ou nada. None = None significa que o valor padrão quando não envia nada é nada
    return {
        "status_filtrado": status,
        "quantidade_clientes": 120
    }

@app.get("/estoque")
def listar_estoque(categoria: str | None = None):
    return {
        "categoria_filtrada": categoria,
        "quantidade_itens": 580,
        "valor_total_estoque": 93250.40
    }
#---------------------------------------

# 5. Query parameter opcional com valor padrão
@app.get("/ranking/clientes")
def ranking_clientes(limite: int = 10): #Valor padrão quando não enviar nada é 10
    return {
        "limite": limite,
        "criterio": "maior_faturamento"
    }

@app.get("/ranking/produtos")
def ranking_produtos(limite: int = 10):
    return {
        "limite": limite,
        "criterio": "maior_margem",
        "quantidade_produtos_analisados": 250
    }
# ======================================================================================

# ======================================= AULA 3 =======================================































