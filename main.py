# BIBLIOTECAS
import datetime
import csv
from PIL import Image
import os
import glob

# LISTAS / DICIONÁRIOS
pacientes = []
historico_medico = []
leitos = []
equipamentos = []
medicamentos = []
visitas = []
profissionais_saude = []

LEITOS_UTI = 20

def menu():
  print('''Escolha uma opção:
  [ 1 ]  - Gestão de Leitos
  [ 2 ]  - Controle de Equipamentos
  [ 3 ]  - Administração de Medicamentos
  [ 4 ]  - Agendamento e Controle de Visitas
  [ 5 ]  - Pontuário Eletrônico
  [ 6 ]  - Gestão de Equipes
  [ 7 ]  - Cadastro de Visitantes
  [ 8 ]  - Relatórios e Análises
  [ 9 ]  - Localizar Arquivos TXT
  [ 10 ] - Exluir Arquivos TXT
  [ 11 ] - Localizar Arquivos CSV
  [ 12 ] - Exluir Arquivos CSV ''')

# CÓDIGO

# MÓDULO 1
def menu_gestao_leitos():
  print('''Escolha uma opção
  1. Monitoramento em Tempo Real
  2. Priorização de Leitos
  3. Disponibilidade de Leitos
  4. Histórico de Ocupação
  5. Alertas de Capacidade Máxima
  6. Relatórios de Ocupação
  7. Exportar em CSV''')

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


# MÓDULO 2
class Equipamento:
    def __init__(self, nome, modelo, numero_serie, data_aquisicao):
        self.nome = nome
        self.modelo = modelo
        self.numero_serie = numero_serie
        self.data_aquisicao = data_aquisicao
        self.manutencoes = []

    def registrar_manutencao(self, data, tipo, intervencao):
        self.manutencoes.append({"data": data, "tipo": tipo, "intervencao": intervencao})

equipamentos = []

def cadastrar_equipamento(nome, modelo, numero_serie, data_aquisicao):
    equipamento = Equipamento(nome, modelo, numero_serie, data_aquisicao)
    equipamentos.append(equipamento)

def registrar_manutencao(numero_serie, data, tipo, intervencao):
    for equipamento in equipamentos:
        if equipamento.numero_serie == numero_serie:
            equipamento.registrar_manutencao(data, tipo, intervencao)
            print("Manutenção registrada com sucesso.")
            return

    print("Equipamento não encontrado.")

def historico_manutencoes(numero_serie):
    for equipamento in equipamentos:
        if equipamento.numero_serie == numero_serie:
            print(f"Histórico de manutenções para {equipamento.nome} ({equipamento.modelo}):")
            for manutencao in equipamento.manutencoes:
                print(f"Data: {manutencao['data']}, Tipo: {manutencao['tipo']}, Intervenções: {manutencao['intervencao']}")
            return

    print("Equipamento não encontrado.")

def main():
    while True:
      print('''Escolha uma opção:
      1. Cadastrar Equipamento
      2. Registrar Manutenção
      3. Ver Histórico de Manutenções
      4. Sair''')
      opcao_eq = int(input("Escolha uma opção: "))
      if opcao_eq == 1:
          nome = input("Nome do equipamento: ")
          modelo = input("Modelo: ")
          numero_serie = input("Número de série: ")
          data_aquisicao = input("Data de aquisição: ")
          cadastrar_equipamento(nome, modelo, numero_serie, data_aquisicao)
      elif opcao_eq == 2:
          numero_serie = input("Número de série do equipamento: ")
          data = input("Data da manutenção: ")
          tipo = input("Tipo de manutenção: ")
          intervencao = input("Intervenções realizadas: ")
          registrar_manutencao(numero_serie, data, tipo, intervencao)
      elif opcao_eq == 3:
          numero_serie = input("Número de série do equipamento: ")
          historico_manutencoes(numero_serie)
      elif opcao_eq == 4:
          break
      else:
          print("Opção inválida. Tente novamente.")

# MÓDULO 3
class Medicamento:
  def __init__(self, nome, principio_ativo, dosagem, forma_administracao):
      self.nome = nome
      self.principio_ativo = principio_ativo
      self.dosagem = dosagem
      self.forma_administracao = forma_administracao

class EstoqueMedicamentos:
  def __init__(self):
      self.medicamentos = []

  def adicionar_medicamento(self, medicamento, quantidade, lote, data_validade, fornecedor):
      self.medicamentos.append({
          'medicamento': medicamento,
          'quantidade': quantidade,
          'lote': lote,
          'data_validade': data_validade,
          'fornecedor': fornecedor
      })

  def verificar_estoque_baixo(self, medicamento):
      for med in self.medicamentos:
          if med['medicamento'] == medicamento and med['quantidade'] < 10:
              return True
      return False

