import random

class Player:
    def __init__(self, id, name, positon):
        self.id = id
        self.name = name
        self.positon = positon

    def getName():
        return self.name

    def setName(nm):
        self.name = nm

    def getPosition():
        return self.positon

    def setPosition(pos):
        self.positon = pos

universe = []
owners = {"hare", "paul", "tortoise"}

paulValue = {1:40, 2:6, 3:25}
tortoiseValue = {1:40, 2:5, 3:20}
hareValue = {1:40, 2:4, 3:23}

paulCount = tortoiseCount = hareCount = 0

posList = ["paul", "tortoise", "hare"]

posPaul = 0
posTortoise = 1
posHare = 2

startPos = 0
nomTurnPos = startPos
    

# retreive & build players via webapi call?
# now hard code.    
def buildUniverse():
    universe.append(Player(1, 'Mike Trout', 'OF'))
    universe.append(Player(2, 'Christian Yelich', 'OF'))
    
def bidWar(player, nomOwn):
    payValStart = 1 #change later to be more dynamic and owner specific
    paulPrime = 0
    tortoisePrime = 0
    harePrime = 0
    playerTaken = 0
    highBid = payValStart
    iTimes = {}
    
    currWinner = nomOwn
    
    if paulValue[player.id] >= payValStart:
         paulPrime = 1
    
    if tortoiseValue[player.id] >= payValStart:
         tortoisePrime = 1
    
    if hareValue[player.id] >= payValStart:
         harePrime = 1
         
    #while more than one person is involved in the bidding
    while (paulPrime + tortoisePrime + harePrime) >= 1:
       
        if paulPrime == 1 and currWinner != 'paul':
            paulTime = random.uniform(1, 9)
        else:
            paulTime = 100
        if tortoisePrime == 1 and currWinner != 'tortoise':
            tortoiseTime = random.uniform(1, 10)
        else: 
            tortoiseTime = 100
        if harePrime == 1 and currWinner != 'hare':
            hareTime = random.uniform(1, 8)
        else:
            hareTime = 100
            
        bidTimes = {'paul':paulTime, 'tortoise':tortoiseTime, 'hare':hareTime}
        
        for w, t in bidTimes.items():
            iTimes[w] = t
            
        minTime = min(iTimes['paul'],iTimes['hare'],iTimes['tortoise']) 
           
        
        for w, t in bidTimes.items():
            if minTime == t:
                highBid = highBid + 1
                currWinner = w
                
        print highBid
        print currWinner
                    
        if highBid >= paulValue[player.id]:
            paulPrime = 0
        if highBid >= tortoiseValue[player.id]:
            tortoisePrime = 0
        if highBid >= hareValue[player.id]:
            harePrime = 0
        
    winningOwner = currWinner
    winningPrice = highBid
    
    return (winningOwner, winningPrice)
        
                
# Main Method
if __name__ == '__main__':
    "This code runs when you invoke the script from the command line"  
    
    count = range(5)
    multiAucResults = []
    aucResults = []

    buildUniverse()
    
    for i in count:             
     
        nomTurnPos = startPos
    
        for p in universe:
            nominatingOwner = posList[nomTurnPos]
            
            #print "%s will make the next nomination" % nominatingOwner
        
            bidResult = bidWar(p, nominatingOwner)
         
            aucResults.append(bidResult)     
            
            nomTurnPos = nomTurnPos + 1   
        
        
    multiAucResults.append(aucResults)
         
    print multiAucResults
   
    for j in multiAucResults:
        for owner, price in j:
            if owner == 'paul':
                paulCount += 1
            if owner == 'tortoise':
                tortoiseCount += 1
            if owner == 'hare':
                hareCount += 1
"""                
    print "Paul won the player %d times" % paulCount
    print "The Hare won the player %d times" % hareCount
    print "The Tortoise won the player %d times" % tortoiseCount      
"""        
