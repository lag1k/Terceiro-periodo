# 4.	Classe Pessoa:
#
# Atributos: nome, idade, altura, peso
# Métodos: envelhecer, crescer, ganhar_peso, perder_peso
# •	envelhecer(): Aumenta a idade da pessoa em um ano.
# •	Crescer(centímetros): Aumenta a altura da pessoa em centímetros, se a pessoa tiver menos de 21 anos.
# •	Ganhar_peso(quilos): Aumenta o peso da pessoa em quilos.
# •	Perder_peso(quilos): Diminui o peso da pessoa em quilos.

class Nome:
    def __init__(self):
        self.nome = ""

    def setNome(self, nome):
        self.nome = nome

    def getNome(self):
        return self.nome
    
class Pessoa:
    def __init__(self, nome, idade, altura, peso):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.peso = peso

    def envelhecer(self):
        self.idade += 1

    def crescer(self, centimetros):
        if self.idade < 21:
            self.altura += centimetros

    def ganhar_peso(self, quilos):
        self.peso += quilos

    def perder_peso(self, quilos):
        self.peso -= quilos

    def __str__(self):
        return f'Nome: {self.nome}, Idade: {self.idade}, Altura: {self.altura} cm, Peso: {self.peso} kg'
    
    def 
    

# Exemplo de uso
pessoa = Pessoa(nome="João", idade=20, altura=170, peso=70)
print(pessoa)

pessoa.envelhecer()
pessoa.crescer(5)
pessoa.ganhar_peso(2)
pessoa.perder_peso(1)

print(pessoa)
