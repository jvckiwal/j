import csv

with open('servidores_ativos.csv', encoding='utf-8') as dados:

  arquivo = csv.reader(dados, delimiter=',')

def totalservidores(servidores_ativos, nomes):
            contador = 0

            # Itera sobre as linhas e incrementa o contador para cada linha com a coluna não vazia
            for linha in arquivo:
                if nome in linha and linha[nome]:
                    contador += 1

            return contador
            
    quantidade_linhas_coluna = totalservidores(servidores_ativos, nome)

   if quantidade_linhas_coluna is not None:
    print(f"A quantidade de linhas na coluna é: {quantidade_linhas_coluna}")

def menu_principal():
    caminho_arquivo = "servidores_ativos.csv"  
    dados = carregar_dados(caminho_arquivo)
    while True:
        print("\nMenu Principal:")
        print("1. Relatório")
        print("2. Criar arquivo parcial")
        print("3. Buscar dados")
        print("4. Filtrar por unidades organizacionais")
        print("5. Filtrar por número de servidores em cargo x")
        print("6. Mostrar número total de cargos")
        print("7. Filtrar número de cargos por unidade")
        print("8. Mostrar número de servidores por unidade")
        print("0. Sair")

        opcao = input("Digite a opção desejada: ")

        if opcao == "1":
            relatorio(dados)
        elif opcao == "2":
            nome_arquivo_parcial = input("Informe o nome do arquivo parcial: ")
            criar_arquivo_parcial(dados, nome_arquivo_parcial)
        elif opcao == "3":
            buscar_dados(dados)
        elif opcao == "4":
            filtrar_unidades_organizacionais(dados)
        elif opcao == "5":
            filtrar_numero_servidores_por_cargo(dados)
        elif opcao == "6":
            mostrar_numero_total_cargos(dados)
        elif opcao == "7":
            filtrar_numero_cargos_por_unidade(dados)
        elif opcao == "8":
            mostrar_numero_servidores_por_unidade(dados)
        elif opcao == "0":
            print("Saindo do programa. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu_principal()
