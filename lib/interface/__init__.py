from rich import print
from rich.panel import Panel

def leiaint(msg):
    ok = False 
    valor = 0 
    while True:
        n = input(msg)
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[031mERRO! Digite um número inteiro válido \033[m')
        if ok:
            break
    return valor


def linha(tam = 42):
    return '-' * tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(*lista):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'[yellow]{c}[/] - [blue]{item}[/]')
        c += 1
    print(linha())
    opc = leiaint('\033[32mSua opção: \033[m')
    return opc

def menu2(op1,op2,op3):
    cabeçalho('MENU PRINCIPAL')
    print(Panel(f'''[yellow]1[/] - [blue]{op1}[/]
[yellow]2[/] - [blue]{op2}[/]
[yellow]3[/] - [blue]{op3}[/]''',title='ECOLHA UMA OPÇÃO',width=35))
    opc = leiaint('\033[32mSua opção: \033[m')
    return opc