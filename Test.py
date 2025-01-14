from app.utils.pokeapi import get_pokemon_name, get_pokemon_stats, battle_pokemon


def test_get_pokemon_name():
    print("Testing get_pokemon_name...")
    name = get_pokemon_name(1)  # Bulbasaur
    print(f"Pokemon name for ID 1: {name}")

def test_get_pokemon_stats():
    print("Testing get_pokemon_stats...")
    stats = get_pokemon_stats(1)  # Bulbasaur
    print(f"Pokemon stats for ID 1: {stats}")

def test_battle_pokemon():
    print("Testing battle_pokemon...")
    result = battle_pokemon(1, 2)  # Bulbasaur vs Ivysaur
    print(f"Battle result between ID 1 and ID 2: {result}")

if __name__ == "__main__":
    test_get_pokemon_name()
    test_get_pokemon_stats()    
    test_battle_pokemon()