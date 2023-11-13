# Exxample Game Functions Project, Jordan Henry v10.0
import random 

def functionOne():
    pass 

def functionTwo(param1):
    pass

def functionThree(param1 = "Default  Value"):
    print(param1)

def FunctionFour(param1, param2, param3):
    pass

def racing(mph, playerSpeeding, playerSlowingDown, crashing):
    if mph > 100 and playerSpeeding:
      playerWinning = True
    elif mph < 100 and playerSlowingDown and crashing: 
      playerWinning = False 
    else:
       print("Catch up, your gonna get hit!\n")
       playerWinning = False 
       playerLoosing = True 
racing(120,50)