class RegistroAdministracao:
  def __init__(self):
      self.registros = []

  def registrar_administracao(self, medicamento, data, horario, paciente, dosagem, responsavel):
      self.registros.append({
          'medicamento': medicamento,
          'data': data,
          'horario': horario,
          'paciente': paciente,
          'dosagem': dosagem,
          'responsavel': responsavel
      })

class ProntuarioEletronico:
  def __init__(self):
      self.registros = []

  def adicionar_registro(self, paciente, medicamento, data, dosagem):
      self.registros.append({
          'paciente': paciente,
          'medicamento': medicamento,
          'data': data,
          'dosagem': dosagem
      })

def adicionar_medicamento_ao_estoque(estoque, medicamento, quantidade, lote, data_validade, fornecedor):
  estoque.adicionar_medicamento(medicamento, quantidade, lote, data_validade, fornecedor)

def verificar_estoque_baixo(estoque, medicamento):
  return estoque.verificar_estoque_baixo(medicamento)

def registrar_administracao(registro, medicamento, data, horario, paciente, dosagem, responsavel):
  registro.registrar_administracao(medicamento, data, horario, paciente, dosagem, responsavel)

def adicionar_registro_prontuario(prontuario, paciente, medicamento, data, dosagem):
  prontuario.adicionar_registro(paciente, medicamento, data, dosagem)

def exibir_menu():
  print('''MENU
  1. Adicionar Medicamentos ao Estoque
  2. Verificar Estoque Baixo
  3. Registrar Administração
  4. Adicionar Registro ao Pontuário Eletrônico
  5. Sair''')

estoque = EstoqueMedicamentos()
registro = RegistroAdministracao()
prontuario = ProntuarioEletronico()

# MÓDULO 4
def menu_controle_visita():
  print('''Escolha uma opção:
  [ 1 ] - Agendar Visita
  [ 2 ] - Restrições das Visitas
  [ 3 ] - Registro de Visitantes
  [ 4 ] - Detalhes do Agendamento
  [ 5 ] - Cancelamento e Reagendamento de Visita''')

def agendamento_visita():
  nome = input('Nome:')
  cpf = input('CPF: ')
  print('''Guia Informativo sobre parentesco:
  Grau 1: Mãe ou Pai, Filha ou Filho.
  Grau 2: Avó ou Avô, Neta ou Neto, Irmã ou Irmão.
  Grau 3: Bisavó ou Bisavô, Bisneta ou Bisneto, Tia ou Tio, Sobrinha ou Sobrinho.''')
  paciente = input('Paciente que deseja visitar: ')
  parentesco = input('Qual seu grau de parentesco com o paciente? ')
  dia_visita = input('Dia da semana para visita: ')
  while dia_visita in visitas:
    dia_visita = input('Dia já agendado! Escolha outro: ')
    if dia_visita not in visitas:
      print('Dia agendado com sucesso!')
      break
  data_agendamento = input('Data do agendamento (dd/mm/aaa): ')
  while data_agendamento in visitas:
    data_agendamento = input('DATA JÁ AGENDADA! Escolha outra data: ')
    if data_agendamento not in visitas:
      print('Data agendada com sucesso!')
      break
  hora_agendamento = input('Hora do agendamento (hh:mm): ')
  while hora_agendamento in visitas:
    hora_agendamento = input('HORA JÁ AGENDADA! Escolha outra hora: ')
    if hora_agendamento not in visitas:
      print('Hora agendada com sucesso!')
      break
  visitas.append({'Nome': nome, 'CPF': cpf, 'Paciente': paciente, 'Parentesco': parentesco, 'Data do Agendamento': data_agendamento, 'Hora do agendamento': hora_agendamento})
  print(visitas)
  print(f'Agendamento realizado com sucesso!')

def restricoes():
  print('''RESTRIÇÕES:
  Número máximo de visitas por pessoa: 2
  Duração máxima da visita: 2H
  Dias permitidos: Terça e Quinta''')
  num_max_visitas = 2
  visitas = int(input('Digite a quandidade de visitas que pretende ver o paciente: '))
  if visitas > 2:
    print('Número máximo de visitas excedido! Permitido apenas 2 pessoas por paciente.')
  horario_dia_visita = {'terca': ['10:00-12:00'],
                        'quinta': ['10:00-12:00', '15:00-17:00']}
  dia_visita = input('Digite o dia da visita (TERÇA ou QUINTA): ')
  if dia_visita != 'Terça' and dia_visita != 'Quinta':
    print('Dias de visita inválido! Visitas apenas nos dias TERÇA e QUINTA')
  hora_inico = input(f'Digite o horário do início da visita (hh:mm): ')
  print('LEMBRANDO: Só é permitido 2 HORAS de vista por paciente!')
  hora_final = input(f'Digite o horário do término da visita (hh:mm): ')
  if dia_visita in horario_dia_visita:
    for horario in horario_dia_visita[dia_visita]:
      hora_inicio, hora_final = horario.split('-')
      if hora_inicio and hora_final in horario_dia_visita:
        print('Dia e Horário dentro das Restrições!')
        return True
  print(f'Restrições da visita: Pemitido apenas {num_max_visitas} pessoas por visita, Com duração máxima de 2H, Sendo permitido entre os dias e horários {horario_dia_visita}')
  print()

