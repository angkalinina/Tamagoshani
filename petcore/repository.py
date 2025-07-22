import json
import os
from models import Pet
from db import SessionLocal
from .character import Tamagotchi

class PetRepository:
    SAVE_FOLDER = "saves"

    @classmethod
    def _get_filepath(cls, user_id: int) -> str:
        return os.path.join(cls.SAVE_FOLDER, f"{user_id}.json")

    @classmethod
    def load(cls, user_id: int) -> Tamagotchi:
        filepath = cls._get_filepath(user_id)
        if not os.path.exists(filepath):
            return Tamagotchi(name=f"Tama_{user_id}")

        with open(filepath, "r") as f:
            data = json.load(f)

        pet = Tamagotchi(name=data.get("name", f"Tama_{user_id}"))
        pet.hunger = data.get("hunger", 50)
        pet.energy = data.get("energy", 100)
        return pet

    @classmethod
    def save(cls, user_id: int, pet: Tamagotchi):
        os.makedirs(cls.SAVE_FOLDER, exist_ok=True)
        filepath = cls._get_filepath(user_id)
        data = {
            "name": pet.name,
            "hunger": pet.hunger,
            "energy": pet.energy
        }
        with open(filepath, "w") as f:
            json.dump(data, f)
 @staticmethod
    def load(user_id: int) -> Tamagotchi:
        db = SessionLocal()
        pet_db = db.query(Pet).filter(Pet.user_id == user_id).first()
        db.close()
        if not pet_db:
            return Tamagotchi(name=f"Tama_{user_id}")
        pet = Tamagotchi(name=pet_db.name)
        pet.hunger = pet_db.hunger
        pet.energy = pet_db.energy
        return pet

    @staticmethod
    def save(user_id: int, pet: Tamagotchi):
        db = SessionLocal()
        pet_db = db.query(Pet).filter(Pet.user_id == user_id).first()
        if not pet_db:
            pet_db = Pet(user_id=user_id, name=pet.name)
            db.add(pet_db)
        pet_db.hunger = pet.hunger
        pet_db.energy = pet.energy
        db.commit()
        db.close()