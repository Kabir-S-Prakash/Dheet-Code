from engine.main import Game
import script1
import script

if __name__ == "__main__":
    G = Game((40, 40), script, script1)
    G.run_game()