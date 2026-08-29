#CRIANDO UM SISTEMA DE LOGON SIMPLES PARA TESTE DE SYNTAX E SCRIPTS USANDO .py NO PYCHARM ( ESTUDO/TREINO )
#FEITO TUDO DE CABEÇA USANDO CONHECIMENTO BASICO DOS SCRIPTS.(TESTE DE MEMORIA,RACIOCINIO,CODIGOS)
#(SCRIPT NAO FINALIZADO)
print('Olá senhor(a)!Vamos criar o seu cadastro?')
log1 = str(input('CRIE UM NOME DE USUÁRIO:\n'))
log2 = str(input('CRIE UM LOG-IN,USE UMA CONTA DE EMAIL\nLOGIN:'))
while True:
    log3 = str(input('AGORA CRIE UMA SENHA PARA ESSE USUÁRIO ABAIXO.\n(Sua senha deve conter 8 ou mais caracteres)\nSENHA: '))
    if len(log3) >= 8:
        print(f'SEU CADASTRO FOI BEM SUCEDIDO, {log1}!\n')
        o = input('deseja ver suas credenciais? [s/n]:\n')
        if o in ['s', 'sim']:
           usuario = log2
           senha = log3
           frase = 'suas credenciais são:\nlogin:{}\nsenha:{}'.format(usuario, senha)
           print(frase, '\nTenhá um bom dia!')
        else:
            print('opção não exibida por decisao do usuário.\ntenha um bom dia!')
        break

    else:
        print('sua senha deve conter 8 ou mais caracteres!')

usuario_correct = log2
senha_correct = log3
while True:
  usuario_correct = input('Digite seu email:\n')
  senha_correct = input('Digite sua senha:\n')
  if usuario_correct == log2 and senha_correct == log3:
    print('Login realizado com sucesso!')
    break
  else:
    print('Usuário ou senha incorreta! Tente novamente.')
