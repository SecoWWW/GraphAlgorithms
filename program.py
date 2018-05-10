#!/usr/bin/python3


def createTournament(number):
    original_number = number
    number += 1    
    totalRounds = (number-1)*2
    mathcesPerRound = int(number/2)
    rounds = [["" for x in range(mathcesPerRound)]for y in range(totalRounds)]  
    lastRound = ["HOME"] * number     
    # print(rounds)

    for session in range(0, totalRounds):
        for match in range(0, mathcesPerRound):
            home = (session + match) % (number-1)
            away = (number - 1 - match + session) % (number-1)            
            
            if match == 0:
                away = number - 1 
            if home > original_number-1 or away > original_number-1:
                continue           
            if session < totalRounds/2:
                if session == 0:
                    rounds[session][match] = homeAndAway(home, away, lastRound)
                else:
                    if lastRound[home] == "AWAY" and lastRound[away] == "HOME":
                        rounds[session][match] = homeAndAway(home, away, lastRound)                        
                    elif lastRound[home] == "HOME" and lastRound[away] == "AWAY":
                        rounds[session][match] = homeAndAway(away, home, lastRound)
                    else:
                         rounds[session][match] = homeAndAway(home, away, lastRound)
                    
            else:
                if session == totalRounds/2:
                    rounds[session][match] = homeAndAway(away, home, lastRound)
                else:
                    if lastRound[home] == "HOME" and lastRound[away] == "AWAY":
                        rounds[session][match] = homeAndAway(away, home, lastRound)                        
                    elif lastRound[home] == "AWAY" and lastRound[away] == "HOME":
                        rounds[session][match] = homeAndAway(home, away, lastRound)
                    else:
                         rounds[session][match] = homeAndAway(away, home, lastRound)                            
    nicePrint(rounds)

def homeAndAway(home, away, lastRound):
    lastRound[home] = "HOME"
    lastRound[away] = "AWAY"
    return "Team " + str(home + 1) + " vs " + str(away + 1)

def nicePrint(rounds):
    for round in range(0,len(rounds)):
        print("Round number: "+ str(round+1))
        for match in range(0,len(rounds[round])):
            if(rounds[round][match] != ""):
                print(rounds[round][match])

if __name__ == "__main__":
    numberOfTeams = int(input("How many teams are in the tournament: "))
    createTournament(numberOfTeams)    
