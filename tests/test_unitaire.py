"""
This module contains unit tests for the POKE-TEST application.
"""

from fastapi.testclient import TestClient
from unittest.mock import patch
from main import app

client = TestClient(app)

def test_battle_endpoint_winner():
    """
    Test the /battle/ endpoint for determining the winner.
    """
    response = client.post("pokemons/battle/", json={
        "first_pokemon_id": 1,
        "second_pokemon_id": 2
    })
    assert response.status_code == 200
    json_response = response.json()
    assert "winner" in json_response
    assert json_response["winner"] == "ivysaur"


def test_fetch_random_pokemons():
    """
    Test the /pokemonsRandom/ endpoint for fetching random pokemons.
    """
    response = client.get("pokemons/pokemonsRandom/")
    assert response.status_code == 200
    assert len(response.json()) == 1


def test_battle_endpoint_second_wins():
    """
    Test the /battle/ endpoint with mocked battle_pokemon where the second pokemon wins.
    """
    response = client.post("pokemons/battle/", json={
        "first_pokemon_id": 4,
        "second_pokemon_id": 3
    })
    assert response.status_code == 200
    assert response.json()["winner"] == "venusaur"


def test_battle_endpoint_draw():
    """
    Test the /battle/ endpoint with mocked battle_pokemon resulting in a draw.
    """
    response = client.post("pokemons/battle/", json={
        "first_pokemon_id": 5,
        "second_pokemon_id": 5
    })
    assert response.status_code == 200
    assert response.json()["winner"] == "draw"
    
def test_create_trainer():
    """
    Test si trainer is present
    """
    response = client.post("trainers/", json={
       "name" : "sacha",
       "birthdate" : "1986-05-21" 
    })
    assert response.status_code == 200
    
@patch("app.routers.pokemons.battle_pokemon", return_value={"winner": "ivysaur", "score": "2-1"})
def test_battle_endpoint_winner_mock(mock_battle_pokemon):
    """
    Test the /battle/ endpoint for determining the winner (mocked version).
    """
    response = client.post("pokemons/battle/", json={
        "first_pokemon_id": 1,
        "second_pokemon_id": 2
    })
    assert response.status_code == 200
    json_response = response.json()
    assert "winner" in json_response
    assert json_response["winner"] == "ivysaur"
    mock_battle_pokemon.assert_called_once_with(1, 2)

@patch("app.routers.pokemons.battle_pokemon", return_value={"winner": "venusaur", "score": "0-1"})
def test_battle_endpoint_second_wins_mock(mock_battle_pokemon):
    """
    Test the /battle/ endpoint where the second pokemon wins (mocked version).
    """
    response = client.post("pokemons/battle/", json={
        "first_pokemon_id": 4,
        "second_pokemon_id": 3
    })
    assert response.status_code == 200
    json_response = response.json()
    assert json_response["winner"] == "venusaur"
    mock_battle_pokemon.assert_called_once_with(4, 3)
    
@patch("app.routers.trainers.get_trainers", return_value=[
    {"id": 1, "name": "sacha", "birthdate": "1986-05-21"}
])
def test_trainer_mock(mock_get_trainers):
    """
    Test the /trainers/ GET endpoint with mocked get_trainers.
    Vérifie si 'sacha' est présent dans la liste des trainers.
    """
    response = client.get("/trainers")  # Corrected endpoint path
    assert response.status_code == 200
    trainers_list = response.json()
    assert any(trainer["name"] == "sacha" for trainer in trainers_list)
    mock_get_trainers.assert_called_once()