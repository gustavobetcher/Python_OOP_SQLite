class Pessoa:
  #Atributos
  id = None
  nome = None

  #Metodo Construtor
  def __init__(self, id, nome):
    self.id = id
    self.nome = nome
  def __str__(self):
    return(f"{self.nome} ({self.id})")