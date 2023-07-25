import xml.etree.ElementTree as ET
from Src.Api.api_go_on import Goon
from datetime import datetime, timedelta
import re

def parse_goon_xml_to_dict(xml_str) -> dict:
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

def goon_to_desk(horario, atraso):
    go_on = Goon()

    horario_inicial = horario - timedelta(minutes=atraso)
    horario_final = horario

    response = go_on.get_all_located_orders_by_agent(
        agente_codigo=0,
        mobile_agent= "Internal",
        data= horario
    )
    
    if not response:
        return False
    
    xml = response["answersXML"].replace('<>', '-')

    data_goon = parse_goon_xml_to_dict(xml)

    chamado_desk = re.compile("[#][0-9]{4}[-][0-9]{6}")

    data_to_desk = []
    for os in data_goon:
        if bool(chamado_desk.search(os["Descricao"])):
            os["StatusSequence"] = [att for att in os["StatusSequence"] if horario_inicial <= datetime.strptime(att["DataHora"], "%d/%m/%Y %H:%M:%S") <= horario_final]
            if os["StatusSequence"]:
                os["chamadoDesk"] = chamado_desk.search(os["Descricao"]).group().replace('#', '')
                data_to_desk.append(os)

    return data_to_desk