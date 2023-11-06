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

class SistemaGestaoHospitalar:
    def __init__(self):
        self.profissionais = []
        self.plantoes = []

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

    def listar_plantoes(self):
        print("Lista de Plantões:")
        for plantao in self.plantoes:
            print(plantao)
        print("")

    def menu(self):
        while True:
            print("Sistema de Gestão Hospitalar")
            print("1 - Cadastrar profissional")
            print("2 - Listar profissionais")
            print("3 - Alocar plantão")
            print("4 - Listar plantões")
            print("5 - Sair")
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
                print("Saindo do sistema...")
                break
            else:
                print("Opção inválida! Tente novamente.\n")

# Executar o sistema
if __name__ == "__main__":
    sistema = SistemaGestaoHospitalar()
    sistema.menu()
