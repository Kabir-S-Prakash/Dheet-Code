from random import randint 

name = 'DheetCode'

woodPos = [()]
rumPos = [()]
island1Pos = () #has coordinates as integers
island2Pos = ()
island3Pos = ()

def moveTo(x , y , Pirate):
    position = Pirate.getPosition()
    if position[0] == x and position[1] == y:
        return 0
    if position[0] == x:
        return (position[1] < y) * 2 + 1
    if position[1] == y:
        return (position[0] > x) * 2 + 2
    if randint(1, 2) == 1:
        return (position[0] > x) * 2 + 2
    else:
        return (position[1] < y) * 2 + 1
    
def checkfriends(pirate , quad ):
    sum = 0 
    up = pirate.investigate_up()[1]
    down = pirate.investigate_down()[1]
    left = pirate.investigate_left()[1]
    right = pirate.investigate_right()[1]
    ne = pirate.investigate_ne()[1]
    nw = pirate.investigate_nw()[1]
    se = pirate.investigate_se()[1]
    sw = pirate.investigate_sw()[1]
    
    if(quad=='ne'):
        if(up == 'friend'):
            sum +=1 
        if(ne== 'friend'):
            sum +=1 
        if(right == 'friend'):
            sum +=1 
    if(quad=='se'):
        if(down == 'friend'):
            sum +=1 
        if(right== 'friend'):
            sum +=1 
        if(se == 'friend'):
            sum +=1 
    if(quad=='sw'):
        if(down == 'friend'):
            sum +=1 
        if(sw== 'friend'): 
            sum +=1 
        if(left == 'friend'):
            sum +=1 
    if(quad=='nw'):
        if(up == 'friend'):
            sum +=1 
        if(nw == 'friend'):
            sum +=1 
        if(left == 'friend'):
            sum +=1 

    return sum
    
def spread(pirate):
    sw = checkfriends(pirate ,'sw' )
    se = checkfriends(pirate ,'se' )
    ne = checkfriends(pirate ,'ne' )
    nw = checkfriends(pirate ,'nw' )
    
    my_dict = {'sw': sw, 'se': se, 'ne': ne, 'nw': nw}
    sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[1]))

    x, y = pirate.getPosition()
    
    if( x == 0 , y == 0):
        return randint(1,4)
    
    if(sorted_dict[list(sorted_dict())[3]] == 0 ):
        return randint(1,4)
    
    if(list(sorted_dict())[0] == 'sw'):
        return moveTo(x-1 , y+1 , pirate)
    elif(list(sorted_dict())[0] == 'se'):
        return moveTo(x+1 , y+1 , pirate)
    elif(list(sorted_dict())[0] == 'ne'):
        return moveTo(x+1 , y-1 , pirate)
    elif(list(sorted_dict())[0] == 'nw'):
        return moveTo(x-1 , y-1 , pirate)

