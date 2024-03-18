from random import randint 
import time
import random

name = 'DheetCode'

woodPos = [()]
rumPos = [()]

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

def downRight():
    r = randint(1,10000000)
    if r%100>=1 and r%100<=40:
        return 3
    if r%100>=41 and r%100<=80:
        return 2
    if r%100>=81 and r%100<=90:
        return 1
    if r%100>=91 and r%100<100:
        return 4
    
def upRight():
    r = randint(1,10000000)
    if r%100>=1 and r%100<=40:
        return 1
    if r%100>=41 and r%100<=80:
        return 2
    if r%100>=81 and r%100<=90:
        return 3
    if r%100>=91 and r%100<100:
        return 4
    
def downLeft():
    r = randint(1,1000000)
    if r%100>=1 and r%100<=40:
        return 3
    if r%100>=41 and r%100<=80:
        return 4
    if r%100>=81 and r%100<=90:
        return 1
    if r%100>=91 and r%100<100:
        return 2
    
def upLeft():
    r = randint(1,1000000)
    if r%100>=1 and r%100<=40:
        return 1
    if r%100>=41 and r%100<=80:
        return 4
    if r%100>=81 and r%100<=90:
        return 3
    if r%100>=91 and r<100:
        return 2

def spread(pirate):
    random.seed(time.time())
    sw = checkfriends(pirate ,'sw' )
    se = checkfriends(pirate ,'se' )
    ne = checkfriends(pirate ,'ne' )
    nw = checkfriends(pirate ,'nw' )
    
    my_dict = {'sw': sw, 'se': se, 'ne': ne, 'nw': nw}
    sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[1]))

    x, y = pirate.getPosition()
    xi, yi = pirate.getDeployPoint()
    
    if (xi==0 and yi==0 and x<15 and y<15):
        return downRight()
    
    elif (xi==39 and yi==39 and x>24 and y>24):
        return upLeft()
    
    elif (xi==0 and yi==39 and x<15 and y>24):
        return upRight()
    
    elif (xi==39 and yi==0 and x>24 and y<15):
        return downLeft()
    
    elif(sorted_dict[list(sorted_dict)[3]] == 0 ):
        return randint(1,4)
    
    elif(list(sorted_dict)[0][0] == 'sw'):
        return moveTo(x-1 , y+1 , pirate)
    elif(list(sorted_dict)[0][0] == 'se'):
        return moveTo(x+1 , y+1 , pirate)
    elif(list(sorted_dict)[0][0] == 'ne'):
        return moveTo(x+1 , y-1 , pirate)
    elif(list(sorted_dict)[0][0] == 'nw'):
        return moveTo(x-1 , y-1 , pirate)
    else:
        return randint(1,4)

def findOppOnIsland(island,pirate):   #island as string 
    x = pirate.getPosition()[0]
    y = pirate.getPosition()[1]
    up = pirate.investigate_up()
    down = pirate.investigate_down()
    left = pirate.investigate_left()
    right = pirate.investigate_right()
    current = pirate.investigate_current()
    nw = pirate.investigate_nw()
    ne = pirate.investigate_ne()
    se = pirate.investigate_se()
    sw = pirate.investigate_sw()
    if (current[1] == "enemy" or current[1] == "both"):
        s = island[-1] + str(x) + "," + str(y)
        pirate.setTeamSignal(s)
    elif(up[1] == "enemy" or up[1] == "both"):
        s = island[-1] + str(x) + "," + str(y-1)
        pirate.setTeamSignal(s)
    elif(down[1] == "enemy" or down[1] == "both"):
        s = island[-1] + str(x) + "," + str(y+1)
        pirate.setTeamSignal(s)
    elif(left[1] == "enemy" or left[1] == "both"):
        s = island[-1] + str(x-1) + "," + str(y)
        pirate.setTeamSignal(s)
    elif(right[1] == "enemy" or right[1] == "both"):
        s = island[-1] + str(x+1) + "," + str(y)
        pirate.setTeamSignal(s)
    elif(nw[1] == "enemy" or nw[1] == "both"):
        s = island[-1] + str(x-1) + "," + str(y-1)
        pirate.setTeamSignal(s)
    elif(ne[1] == "enemy" or ne[1] == "both"):
        s = island[-1] + str(x+1) + "," + str(y-1)
        pirate.setTeamSignal(s)
    elif(se[1] == "enemy" or se[1] == "both"):
        s = island[-1] + str(x+1) + "," + str(y+1)
        pirate.setTeamSignal(s)
    elif(sw[1] == "enemy" or sw[1] == "both"):
        s = island[-1] + str(x-1) + "," + str(y+1)
        pirate.setTeamSignal(s)

