import Pyro4
import sys
from Pyro4.util import SerializerBase


pokedex = Pyro4.Proxy("PYRO:obj_2ac6a29cdd1e40c58a87579bb6c6f2c5@localhost:58469")
try:
    pokedex._pyroBind()
except:
    sys.exit(-1)

while True:
    print("\nMenu:")
    print("1. Adicionar Pokémon")
    print("2. Ler Pokémon")
    print("3. Atualizar Pokémon")
    print("4. Excluir Pokémon")
    print("5. Sair")

    choice = input("Escolha uma opção: ")

    if choice == "1":
        nome = input("Nome do Pokémon: ")
        tipo = input("Tipo do Pokémon: ")
        raridade = input("Raridade do Pokémon: ")
        peso = float(input("Peso do Pokémon: "))
        altura = float(input("Altura do Pokémon: "))
        numero = int(input("Número na Pokédex: "))

        data = {
            'numero': numero,
            'nome': nome,
            'tipo': tipo,
            'raridade': raridade,
            'peso': peso,
            'altura': altura
        }
        pokedex.create_pokemon(data)

    elif choice == "2":
        leitura = pokedex.read_pokedex()
        for pokemon in leitura:
            print(f"Nome: {pokemon['nome']}, Tipo: {pokemon['tipo']}, Raridade: {pokemon['raridade']}, Peso: {pokemon['peso']}, Altura: {pokemon['altura']}")

    elif choice == "3":
        numero = int(input("Número na Pokédex do Pokémon a ser atualizado: "))
        nome = input("Novo nome do Pokémon: ")
        tipo = input("Novo tipo do Pokémon: ")
        raridade = input("Nova raridade do Pokémon: ")
        peso = float(input("Novo peso do Pokémon: "))
        altura = float(input("Nova altura do Pokémon: "))

        data = {
            'numero': numero,
            'nome': nome,
            'tipo': tipo,
            'raridade': raridade,
            'peso': peso,
            'altura': altura
        }
        pokedex.update_pokemon(numero, data)

    elif choice == "4":
        numero = int(input("Número na Pokédex do Pokémon a ser excluído: "))
        pokedex.delete_pokemon(numero)

    elif choice == "5":
        print("Encerrando o programa.")
        break

    else:
        print("Opção inválida. Tente novamente.")