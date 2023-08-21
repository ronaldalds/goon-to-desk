# from Src.Api.api_desk import Desk
# from Src.Api.api_desk import Desk
# from datetime import datetime
# from Src.Util.status import DIAS_SEMANA, MESES_ANO
# status = {
#     'Status': 'AGEN',
#     'DataHora': '23/07/2023 22:47:12',
#     'DataHoraAgendamento': None,
#     'Longitude': None,
#     'Latitude': None,
#     'AgenteCodigo': None,
#     'MobileAgentExternalId': None,
#     'MobileAgentName': 'asdfafga',
#     'MobileAgentPhone': None
# }

# desk = Desk()
# horario = datetime.strptime(status["DataHora"], "%d/%m/%Y %H:%M:%S")
# dia_semana = DIAS_SEMANA[horario.weekday()]
# dia_mes = horario.day
# mes = MESES_ANO[horario.month]
# ano = horario.year
# hora = horario.strftime("%H:%M")
# request = desk.interagir_chamado(
#     chamado_desk="0723-002233",
#     forma_atendimento="000009",
#     cod_status="000006",
#     operador=130,
#     horario=horario,
#     descricao=f"{dia_semana}, {dia_mes} de {mes} de {ano} às {hora}\nOS Go.On: 99999\nStatus: Despachado\nAgente: Ronald Almeida"
# )

# descricao=f"{dia_semana}, {dia_mes} de {mes} de {ano} às {hora}\nOS Go.On: 99999\nStatus: Despachado\nAgente: Ronald Almeida"

# print(request)

# from Src.Service.go_on_service import goon_to_desk
from Src.Api.api_go_on import Goon
from Src.Api.api_desk import Desk
from datetime import datetime, timedelta
# import re

desk = Desk()
response = desk.operador_do_chamado("0823-001332")
print(response)
# horario_final = datetime.now()

# horario_inicial = horario_final - timedelta(days=3)

# horario = datetime(year=2023, month=7, day=25, hour=13, minute=00)

# horario = datetime.now()
# go = Goon()
# response = go.get_all_located_orders_by_agent(
#         agente_codigo=0,
#         mobile_agent= "Internal",
#         data= horario
#     )
# chamado_desk = re.compile("[#][0-9]{4}[-][0-9]{6}")
# data_to_desk = []
# for os in response:
#         if bool(chamado_desk.search(os["Descricao"])):
#             os["chamadoDesk"] = chamado_desk.search(os["Descricao"]).group().replace('#', '')
#             data_to_desk.append(os)
# print(data_to_desk)
# response = go.get_service_orders(data_inicial=horario_inicial, data_fim=horario_final)
# print(response)
# agente = status["MobileAgentName"] if status["MobileAgentName"] != None else "Sem Agente designado"

# print(agente)

# print(goon_to_desk(horario, 120))