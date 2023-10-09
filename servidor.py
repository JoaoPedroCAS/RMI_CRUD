import Pyro4
from Pyro4.util import SerializerBase

@Pyro4.expose
class PokedexServer:
    def __init__(self):
        self.pokedex = []

    def create_pokemon(self, data):
        self.pokedex.append(data)

    def read_pokedex(self):
        return self.pokedex

    def update_pokemon(self, pokedex_number, data):
        for i, pokemon in enumerate(self.pokedex):
            if pokemon['numero'] == pokedex_number:
                self.pokedex[i] = data  # Atualiza os dados de um Pokémon na Pokedex.
                return True
        return False
    def delete_pokemon(self, pokedex_number):
        for i, item_data in enumerate(self.pokedex):
            if item_data["numero"] == pokedex_number:
                del self.pokedex[i]
                return True
        return False
    
def main():

    daemon = Pyro4.Daemon()
    uri = daemon.register(PokedexServer)

    #dns_fake = Pyro4.locateNS()
    #dns_fake.register("pokedex",uri)

    print(uri)
    daemon.requestLoop()

if __name__ == '__main__':
    main()