def registro_visitantes():
  nome = input('Digite seu nome: ')
  cpf = input('Digite seu CPF: ')
  while nome and cpf not in visitas:
    print('Visita não agendada! Nome e CPF não encontrados.')
    print('Se dirija a parte do Agendamento de Visita e realize o seu!')
    if nome and cpf in visitas:
       print('Visita registrada! Acesso permitido.')
       break
  # Garantir que apenas pessoas autorizadas (com agendamento) possam entrar no local
  print()

def detalhes_agendamento():
  nome = input('Digite seu nome: ')
  cpf = input('Digite seu CPF: ')
  for agendamento in visitas:
    nome, cpf, paciente, parentesco, data_agendamento, hora_agendamento = agendamento
    print('Detalhes do seu agendamento: ')
    print(agendamento)
    print(f'ATENÇÃO! Restrições da Visita: {restricoes()}')
  print()

def cancelamento_reagendamento_visita():
  nome = input('Nome: ')
  cpf = input('CPF: ')
  while nome and cpf not in visitas:
    print('Visita não agendada! Nome e CPF não encontrados.') 
    if nome and cpf in visitas:
      for c in visitas:
        nome, cpf, paciente, parentesco, data_agendamento, hora_agendamento = c
        print(c)
        r = input('Deseja cancelar essa visita? ')
        if r == 'Ss' or r == 'SIM' or r == 'sim' or r == 'Sim' :
          visitas.remove({'Nome': nome, 'CPF': cpf, 'Parentesco': parentesco, 'Data do Agendamento': data_agendamento, 'Hora do agendamento': hora_agendamento})
        else:
          break
    print('Visita cancelada com sucesso!')
    reagendamento = input('Deseja reagendar sua visita? ')
    if reagendamento == 'Ss' or reagendamento == 'SIM' or reagendamento == 'sim' or reagendamento == 'Sim':
      print('PRESTE ATENÇÃO AS RESTRIÇÕES!')
      nome = input('Nome:')
      cpf = input('CPF: ')
      paciente = input('Paciente que deseja visitar: ')
      parentesco = input('Qual seu grau de parentesco com o paciente? ')
      data_agendamento = input('Data do agendamento (dd/mm/aaa): ')
      hora_agendamento = input('Hora do agendamento (hh:mm): ')
      visitas.append({'Nome': nome, 'CPF': cpf, 'Parentesco': parentesco, 'Data do Agendamento': data_agendamento, 'Hora do agendamento': hora_agendamento})
      print('Reagenado com sucesso!')
    else:
      break

  print()

# MÓDULO 5
def menu_pontuario():
  print('''Escolha uma opção:
  [ 1 ] - Cadastrar Pacientes
  [ 2 ] - Registrar Diagnósticos
  [ 3 ] - Acompanhamento do Tratamento
  [ 4 ] - Evolução Clínica
  [ 5 ] - Anexo de Exames e Imagens''')

def cadastrar_paciente():
  nome = input('Nome: ')
  cpf = input('CPF: ')
  idade = int(input('Idade: '))
  sexo = input('Sexo [F / M]: ')
  while sexo not in 'FfMm':
    sexo = input('ERRO! Digite somente F(feminino) ou M(masculino): ')
    if sexo == 'FfMm':
      break
  historico_med = input('Histórico Médico: ')
  contato_emerg = int(input('Contato de Emergência: '))
  contato_emerg_sec = int(input('Digite outro Contato de Emergência: '))
  pacientes.append({'Nome': nome, 'CPF': cpf, 'Idade': idade, 'Sexo': sexo, 'Histórico Médico': historico_med, 'Contato Emergência Principal': contato_emerg, 'Contato Emergência Secundário': contato_emerg_sec})
  # ARQUIVOS .TXT
  with open('pacientes.txt', 'w') as arq:
      for p in pacientes:
          arq.write(pacientes[p])
          print()
  # ARQUIVO DE LEITURA
  try:
    with open('pacientes.txt', 'r') as arq:
        for r in pacientes:
            arq.readlines(pacientes[r])
            print(r)
            print()
  except FileNotFoundError as erro:
    print(f'Erro {erro}. Arquivo não encontrado!')
  print('Paciente cadastrado com sucesso!')

