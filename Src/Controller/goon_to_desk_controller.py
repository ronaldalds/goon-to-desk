from pyrogram import Client
from pyrogram.types import Message
from Src.Service.go_on_service import get_os_goon
from Src.Service.desk_service import set_chamado_desk
from datetime import datetime, timedelta
from time import sleep
from dotenv import dotenv_values

env = dotenv_values(".env")

running = False
tempo_ciclo = int(env["TIME_CLICO"])

def handle_start_goon_to_desk(client: Client, message: Message):
    global running
    if not running:
        running = True
        data = datetime.now()
        message.reply_text("goon_to_desk em execução.")
        print(f"goon_to_desk em execução: {data}- {data.timestamp()}")

        while running:
            sleep(1)
            if datetime.now().strftime("%d/%m/%Y %H:%M") == ((data + timedelta(minutes=tempo_ciclo)).strftime("%d/%m/%Y %H:%M")):
                data = datetime.now()
                print(data)
                res = get_os_goon(data, tempo_ciclo)
                if res:
                    for ocorrencia in res:
                        set_chamado_desk(ocorrencia)

            # Verifica se a execução deve continuar ou parar
            if not running:
                message.reply_text("goon_to_desk parado.")
                break
    else:
        message.reply_text("goon_to_desk em execução.")

def handle_stop_goon_to_desk(client: Client, message: Message):
    global running
    if running:
        running = False
        message.reply_text("Pedido de parada do goon_to_desk iniciado...")
    else:
        message.reply_text("goon_to_desk parado")
        
def handle_status_goon_to_desk(client: Client, message: Message):
    global running
    try:
        if running:
            message.reply_text("goon_to_desk em execução")
        else:
            message.reply_text("goon_to_desk parado")
    except:
        message.reply_text("goon_to_desk parado")