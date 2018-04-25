#!/usr/bin/python3


def createTournament(number):
    totalRounds = (number-1)*2
    mathcesPerRound = int(number/2)
    rounds = [["" for x in range(mathcesPerRound)]for y in range(totalRounds)]    
    # print(rounds)

    for session in range(0, totalRounds):
        for match in range(0, mathcesPerRound):
            home = (session + match) % (number-1)
            away = (number - 1 - match + session) % (number-1)

            if match == 0:
                away = number - 1
            if session < totalRounds/2:
                rounds[session][match] = "Team " + str(home + 1) + " vs " + str(away + 1)
            else:
                rounds[session][match] = "Team " + str(away + 1) + " vs " + str(home + 1)            
    print(rounds)

if __name__ == "__main__":
    numberOfTeams = int(input("How many teams are in the tournament: "))
    createTournament(numberOfTeams)    