def registro_diagnostico():
  nome_paciente = input('Nome do paciente: ')
  cpf_paciente = input('CPF do paciente: ')
  while nome_paciente and cpf_paciente in pacientes: 
    print('Paciente com o diagnóstico já registrado')
    nome_paciente = input('Digite outro nome: ')
    cpf_paciente = input('Digite outro CPF: ')
    if nome_paciente and cpf_paciente not in pacientes:
      continue
  sintomas = input('Sintomas: ')
  diagnostico = input('Diagnóstico do paciente: ')
  descricao_condicao = input('Condição do paciente: ')
  tratamento = input('Recomendações de tratamento: ')
  data_diagnostico = int(input('Data do diagnóstico (dd/mm/aaaa): '))
  historico_medico.append({'Paciente': nome_paciente, 'CPF': cpf_paciente, 'Sintomas': sintomas, 'Diagnóstico': diagnostico, 'Condição do Paciente': descricao_condicao, 'Tratamento': tratamento, 'Data do Diagnóstico': data_diagnostico})
  # ARQUIVOS .TXT
  with open('diagnostico_pacientes.txt', 'w') as arq_p:
    for p in historico_medico:
#      nome_paciente, cpf_paciente, sintomas, diagnostico, descricao_condicao, tratamento, data_diagnostico = p
        arq_p.write(historico_medico[p])
        print()
  # ARQUIVO DE LEITURA
  try:
    with open('diagnostico_pacientes.txt', 'r') as arq_p:
        for r in pacientes:
            arq_p.readlines(pacientes[r])
            print(r)
            print()
  except FileNotFoundError as erro:
    print(f'Erro {erro}. Arquivo não encontrado!')

  print('Diagnótico registrado com sucesso!')

def acompanhamento_tratamento():
  print('''O que gostaria de fazer?
  1 - Analisar Diagnóstico
  2 - Prescrever medicamentos
  3 - Prescrever procedimentos
  4 - Prescrever terapia
  5 - Prescrever exames''')
  opc = int(input('Opção: '))
  if opc == 1:
    nome = input('Nome do Paciente: ')
    cpf = input('CPF do Paciente: ')
    for t in pacientes:
      nome, cpf, diagnostico, descricao_condicao, tratamento, data_diagnostico = t.values()
      print(':: Histórico Médico do Paciente ::')
      print(t)
  elif opc == 2:
    nome = input('Nome do Paciente: ')
    cpf = input('CPF do Paciente: ')
    while nome and cpf in historico_medico:
      medicamento = input('Medicamento que deseja prescrever: ')
      historico_medico.append({'Medicamento': medicamento})
      print(f'Medicamento {medicamento} prescrito ao paciente {nome} com sucesso!')
  elif opc == 3:
    nome = input('Nome do Paciente: ')
    cpf = input('CPF do Paciente: ')
    while nome and cpf in historico_medico:
      procedimento = input('Procedimento que deseja prescrever: ')
      historico_medico.append({'Procedimento': procedimento})
      print(f'Procedimento {procedimento} prescrito ao paciente {nome} com sucesso!')
  elif opc == 4:
    nome = input('Nome do Paciente: ')
    cpf = input('CPF do Paciente: ')
    while nome and cpf in historico_medico:
      terapia = input('Terapia que deseja prescrever: ')
      data_terapia = input('Data da Terapia (dd/mm/aaaa): ')
      historico_medico.append({'Terapia': terapia, 'Data da Terapia': data_terapia})
      print(f'Terapia {terapia} prescrito ao paciente {nome}, para a data {data_terapia} com sucesso!')
  elif opc == 5:
    nome = input('Nome do Paciente: ')
    cpf = input('CPF do Paciente: ')
    while nome and cpf in historico_medico:
      exame = input('Exame que deseja prescrever: ')
      data_exame = input('Data do exame (dd/mm/aaaa): ')
      historico_medico.append({'Exame': exame, 'Data do exame': data_exame})
      print(f'Exame {exame} prescrito ao paciente {nome}, para a data {data_exame} com sucesso!')
  else:
    print('OPÇÃO INVÁLIDA')

