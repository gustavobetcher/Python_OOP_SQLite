#Importar nosso arquivo Pessoa.py no diretorio model
from model.Pessoa import Pessoa
from database.Database import Database
from dao.PessoaDAO import PessoaDAO

#Exemplo de uso
gustavo = Pessoa(1, "Gustavo Betcher")
print(gustavo)

#Quero mostrar apenas o nome
print(gustavo.nome)


print("DAQUI PARA BAIXO É ACESSO AO BD")
#Chamar o objeto de BD
db =  Database()

#Intancia o objeto
pessoaDAO = PessoaDAO(db.conexao, db.cursor)

#Quero carregar uma lista com o que veio do BD
pessoas = pessoaDAO.getAll(orderBy=True)
for pessoa in pessoas:
  print(pessoa)

#Criar um objeto com qualquer ator/atriz/diretor/diretora
novo = Pessoa(0, "Denzel Washington")

#Olha que simples...
novo = pessoaDAO.save(novo)

#consulta o banco de novo..
pessoas = pessoaDAO.getAll(orderBy=True)
for pessoa in pessoas:
  print(pessoa)