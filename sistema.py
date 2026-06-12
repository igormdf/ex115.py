from lib.interface import *
from time import sleep
from lib.arquivo import *

arq = 'arquivo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu2('Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema')
    if resposta == 1:
        #listar o conteúdo de um aqrquivo
        lerArquivo(arq)
    elif resposta == 2:
        #cadastrar uma nova pessoa
        cabeçalho('NOVO CADASTRADO')
        nome = input('Nome: ')
        idade = int(input('idade: '))
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabeçalho('Saindo so sistema... até logo!')
        break
    else:
        print('[red]ERRO! Digite uma opção válida![/]')
    sleep(2) 