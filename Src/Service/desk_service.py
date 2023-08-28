from Src.Api.api_desk import Desk
from datetime import datetime
from Src.Util.status import DIAS_SEMANA, MESES_ANO, STATUS_GOON, FORMA_ATENDIMENTO_DESK, STATUS_DESK

def set_chamado_desk(os_goon):
    try:
        # instancia objeto Desk
        desk = Desk()

        # id do chamado no desk
        chamado_desk = os_goon["chamadoDesk"]

        # descrição da O.S
        descricao = os_goon["Descricao"].replace(f"#{chamado_desk}", '')

        # id os no go.on
        numero_os = os_goon["NumeroOS"]

        # operador para interagir no chamado do desk
        operador = desk.operador_do_chamado(chamado_desk)

        if not operador:
            return

        # itera em quantos status acumulado tem para interagir no chamado do desk
        for status in os_goon["StatusSequence"]:
            # transforma a string data em objeto datetime
            horario = datetime.strptime(status["DataHora"], "%d/%m/%Y %H:%M:%S")

            # dia da semana string
            dia_semana = DIAS_SEMANA[horario.weekday()]

            # dia do mes int
            dia_mes = horario.day

            # mes do ano string
            mes = MESES_ANO[horario.month]

            # ano int
            ano = horario.year

            # hora e minuto str
            hora = horario.strftime("%H:%M")

            # situação do chamado no momento
            situacao = STATUS_GOON[status["Status"]]

            # agente designado para a OS no go.on
            agente = status["MobileAgentName"] if status["MobileAgentName"] != None else "Sem Agente designado"
            
            # momento da criação do status "Qui, 20 de Julho de 2023 às 14:37"
            momento = f"{dia_semana}, {dia_mes} de {mes} de {ano} às {hora}"

            detalhamento_status = f"{momento}\nOS Go.On: {numero_os}\nDescrição: {descricao}\nStatus: {situacao}\nAgente: {agente}"

            # faz request no end point API desk para interagir com o chamado
            request = desk.interagir_chamado(
                chamado_desk = chamado_desk,
                forma_atendimento = FORMA_ATENDIMENTO_DESK["Desk Manager"],
                cod_status = STATUS_DESK["Andamento"],
                operador = operador,
                horario = horario,
                descricao = detalhamento_status
            )

            return request
    except Exception as e:
        print(f"Error set_chamado_desk: {e}")
        return