"""
Schemas for the PokeAPI application.
"""

from datetime import date
from typing import List, Optional, Union
from pydantic import BaseModel

class ItemBase(BaseModel):
    """
    Base schema for an item.
    """
    name: str
    description: Union[str, None] = None

class ItemCreate(ItemBase):
    """
    Schema for creating a new item.
    """

class Item(ItemBase):
    """
    Schema for representing an item.
    """
    id: int
    trainer_id: int

    class Config:
        """
        Configuration for the schema.
        """
        orm_mode = True

class PokemonBase(BaseModel):
    """
    Base schema for a Pokemon.
    """
    api_id: int
    custom_name: Optional[str] = None

class PokemonCreate(PokemonBase):
    """
    Schema for creating a new Pokemon.
    """

class Pokemon(PokemonBase):
    """
    Schema for representing a Pokemon.
    """
    id: int
    name: str
    trainer_id: int

    class Config:
        """
        Configuration for the schema.
        """
        orm_mode = True

class TrainerBase(BaseModel):
    """
    Base schema for a trainer.
    """
    name: str
    birthdate: date

class TrainerCreate(TrainerBase):
    """
    Schema for creating a new trainer.
    """

class Trainer(TrainerBase):
    """
    Schema for representing a trainer.
    """
    id: int
    inventory: List[Item] = []

    class Config:
        """
        Configuration for the schema.
        """
        orm_mode = True

class BattleRequest(BaseModel):
    """
    Schema for a battle request.
    """
    first_pokemon_id: int
    second_pokemon_id: int

class BattleResult(BaseModel):
    """
    Schema for the result of a battle.
    """
    winner: str
    score: str

class Stat(BaseModel):
    """
    Schema for a Pokemon's stat.
    """
    name: str
    base_stat: int
    
class PokeRandom(BaseModel):
    """
    Schema for 3 random pokemons with their stats from the api.
    """
    pokemons: dict