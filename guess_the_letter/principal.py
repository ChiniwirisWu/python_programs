import Players as pl
import constants as co
import game_logic as gl


while co.game_state:
    logout = pl.menu()
    if(not logout):
        co.game_state = False
        continue
    gl.gamePlay()
    
    


