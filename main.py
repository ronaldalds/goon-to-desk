from pyrogram import Client, filters
from pyrogram.types import Message
from Src.Middleware.authentication import authorization_group, authorization_adm
from Src.Controller.goon_to_desk_controller import handle_start_goon_to_desk, handle_stop_goon_to_desk, handle_status_goon_to_desk
from dotenv import dotenv_values

env = dotenv_values(".env")

version = "0.0.4"

app = Client(
    name=env["BOT_NAME_TELEGRAM"], 
    api_hash=env["API_HASH_TELEGRAM"],
    api_id=env["API_ID_TELEGRAM"],
    bot_token=env["BOT_TOKEN_TELEGRAM"]
    )

chat_adm = [
    int(env["CHAT_ID_ADM"]),
]

chat_goon_to_desk = [
    int(env["CHAT_ID_GROUP_GO_TO_DESK"]),
]

@app.on_message(filters.command("start"))
def start(client, message: Message):
    message.reply_text(f"""
/goon - Integração goon e desk
/chat - Informa seu chat_id
/chatgroup - Informa chat_id grupo
""")

@app.on_message(filters.command("goon"))
@authorization_group(chat_goon_to_desk)
def financeiro(client, message: Message):
    message.reply_text(f"""
/iniciar_goon - Iniciar integração
/parar_goon - Parar integração
/status_goon - Status integração
""")

@app.on_message(filters.command("chatgroup"))
@authorization_adm(chat_adm)
def handle_chatgroup_id(client: Client, message: Message):
    client.send_message(message.from_user.id, message)

@app.on_message(filters.command("chat"))
def handle_chat_id(client: Client, message: Message):
    text = f"{message.from_user.first_name}.{message.from_user.last_name} - ID:{message.from_user.id}"
    client.send_message(message.from_user.id, text)
    print(text)

# iniciar x9
@app.on_message(filters.command("iniciar_goon"))
@authorization_group(chat_goon_to_desk)
def iniciar_goon_to_desk(client: Client, message: Message):
    handle_start_goon_to_desk(client, message)

# parar x9
@app.on_message(filters.command("parar_goon"))
@authorization_group(chat_goon_to_desk)
def parar_goon_to_desk(client: Client, message: Message):
    handle_stop_goon_to_desk(client, message)

# status x9
@app.on_message(filters.command("status_goon"))
@authorization_group(chat_goon_to_desk)
def status_goon_to_desk(client: Client, message: Message):
    handle_status_goon_to_desk(client, message)

# stop service
@app.on_message(filters.command("stop_service"))
@authorization_adm(chat_adm)
def stop(client: Client, message: Message):
    print("Service Stopping")
    app.stop()

print("Service Telegram Up!")
print(f"Version {version}")
app.run()

