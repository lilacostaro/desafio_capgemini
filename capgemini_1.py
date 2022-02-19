"""
DESAFIO DE PROGRAMAÇÃO - ACADEMIA CAPGEMINI
Data: 18/02/2022
Autor: Camila Rodrigues Costa
# Questão 01

Escreva um algoritmo que mostre na tela uma escada de tamanho n utilizando o caractere * e espaços. 
A base e altura da escada devem ser iguais ao valor de n. 
A última linha não deve conter nenhum espaço.
"""

def printStar(n):
    
    # definindo a quantidade de espaços
    espacos = n - 1
    
    # definindo o loop que definira o numero de linhas
    for i in range(0, n):
        
        # definindo o loop que cuidara dos espacos vazios
        for j in range(0, espacos):
            print(end=' ')
        
        # Diminuindo o espaco depois de cada loop
        espacos = espacos - 1
        
        # definindo o loop que cuidara do numero de colunas
        for j in range(0, i+1):
            # printing the stars
            print('*', end='')
            
        # finalizando a linha depois de cada 
        print('\r')
        
    print('\n')
      
# Testes unitarios
if __name__=='__main__':
    printStar(n = 2)
    printStar(n = 4)
    printStar(n = 6)
    printStar(n = 8)
    printStar(n = 10)
    