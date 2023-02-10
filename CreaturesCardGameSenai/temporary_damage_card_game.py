from card_game import CardGame
from creature import Creature


class TemporaryDamageCardGame(CardGame):
    def hit(self, attacker: Creature, defender: Creature):
        self.last_health = defender.health
        defender.health -= attacker.attack
        
        print('-' * 15, 'Temporary damage hit', '-' * 15)
        print(f'{attacker.name} causou {attacker.attack} de dano...\n')
        print(f"{defender.name}'s HP: {defender.health}")
        defender.health - self.last_health