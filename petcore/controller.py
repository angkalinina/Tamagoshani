from .repository import PetRepository
from .actions import PetAction, apply_action
from .character import Tamagotchi


_instances = {}

def get_pet(user_id: int) -> Tamagotchi:
    pet = PetRepository.load(user_id)
    apply_action(pet, PetAction.TICK)
    return pet


def get_pet_status(user_id: int) -> str:
    pet = PetRepository.load(user_id)
    return pet.get_status_message()


def interact_with_pet(user_id: int, action_str: str) -> str:
    pet = PetRepository.load(user_id)
    try:
        action = PetAction[action_str.upper()]
        apply_action(pet, action)
        PetRepository.save(user_id, pet)
        return pet.get_status_message()
    except KeyError:
        return f"Unknown action: {action_str}"