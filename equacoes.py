import math

#funcoes
def mostrar_menu():
    print('1 - Calcular equação do 1º grau.')
    print('2 - Calcular equação do 2º grau.')
    print('3 - Sair do Programa.')


#faz um def so pra a equacao de 2 grau porque ela pode retornar mais de 1 resultado e usando o return normalmente só retornaria 1 valor, nao importando a linguagem usada, quando coloca o returna a equacao para de ser executa e no 'else' da equacao foi preciso  usar outro metodo para que retorne mais de 1 valor
#equacao de 2 grau
def calcular_grau_2(a,b,c):
    delta = (b**2)-(4*b*c)
    if delta < 0:
        yield 'A equação não possui raízes reais.'
    elif delta == 0:
        yield f'Valor de x é {(-b)/(2*a)}.'
    else:
        #sqrl é pra fazer a raiz quadrada
        raiz_delta = math.sqrt(delta)
        x1 = (-b + raiz_delta)/(2*a)
        x2 = (-b - raiz_delta)/(2*a)
        yield f'Valor de x1: {x1}.'
        yield f'Valor de x2: {x2}.'
        #é o mesmo return, so que o yield nao para de executar, ela so pausa, nao executa tudo de novo, ela da continuacao, ela traz o valor quando pausa, vai para a proxima linha trazendo esse novo valor ainda retorna a linha de baixo 
        #retorna o valor e pausa

        #nao é possivel trabalhar com wield e return na mesma funcao 
        #só pode usar um ou outro

#equacoes de 1 grau
calcular_grau_1 = lambda a,b: -b/a


