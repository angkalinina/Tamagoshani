from .character import Tamagotchi

_instances = {}

def get_pet(user_id: int) -> Tamagotchi:
    if user_id not in _instances:
        _instances[user_id] = Tamagotchi(name=f"Tama_{user_id}")
    pet = _instances[user_id]
    pet.tick()
    return pet

def get_pet_status(user_id: int) -> str:
    return get_pet(user_id).get_status_message()

def interact_with_pet(user_id: int, action: str) -> str:
    pet = get_pet(user_id)
    if action == "feed":
        pet.feed()
    elif action == "play":
        pet.play()
    elif action == "rest":
        pet.rest()
    return pet.get_status_message()
