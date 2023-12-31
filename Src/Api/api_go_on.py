import json
import time
import xml.etree.ElementTree as ET
from zeep import Client
from dotenv import dotenv_values

env = dotenv_values(".env")

class Goon:
    def __init__(self):
        self._url = env["URL_API_GO_ON"]

    def parse_goon_xml_to_dict(self, xml_str):
        # Faz o parse do XML para obter o elemento raiz
        root = ET.fromstring(xml_str)

        # Lista para armazenar os dados
        results = []

        # Percorre todas as tags FormAnswer
        for form_answer in root.findall('FormAnswer'):
            form_data = {}

            # Extrai as informações da tag FormAnswer
            for child in form_answer:
                form_data[child.tag] = child.text

            # Lista para armazenar os dados da StatusSequence
            status_sequence_data = []

            # Percorre todas as tags StatusInfo dentro de StatusSequence
            for status_info in form_answer.findall('.//StatusSequence/StatusInfo'):
                status_info_data = {}

                # Extrai as informações da tag StatusInfo
                for child in status_info:
                    status_info_data[child.tag] = child.text

                status_sequence_data.append(status_info_data)

            form_data['StatusSequence'] = status_sequence_data

            # Lista para armazenar os dados da ItemAnswers
            item_answers_data = []

            # Percorre todas as tags ItemAnswer dentro de ItemAnswers
            for item_answer in form_answer.findall('.//ItemAnswers/ItemAnswer'):
                item_answer_data = {}

                # Extrai as informações da tag ItemAnswer
                for child in item_answer:
                    if child.tag == 'Answer':
                        item_answer_data[child.tag] = {
                            inner_child.tag: inner_child.text for inner_child in child
                        }
                    else:
                        item_answer_data[child.tag] = child.text

                item_answers_data.append(item_answer_data)

            form_data['ItemAnswers'] = item_answers_data

            results.append(form_data)

        return results

    def get_all_located_orders_by_agent(self, agente_codigo, mobile_agent, data):
        reques_data = {
            'authCode': env["AUTH_CODE_GET_ALL_LOCATED_ORDERS_BY_AGENT"],
            'clientCode': env["CLIENT_CODE"],
            'agenteCodigo': agente_codigo,
            'mobileAgentCodeSource': mobile_agent,
            'dataFinalizacaoCancelamento': data,
        }

        data_goon = []

        try:
            client = Client(self._url)
            response = client.service.GetAllocatedOrdersByAgent(**reques_data)
        
            dicionario = json.loads(response)

            if not dicionario["success"]:
                return dicionario["success"]
            
            xml = dicionario["answersXML"].replace('<>', '-')

            data_goon = self.parse_goon_xml_to_dict(xml)

            return data_goon

        except Exception as e:
            print(f"Error getting get all located: {e}")
            return False
        