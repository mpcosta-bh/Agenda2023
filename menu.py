import sqlite3 # importa a pasta SQL  para dentro do python

conexao = sqlite3.connect("gestaoNIT.sqlite3") # Conecta o banco de dados com Python
cursor = conexao.cursor() # cursor para executar comandos SQL, tanto os DML como os DDL
##################################################
menu = ['1-Cadastrar usuário', '2-Cadastrar na Agenda', '3-Editar contato', '4-Visualizar contato', '5-Excluir contato']
print('''Digite a opção que você deseja:
      1-Cadastrar usuário
      2-Cadastrar na Agenda
      3-Editar contato
      4-Visualizar contato
      5-Excluir contato
      ''')

opt = int(input('Opção: '))
##################################################
if opt == 1:# Cadastrar usuário ADM
    tipo = input("Digite o tipo de usuário: ")
    nome = input("Digite o seu nome: ")
    email = input("Digite o seu email: ")
    senha = input("Digite a sua senha: ")
    
    comando_sql = """INSERT INTO Usuarios (tipo, nome, email, senha) VALUES (?,?,?,?)"""
    valores = [tipo, nome, email, senha]
    cursor.execute(comando_sql, valores)

elif opt == 2:
    print('2')
elif opt ==3:
    print('3')
elif opt == 4:
    print('4')
elif opt == 5:
    print('5')
else:
    print('Opção inválida')
    
conexao.commit() # A função “commit”, associada à variável “conexao”, chamada logo em seguida, 
                 # serve para efetivamente salvar as alterações realizadas no banco de dados. 
conexao.close()  # é chamada para fechar a conexão