# Marco Di Toro | 150 | GES

from motorista_CLI import Motorista_CLI
from motorista_DAO import Motorista_DAO


if __name__ == '__main__':
    motoristaDAO = Motorista_DAO('EX01-Marco', 'Motoristas')

    cli = Motorista_CLI(motoristaDAO)
    cli.run()
