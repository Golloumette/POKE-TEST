"""
Module for interacting with the PokeAPI and handling Pokemon battles.
"""

import requests

BASE_URL = "https://pokeapi.co/api/v2"

def get_pokemon_name(api_id):
    """
    Get a pokemon name from the API pokeapi
    """
    return get_pokemon_data(api_id)['name']

def get_pokemon_stats(api_id):
    """
    Get pokemon stats from the API pokeapi
    """
    pokemon_data = get_pokemon_data(api_id)
    statistique = pokemon_data['stats']
    stats = {}
    for stat in statistique:
        stats[stat['stat']['name']] = stat['base_stat']
    return stats

def get_pokemon_data(api_id):
    """
    Get data of pokemon name from the API pokeapi
    """
    return requests.get(f"{BASE_URL}/pokemon/{api_id}", timeout=10).json()

def battle_compare_stats(first_pokemon_stats, second_pokemon_stats):
    """
    Compare given stat between two pokemons
    """
    first_pokemon_score = 0
    second_pokemon_score = 0
    name_stat = ['hp', 'attack', 'defense', 'special-attack', 'special-defense', 'speed']

    for stat in name_stat:
        if first_pokemon_stats[stat] > second_pokemon_stats[stat]:
            first_pokemon_score += 1
        elif first_pokemon_stats[stat] < second_pokemon_stats[stat]:
            second_pokemon_score += 1

    if first_pokemon_score > second_pokemon_score:
        return {
            "winner": "first_pokemon",
            "score": f"{first_pokemon_score} - {second_pokemon_score}"
        }
    if first_pokemon_score < second_pokemon_score:
        return {
            "winner": "second_pokemon",
            "score": f"{first_pokemon_score} - {second_pokemon_score}"
        }
    return {
        "winner": "draw",
        "score": f"{first_pokemon_score} - {second_pokemon_score}"
    }

def battle_pokemon(first_api_id, second_api_id):
    """
    Do battle between 2 pokemons
    """
    first_pokemon = get_pokemon_stats(first_api_id)
    second_pokemon = get_pokemon_stats(second_api_id)
    battle_result = battle_compare_stats(
        first_pokemon, second_pokemon
    )
    return battle_result