def ActPirate(pirate):
    island1Pos = ()
    island2Pos = ()
    island3Pos = ()
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
        (up == "island1" and nw[0] == "island1" and ne[0] == "island1" and (s[0] == "" or s[3] == "oppCaptured"))
        or (up == "island2" and nw[0] == "island2" and ne[0] == "island2" and (s[1] == "" or s[4] == "oppCaptured"))
        or (up == "island3" and nw[0] == "island3" and ne[0] == "island3" and (s[2] == "" or s[5] == "oppCaptured"))
    ):
        sig = up[-1] + str(x) + "," + str(y - 2)
        if(int(up[-1])==1):
            island1Pos = (x,y-2)
        elif(int(up[-1])==2):
            island2Pos = (x,y-2)
        elif(int(up[-1])==3):
            island3Pos = (x,y-2)
        #pirate.setTeamSignal(sig)
        return 1
    if (
        (up == "island1" and nw[0] == "island1" and ne[0] != "island1" and (s[0] == "" or s[3] == "oppCaptured"))
        or (up == "island2" and nw[0] == "island2" and ne[0] != "island2" and (s[1] == "" or s[4] == "oppCaptured"))
        or (up == "island3" and nw[0] == "island3" and ne[0] != "island3" and (s[2] == "" or s[5] == "oppCaptured"))
    ):
        sig = up[-1] + str(x-1) + "," + str(y - 2)
        if(int(up[-1])==1):
            island1Pos = (x-1,y-2)
        elif(int(up[-1])==2):
            island2Pos = (x-1,y-2)
        elif(int(up[-1])==3):
            island3Pos = (x-1,y-2)
        #pirate.setTeamSignal(sig)
        return 1
    if (
        (up == "island1" and nw[0] != "island1" and ne[0] == "island1" and (s[0] == "" or s[3] == "oppCaptured"))
        or (up == "island2" and nw[0] != "island2" and ne[0] == "island2" and (s[1] == "" or s[4] == "oppCaptured"))
        or (up == "island3" and nw[0] != "island3" and ne[0] == "island3" and (s[2] == "" or s[5] == "oppCaptured"))
    ):
        sig = up[-1] + str(x+1) + "," + str(y - 2)
        if(int(up[-1])==1):
            island1Pos = (x+1,y-2)
        elif(int(up[-1])==2):
            island2Pos = (x+1,y-2)
        elif(int(up[-1])==3):
            island3Pos = (x+1,y-2)
        #pirate.setTeamSignal(sig)
        return 1
    if (
        (down == "island1" and sw[0] == "island1" and se[0] == "island1" and (s[0] == "" or s[3] == "oppCaptured"))
        or (down == "island2" and sw[0] == "island2" and se[0] == "island2" and (s[1] == "" or s[4] == "oppCaptured"))
        or (down == "island3" and sw[0] == "island3" and se[0] == "island3" and (s[2] == "" or s[5] == "oppCaptured"))
    ):
        sig = down[-1] + str(x) + "," + str(y + 2)
        if(int(down[-1])==1):
            island1Pos = (x,y+2)
        elif(int(down[-1])==2):
            island2Pos = (x,y+2)
        elif(int(down[-1])==3):
            island3Pos = (x,y+2)
        #pirate.setTeamSignal(sig)
        return 3
    if (
        (down == "island1" and sw[0] == "island1" and se[0] != "island1" and (s[0] == "" or s[3] == "oppCaptured"))
        or (down == "island2" and sw[0] == "island2" and se[0] != "island2" and (s[1] == "" or s[4] == "oppCaptured"))
        or (down == "island3" and sw[0] == "island3" and se[0] != "island3" and (s[2] == "" or s[5] == "oppCaptured"))
    ):
        sig = down[-1] + str(x-1) + "," + str(y + 2)
        if(int(down[-1])==1):
            island1Pos = (x-1,y+2)
        elif(int(down[-1])==2):
            island2Pos = (x-1,y+2)
        elif(int(down[-1])==3):
            island3Pos = (x-1,y+2)
        #pirate.setTeamSignal(sig)
        return 3
    if (
        (down == "island1" and sw[0] != "island1" and se[0] == "island1" and (s[0] == "" or s[3] == "oppCaptured"))
        or (down == "island2" and sw[0] != "island2" and se[0] == "island2" and (s[1] == "" or s[4] == "oppCaptured"))
        or (down == "island3" and sw[0] != "island3" and se[0] == "island3" and (s[2] == "" or s[5] == "oppCaptured"))
    ):
        sig = down[-1] + str(x+1) + "," + str(y + 2)
        if(int(down[-1])==1):
            island1Pos = (x+1,y+2)
        elif(int(down[-1])==2):
            island2Pos = (x+1,y+2)
        elif(int(down[-1])==3):
            island3Pos = (x+1,y+2)
        #pirate.setTeamSignal(sig)
        return 3
    if (
        (left == "island1" and nw[0] == "island1" and sw[0] == "island1" and (s[0] == "" or s[3] == "oppCaptured"))
        or (left == "island2" and nw[0] == "island2" and sw[0] == "island2" and (s[1] == "" or s[4] == "oppCaptured"))
        or (left == "island3" and nw[0] == "island3" and sw[0] == "island3" and (s[2] == "" or s[5] == "oppCaptured"))
    ):
        sig = left[-1] + str(x - 2) + "," + str(y)
        if(int(left[-1])==1):
            island1Pos = (x-2,y)
        elif(int(left[-1])==2):
            island2Pos = (x-2,y)
        elif(int(left[-1])==3):
            island3Pos = (x-2,y)
        #pirate.setTeamSignal(sig)
        return 4
    if (
        (left == "island1" and nw[0] == "island1" and sw[0] != "island1" and (s[0] == "" or s[3] == "oppCaptured"))
        or (left == "island2" and nw[0] == "island2" and sw[0] != "island2" and (s[1] == "" or s[4] == "oppCaptured"))
        or (left == "island3" and nw[0] == "island3" and sw[0] != "island3" and (s[2] == "" or s[5] == "oppCaptured"))
    ):
        sig = left[-1] + str(x - 2) + "," + str(y-1)
        if(int(left[-1])==1):
            island1Pos = (x-2,y-1)
        elif(int(left[-1])==2):
            island2Pos = (x-2,y-1)
        elif(int(left[-1])==3):
            island3Pos = (x-2,y-1)
        #pirate.setTeamSignal(sig)
        return 4
    if (
        (left == "island1" and nw[0] != "island1" and sw[0] == "island1" and (s[0] == "" or s[3] == "oppCaptured"))
        or (left == "island2" and nw[0] != "island2" and sw[0] == "island2" and (s[1] == "" or s[4] == "oppCaptured"))
        or (left == "island3" and nw[0] != "island3" and sw[0] == "island3" and (s[2] == "" or s[5] == "oppCaptured"))
    ):
        sig = left[-1] + str(x - 2) + "," + str(y+1)
        if(int(left[-1])==1):
            island1Pos = (x-2,y+1)
        elif(int(left[-1])==2):
            island2Pos = (x-2,y+1)
        elif(int(left[-1])==3):
            island3Pos = (x-2,y+1)
        #pirate.setTeamSignal(sig)
        return 4
    if (
        (right == "island1" and ne[0] == "island1" and se[0] == "island1" and (s[0] == "" or s[3] == "oppCaptured"))
        or (right == "island2" and ne[0] == "island2" and se[0] == "island2" and (s[1] == "" or s[4] == "oppCaptured"))
        or (right == "island3" and ne[0] == "island3" and se[0] == "island3" and (s[2] == "" or s[5] == "oppCaptured"))
    ):
        sig = right[-1] + str(x + 2) + "," + str(y)
        if(int(right[-1])==1):
            island1Pos = (x+2,y)
        elif(int(right[-1])==2):
            island2Pos = (x+2,y)
        elif(int(right[-1])==3):
            island3Pos = (x+2,y)
        #pirate.setTeamSignal(sig)
        return 2
    if (
        (right == "island1" and ne[0] == "island1" and se[0] != "island1" and (s[0] == "" or s[3] == "oppCaptured"))
        or (right == "island2" and ne[0] == "island2" and se[0] != "island2" and (s[1] == "" or s[4] == "oppCaptured"))
        or (right == "island3" and ne[0] == "island3" and se[0] != "island3" and (s[2] == "" or s[5] == "oppCaptured"))
    ):
        sig = right[-1] + str(x + 2) + "," + str(y-1)
        if(int(right[-1])==1):
            island1Pos = (x+2,y-1)
        elif(int(right[-1])==2):
            island2Pos = (x+2,y-1)
        elif(int(right[-1])==3):
            island3Pos = (x+2,y-1)
        #pirate.setTeamSignal(sig)
        return 2
    if (
        (right == "island1" and ne[0] != "island1" and se[0] == "island1" and (s[0] == "" or s[3] == "oppCaptured"))
        or (right == "island2" and ne[0] != "island2" and se[0] == "island2" and (s[1] == "" or s[4] == "oppCaptured"))
        or (right == "island3" and ne[0] != "island3" and se[0] == "island3" and (s[2] == "" or s[5] == "oppCaptured"))
    ):
        sig = right[-1] + str(x + 2) + "," + str(y+1)
        if(int(right[-1])==1):
            island1Pos = (x+2,y+1)
        elif(int(right[-1])==2):
            island2Pos = (x+2,y+1)
        elif(int(right[-1])==3):
            island3Pos = (x+2,y+1)
        #pirate.setTeamSignal(sig)
        return 2
    if (
        (ne[0] == "island1" and up != "island1" and right != "island1" and (s[0] == "" or s[3] == "oppCaptured"))
        or (ne[0] == "island2" and up != "island2" and right != "island2" and (s[1] == "" or s[4] == "oppCaptured"))
        or (ne[0] == "island3" and up != "island3" and right != "island3" and (s[2] == "" or s[5] == "oppCaptured"))
    ):
        sig = ne[0][-1] + str(x+2) + "," + str(y-2)
        if(int(ne[0][-1])==1):
            island1Pos = (x+2,y-2)
        elif(int(ne[0][-1])==2):
            island2Pos = (x+2,y-2)
        elif(int(ne[0][-1])==3):
            island3Pos = (x+2,y-2)
        #pirate.setTeamSignal(sig)
        if int(sig[0][0]) ==1:
            if(x != island1Pos[0] and y != island1Pos[1] and (s[0] == '' or s[0] == "myCapturing" or s[3] != "oppCapturing")):
                moveTo(island1Pos[0],island1Pos[1],pirate)
        if int(sig[0][0]) ==2:
            if(x != island2Pos[0] and y != island2Pos[1] and (s[1] == '' or s[1] == "myCapturing" or s[4] != "oppCapturing")):
                moveTo(island2Pos[0],island2Pos[1],pirate)
        if int(sig[0][0]) ==3:
            if(x != island3Pos[0] and y != island3Pos[1] and (s[2] == '' or s[2] == "myCapturing" or s[5] != "oppCapturing")):
                moveTo(island3Pos[0],island3Pos[1],pirate)
    if (
        (nw[0] == "island1" and up != "island1" and left != "island1" and (s[0] == "" or s[3] == "oppCaptured"))
        or (nw[0] == "island2" and up != "island2" and left != "island2" and (s[1] == "" or s[4] == "oppCaptured"))
        or (nw[0] == "island3" and up != "island3" and left != "island3" and (s[2] == "" or s[5] == "oppCaptured"))
    ):
        sig = nw[0][-1] + str(x-2) + "," + str(y-2)
        if(int(nw[0][-1])==1):
            island1Pos = (x-2,y-2)
        elif(int(nw[0][-1])==2):
            island2Pos = (x-2,y-2)
        elif(int(nw[0][-1])==3):
            island3Pos = (x-2,y-2)
        #pirate.setTeamSignal(sig)
        if int(sig[0][0]) ==1:
            if(x != island1Pos[0] and y != island1Pos[1] and (s[0] == '' or s[0] == "myCapturing" or s[3] != "oppCapturing")):
                moveTo(island1Pos[0],island1Pos[1],pirate)
        if int(sig[0][0]) ==2:
            if(x != island2Pos[0] and y != island2Pos[1] and (s[1] == '' or s[1] == "myCapturing" or s[4] != "oppCapturing")):
                moveTo(island2Pos[0],island2Pos[1],pirate)
        if int(sig[0][0]) ==3:
            if(x != island3Pos[0] and y != island3Pos[1] and (s[2] == '' or s[2] == "myCapturing" or s[5] != "oppCapturing")):
                moveTo(island3Pos[0],island3Pos[1],pirate)

    if (
        (sw[0] == "island1" and down != "island1" and left != "island1" and (s[0] == "" or s[3] == "oppCaptured"))
        or (sw[0] == "island2" and down != "island2" and left != "island2" and (s[1] == "" or s[4] == "oppCaptured"))
        or (sw[0] == "island3" and down != "island3" and left != "island3" and (s[2] == "" or s[5] == "oppCaptured"))
    ):
        sig = sw[0][-1] + str(x-2) + "," + str(y+2)
        if(int(sw[0][-1])==1):
            island1Pos = (x-2,y+2)
        elif(int(sw[0][-1])==2):
            island2Pos = (x-2,y+2)
        elif(int(sw[0][-1])==3):
            island3Pos = (x-2,y+2)
        #pirate.setTeamSignal(sig)
        if int(sig[0][0]) ==1:
            if(x != island1Pos[0] and y != island1Pos[1] and (s[0] == '' or s[0] == "myCapturing" or s[3] != "oppCapturing")):
                moveTo(island1Pos[0],island1Pos[1],pirate)
        if int(sig[0][0]) ==2:
            if(x != island2Pos[0] and y != island2Pos[1] and (s[1] == '' or s[1] == "myCapturing" or s[4] != "oppCapturing")):
                moveTo(island2Pos[0],island2Pos[1],pirate)
        if int(sig[0][0]) ==3:
            if(x != island3Pos[0] and y != island3Pos[1] and (s[2] == '' or s[2] == "myCapturing" or s[5] != "oppCapturing")):
                moveTo(island3Pos[0],island3Pos[1],pirate)

    if (
        (se[0] == "island1" and down != "island1" and right != "island1" and (s[0] == "" or s[3] == "oppCaptured"))
        or (se[0] == "island2" and down != "island2" and right != "island2" and (s[1] == "" or s[4] == "oppCaptured"))
        or (se[0] == "island3" and down != "island3" and right != "island3" and (s[2] == "" or s[5] == "oppCaptured"))
    ):
        sig = se[0][-1] + str(x+2) + "," + str(y+2)
        if(int(se[0][-1])==1):
            island1Pos = (x+2,y+2)
        elif(int(se[0][-1])==2):
            island2Pos = (x+2,y+2)
        elif(int(se[0][-1])==3):
            island3Pos = (x+2,y+2)
        #pirate.setTeamSignal(sig)
        if int(sig[0][0]) ==1:
            if(x != island1Pos[0] and y != island1Pos[1] and (s[0] == '' or s[0] == "myCapturing" or s[3] != "oppCapturing")):
                moveTo(island1Pos[0],island1Pos[1],pirate)
        if int(sig[0][0]) ==2:
            if(x != island2Pos[0] and y != island2Pos[1] and (s[1] == '' or s[1] == "myCapturing" or s[4] != "oppCapturing")):
                moveTo(island2Pos[0],island2Pos[1],pirate)
        if int(sig[0][0]) ==3:
            if(x != island3Pos[0] and y != island3Pos[1] and (s[2] == '' or s[2] == "myCapturing" or s[5] != "oppCapturing")):
                moveTo(island3Pos[0],island3Pos[1],pirate)
    
    if (island1Pos != () and x == island1Pos[0] and y == island1Pos[1] and s[0] != "myCaptured"):
        return 0
    if (island2Pos != () and x == island2Pos[0] and y == island2Pos[1] and s[1] != "myCaptured"):
        return 0
    if (island3Pos != () and x == island3Pos[0] and y == island3Pos[1] and s[2] != "myCaptured"):
        return 0
    if island1Pos != () and pirate.trackPlayers()[3] == "oppCapturing":
        if (x != island1Pos[0] and y != island1Pos[1]):
            return moveTo(island1Pos[0],island1Pos[1], pirate)

    if island2Pos != () and pirate.trackPlayers()[4] == "oppCapturing":
        if (x != island2Pos[0] and y != island2Pos[1]):
            return moveTo(island2Pos[0],island2Pos[1], pirate)

    if island3Pos != () and pirate.trackPlayers()[5] == "oppCapturing":
        if (x != island3Pos[0] and y != island3Pos[1]):
            return moveTo(island3Pos[0],island3Pos[1], pirate)
        
    
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
    #print(l)
    if s:
        island_no = int(s[0][0])
        signal = l[island_no - 1]
        if signal == "myCaptured":
            team.setTeamSignal("")
