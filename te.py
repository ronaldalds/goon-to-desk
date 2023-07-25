# from Src.Api.api_desk import Desk

# desk = Desk()
# print(desk.authentication())
from Src.Service.go_on_service import goon_to_desk
from datetime import datetime, timedelta

horario_final = datetime.now()

horario_inicial = horario_final - timedelta(minutes=30)

horario = datetime(year=2023, month=7, day=25, hour=13, minute=00)

print(goon_to_desk(horario, 30))