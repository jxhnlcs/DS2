from card_game import CardGame
from creature import Creature


class PermanentDamageCardGame(CardGame):
    def hit(self, attacker: Creature, defender: Creature):
        defender.health -= attacker.attack
        
        print('-' * 15, 'Permanent damage hit', '-' * 15)
        print(f'{attacker.name} causou {attacker.attack} de dano...\n')
        print(f"{defender.name}'s HP: {defender.health}")