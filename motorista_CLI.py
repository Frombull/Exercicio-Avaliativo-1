from motorista_DAO import Motorista_DAO
from passageiro import Passageiro
from motorista import Motorista
from corrida import Corrida


class CLI:
    def __init__(self):
        self.commands = {}

    def add_command(self, name, function):
        self.commands[name] = function

    def run(self):
        while True:
            command = input("Entre com um comando: ")
            if command.lower() in ["quit", "exit"]:
                break
            elif command in self.commands:
                self.commands[command]()
            else:
                print("Comando invalido.")


class Motorista_CLI(CLI):
    def __init__(self, motorista_DAO: Motorista_DAO):
        super().__init__()
        self.motorista_DAO = motorista_DAO

        # CRUD
        self.add_command("create", self.create_motorista)   # C
        self.add_command("read", self.read_motorista)       # R
        self.add_command("update", self.update_motorista)   # U
        self.add_command("delete", self.delete_motorista)   # D

    def create_motorista(self):
        n_corridas = 0
        corridas = []
        notas = 0

        while True:
            n_corridas += 1

            print(f'Corrida: {n_corridas}')

            nota = int(input('| Nota: '))
            distancia = float(input('| Distancia: '))
            valor = float(input('| Valor: '))

            print('| Passageiro')
            nome_passageiro = str(input('| Nome: '))
            documento_passageiro = str(input('| Documento: '))

            passageiro = Passageiro(nome_passageiro, documento_passageiro)

            corrida = Corrida(nota, distancia, valor, passageiro)

            corridas.append(corrida)
            notas += nota

            if input('Deseja fazer mais uma corrida? (S/N) ').lower() == 'n':
                break

        nota = int(notas / n_corridas)
        motorista = Motorista(corridas, nota)

        self.motorista_DAO.create_motorista(motorista)

    def read_motorista(self):
        id = input("ID do motorista: ")
        motorista = self.motorista_DAO.read_motorista_id(id)

        if motorista:
            print(f'Nota: {motorista["nota"]}')
            print(f'Corridas: ')
            for corrida in motorista["corridas"]:
                passageiro = corrida["passageiro"]

                print(f'| Nota: {corrida["nota"]}')
                print(f'| Valor: {corrida["valor"]}')
                print(f'| Distancia: {corrida["distancia"]}')

                print(f'| Passageiro: ')
                print(f'| Nome: {passageiro["nome"]}')
                print(f'| Documento: {passageiro["documento"]}')

    def update_motorista(self):
        id = input("Id motorista: ")

        n_corridas = 0
        corridas = []
        notas = 0

        while True:
            n_corridas += 1

            print(f'Corrida: {n_corridas}')

            nota = int(input('| Nota: '))
            valor = float(input('| Valor: '))
            distancia = float(input('| Distancia: '))

            print('| Passageiro')
            nome_passageiro = str(input('| Nome: '))
            documento_passageiro = str(input('| Documento: '))

            passageiro = Passageiro(nome_passageiro, documento_passageiro)

            corrida = Corrida(nota, distancia, valor, passageiro)

            corridas.append(corrida)
            notas += nota

            if input('Deseja fazer mais uma corrida? (S/N) ').lower == 'n':
                break

        nota = int(notas / n_corridas)
        motorista = Motorista(corridas, nota)

        self.motorista_DAO.update_motorista(id, motorista)

    def delete_motorista(self):
        id = input("Id motorista: ")
        self.motorista_DAO.delete_motorista(id)

    def run(self):
        print("Comandos da CLI: | CREATE | READ | UPDATE | DELETE | QUIT |")
        super().run()
