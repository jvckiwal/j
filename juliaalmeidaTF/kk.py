import csv
with open('servidores_ativos.csv', 'rt', encoding='utf-8') as arquivo:
    csv_reader = csv.reader(arquivo, delimiter=';')

def contar_linhas_coluna(arquivo, coluna):
    contador = 0

    with open(arquivo, 'r') as file:
        # Lê o cabeçalho para obter o índice da coluna
        cabeçalho = file.readline().strip().split(',')
        indice_coluna = cabeçalho.index(coluna)

        # Itera sobre as linhas do arquivo
        for linha in file:
            valores = linha.strip().split(',')
            # Se a coluna existir na linha, incrementa o contador
            if indice_coluna < len(valores):
                contador += 1

    return contador


def menu_principal():
    while True:
        print("\nMenu Principal:")
        print("1. Número total de servidores")
        print("0. Sair")

        opcao = input("Digite a opção desejada: ")

        if opcao == "1":
          arquivo_csv = 'servidores_ativos.csv'
          coluna_desejada = 'nome'
          resultado = contar_linhas_coluna(arquivo_csv, coluna_desejada)
          print(f'O número de servidores é: {resultado}')

        elif opcao == "0":
            print("Saindo do programa. Até logo!")
            break
        

if __name__ == "__main__":
    menu_principal()

