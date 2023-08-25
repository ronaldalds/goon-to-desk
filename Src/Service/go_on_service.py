
from Src.Api.api_go_on import Goon
from datetime import datetime, timedelta
import re

def get_os_goon(horario, atraso):
    try:
        go_on = Goon()

        horario_inicial = horario - timedelta(minutes=atraso)
        horario_final = horario
        data_to_desk = []

        response = go_on.get_all_located_orders_by_agent(
            agente_codigo=0,
            mobile_agent= "Internal",
            data= horario
        )
        
        if not response:
            return data_to_desk

        chamado_desk = re.compile("[#][0-9]{4}[-][0-9]{6}")

        for os in response:
            if bool(chamado_desk.search(os["Descricao"])):
                os["StatusSequence"] = [att for att in os["StatusSequence"] if horario_inicial <= datetime.strptime(att["DataHora"], "%d/%m/%Y %H:%M:%S") <= horario_final]
                if os["StatusSequence"]:
                    os["chamadoDesk"] = chamado_desk.search(os["Descricao"]).group().replace('#', '')
                    data_to_desk.append(os)

        return data_to_desk
    except Exception as e:
        print(f"Error: {e}")
        return data_to_desk