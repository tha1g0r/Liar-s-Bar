import random

class DeckPlayer:
    def __init__(self, name):
        self.name = name
        self.cylinder = ["bullet", "empty", "empty", "empty", "empty", "empty"]
        random.shuffle(self.cylinder)
        self.alive = True

class DicePlayer:
    def __init__(self, name):
        self.name = name
        self.life = 2
        self.alive = True

def validate_name(name, players_names):
    if name in players_names:
        return True
    return False

def validate_alive(name, game_players):
    for player in game_players:
        if (player.name == name):
            return player.alive
    return False

def count_alive(game_players):
    alive_count = 4
    for player in game_players:
        if not (player.alive):
            alive_count -= 1
        else:
            winner = player
    
    if (alive_count == 1):
        print(f"\nParabéns, {winner.name}!!!")
    
    return alive_count
        
def enter_players_names():
    print("Insira o nome dos jogadores -")
    player_1_name = input("  1º jogador: ").upper().strip()
    player_2_name = input("  2º jogador: ").upper().strip()
    player_3_name = input("  3º jogador: ").upper().strip()
    player_4_name = input("  4º jogador: ").upper().strip()

    return [player_1_name, player_2_name, player_3_name, player_4_name]

def create_deck_players(players_names:list):
    return [DeckPlayer(name) for name in players_names]

def random_deck():
    decks = ["Ace", "Queen", "King"]
    deck = decks[random.randint(0, 2)]
    return f"{deck}'s table!"

def liars_deck(players_names:list, deck_players:list):
    print(f"\n{random_deck()}")
    playing = True
    while (playing):
        # show_bullets(deck_players) ###
        liar_name = input("\nJogador a ir para a roleta: ").upper().strip()

        if (validate_name(liar_name, players_names)):
            if (validate_alive(liar_name, deck_players)):
                for player in deck_players:
                    if (player.name == liar_name):
                        print(player.cylinder[0]) #
                        if (player.cylinder[0] == "bullet"):
                            print(f"Fim de jogo para você, {liar_name}!")
                            player.alive = False
                            alive_count = count_alive(deck_players)
                            if (alive_count == 1):
                                playing = False
                        else:
                            print("Ufa...")
                            player.cylinder.pop(0)
            else:
                print("O jogador referido se encontra morto.")

        else:
            print("Nome inválido.")

def create_dice_players(players_names:list):
    return [DicePlayer(name) for name in players_names]

def check_dice_dead(player:object):
    if (player.life == 0):
        player.alive = False
        print(f"{player.name} está morto(a)!")

def liars_dice(players_names:list, dice_players:list):
    playing = True
    while (playing):
        liar_name = input("\nJogador a ser envenenado: ").upper().strip()

        if (validate_name(liar_name, players_names)):
            if (validate_alive(liar_name, dice_players)):
                for player in dice_players:
                    if (player.name == liar_name):
                        print(f"{liar_name} foi envenenado.")
                        player.life -= 1
                        check_dice_dead(player)
                        alive_count = count_alive(dice_players)
                        if (alive_count == 1):
                            playing = False
            else:
                print("O jogador referido se encontra morto.")

        else:
            print("Nome inválido.")

def show_bullets(deck_playes:list):
    for player in deck_playes:
        print(player.cylinder)

def main():
    print("========== Liar's Bar ==========\n")

    # Entering players names
    players_names = enter_players_names()
    # print(players_names) ###

    playing = True
    while (playing):
        print("""
Modos de jogo:
  1 - Liar's Deck
  2 - Liar's Dice\n""")
        choosing_game_mode = True
        while (choosing_game_mode):
            game = int(input("Escolha o modo de jogo: "))
            # print("\n")

            if (game==1):
                deck_players = create_deck_players(players_names)
                # show_bullets(deck_players) ###
                liars_deck(players_names, deck_players)
                choosing_game_mode = False

            elif (game==2):
                dice_players = create_dice_players(players_names)
                liars_dice(players_names, dice_players)
                choosing_game_mode = False
            
            else:
                print("Modo de jogo inválido.\n")
        
        again = input("\nJogar novamente? (s/n): ").upper().strip()
        if (again != "S"):
            playing == False

main()