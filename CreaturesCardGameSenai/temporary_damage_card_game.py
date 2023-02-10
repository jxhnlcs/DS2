from card_game import CardGame
from creature import Creature


class TemporaryDamageCardGame(CardGame):
    def hit(self, attacker: Creature, defender: Creature):
        self.last_health = defender.health
        defender.health -= attacker.attack
        defender.health - self.last_health