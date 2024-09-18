from abc import ABC, abstractmethod

# Шаг 1: Создаем абстрактный класс Weapon
class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass

# Шаг 2: Реализуем конкретные типы оружия
class Sword(Weapon):
    def attack(self):
        return "удар мечом"

class Bow(Weapon):
    def attack(self):
        return "удар из лука"

# Другие виды оружия можно добавлять без изменения существующего кода
class Dagger(Weapon):
    def attack(self):
        return "удар кинжалом"

# Шаг 3: Модифицируем класс Fighter
class Fighter:
    def __init__(self, name):
        self.name = name
        self.weapon = None

    def change_weapon(self, weapon: Weapon):
        self.weapon = weapon
        print(f"{self.name} выбирает {self.weapon.__class__.__name__.lower()}.")

    def attack_monster(self, monster):
        if self.weapon:
            print(f"{self.name} наносит {self.weapon.attack()}.")
            monster.take_damage()
        else:
            print(f"{self.name} не имеет оружия для атаки!")

# Класс Monster
class Monster:
    def __init__(self, health=100):
        self.health = health

    def take_damage(self):
        self.health -= 50
        if self.health <= 0:
            print("Монстр побежден!")
        else:
            print(f"У монстра осталось {self.health} здоровья.")

# Шаг 4: Реализация боя
def main():
    fighter = Fighter("Боец")
    monster = Monster()

    # Выбираем меч и атакуем
    sword = Sword()
    fighter.change_weapon(sword)
    fighter.attack_monster(monster)

    # Выбираем лук и атакуем
    bow = Bow()
    fighter.change_weapon(bow)
    fighter.attack_monster(monster)

    # Добавляем новое оружие - кинжал и атакуем
    dagger = Dagger()
    fighter.change_weapon(dagger)
    fighter.attack_monster(monster)

if __name__ == "__main__":
    main()