def evolucao_clinica():
  print('''Escolha uma opção:
  1 - Ver histórico médico
  2 - Atualizar situação clínica''')
  op = int(input('Opção: '))
  if op == 1:
    nome = input('Nome do Paciente: ')
    cpf = input('CPf do Paciente: ')
    for historico in historico_medico:
      nome, cpf, diagnostico, data_diagnostico, descricao_condicao, tratamento, medicamentos, procedimentos, terapia, data_terapia, exame, data_exame = historico
      print(':: HISTÓRICO MÉDICO DO PACIENTE ::')
      print(historico)
  elif op == 2:
    cpf = input('CPF do Paciente: ')
    while cpf in historico_medico:
      print('ATUALIZAÇÃO DA SITUAÇÃO CLÍNICA')
      novo_diagnostico = input('Novo Dignóstico: ')
      data_novo_diagnostico = input('Data (DD/MM/AAAA): ')
      nova_condicao = input('Nova Condição: ')
      novo_tratamento = input('Novo Tratamento: ')
      novo_medicamento = input('Novo Medicamento: ')
      novo_procedimento = input('Novo Procedimento: ')
      novo_exame = input('Novo Exame: ')
      data_novo_exame = input('Data (DD/MM/AAAA): ')
      observacoes = input('Observações: ')
      historico_medico.append({'CPF': cpf, 'Novo Dignóstico': novo_diagnostico, 'Data do Novo diagnóstico': data_novo_diagnostico, 'Nova Condição': nova_condicao, 'Novo Tratamento': novo_tratamento, 'Novo Medicamento': novo_medicamento, 'Novo Procedimento': novo_procedimento, 'Novo Exame': novo_exame, 'Data do Novo exame': data_novo_exame, 'Observações': observacoes})
  # ARQUIVOS .TXT
    with open('diagnostico_pacientes.txt', 'w') as arq_h:
      for h in historico_medico:
          arq_h.write(historico_medico[h])
          print()
    # ARQUIVO DE LEITURA
    try:
      with open('diagnostico_pacientes.txt', 'r') as arq_h:
          for h in pacientes:
              arq_h.readlines(historico_medico[h])
              print(h)
              print()
    except FileNotFoundError as erro:
      print(f'Erro {erro}. Arquivo não encontrado!')
  # documentar a evolução clínica de cada paciente ao longo do tempo, incluindo mudança no estado de saúde, resultado de exames e observações relevantes
  print('Evolução clínica atualizada com sucesso!')

def anexos_imagens():
  try:
    path = input('Insira o caminho da imagem: ') #imagens/pontuario.png
    if os.path.isfile(path):
      img = Image.open(path)
      print(img.format, img.size, img.mode)
  except FileNotFoundError as erro:
      print(f'ERRO {erro}! Arquivo não encontrado. Por favor, tente novamente.')

# MÓDULO 6
class ProfissionalSaude:
  def __init__(self, nome, cargo, experiencia, contato):
      self.nome = nome
      self.cargo = cargo
      self.experiencia = experiencia
      self.contato = contato

  def __str__(self):
      return f"{self.nome}, {self.cargo}, {self.experiencia} anos de experiência, Contato: {self.contato}"

class Plantao:
  def __init__(self, profissional, data, hora_inicio, hora_fim):
      self.profissional = profissional
      self.data = data
      self.hora_inicio = hora_inicio
      self.hora_fim = hora_fim

  def __str__(self):
      return f"Plantão: {self.data}, das {self.hora_inicio} às {self.hora_fim}, Profissional: {self.profissional.nome}"

def cadastrar_profissional(self):
  nome = input("Digite o nome do profissional: ")
  cargo = input("Digite o cargo: ")
  experiencia = input("Digite a experiência (em anos): ")
  contato = input("Digite o contato: ")
  profissional = ProfissionalSaude(nome, cargo, experiencia, contato)
  self.profissionais.append(profissional)
  print("Profissional cadastrado com sucesso!\n")

def listar_profissionais(self):
  print("Lista de Profissionais:")
  for profissional in self.profissionais:
      print(profissional)
  print("")

def alocar_plantao(self):
  nome = input("Digite o nome do profissional para o plantão: ")
  profissional = next((p for p in self.profissionais if p.nome == nome), None)
  if not profissional:
      print("Profissional não encontrado.")
      return
  data = input("Digite a data do plantão (dd/mm/yyyy): ")
  hora_inicio = input("Digite a hora de início (HH:MM): ")
  hora_fim = input("Digite a hora de fim (HH:MM): ")
  plantao = Plantao(profissional, data, hora_inicio, hora_fim)
  self.plantoes.append(plantao)
  print("Plantão alocado com sucesso!\n")

def trocar_plantao(self):
  nome_atual = input("Digite o nome do profissional atual: ")
  nome_novo = input("Digite o nome do novo profissional: ")
  data = input("Digite a data do plantão a ser trocado (dd/mm/yyyy): ")

  plantao_atual = next((p for p in self.plantoes if p.profissional.nome == nome_atual and p.data == data), None)
  profissional_novo = next((p for p in self.profissionais if p.nome == nome_novo), None)

  if plantao_atual and profissional_novo:
      plantao_atual.profissional = profissional_novo
      print("Plantão trocado com sucesso.")
  else:
      print("Não foi possível realizar a troca de plantão.")

def listar_plantoes(self):
  print("Lista de Plantões:")
  for plantao in self.plantoes:
      print(plantao)
  print("")

def exportar_dados_csv(self, filepath):
  with open(filepath, 'w', newline='') as csvfile:
    fieldnames = ['nome', 'cargo', 'experiencia', 'contato']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for profissional in self.profissionais:
        writer.writerow({'nome': profissional.nome, 'cargo': profissional.cargo, 
                         'experiencia': profissional.experiencia, 'contato': profissional.contato})
    print("Dados exportados com sucesso para", filepath)

