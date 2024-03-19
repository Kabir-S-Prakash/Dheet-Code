from engine.main import Game
import scriptblue
import script

if __name__ == "__main__":
    G = Game((40, 40), script, script)
    G.run_game()