def ActPirate(pirate):
    up = pirate.investigate_up()[0]
    down = pirate.investigate_down()[0]
    left = pirate.investigate_left()[0]
    right = pirate.investigate_right()[0]
    current = pirate.investigate_current()
    nw = pirate.investigate_nw()
    ne = pirate.investigate_ne()
    se = pirate.investigate_se()
    sw = pirate.investigate_sw()
    x, y = pirate.getPosition()
    pirate.setSignal("")
    s = pirate.trackPlayers()
    
    if (
        (up == "island1" and nw[0] == "island1" and ne[0] == "island1" and s[0] != "myCaptured")
        or (up == "island2" and nw[0] == "island2" and ne[0] == "island2" and s[1] != "myCaptured")
        or (up == "island3" and nw[0] == "island3" and ne[0] == "island3" and s[2] != "myCaptured")
    ):
        s = up[-1] + str(x) + "," + str(y - 2)
        if(int(up[-1])==1):
            island1Pos = (x,y-2)
        elif(int(up[-1])==2):
            island2Pos = (x,y-2)
        elif(int(up[-1])==3):
            island3Pos = (x,y-2)
        pirate.setTeamSignal(s)

    if (
        (up == "island1" and nw[0] == "island1" and ne[0] != "island1" and s[0] != "myCaptured")
        or (up == "island2" and nw[0] == "island2" and ne[0] != "island2" and s[1] != "myCaptured")
        or (up == "island3" and nw[0] == "island3" and ne[0] != "island3" and s[2] != "myCaptured")
    ):
        s = up[-1] + str(x-1) + "," + str(y - 2)
        if(int(up[-1])==1):
            island1Pos = (x-1,y-2)
        elif(int(up[-1])==2):
            island2Pos = (x-1,y-2)
        elif(int(up[-1])==3):
            island3Pos = (x-1,y-2)
        pirate.setTeamSignal(s)

    if (
        (up == "island1" and nw[0] != "island1" and ne[0] == "island1" and s[0] != "myCaptured")
        or (up == "island2" and nw[0] != "island2" and ne[0] == "island2" and s[1] != "myCaptured")
        or (up == "island3" and nw[0] != "island3" and ne[0] == "island3" and s[2] != "myCaptured")
    ):
        s = up[-1] + str(x+1) + "," + str(y - 2)
        if(int(up[-1])==1):
            island1Pos = (x+1,y-2)
        elif(int(up[-1])==2):
            island2Pos = (x+1,y-2)
        elif(int(up[-1])==3):
            island3Pos = (x+1,y-2)
        pirate.setTeamSignal(s)

    if (
        (down == "island1" and sw[0] == "island1" and se[0] == "island1" and s[0] != "myCaptured")
        or (down == "island2" and sw[0] == "island2" and se[0] == "island2" and s[1] != "myCaptured")
        or (down == "island3" and sw[0] == "island3" and se[0] == "island3" and s[2] != "myCaptured")
    ):
        s = down[-1] + str(x) + "," + str(y + 2)
        if(int(down[-1])==1):
            island1Pos = (x,y+2)
        elif(int(down[-1])==2):
            island2Pos = (x,y+2)
        elif(int(down[-1])==3):
            island3Pos = (x,y+2)
        pirate.setTeamSignal(s)

    if (
        (down == "island1" and sw[0] == "island1" and se[0] != "island1" and s[0] != "myCaptured")
        or (down == "island2" and sw[0] == "island2" and se[0] != "island2" and s[1] != "myCaptured")
        or (down == "island3" and sw[0] == "island3" and se[0] != "island3" and s[2] != "myCaptured")
    ):
        s = down[-1] + str(x-1) + "," + str(y + 2)
        if(int(down[-1])==1):
            island1Pos = (x-1,y+2)
        elif(int(down[-1])==2):
            island2Pos = (x-1,y+2)
        elif(int(down[-1])==3):
            island3Pos = (x-1,y+2)
        pirate.setTeamSignal(s)

    if (
        (down == "island1" and sw[0] != "island1" and se[0] == "island1" and s[0] != "myCaptured")
        or (down == "island2" and sw[0] != "island2" and se[0] == "island2" and s[1] != "myCaptured")
        or (down == "island3" and sw[0] != "island3" and se[0] == "island3" and s[2] != "myCaptured")
    ):
        s = down[-1] + str(x+1) + "," + str(y + 2)
        if(int(down[-1])==1):
            island1Pos = (x+1,y+2)
        elif(int(down[-1])==2):
            island2Pos = (x+1,y+2)
        elif(int(down[-1])==3):
            island3Pos = (x+1,y+2)
        pirate.setTeamSignal(s)

    if (
        (left == "island1" and nw[0] == "island1" and sw[0] == "island1" and s[0] != "myCaptured")
        or (left == "island2" and nw[0] == "island2" and sw[0] == "island2" and s[1] != "myCaptured")
        or (left == "island3" and nw[0] == "island3" and sw[0] == "island3" and s[2] != "myCaptured")
    ):
        s = left[-1] + str(x - 2) + "," + str(y)
        if(int(left[-1])==1):
            island1Pos = (x-2,y)
        elif(int(left[-1])==2):
            island2Pos = (x-2,y)
        elif(int(left[-1])==3):
            island3Pos = (x-2,y)
        pirate.setTeamSignal(s)

    if (
        (left == "island1" and nw[0] == "island1" and sw[0] != "island1" and s[0] != "myCaptured")
        or (left == "island2" and nw[0] == "island2" and sw[0] != "island2" and s[1] != "myCaptured")
        or (left == "island3" and nw[0] == "island3" and sw[0] != "island3" and s[2] != "myCaptured")
    ):
        s = left[-1] + str(x - 2) + "," + str(y-1)
        if(int(left[-1])==1):
            island1Pos = (x-2,y-1)
        elif(int(left[-1])==2):
            island2Pos = (x-2,y-1)
        elif(int(left[-1])==3):
            island3Pos = (x-2,y-1)
        pirate.setTeamSignal(s)

    if (
        (left == "island1" and nw[0] != "island1" and sw[0] == "island1" and s[0] != "myCaptured")
        or (left == "island2" and nw[0] != "island2" and sw[0] == "island2" and s[1] != "myCaptured")
        or (left == "island3" and nw[0] != "island3" and sw[0] == "island3" and s[2] != "myCaptured")
    ):
        s = left[-1] + str(x - 2) + "," + str(y+1)
        if(int(left[-1])==1):
            island1Pos = (x-2,y+1)
        elif(int(left[-1])==2):
            island2Pos = (x-2,y+1)
        elif(int(left[-1])==3):
            island3Pos = (x-2,y+1)
        pirate.setTeamSignal(s)

    if (
        (right == "island1" and ne[0] == "island1" and se[0] == "island1" and s[0] != "myCaptured")
        or (right == "island2" and ne[0] == "island2" and se[0] == "island2" and s[1] != "myCaptured")
        or (right == "island3" and ne[0] == "island3" and se[0] == "island3" and s[2] != "myCaptured")
    ):
        s = right[-1] + str(x + 2) + "," + str(y)
        if(int(right[-1])==1):
            island1Pos = (x+2,y)
        elif(int(right[-1])==2):
            island2Pos = (x+2,y)
        elif(int(right[-1])==3):
            island3Pos = (x+2,y)
        pirate.setTeamSignal(s)

    if (
        (right == "island1" and ne[0] == "island1" and se[0] != "island1" and s[0] != "myCaptured")
        or (right == "island2" and ne[0] == "island2" and se[0] != "island2" and s[1] != "myCaptured")
        or (right == "island3" and ne[0] == "island3" and se[0] != "island3" and s[2] != "myCaptured")
    ):
        s = right[-1] + str(x + 2) + "," + str(y-1)
        if(int(right[-1])==1):
            island1Pos = (x+2,y-1)
        elif(int(right[-1])==2):
            island2Pos = (x+2,y-1)
        elif(int(right[-1])==3):
            island3Pos = (x+2,y-1)
        pirate.setTeamSignal(s)

    if (
        (right == "island1" and ne[0] != "island1" and se[0] == "island1" and s[0] != "myCaptured")
        or (right == "island2" and ne[0] != "island2" and se[0] == "island2" and s[1] != "myCaptured")
        or (right == "island3" and ne[0] != "island3" and se[0] == "island3" and s[2] != "myCaptured")
    ):
        s = right[-1] + str(x + 2) + "," + str(y+1)
        if(int(right[-1])==1):
            island1Pos = (x+2,y+1)
        elif(int(right[-1])==2):
            island2Pos = (x+2,y+1)
        elif(int(right[-1])==3):
            island3Pos = (x+2,y+1)
        pirate.setTeamSignal(s)

    if (
        (ne[0] == "island1" and up != "island1" and right != "island1" and s[0] != "myCaptured")
        or (ne[0] == "island2" and up != "island2" and right != "island2" and s[1] != "myCaptured")
        or (ne[0] == "island3" and up != "island3" and right != "island3" and s[2] != "myCaptured")
    ):
        s = ne[0][-1] + str(x+2) + "," + str(y-2)
        if(int(ne[0][-1])==1):
            island1Pos = (x+2,y-2)
        elif(int(ne[0][-1])==2):
            island2Pos = (x+2,y-2)
        elif(int(ne[0][-1])==3):
            island3Pos = (x+2,y-2)
        pirate.setTeamSignal(s)

    if (
        (nw[0] == "island1" and up != "island1" and left != "island1" and s[0] != "myCaptured")
        or (nw[0] == "island2" and up != "island2" and left != "island2" and s[1] != "myCaptured")
        or (nw[0] == "island3" and up != "island3" and left != "island3" and s[2] != "myCaptured")
    ):
        s = nw[0][-1] + str(x-2) + "," + str(y-2)
        if(int(nw[0][-1])==1):
            island1Pos = (x-2,y-2)
        elif(int(nw[0][-1])==2):
            island2Pos = (x-2,y-2)
        elif(int(nw[0][-1])==3):
            island3Pos = (x-2,y-2)
        pirate.setTeamSignal(s)

    if (
        (sw[0] == "island1" and down != "island1" and left != "island1" and s[0] != "myCaptured")
        or (sw[0] == "island2" and down != "island2" and left != "island2" and s[1] != "myCaptured")
        or (sw[0] == "island3" and down != "island3" and left != "island3" and s[2] != "myCaptured")
    ):
        s = sw[0][-1] + str(x-2) + "," + str(y+2)
        if(int(sw[0][-1])==1):
            island1Pos = (x-2,y+2)
        elif(int(sw[0][-1])==2):
            island2Pos = (x-2,y+2)
        elif(int(sw[0][-1])==3):
            island3Pos = (x-2,y+2)
        pirate.setTeamSignal(s)

    if (
        (se[0] == "island1" and down != "island1" and right != "island1" and s[0] != "myCaptured")
        or (se[0] == "island2" and down != "island2" and right != "island2" and s[1] != "myCaptured")
        or (se[0] == "island3" and down != "island3" and right != "island3" and s[2] != "myCaptured")
    ):
        s = se[0][-1] + str(x+2) + "," + str(y+2)
        if(int(se[0][-1])==1):
            island1Pos = (x+2,y+2)
        elif(int(se[0][-1])==2):
            island2Pos = (x+2,y+2)
        elif(int(se[0][-1])==3):
            island3Pos = (x+2,y+2)
        pirate.setTeamSignal(s)
    
    if pirate.getTeamSignal() != "":
        s = pirate.getTeamSignal()
        l = s.split(",")
        x = int(l[0][1:])
        y = int(l[1])
    
        return moveTo(x, y, pirate)

    else:
        return spread(pirate)


def ActTeam(team):
    l = team.trackPlayers()
    s = team.getTeamSignal()

    team.buildWalls(1)
    team.buildWalls(2)
    team.buildWalls(3)

    if s:
        island_no = int(s[0])
        signal = l[island_no - 1]
        if signal == "myCaptured":
            team.setTeamSignal("")
