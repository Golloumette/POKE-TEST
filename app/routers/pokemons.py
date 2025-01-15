"""
Router for handling Pokemon-related endpoints.
"""

from typing import List
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from .. import actions, schemas
from ..utils.utils import get_db
from ..utils.pokeapi import battle_pokemon

router = APIRouter()

@router.get("/", response_model=List[schemas.Pokemon])
def get_pokemons(skip: int = 0, limit: int = 100, database: Session = Depends(get_db)):
    """
    Return all pokemons
    Default limit is 100
    """
    pokemons = actions.get_pokemons(database, skip=skip, limit=limit)
    return pokemons

@router.post("/battle/", response_model=schemas.BattleResult)
def battle_pokemons(battle_request: schemas.BattleRequest):
    """
    Battle between two pokemons by their IDs
    """
    result = battle_pokemon(
        battle_request.first_pokemon_id,
        battle_request.second_pokemon_id
    )
    return result

@router.get("/pokemonsRandom/", response_model=schemas.PokeRandom)
def get_random_pokemons_endpoint():
    """
    Return 3 random pokemons with their stats from the api.
    """
    pokemons = get_random_pokemons_endpoint()
    return pokemons