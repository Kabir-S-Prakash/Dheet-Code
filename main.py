from engine.main import Game
import scriptblue
import script1

if __name__ == "__main__":
    G = Game((40, 40), script1, script1)
    G.run_game()