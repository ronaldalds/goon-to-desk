import requests
from datetime import datetime
from dotenv import dotenv_values

env = dotenv_values(".env")

class Desk:
    def __init__(self):
        self.__url_auth = env["END_POINT_AUTH"]
        self.__url_interagir = env["END_POINT_INTERAGIR"]

    def authentication(self):
        headers = {"Authorization": env["CHAVE_DESK_ADM"]}
        data_json = {
            "PublicKey": env["CHAVE_DESK_AMBIENTE"]
        }
        response = requests.post(self.__url_auth, json=data_json, headers=headers)

        if response.status_code == 200:
            return response.json()
        else:
            return False
        
    def interagir_chamado(self,
                          chamado_desk,
                          forma_atendimento,
                          cod_status,
                          operador,
                          horario: datetime,
                          descricao
                          ):

        headers = {"Authorization": self.authentication()}

        data_json = {
                "Chave": chamado_desk,
                "TChamado": {
                    "CodFormaAtendimento": forma_atendimento,
                    "CodStatus": cod_status,
                    "Descricao": descricao,
                    "CodOperador": operador,
                    "DataInteracao": horario.strftime("%d/%m/%Y"),
                    "HoraInicial": horario.strftime("%H:%M"),
                    "HoraFinal": horario.strftime("%H:%M")
                }
            }
        
        response = requests.put(self.__url_interagir, json=data_json, headers=headers)

        if response.status_code == 200:
            return response.json()
        else:
            return False