from enum import Enum, auto
from .character import Tamagotchi


class PetAction(Enum):
    FEED = auto()
    PLAY = auto()
    REST = auto()
    TICK = auto()


def apply_action(pet: Tamagotchi, action: PetAction) -> str:
    if action == PetAction.FEED:
        pet.feed()
    elif action == PetAction.PLAY:
        pet.play()
    elif action == PetAction.REST:
        pet.rest()
    elif action == PetAction.TICK:
        pet.tick()

    return pet.get_status_message()
