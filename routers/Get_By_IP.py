# Importa as bibliotecas necessárias

from fastapi import APIRouter, Request
from repositories import Repositories
from scheama import ResponseData, Forecast
from fastapi.templating import Jinja2Templates

# Instancia uma rota do FastAPI
router = APIRouter()
templates = Jinja2Templates(directory="templates")

# Com base na geolocalização do IP do usuário, retorna as informações sobre o clima
# para a sua cidade
@router.get("/Results/Results_heather",  response_model= ResponseData, response_description="I found the Data ;)")
def get_data_Ip( request: Request):
    
    data = Repositories.Find_By_IP()
    ThisDay, Forecasts1, Forecasts2 = Repositories.Next_Days(data["results"]["forecast"])

    return templates.TemplateResponse("Results/Results_heather.html",{"request": request, "Temp": data["results"]["temp"],
                                        "Wind_speedy":data["results"]["wind_speedy"], "Humidity": data["results"]["humidity"],
                                        "City": data["results"]["city"],"ThisDay": ThisDay ,"forecasts":Forecasts1, "forecasts2": Forecasts2})