import datetime

class Tamagotchi:
    def __init__(self, name="Tama"):
        self.name = name
        self.hunger = 50
        self.energy = 100
        self.last_updated = datetime.datetime.now()

    def feed(self):
        self.hunger = min(100, self.hunger + 20)

    def play(self):
        self.energy = max(0, self.energy - 15)

    def rest(self):
        self.energy = min(100, self.energy + 10)

    def tick(self):
        now = datetime.datetime.now()
        minutes_passed = (now - self.last_updated).seconds // 60
        if minutes_passed > 0:
            self.hunger = max(0, self.hunger - minutes_passed)
            self.energy = max(0, self.energy - minutes_passed // 2)
            self.last_updated = now

    def get_status(self):
        return {
            "name": self.name,
            "hunger": self.hunger,
            "energy": self.energy
        }

    def get_status_message(self):
        return (
            f" {self.name}'s Status:\n"
            f"Hunger: {self.hunger}\n"
            f"️ Energy: {self.energy}"
        )
