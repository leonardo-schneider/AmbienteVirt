from fastapi import FastAPI, Query
import requests

app = FastAPI()
url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
response = requests.get(url)

@app.get('/api/hello')
def hello_world():
    '''
    Endpoint que exibe uma mensagem expecional do mundo da programacao
    '''
    return{'Hello': 'World'}

@app.get('/api/restaurantes/')
def get_restaurantes(restaurante: str = Query(None)):
    
    ''' 
    Endpoint para ver os cardapios dos restaurantes
    
    '''
    if response.status_code == 200:
        dados_json = response.json()
        if restaurante is None:
            return {'dados': dados_json} 
        
        dados_restaurante = []
        for item in dados_json:
            if item['Company'] == restaurante:
                dados_restaurante.append({
                    "item": item['Item'],
                    "price": item['price'],
                    "description": item['description']
            })    
        return{'Restaurante':restaurante,'Cardapio':dados_restaurante}
    else:
        return{'Erro':f'{response.status_code} - {response.text}'}