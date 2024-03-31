sword = ["Wooden Sword", "Stone Sword", "Iron Sword", "Diamond Sword"]


class Enemy():

  def __init__(self, hp, damage):
    self.hp = hp
    self.damage = damage

  def check(self):
    print("======Enemy status=======")
    print("hp : " + str(self.hp))
    print("damage : " + str(self.damage))

  def damaged(self, damage):
    self.hp = self.hp - damage

  def attack(self):
    print("\nYou have been attacked by the enemy")
    print("He did " + str(self.damage) + " damage")
    player.damaged(int(self.damage))


class Player():

  def __init__(self, hp, mana, damage, equipped_sword, inventory):
    self.hp = hp
    self.equipped_sword = equipped_sword
    self.mana = mana
    self.damage = damage
    self.inventory = inventory

  def check(self):
    print("=======Player Status========")
    print("hp : " + str(self.hp))
    print("mana : " + str(self.mana))
    print("damage : " + str(self.damage))
    print("equipped sword : " + str(self.equipped_sword))
    print("inventory :")
    for i in self.inventory:
      print(i)

  def set_weapon(self, x):
    if x == 0:
      self.damage = 10
      self.equipped_sword = sword[0]
    elif x == 1:
      self.damage = 15
      self.equipped_sword = sword[1]
    elif x == 2:
      self.damage = 20
      self.equipped_sword = sword[2]
    elif x == 3:
      self.damage = 40
      self.equipped_sword = sword[3]

    print("You Equipped a " + str(self.equipped_sword))

  def damaged(self, damage):
    self.hp = self.hp - damage
    print("You have been attacked -" + str(damage))
    print("HP : " + str(self.hp))

  def heal(self):
    for i in self.inventory:
      if i == "Healing Potion":
        self.hp = self.hp + 10
        print("You have been healed")
      else:
        pass
      self.inventory.remove("Healing Potion")

  def add_item(self, items):
    self.inventory.append(items)
    print(items + " has been added to your inventory")

  def player_attack(self):
    print("You attacked the enemy with your " + str(self.equipped_sword))
    print("You did " + str(self.damage) + " damage")
    enemy.damaged(int(self.damage))


enemy = Enemy(100, 20)
player = Player(hp=100,
                equipped_sword=sword[0],
                mana=100,
                damage=10,
                inventory=[])

enemy.check()
player.check()

enemy.attack()

player.check()

player.add_item("Healing Potion")
player.heal()
player.check()
