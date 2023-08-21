import requests
from datetime import datetime, timedelta
from dotenv import dotenv_values

env = dotenv_values(".env")

class Desk:
    def __init__(self):
        self.__url_auth = env["END_POINT_AUTH"]
        self.__url_interagir = env["END_POINT_INTERAGIR"]
        self.__url_lista_chamados = env["END_POINT_LISTA_CHAMADOS"]
        self.__url_lista_operadores = env["END_POINT_LISTA_OPERADORES"]
        self.__auth = self.authentication()

    def authentication(self):
        try:
            headers = {"Authorization": env["CHAVE_DESK_ADM"]}
            data_json = {"PublicKey": env["CHAVE_DESK_AMBIENTE"]}
            response = requests.post(self.__url_auth, json=data_json, headers=headers)

            if response.status_code == 200:
                return response.json()
            else:
                print(response)
            
        except Exception as e:
            print(f"Error getting: {e}")
        
    def interagir_chamado(self,
                          chamado_desk,
                          forma_atendimento,
                          cod_status,
                          operador,
                          horario: datetime,
                          descricao
                          ):
        try:
            headers = {"Authorization": self.__auth}
            horario_inicial = horario - timedelta(minutes=2)
            data_json = {
                    "Chave": chamado_desk,
                    "TChamado": {
                        "CodFormaAtendimento": forma_atendimento,
                        "CodStatus": cod_status,
                        "Descricao": descricao,
                        "CodCausa": "",
                        "CodOperador": operador,
                        "CodGrupo": "",
                        "DataInteracao": horario.strftime("%d-%m-%Y"),
                        "HoraInicial": horario_inicial.strftime("%H:%M:%S"),
                        "HoraFinal": horario.strftime("%H:%M")
                    }
                }
            print(chamado_desk)
            print(data_json["TChamado"])
            response = requests.put(self.__url_interagir, json=data_json, headers=headers)

            if response.status_code == 200:
                return response.json()
            else:
                print(response)
        
        except Exception as e:
            print(f"Error Interagir: {e}")
        
    def lista_chamados(self):
        try:
            headers = {"Authorization": self.__auth}

            data_json = {
                    "Pesquisa":"",
                    "Tatual":"",
                    "Ativo":"Todos",
                    "StatusSLA":"N",
                    "Colunas":
                    {
                        "Chave":"on",
                        "CodChamado":"on",
                        "ChaveUsuario":"on",
                        "NomeUsuario":"on",
                        "SobrenomeUsuario":"on",
                        "NomeOperador":"on",
                        "SobrenomeOperador":"on"
                    },
                    "Ordem": [
                        {
                        "Coluna": "Chave",
                        "Direcao": "false"
                        }
                    ]
                    }
            
            response = requests.post(self.__url_lista_chamados, json=data_json, headers=headers)

            if response.status_code == 200:
                return response.json()
            else:
                print(response)
        
        except Exception as e:
            print(f"Error lista chamados: {e}")
        
    def lista_operador(self):
        try:
            headers = {"Authorization": self.__auth}

            data_json = {
                    "Colunas": {
                        "Chave": "on",
                        "Nome": "on",
                        "Sobrenome": "on",
                        "Email": "on",
                        "OnOff": "on",
                        "GrupoPrincipal": "on",
                        "EmailGrupo": "on",
                        "CodGrupo": "on"
                    },  
                    "Pesquisa": "",
                    "Ativo": "S",
                    "Filtro":
                    {
                    "Ramal":[""],
                        "GrupoPrincipal":[""],
                        "Perfil":[""],
                        "Online":[""],
                        "LicencaDMS":[""],
                        "LicencaCHAT":[""],
                        "LicencaRCS":[""],
                        "LicencaFornecedor":[""]
                    },
                    "Ordem":
                    [ 
                        {
                        "Coluna": "Nome", 
                        "Direcao": "true"
                        }
                    ]
                    }
            
            response = requests.post(self.__url_lista_operadores, json=data_json, headers=headers)

            if response.status_code == 200:
                return response.json()
            else:
                print(response)
        
        except Exception as e:
            print(f"Error lista operador: {e}")
        
    def operador_do_chamado(self, id_chamado):
        chamados = self.lista_chamados()
        operadores = self.lista_operador()
        
        for chamado in chamados["root"]:
            try:
                if chamado["CodChamado"] == id_chamado:
                    try:
                        operador_chamado = {
                            "NomeOperador": chamado["NomeOperador"],
                            "SobrenomeOperador": chamado["SobrenomeOperador"],
                        }
                        for operador in operadores["root"]:
                            if (operador["Nome"] == operador_chamado["NomeOperador"]) and (operador["Sobrenome"] == operador_chamado["SobrenomeOperador"]):
                                return operador["Chave"]

                    except Exception as e:
                        print(f"chamado sem Operador associado! {e}")
                        return False

            except Exception as e:
                print(f"Error operador do chamado {e}")
                return False