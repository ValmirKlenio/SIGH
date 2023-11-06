
import csv

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

class Visitante:
    def __init__(self, nome, documento, relacao, data_autorizacao):
        self.nome = nome
        self.documento = documento
        self.relacao = relacao
        self.data_autorizacao = data_autorizacao

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

class SistemaGestaoHospitalar:
    def __init__(self):
        self.profissionais = []
        self.plantoes = []
        self.visitantes = []
        self.pacientes = []

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

    def cadastrar_paciente(self):
        nome = input("Digite o nome do paciente: ")
        quarto = input("Digite o número do quarto: ")
        limite_visitantes = int(input("Digite o limite de visitantes: "))
        paciente = Paciente(nome, quarto, limite_visitantes)
        self.pacientes.append(paciente)
        print("Paciente cadastrado com sucesso!\n")

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

    def menu(self):
        while True:
            print("Sistema de Gestão Hospitalar")
            print("1 - Cadastrar profissional")
            print("2 - Listar profissionais")
            print("3 - Alocar plantão")
            print("4 - Listar plantões")
            print("5 - Trocar plantão")
            print("6 - Cadastrar visitante")
            print("7 - Verificar autorização de visitante")
            print("8 - Registrar entrada de visitante")
            print("9 - Registrar saída de visitante")
            print("10 - Cadastrar paciente")
            print("11 - Exportar dados para CSV")
            print("12 - Importar dados de CSV")
            print("0 - Sair")
            opcao = input("Escolha uma opção: ")

            if opcao == '1':
                self.cadastrar_profissional()
            elif opcao == '2':
                self.listar_profissionais()
            elif opcao == '3':
                self.alocar_plantao()
            elif opcao == '4':
                self.listar_plantoes()
            elif opcao == '5':
                self.trocar_plantao()
            elif opcao == '6':
                self.cadastrar_visitante()
            elif opcao == '7':
                self.verificar_autorizacao_visitante()
            elif opcao == '8':
                self.registrar_entrada_visitante()
            elif opcao == '9':
                self.registrar_saida_visitante()
            elif opcao == '10':
                self.cadastrar_paciente()
            elif opcao == '11':
                filepath = input("Digite o caminho do arquivo CSV para exportação: ")
                self.exportar_dados_csv(filepath)
            elif opcao == '12':
                filepath = input("Digite o caminho do arquivo CSV para importação: ")
                self.importar_dados_csv(filepath)
            elif opcao == '0':
                print("Programa Encerrado!!")
                break
            else:
                print("Opção inválida!\n")

if __name__ == "__main__":
    sistema = SistemaGestaoHospitalar()
    sistema.menu()