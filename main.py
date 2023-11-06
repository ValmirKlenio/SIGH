# BIBLIOTECAS
import csv
from PIL import Image
import os

# LISTAS / DICIONÁRIOS
leitos = []
equipamentos = []
medicamentos = []
profissionais_saude = []
pacientes = []
historico_medico = []
visitas = []

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

# MÓDULO 4

# MÓDULO 5

# MÓDULO 6

# MÓDULO 7

# MÓDULO 8

# CÓDIGO

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

  elif opcao == 5:
    print('..:: PONTUAÇÃO ELETRÔNICA ::..')

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
