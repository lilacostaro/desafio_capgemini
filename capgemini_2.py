"""
DESAFIO DE PROGRAMAÇÃO - ACADEMIA CAPGEMINI
Data: 18/02/2022
Autor: Camila Rodrigues Costa
# Questão 02

Débora se inscreveu em uma rede social para se manter em contato com seus amigos. 
A página de cadastro exigia o preenchimento dos campos de nome e senha, porém a senha precisa ser forte. 
O site considera uma senha forte quando ela satisfaz os seguintes critérios:

Possui no mínimo 6 caracteres.
Contém no mínimo 1 digito.
Contém no mínimo 1 letra em minúsculo.
Contém no mínimo 1 letra em maiúsculo.
Contém no mínimo 1 caractere especial. Os caracteres especiais são: !@#$%^&*()-+

Débora digitou uma string aleatória no campo de senha, porém ela não tem certeza se é uma senha forte. 
Para ajudar Débora, construa um algoritmo que informe qual é o número mínimo de caracteres que devem ser adicionados para uma string qualquer ser considerada segura.
"""

def check_senha(senha):
    # Checando se a senha contem a quantidade correta de caracteres
    if len(senha) >= 6:
        print('\nSenha Segura')
    # Retornando o valor de caracteres necessarios para senha ser aceita    
    else:
        caracteres = 6 - len(senha)
        print(f'\nSua senha precisa de mais {caracteres} caracteres!')
    
if __name__=='__main__':
    check_senha(senha = 'Ya3')
    check_senha(senha = '1ytB')
    check_senha(senha = 'yL$zb25')
    check_senha(senha = '*oL1')