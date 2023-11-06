import datetime

class Hospital:
    def __init__(self):
        self.historico_ocupacao = {}

    def registrar_ocupacao(self, data, uti, ala_a, ala_b):
        self.historico_ocupacao[data] = {'UTI': uti, 'Ala A': ala_a, 'Ala B': ala_b}
    
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

def solicitar_dados():
    data = input("Digite a data de ocupação (dd/mm/aaaa): ")
    uti = int(input("Digite o número de leitos ocupados na UTI: "))
    ala_a = int(input("Digite o número de leitos ocupados na Ala A: "))
    ala_b = int(input("Digite o número de leitos ocupados na Ala B: "))
    return data, uti, ala_a, ala_b

def main():
    hospital = Hospital()

    while True:
        print("\nSistema de Gestão Hospitalar")
        print("1. Registrar ocupação de leitos")
        print("2. Gerar relatório de ocupação")
        print("3. Ver histórico completo de ocupação")
        print("4. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            data, uti, ala_a, ala_b = solicitar_dados()
            data_obj = datetime.datetime.strptime(data, '%d/%m/%Y').date()
            hospital.registrar_ocupacao(data_obj, uti, ala_a, ala_b)
        elif escolha == '2':
            inicio = input("Digite a data inicial para o relatório (dd/mm/aaaa): ")
            fim = input("Digite a data final para o relatório (dd/mm/aaaa): ")
            inicio_obj = datetime.datetime.strptime(inicio, '%d/%m/%Y').date()
            fim_obj = datetime.datetime.strptime(fim, '%d/%m/%Y').date()
            hospital.gerar_relatorio_ocupacao(inicio_obj, fim_obj)
        elif escolha == '3':
            hospital.imprimir_historico_completo()
        elif escolha == '4':
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
