STATUS_GOON = {
    'DESP': 'Despachado',
    'AGEN': 'Agendado',
    'ACTE': 'Recebido pelo Agente',
    'TACM': 'Agente a caminho',
    'CCLI': 'Cancelado pelo cliente',
    'COPE': 'Cancelado pelo operador',
    'CTEC': 'Cancelado pelo agente',
    'INIC': 'Em Atendimento',
    'FIOK1': 'Pausado',
    'DESP2': 'Despachado',
    'ACTE2': 'Recebido pelo Agente',
    'FIOK': 'Finalizado',
}

USUARIO_DESK = {
    "Iran": 123, # Iran
    "Guilherme": 121, # Guilherme
    "Erivelton": 130, # Erivelton
    "Daniel": 124, # Daniel
    "Wescley": 125, # Wescley
    "Silvio": 131, # Silvio
    "Bruno": 201 # Bruno
}

CHAVE_OPERADOR_DESK = {
    46: USUARIO_DESK["Erivelton"],
}

STATUS_DESK = {
   "Agendamento": "000004",
   "Andamento": "000006",
   "Cancelado": "000003",
   "Resolvido": "000002"
}

FORMA_ATENDIMENTO_DESK = {
   "Desk Manager": "000009",
   "Acesso Remoto": "000001",
   "Whatsapp": "000051"
}

DIAS_SEMANA = {
    0: "Seg",
    1: "Ter",
    2: "Qua",
    3: "Qui",
    4: "Sex",
    5: "Sáb",
    6: "Dom"
}

MESES_ANO = [
    None,
    "Janeiro",
    "Fevereiro",
    "Março",
    "Abril",
    "Maio",
    "Junho",
    "Julho",
    "Agosto",
    "Setembro",
    "Outubro",
    "Novembro",
    "Dezembro"
]