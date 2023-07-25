import requests
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
        
    def interagir_chamado(self, os: dict):
        headers = {"Authorization": self.authentication()}
        data_json = {
            "Chave":"0723-001927",
            "TChamado": {
                "CodFormaAtendimento": "000009",
                "CodStatus": "000006",
                "CodAprovador":[""],
                "TransferirOperador":"",
                "TransferirGrupo":"",
                "CodTerceiros":"",
                "Protocolo":"",
                "Descricao": "TEST TEST TEST TEST",
                "CodAgendamento":"",
                "DataAgendamento":"",
                "HoraAgendamento":"",
                "CodCausa":"",
                "CodOperador":"",
                "CodGrupo":"",
                "EnviarEmail":"S",
                "EnvBase":"N",
                "CodFPMsg":"",
                "DataInteracao": "29-08-2017",
                "HoraInicial": "09:46:42",
                "HoraFinal": "09:47",
                "SMS": "",
                "ObservacaoInterna": "",
                "PrimeiroAtendimento": "N",
                "SegundoAtendimento": "N"
            },
            "TIc":{
                "Chave":{
                    "278":"on",
                    "280":"on"	
                }
            }
        }