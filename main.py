import equacoes as eq

if __name__ == '__main__':
    while True:
        eq.mostrar_menu()
        opcoes = input('Opção desejada: ')
        match opcoes:
            case '1':
                a = float(input('Valor de "a": ' ).replace(',','.'))
                b = float(input('Valor de "b": ' ).replace(',','.'))
                print(f'Valor de x: {eq.calcular_grau_1(a,b)}.')
                continue
            case '2':
                a = float(input('Valor de "a": ' ).replace(',','.'))
                b = float(input('Valor de "b": ' ).replace(',','.'))
                c = float(input('Valor de "c": ' ).replace(',','.'))
                result = eq.calcular_grau_2(a, b, c)
                for x in result:
                    print(x)
                continue
            case '3':
                print('Programa encerrado.')
                break
            case _:
                print('Opção inválida!')
                continue
