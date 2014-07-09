import random
cp1 = random.randint(1,3)

ptie = 0
plosscount = 0
pwincount = 0

def ploss():
    global plosscount
    print "Player loses :("
    plosscount = plosscount + 1
    return plosscount
def pwin():
    global pwincount
    print "Player wins!"
    pwincount = pwincount + 1
    return pwincount

print "This is a simple game of Rock, Paper, Scissors."

ploop = raw_input ("Do you want to play? (y/n): ")

while ploop == "y" :
    print "Rock:1 Paper:2 Scissors:3"
    hp1 = raw_input("Please make your selection from the list above: ")
    hp1 = int(hp1)
    print "Computer choice:",cp1
    if hp1 == cp1 :
        global ptie
        print "Tie"
        ptie = ptie +1
    elif cp1 == 1 :
        if hp1 == 2 :
            pwin()
        else :
            ploss()
    elif cp1 == 2 :
        if hp1 == 1 :
            ploss()
        else :
            pwin()
    else :
        if cp1 == 3 :
            if hp1 == 2 :
                ploss()
            else :
                pwin()
    ploop = raw_input ("Do you want to play again? (y/n): ")         

print "Wins:",pwincount,"Losses:",plosscount,"Ties:",ptie    
print "end"

