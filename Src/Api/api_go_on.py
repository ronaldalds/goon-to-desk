import json
from zeep import Client
from dotenv import dotenv_values

env = dotenv_values(".env")

class Goon:
    def __init__(self):
        self._url = env["URL_API_GO_ON"]
        self._client = Client(self._url)

    def get_all_located_orders_by_agent(self, agente_codigo, mobile_agent, data) -> dict:
        reques_data = {
            'authCode': env["AUTH_CODE_GET_ALL_LOCATED_ORDERS_BY_AGENT"],
            'clientCode': env["CLIENT_CODE"],
            'agenteCodigo': agente_codigo,
            'mobileAgentCodeSource': mobile_agent,
            'dataFinalizacaoCancelamento': data,
        }

        try:
            response = self._client.service.GetAllocatedOrdersByAgent(**reques_data)
        
            dicionario = json.loads(response)

            if not dicionario["success"]:
                return dicionario["success"]
            
            return dicionario

        except Exception as e:
            print(f"Error getting: {e}")
            return False
