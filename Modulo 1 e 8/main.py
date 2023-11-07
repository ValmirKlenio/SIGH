# MÓDULO 1: Linha 3 até linha 226

import csv
import datetime

def menu_gestao_leitos():
  print('''Escolha uma opção
  1. Monitoramento em Tempo Real
  2. Priorização de Leitos
  3. Disponibilidade de Leitos
  4. Histórico de Ocupação
  5. Alertas de Capacidade Máxima
  6. Relatórios de Ocupação''')

class Hospital:
  leitos_uti = 20
  CAPACIDADE_ALA_A = 10
  CAPACIDADE_ALA_B = 10

  def __init__(self, id_leito):
    self.leitos_uti = 20
    self.ala_a = 10
    self.ala_b = 10
    self.leitos_ocupados = 0
    self.id_leito = id_leito
    self.leitos_disponiveis = self.leitos_uti - self.leitos_ocupados
    self.leitos = []
    self.historico_ocupacao = {}

  def monitoramento_leitos(self):
    print(f'Leitos UTI: {self.leitos_uti}')
    self.id_leito = int(input('Digite o ID do leito: '))
    if self.id_leito in self.leitos:
      print('Leito já reservado! Tente novamente.')
    while self.id_leito not in self.leitos:
      leito = input('Deseja reserver um leito: ')
      if leito == 'Ss' or leito == 'SIM' or leito == 'Sim' or leito == 'sim':
        self.leitos_uti -= 1
        self.leitos_ocupados += 1
        self.leitos.append({'ID do leito': self.id_leito, 'Status': 'Reservado'})
        print('Leito reservado com sucesso!')
    with open('leitos.csv', 'w', newline='') as arquivo_leitos:
      escritor_csv = csv.writer(arquivo_leitos)
      escritor_csv.writerows(arquivo_leitos)
      print(escritor_csv)
    try:
      with open('dados.csv.csv', 'r') as arquivo_leitos:
        leitor_csv = arquivo_leitos.read()
        print(leitor_csv)
    except FileNotFoundError as erro:
      print(f'ERRO: {erro}. Tente novamente mais tarde!')
    print(f'Leitos UTI em tempo real: {self.leitos_uti}')
  
  def priorizacao_leitos(self):
    print(f'Leitos UTI: {self.leitos_uti}')
    situacao_paciente = input('Digite a situação do paciente [URGENTE ou EMERGÊNCIA]: ')
    if situacao_paciente == 'URGENTE' or situacao_paciente == 'urgente' or situacao_paciente == 'Uu':
      id_leito = int(input('Digite o ID do leito para reserva: '))
      self.leitos_uti -= 1
      self.leitos.append({'ID do leito': id_leito, 'Status': 'Reservado'})
      print('Leito reservado com sucesso!')
    elif situacao_paciente == 'EMERGENCIA' or situacao_paciente == 'emergencia' or situacao_paciente == 'Ee':
      if self.leitos_uti < 20:
        self.id_leito = int(input('Digite o ID do leito para reserva: '))
        self.leitos_uti -= 1
        self.leitos.append({'ID do leito': self.id_leito, 'Status': 'Reservado'})
        print('Leito reservado com sucesso!')
      else:
        print('Sua situação é estável, entre na fila e espere a disponibilidade de um leito.')
  
  def disponibilidade_leitos(self):
    disponib_leito = input('Deseja cancelar a reseva desse leito? ')
    if disponib_leito == 'Ss' or disponib_leito == 'SIM' or disponib_leito == 'Sim' or disponib_leito == 'sim':
      leito = int(input('Digite o ID do leito: '))
      if leito in self.leitos:
        self.leitos.remove({'ID do Leito': leito, 'Situação': 'Disponível'})
        self.leitos_uti += 1
        self.leitos_ocupados -= 1
        print('Leito disponível!')
        self.leitos_disponiveis = self.leitos_uti - self.leitos_ocupados
        print(self.leitos_disponiveis)
    else:
      print('Leito indisponível!')
  
  def monitoramento_leitos(self):
    print(f'Leitos UTI: {self.leitos_uti}')
    self.id_leito = int(input('Digite o ID do leito: '))
    if self.id_leito in self.leitos:
      print('Leito já reservado! Tente novamente.')
    while self.id_leito not in self.leitos:
      leito = input('Deseja reserver um leito: ')
      if leito == 'Ss' or leito == 'SIM' or leito == 'Sim' or leito == 'sim':
        self.leitos_uti -= 1
        self.leitos.append({'ID do leito': self.id_leito, 'Status': 'Reservado'})
        print('Leito reservado com sucesso!')
    with open('leitos.csv', 'w', newline='') as arquivo_leitos:
      escritor_csv = csv.writer(arquivo_leitos)
      escritor_csv.writerows(arquivo_leitos)
      print(escritor_csv)
    try:
      with open('dados.csv.csv', 'r') as arquivo_leitos:
        leitor_csv = arquivo_leitos.read()
        print(leitor_csv)
    except FileNotFoundError as erro:
      print(f'ERRO: {erro}. Tente novamente mais tarde!')
    print(f'Leitos UTI em tempo real: {self.leitos_uti}')

  def priorizacao_leitos(self):
    print(f'Leitos UTI: {self.leitos_uti}')
    situacao_paciente = input('Digite a situação do paciente [URGENTE ou EMERGÊNCIA]: ')
    if situacao_paciente == 'URGENTE' or situacao_paciente == 'urgente' or situacao_paciente == 'Uu':
      self.id_leito = int(input('Digite o ID do leito para reserva: '))
      self.leitos_uti -= 1
      self.leitos.append({'ID do leito': self.id_leito, 'Status': 'Reservado'})
      print('Leito reservado com sucesso!')
    elif situacao_paciente == 'EMERGENCIA' or situacao_paciente == 'emergencia' or situacao_paciente == 'Ee':
      if self.leitos_uti < 20:
        self.id_leito = int(input('Digite o ID do leito para reserva: '))
        self.leitos_uti -= 1
        self.leitos.append({'ID do leito': self.id_leito, 'Status': 'Reservado'})
        print('Leito reservado com sucesso!')
      else:
        print('Sua situação é estável, entre na fila e espere a disponibilidade de um leito.')

  def disponibilidade_leitos():
    disponib_leito = input('Deseja cancelar a reseva desse leito? ')
    if disponib_leito == 'Ss' or disponib_leito == 'SIM' or disponib_leito == 'Sim' or disponib_leito == 'sim':
      leito = int(input('Digite o ID do leito: '))
      if leito in self.leitos:
        self.leitos.remove({'ID do Leito': leito, 'Situação': 'Disponível'})
        self.leitos_uti += 1
        print('Leito disponível!')
    else:
      print('Leito indisponível!')

  def registrar_ocupacao(self, data, uti, ala_a, ala_b):
          self.historico_ocupacao[data] = {'UTI': uti, 'Ala A': ala_a, 'Ala B': ala_b}
          self.verificar_capacidade(data)

  def verificar_capacidade(self, data):
      ocupacao = self.historico_ocupacao[data]
      if ocupacao['UTI'] >= self.leitos_uti * 0.9:
          print(f"Alerta: Capacidade da UTI está acima de 90% em {data}")
      if ocupacao['Ala A'] >= self.CAPACIDADE_ALA_A * 0.9:
          print(f"Alerta: Capacidade da Ala A está acima de 90% em {data}")
      if ocupacao['Ala B'] >= self.CAPACIDADE_ALA_B * 0.9:
          print(f"Alerta: Capacidade da Ala B está acima de 90% em {data}")

  def gerar_relatorio_ocupacao(self, inicio, fim):
      print(f"\nRelatório de Ocupação de {inicio} a {fim}")
      print("Data       | UTI | Ala A | Ala B")
      for data, ocupacao in sorted(self.historico_ocupacao.items()):
          if inicio <= data <= fim:
              print(f"{data} | {ocupacao['UTI']}   | {ocupacao['Ala A']}    | {ocupacao['Ala B']}")

  def imprimir_historico_completo(self):
      print("\nHistórico completo de ocupação")
      print("Data       | UTI | Ala A | Ala B")
      for data, ocupacao in sorted(self.historico_ocupacao.items()):
          print(f"{data} | {ocupacao['UTI']}   | {ocupacao['Ala A']}    | {ocupacao['Ala B']}")

  def exportar_para_csv(self, arquivo):
    with open(arquivo, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Data", "UTI", "Ala A", "Ala B"])
        for data, ocupacao in sorted(self.historico_ocupacao.items()):
            writer.writerow([data, ocupacao['UTI'], ocupacao['Ala A'], ocupacao['Ala B']})
        print(f"Dados de ocupação exportados para {arquivo}")

def solicitar_dados():
    data = input("Digite a data de ocupação (dd/mm/aaaa): ")
    uti = int(input("Digite o número de leitos ocupados na UTI: "))
    ala_a = int(input("Digite o número de leitos ocupados na Ala A: "))
    ala_b = int(input("Digite o número de leitos ocupados na Ala B: "))
    return data, uti, ala_a, ala_b

hospital = Hospital()

while True:
  menu_gestao_leitos():
  opcao_leitos = input('Escolha uma opção: ')
  if opcao_leitos == 1:
    print('-*' * 20)
    print('...::: MONITORAMENTO DE LEITOS EM TEMPO REAL :::...')
    print()
    monitoramento_leitos()
    print()
  elif opcao_leitos == 2:
    print('-*' * 20)
    print('...::: PRIORIZAÇÃO DE LEITOS :::...')
    print()
    priorizacao_leitos()
    print()
  elif opcao_leitos == 3:
    print('-*' * 20)
    print('...::: DISPONIBILIDADE DE LEITOS :::...')
    print()
    disponibilidade_leitos()
    print()
  elif opcao_leitos == 4:
    print('-*' * 20)
    print('...::: HISTÓRICO DE OCUPAÇÃO :::...')
    print()
    data, uti, ala_a, ala_b = solicitar_dados()
    data_obj = datetime.datetime.strptime(data, '%d/%m/%Y').date()
    hospital.registrar_ocupacao(data_obj, uti, ala_a, ala_b)
    print()
  elif opcao_leitos == 5:
    print('-*' * 20)
    print('...::: ALERTA DE CAPACIDADE MÁXIMA :::...')
    print()
    inicio = input("Digite a data inicial para o relatório (dd/mm/aaaa): ")
    fim = input("Digite a data final para o relatório (dd/mm/aaaa): ")
    inicio_obj = datetime.datetime.strptime(inicio, '%d/%m/%Y').date()
    fim_obj = datetime.datetime.strptime(fim, '%d/%m/%Y').date()
    hospital.gerar_relatorio_ocupacao(inicio_obj, fim_obj)
    print()
  elif opcao_leitos == 6:
    print('-*' * 20)
    print('...::: RELATÓRIO DE OCUPAÇÃO :::...')
    print()
    hospital.imprimir_historico_completo()
    print()
  else:
    print('OPÇÃO INVÁLIDA! Tente novamente')
    break
  
# MÓDULO 8: Linha 228 até linha 299

def menu_relatorios():
  print('''Escolha uma opção:
  1. Gerar Relatório em TXT
  2. Gerar Relatório em CSV
  3. Métricas de Ocupação de Leitos
  4. Eficiência no Uso de Equipamentos 
  5. Dados do Atendimento aos Pacientes''')

def gerando_relatorio_txt():
  print()

def gerando_relatorio_csv():
  print()

def metricas_ocup_leitos():
  print()

def eficiencia_equipamentos():
  print()

def dados_atend_paciente():
  nome = input('Digite o nome do paciente: ')
  cpf = input('Digite a idade do paciente: ')
  while nome and cpf not in pacientes:
    print('Paciente não atendido ou dados incorretos!')
    break
  while nome and cpf not in historico_medico:
    print('Paciente não encontrado ou dados incorretos!')
    break
  if nome and cpf in pacientes:
    if nome and cpf in historico_medico:
      print(pacientes)
      print(historico_medico)

while True:
  menu_relatorios()
  opcao_relatorios = input('Escolha uma opção: ')
  if opcao_relatorios == 1:
    print('-*' * 20)
    print('...::: GERAR RELATÓRIOS TXT :::...')
    print()
    # CHAMAR FUNÇÃO
    print()
  elif opcao_relatorios == 2:
    print('-*' * 20)
    print('...::: GERAR RELATÓRIOS CSV :::...')
    print()
    # CHAMAR FUNÇÃO
    print()
  elif opcao_relatorios == 3:
    print('-*' * 20)
    print('...::: MÉTRICAS DE OCUPAÇÃO DE LEITOS :::...')
    print()
    # CHAMAR FUNÇÃO
    print()
  elif opcao_relatorios == 4:
    print('-*' * 20)
    print('...::: EFICIÊNCIA NO USO DE EQUIPAMENTOS :::...')
    print()
    # CHAMAR FUNÇÃO
    print()
  elif opcao_relatorios == 5:
    print('-*' * 20)
    print('...::: DADOS DE ATENDIMENTO DE PACIENTES :::...')
    print()
    dados_atend_paciente()
    print()
  else:
    print('OPÇÃO INVÁLIDA! Tente novamente')
    break
