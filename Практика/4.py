class Player:
    max_level = 13
    min_hp = 0


player_1 = Player()
player_2 = Player()

player_1.name = input()
player_1.level = int(input())
player_1.hp = int(input())

player_2.name = input()
player_2.level = int(input())
player_2.hp = int(input())

action = input()
if action == 'player_1 shoots player_2':
    player_2.hp = player_2.hp - 50 if player_2.hp >= 50 else Player.min_hp
    if player_2.hp == Player.min_hp:
        player_1.level = player_1.level + 1 if player_1.level < Player.max_level else Player.max_level
elif action == 'player_2 shoots player_1':
    player_1.hp = player_1.hp - 50 if player_1.hp >= 50 else Player.min_hp
    if player_1.hp == Player.min_hp:
        player_2.level = player_2.level + 1 if player_2.level < Player.max_level else Player.max_level

print(f'player_1. name: {player_1.name}, hp: {player_1.hp}, level: {player_1.level}')
print(f'player_2. name: {player_2.name}, hp: {player_2.hp}, level: {player_2.level}')