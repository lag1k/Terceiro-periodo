class Funcionario:
    def __init__(self, nome, cargo, salario, departamento):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario
        self.departamento = departamento

    def receber_aumento(self, percentual):
        aumento = self.salario * (percentual / 100)
        self.salario += aumento

    def mudar_departamento(self, novo_departamento):
        self.departamento = novo_departamento

    def exibir_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Cargo: {self.cargo}")
        print(f"Salário: R${self.salario:.2f}")
        print(f"Departamento: {self.departamento}")

# Exemplo de uso da classe Funcionario:
funcionario1 = Funcionario("João", "Desenvolvedor", 5000, "TI")
funcionario1.exibir_dados()
funcionario1.receber_aumento(10)
funcionario1.mudar_departamento("Recursos Humanos")
funcionario1.exibir_dados()
