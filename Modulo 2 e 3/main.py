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

if __name__ == "__main__":
    main()

cadastrar_equipamento("Equipamento A", "Modelo 1", "123456", "2023-01-01")
registrar_manutencao("123456", "2023-03-15", "Manutenção de Rotina", "Limpeza e Lubrificação")
historico_manutencoes("123456")


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
    print("===== MENU =====")
    print("1. Adicionar Medicamento ao Estoque")
    print("2. Verificar Estoque Baixo")
    print("3. Registrar Administração")
    print("4. Adicionar Registro ao Prontuário Eletrônico")
    print("5. Sair")

estoque = EstoqueMedicamentos()
registro = RegistroAdministracao()
prontuario = ProntuarioEletronico()

while True:
    exibir_menu()
    opcao_med = input("Escolha uma opção: ")
    if opcao_med == "1":
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

    elif opcao_med == "2":
        nome_medicamento = input("Nome do medicamento a verificar estoque baixo: ")
        if verificar_estoque_baixo(estoque, nome_medicamento):
            print("Estoque baixo para", nome_medicamento)
        else:
            print("Estoque adequado para", nome_medicamento)

    elif opcao_med == "3":
        nome_medicamento = input("Nome do medicamento a registrar administração: ")
        data = input("Data (AAAA-MM-DD): ")
        horario = input("Horário: ")
        paciente = input("Paciente: ")
        dosagem = input("Dosagem: ")
        responsavel = input("Responsável pela administração: ")

        medicamento = Medicamento(nome_medicamento, "", "", "")
        registrar_administracao(registro, medicamento, data, horario, paciente, dosagem, responsavel)
        print("Administração registrada com sucesso.")

    elif opcao_med == "4":
        paciente = input("Paciente: ")
        nome_medicamento = input("Nome do medicamento: ")
        data = input("Data (AAAA-MM-DD): ")
        dosagem = input("Dosagem: ")

        adicionar_registro_prontuario(prontuario, paciente, nome_medicamento, data, dosagem)
        print("Registro adicionado ao prontuário eletrônico.")

    elif opcao_med == "5":
        print("Saindo do programa.")
        break

    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
```