# Abreviaturas e seus significados

"""
temp - temperatura atual em ºC
ate - data da consulta
time - hora da consulta
condition_code - código da condição de tempo atual veja a lista
description - descrição da condição de tempo atual no idioma escolhido
currently - retorna se está de dia ou de noite no idioma escolhido
cid - antigo identificador da cidade, pode não estar presente em alguns casos
city - nome da cidade seguido por uma vírgula (mantido para as libs antigas)
humidity - umidade atual em percentual
cloudiness - nebulosidade em percentual, de 0 a 100 NOVO
rain - volume de chuva em mm na última hora NOVO
wind_speedy - velocidade do vento em km/h
wind_direction - direção do vento em grau NOVO
sunrise - nascer do sol em horário local da cidade
sunset - pôr do sol em horário local da cidade
condition_slug - slug da condição de tempo atual veja a lista
city_name - nome da cidade
forecast - array com a previsão do tempo para outros dias
date - data da previsão dd/mm
weekday - dia da semana abreviado
cloudiness - nebulosidade em percentual, de 0 a 100 NOVO
rain - volume de chuva esperado NOVO
rain_probability - probabilidade de chuva em percentual, de 0 a 100 NOVO
wind_speedy - velocidade do vento em km/h NOVO
max - temperatura máxima em ºC
min - temperatura mínima em ºC
description - descrição da previsão
condition - slug da condição veja a lista
"""

from pydantic import BaseModel
from typing import List

# Classes que instânciam os tipos de dados para as variáveis da base modelo
class Forecast (BaseModel):
    date: str
    weekday: str
    max: int
    min: int
    cloudiness: float
    rain: float
    rain_probability: float
    wind_speedy: str
    description: str
    condition: str


class results(BaseModel):
    temp: int
    date: str
    time: str
    condition_code: str
    description: str
    currently: str
    cid: str
    city: str
    img_id: str
    humidity: int
    cloudiness: float
    rain: str
    wind_speedy: str
    wind_direction: int
    sunrise: str
    sunset: str
    condition_slug: str
    city_name: str
    forecast:  List[Forecast]
    cref: str


class RequestDataCity(BaseModel):
    City: str
    State: str


class RequestDataIP(BaseModel):
    IP: str


class ResponseData(BaseModel):
    by: str
    valid_key: bool
    results: results
    execution_time: float
    from_cache: bool

