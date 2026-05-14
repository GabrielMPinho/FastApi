from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from datetime import datetime

#Ligando o back com o front
app = FastAPI()
app.mount("/frontend", StaticFiles(directory="frontend"), name="POST_Frontend") #Puxei js e css e html

@app.get("/")
def home():
    return FileResponse("frontend/index.html")
#---------------------------------------------------
class Lead(BaseModel): # Criei uma classe chamada Lead que vai seguir este padrão
    nome: str
    origem: str
    score: float

leads = [] # Guardar leads

#---------------------------------------------------

@app.post("/leads")
def cadastro(lead: Lead):
    novo_lead = {
        "nome": lead.nome,
        "origem": lead.origem,
        "score": lead.score,
        "hora_cadastro": datetime.now().strftime("%d/%m/%Y %H:%M")
    }
    leads.append(novo_lead)
    return {
        "mensagem": "Lead recebido com sucesso",
        "lead": novo_lead,

    }

@app.get("/leads")
def listar_leads():
    return {
        "total": len(leads),
        "leads": leads # Retorna cada lead em leads
    }










































