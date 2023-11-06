# BIBLIOTECAS
import datetime
import csv
from PIL import Image
import os

# LISTAS / DICIONÁRIOS
pacientes = []
historico_medico = []
leitos = []
equipamentos = []
medicamentos = []
visitas = []
profissionais_saude = []

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

# MÓDULO 2

# MÓDULO 3

# MÓDULO 4 - visitas = []
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

# MÓDULO 5 - pacientes = [], historico_paciente = []
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

# MÓDULO 7

# MÓDULO 8

# CÓDIGO

# MAIN
while True:
  menu()
  opcao = int(input('Digite a opção desejada: '))
  if opcao == 1:
    print('..:: GESTÃO DE LEITOS ::..')

  elif opcao == 2:
    print('..:: CONTROLE DE EQUIPAMENTOS ::..')

  elif opcao == 3:
    print('..:: ADMINISTRAÇÃO DE MEDICAMENTOS ::..')

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

  elif opcao == 7:
    print('..:: CADASTRO DE VISITANTES ::..')

  elif opcao == 8:
    print('..:: RELATÓRIOS E ANALÍSES ::..')

  elif opcao == 9:
    print('..:: LOCALIZAR ARQUIVOS TXT ::..')

  elif opcao == 10:
    print('..:: EXCLUIR ARQUIVOS TXT ::..')

  elif opcao == 11:
    print('..:: LOCALIZAR ARQUIVOS CSV ::..')

  elif opcao == 12:
    print('..:: EXCLUIR ARQUIVOS CSV ::..')

  else:
    print('Opção inválida!')
