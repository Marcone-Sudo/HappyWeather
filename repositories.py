# Importando bibliotecas necessárias 
import requests
import json
from scheama import ResponseData, Forecast

# Classe que cria as funções necessárias para o funcionamento da página
class Repositories:

    def GetAPIData(webpath):
        '''
        Função que devolve os dados referentes a solicitação
        '''
        response_API = requests.get(webpath)
        new_data = response_API.text
        response_API.close()
        new_data = json.loads(new_data)
        return new_data


    def Find_By_IP():
        '''
        Função que a partir do IP do usuário, obtém as informações referentes por meio da base da API
        '''
        path ="https://api.hgbrasil.com/weather?key=SUA-CHAVE&user_ip=remote"
        API_Data = Repositories.GetAPIData(path)
        return API_Data
        

    def Find_By_City(local):
        '''
        Função que obtém as informações da base da API sobre a cidade que o usuário escolheu
        '''
        city = local.City.capitalize()
        state = local.State.upper()
        path ="https://api.hgbrasil.com/weather?key=SUA-CHAVE&city_name={},{}".format(city, state)
        API_Data = Repositories.GetAPIData(path)
        if city.upper() == API_Data["results"]["city"].split(",")[0].upper():
            return API_Data
        else: 
            return None


    def Next_Days(forecastData):
        '''
        Função que processa as informações referentes ao clima para serem retornadas
        ao usuário final
        '''
        Forecasts2 = []
        for i in forecastData:

            if i["description"] == "Parcialmente nublado":
                Forecasts2.append(Forecast(date = i["date"],
                                                weekday = i["weekday"],
                                                max = i["max"],
                                                min = i["min"],
                                                cloudiness = i["cloudiness"],
                                                rain = i["rain"],
                                                rain_probability = i["rain_probability"],
                                                wind_speedy = i["wind_speedy"],
                                                description = "Parc. nublado",
                                                condition = i["condition"]))

            else:
                Forecasts2.append(Forecast(date = i["date"],
                                                weekday = i["weekday"],
                                                max = i["max"],
                                                min = i["min"],
                                                cloudiness = i["cloudiness"],
                                                rain = i["rain"],
                                                rain_probability = i["rain_probability"],
                                                wind_speedy = i["wind_speedy"],
                                                description = i["description"],
                                                condition = i["condition"]))
        
        # A variável ThisDay contém a informação referente ao dia atual
        ThisDay = Forecasts2[0]
        del Forecasts2[0]
        Forecasts1 = []
        for _ in range(0,4):
            Forecasts1.append(Forecasts2[0])
            del Forecasts2[0]
        return ThisDay, Forecasts1, Forecasts2


