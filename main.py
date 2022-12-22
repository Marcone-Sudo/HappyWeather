# Importação das bibliotecas necessárias
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

# Importando as rotas para a cidade e para o IP
from routers.Get_By_City import router as Get_by_City
from routers.Get_By_IP import router as Get_by_IP

# Instanciando o framework Fast API
app = FastAPI()

# Acessa por meio do Jinja2 os templates HTML contidos no diretório em questão
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

# De acordo com a escolha do usuário é devolvido como resposta a página de interesse
# Inicialmente é carregada a página inicial
@app.get("/", response_class= HTMLResponse)
async def home(request: Request):

    return templates.TemplateResponse("Homepage.html",{"request": request})


# Caso seja selecionada a opção de selecionar uma cidade
@app.get("/pickWay/choice", response_class= HTMLResponse)
async def home(request: Request):

    return templates.TemplateResponse("pickWay/choice.html",{"request": request})


# Caso seja selecionada a opção de Home Page
@app.get("/Homepage", response_class= HTMLResponse)
async def home(request: Request):

    return templates.TemplateResponse("Homepage.html",{"request": request})


app.include_router(Get_by_City)
app.include_router(Get_by_IP)

