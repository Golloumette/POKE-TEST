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

def test_create_trainer():
    """
    Test pour créer un treaner
    """
    response = client.post("trainers/", json={
       "name" : "sacha",
       "birthdate" : "1986-05-21" 
    })
    assert response.status_code == 200


def test_battle_endpoint_mock_first_wins():
    """
    Test the /battle/ endpoint with mocked battle_pokemon where the first pokemon wins.
    """
    response = client.post("pokemons/battle/", json={
        "first_pokemon_id": 3,
        "second_pokemon_id": 4
    })
    assert response.status_code == 200
    assert response.json()["winner"] == "venusaur"


def test_battle_endpoint_mock_draw():
    """
    Test the /battle/ endpoint with mocked battle_pokemon resulting in a draw.
    """
    response = client.post("pokemons/battle/", json={
        "first_pokemon_id": 5,
        "second_pokemon_id": 5
    })
    assert response.status_code == 200
    assert response.json()["winner"] == "draw"

def test_getTrainer():
    response = client.get("trainers/1")
    assert response.status_code == 200
    trainer = response.json()
    assert "name" in trainer 
    assert trainer["name"] == "sacha"

def test_return_mock(mocker):
    mocker.patch(
      "main.get_double",
      return_value=10
   )
    response = client.get("/5")
    assert response.json() == 10
    assert response.status_code == 200