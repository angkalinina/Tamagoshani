import json
import os
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