def importar_dados_csv(self, filepath):
  with open(filepath, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        self.profissionais.append(ProfissionalSaude(row['nome'], row['cargo'], 
                                                    row['experiencia'], row['contato']))
    print("Dados importados com sucesso de", filepath)

def menu_profissionais():
  print('''Escolha uma opção:
  1 - Cadastrar Profissional
  2 - Listar Profissionais
  3 - Alocar Plantão
  4 - Listar Plantões
  5 - Trocar Plantão''')
  
# MÓDULO 7
class Visitante:
  def __init__(self, nome, documento, relacao, data_autorizacao):
      self.nome = nome
      self.documento = documento
      self.relacao = relacao
      self.data_autorizacao = data_autorizacao

class PacienteVisitante:
  def __init__(self):
      self.visitantes = []
      self.pacientes = []
    
class Paciente:
  def __init__(self, nome, quarto, limite_visitantes):
      self.nome = nome
      self.quarto = quarto
      self.limite_visitantes = limite_visitantes
      self.visitantes = []

  def adicionar_visitante(self, visitante):
      if len(self.visitantes) < self.limite_visitantes:
          self.visitantes.append(visitante)
      else:
          print("Limite de visitantes atingido para este paciente.")

def cadastrar_visitante(self):
  nome = input("Digite o nome do visitante: ")
  documento = input("Digite o documento do visitante: ")
  relacao = input("Digite a relação do visitante com o paciente: ")
  data_autorizacao = input("Digite a data de autorização (dd/mm/yyyy): ")
  visitante = Visitante(nome, documento, relacao, data_autorizacao)
  self.visitantes.append(visitante)
  print("Visitante cadastrado com sucesso!\n")

def verificar_autorizacao_visitante(self):
  documento = input("Digite o documento do visitante para verificação: ")
  visitante = next((v for v in self.visitantes if v.documento == documento), None)
  if visitante:
      print("Visitante autorizado.")
  else:
      print("Visitante não autorizado.")

def registrar_entrada_visitante(self):
  documento = input("Digite o documento do visitante para registrar entrada: ")
  visitante = next((v for v in self.visitantes if v.documento == documento), None)
  if visitante:
      print("Entrada do visitante registrada.")
  else:
      print("Visitante não autorizado.")

def registrar_saida_visitante(self):
  documento = input("Digite o documento do visitante para registrar saída: ")
  visitante = next((v for v in self.visitantes if v.documento == documento), None)
  if visitante:
      print("Saída do visitante registrada.")
  else:
      print("Visitante não autorizado.")

def cadastrando_paciente(self):
  nome = input("Digite o nome do paciente: ")
  quarto = input("Digite o número do quarto: ")
  limite_visitantes = int(input("Digite o limite de visitantes: "))
  paciente = Paciente(nome, quarto, limite_visitantes)
  self.pacientes.append(paciente)
  print("Paciente cadastrado com sucesso!\n")

def menu_visitante():
  print('''Escolha uma opção:
  1 - Cadastrar visitante
  2 -  Verificar autorização de visitante
  3 - Registrar entrada de visitante
  4 - Registrar saída de visitante
  5 - Cadastrar paciente
  6 - Exportar dados para CSV
  7 - Importar dados de CSV
  0 - SAIR''')

if __name__ == "__main__":
  sistema = PacienteVisitante()

# MÓDULO 8
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
  if nome and cpf in pacientes:
    if nome and cpf in historico_medico:
      print(pacientes)
      print(historico_medico)
  while nome and cpf not in pacientes:
    print('Paciente não atendido ou dados incorretos!')
    break
  while nome and cpf not in historico_medico:
    print('Paciente não encontrado ou dados incorretos!')
    break


# CÓDIGO

# MAIN
while True:
  menu()
  opcao = int(input('Digite a opção desejada: '))
  if opcao == 1:
    print('..:: GESTÃO DE LEITOS ::..')
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
    elif opcao_leitos == 7:
      print('-*' * 20)
      print('...::: EXPORTAR EM CSV :::...')
      print()
      arquivo_csv = input("Digite o nome do arquivo CSV para exportar: ")
      hospital.exportar_para_csv(arquivo_csv)
      print()
    else:
      print('OPÇÃO INVÁLIDA! Tente novamente')
      break

  elif opcao == 2:
    print('..:: CONTROLE DE EQUIPAMENTOS ::..')
    if __name__ == "__main__":
      main()
    cadastrar_equipamento("Equipamento A", "Modelo 1", "123456", "2023-01-01")
    registrar_manutencao("123456", "2023-03-15", "Manutenção de Rotina", "Limpeza e Lubrificação")
    historico_manutencoes("123456")

  elif opcao == 3:
    print('..:: ADMINISTRAÇÃO DE MEDICAMENTOS ::..')
    exibir_menu()
    opcao_med = int(input("Escolha uma opção: "))
    if opcao_med == 1:
      nome = input("Nome do medicamento: ")
      principio_ativo = input("Princípio Ativo: ")
      dosagem = input("Dosagem: ")
      forma_administracao = input("Forma de Administração: ")

      medicamento = Medicamento(nome, principio_ativo, dosagem, forma_administracao)

      quantidade = int(input("Quantidade: "))
      lote = input("Lote: ")
      data_validade = input("Data de Validade (AAAA-MM-DD): ")
      fornecedor = input("Fornecedor: ")

      adicionar_medicamento_ao_estoque(estoque, medicamento, quantidade, lote, data_validade, fornecedor)
      print("Medicamento adicionado ao estoque.")

    elif opcao_med == 2:
      nome_medicamento = input("Nome do medicamento a verificar estoque baixo: ")
      if verificar_estoque_baixo(estoque, nome_medicamento):
          print("Estoque baixo para", nome_medicamento)
      else:
          print("Estoque adequado para", nome_medicamento)

    elif opcao_med == 3:
      nome_medicamento = input("Nome do medicamento a registrar administração: ")
      data = input("Data (AAAA-MM-DD): ")
      horario = input("Horário: ")
      paciente = input("Paciente: ")
      dosagem = input("Dosagem: ")
      responsavel = input("Responsável pela administração: ")

      medicamento = Medicamento(nome_medicamento, "", "", "")
      registrar_administracao(registro, medicamento, data, horario, paciente, dosagem, responsavel)
      print("Administração registrada com sucesso.")

    elif opcao_med == 4:
      paciente = input("Paciente: ")
      nome_medicamento = input("Nome do medicamento: ")
      data = input("Data (AAAA-MM-DD): ")
      dosagem = input("Dosagem: ")

      adicionar_registro_prontuario(prontuario, paciente, nome_medicamento, data, dosagem)
      print("Registro adicionado ao prontuário eletrônico.")

    elif opcao_med == 5:
        print("Saindo do programa.")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")

  elif opcao == 4:
    print('..:: AGENDAMENTO E CONTROLE DE VISITAS ::..')
    menu_controle_visita()
    opcao_agend = int(input('Escolha uma opção: '))
    if opcao_agend == 1:
      print('-*' * 20)
      print('...::: AGENDAMENTO DA VISITA :::...')
      print()
      agendamento_visita()
      print()
    elif opcao_agend == 2:
      print('-*' * 20)
      print('...::: RESTRIÇÃO DAS VISITAS :::...')
      print()
      restricoes()
      print()
    elif opcao_agend == 3:
      print('-*' * 20)
      print('...::: REGISTRO DA VISITA :::...')
      print()
      registro_visitantes()
      print()
    elif opcao_agend == 4:
      print('-*' * 20)
      print('...::: DETALHES DO AGENDAMENTO   :::...')
      print()
      detalhes_agendamento()
      print()
    elif opcao_agend == 5:
      print('-*' * 20)
      print('...::: CANCELAMENTO E REAGENDAMENTO DE VISITA :::...')
      print()
      cancelamento_reagendamento_visita()
      print()
    else:
      print('OPÇÃO INVÁLIDA')
      break

  elif opcao == 5:
    print('..:: PONTUÁRIO ELETRÔNICO ::..')
    menu_pontuario()
    opcao_pont = int(input('Escolha uma opção: '))
    if opcao_pont == 1:
      print('-*' * 20)
      print('...::: CADASTRO DE PACIENTE :::...')
      print()
      cadastrar_paciente()
      print()
    elif opcao_pont == 2:
      print('-*' * 20)
      print('...::: DIAGNÓSTICO DO PACIENTE :::...')
      print()
      registro_diagnostico()
      print()
    elif opcao_pont == 3:
      print('-*' * 20)
      print('...::: ACOMPANHAMENTO DO TRAMENTO :::...')
      print()
      acompanhamento_tratamento()
      print()
    elif opcao_pont == 4:
      print('-*' * 20)
      print('...::: EVOLUÇÃO CLÍNICA :::...')
      print()
      evolucao_clinica()
      print()
    elif opcao_pont == 5:
      print('-*' * 20)
      print('...::: ANEXO DE EXAMES E IMAGENS :::...')
      print()
      anexos_imagens()
      print()
    else:
      print('OPÇÃO INVÁLIDA')
      break

  elif opcao == 6:
    print('..:: GESTÃO DE EQUIPES ::..')
    menu_profissionais()
    opcao_profissionais = int(input('OPÇÃO: '))
    if opcao_profissionais == 1:
      print('-*' * 20)
      print('..:: CADASTRO DO PROFISSIONAL DE SAÚDE ::..')
      print()
      self.cadastrar_profissional()
      print()
    elif opcao_profissionais == 2:
      print('-*' * 20)
      print('..:: LISTAGEM DE PROFISSIONAIS ::..')
      print()
      self.listar_profissionais()
      print()
    elif opcao_profissionais == 3:
      print('-*' * 20)
      print('..:: ALOCAÇÃO DE PLANTÃO ::..')
      print()
      self.alocar_plantao()
      print()
    elif opcao_profissionais == 4:
      print('-*' * 20)
      print('..:: LISTAGEM DE PLANTÕES ::..')
      print()
      self.listar_plantoes()
      print()
    elif opcao_profissionais == 4:
      print('-*' * 20)
      print('..:: TROCA DE PLANTÃO ::..')
      print()
      self.trocar_plantao()
      print()
    else:
      print('OPÇÃO INVÁLIDA!')
      break

  elif opcao == 7:
    print('..:: CADASTRO DE VISITANTES ::..')
    menu_visitante()
    opcao_visitante = int(input('OPÇÃO: '))
    if opcao_visitante == 1:
      print('-*' * 20)
      print('..:: CADASTRANDO VISITANTE ::..')
      print()
      self.cadastrar_visitante()
      print()
    elif opcao_visitante == 2:
      print('-*' * 20)
      print('..:: VERIFICAR AUTORIZAÇÃO DE VISITA ::..')
      print()
      self.verificar_autorizacao_visitante()
      print()
    elif opcao_visitante == 3:
      print('-*' * 20)
      print('..:: REGISTRO DE ENTRADA DO VISITANTE ::..')
      print()
      self.registrar_entrada_visitante()
      print()
    elif opcao_visitante == 4:
      print('-*' * 20)
      print('..:: REGISTRO DE SAÍDA DO VISITANTE ::..')
      print()
      self.registrar_saida_visitante()
      print()
    elif opcao_visitante == 5:
      print('-*' * 20)
      print('..:: CADASTRO DE PACIENTE ::..')
      print()
      self.cadastrar_paciente()
      print()
    elif opcao_visitante == 6:
      print('-*' * 20)
      print('..:: EXPORTANDO DADOS CSV ::..')
      print()
      filepath = input("Digite o caminho do arquivo CSV para exportação: ")
      self.exportar_dados_csv(filepath)
      print()
    elif opcao_visitante == 7:
      print('-*' * 20)
      print('..:: IMPORTANDO DADOS CSV ::..')
      print()
      filepath = input("Digite o caminho do arquivo CSV para importação: ")
      self.importar_dados_csv(filepath)
      print()
    else:
      print('OPÇÃO INVÁLIDA!')
      break

  elif opcao == 8:
    print('..:: RELATÓRIOS E ANALÍSES ::..')
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

  elif opcao == 9:
    print('..:: LOCALIZAR ARQUIVOS TXT ::..')
    def localizar_arquivos_txt(diretorio):
        try:
            arquivos = os.listdir(diretorio)
            arquivos_txt = [os.path.join(diretorio, arquivo) for arquivo in glob.glob(os.path.join(diretorio, '*.txt'))]
          
            return arquivos_txt
          
        except FileNotFoundError:
            return []

    if __name__ == "__main__":
        diretorio_alvo = "/caminho/do/diretorio"
        arquivos_encontrados = localizar_arquivos_txt(diretorio_alvo)

        if arquivos_encontrados:
            print(f"Arquivos .txt encontrados em '{diretorio_alvo}': ")
            for arquivo in arquivos_encontrados:
                print(arquivo)
        else:
            print(f"Nenhum arquivo .txt encontrado em '{diretorio_alvo}'.")

  elif opcao == 10:
    print('..:: EXCLUIR ARQUIVOS TXT ::..')

  elif opcao == 11:
    print('..:: LOCALIZAR ARQUIVOS CSV ::..')
    def localizar_arquivos_csv(diretorio):
      try:
        arquivos = os.listdir(diretorio)

        arquivos_csv = [os.path.join(diretorio, arquivo) for arquivo in glob.glob(os.path.join(diretorio, '*.csv'))]

        return arquivos_csv

      except FileNotFoundError:
        return []

    if __name__ == "__main__":
        diretorio_alvo = "/caminho/do/diretorio"  # Substitua pelo caminho do diretório que você deseja pesquisar
        arquivos_encontrados = localizar_arquivos_csv(diretorio_alvo)

        if arquivos_encontrados:
            print(f"Arquivos .csv encontrados em '{diretorio_alvo}':")
            for arquivo in arquivos_encontrados:
                print(arquivo)
        else:
            print(f"Nenhum arquivo .csv encontrado em '{diretorio_alvo}'.")

  elif opcao == 12:
    print('..:: EXCLUIR ARQUIVOS CSV ::..')

  else:
    print('Opção inválida!')
    
