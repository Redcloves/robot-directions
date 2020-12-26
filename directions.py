
def coordinates(directions):
    position = ['N', 'E', 'S', 'W']
    coordinates = (0, 0, 'N')
    for i in directions:
        if i is 'F' and coordinates[2] == 'N':
            coordinates = coordinates[0], coordinates[1] + 1, coordinates[2]
        elif i is 'F' and coordinates[2] == 'E':
            coordinates = coordinates[0] + 1, coordinates[1], coordinates[2]
        elif i is 'F' and coordinates[2] == 'S':
            coordinates = coordinates[0], coordinates[1] - 1, coordinates[2]
        elif i is 'F' and coordinates[2] == 'W':
            coordinates = coordinates[0] - 1, coordinates[1], coordinates[2]
        elif i is 'L':
            new = position.index(coordinates[2]) - 1
            coordinates = coordinates[0], coordinates[1], position[new]
        elif i is 'R':
            if position.index(coordinates[2]) + 1 < len(position):
                new = position.index(coordinates[2]) + 1
            else:
                new = 4 - (position.index(coordinates[2]) + 1)
            coordinates = coordinates[0], coordinates[1], position[new]
        else:
            pass
    return coordinates

def NumberOfMoves(coordinates):
    if coordinates[0] == 0 and coordinates[1] == 0:
        return 0
    count = 0
    while coordinates[0] != 0 or coordinates[1] != 0:
        if coordinates[0] == 0 and coordinates[1] != 0:
            if coordinates[1] > 0:
                position = ['N', 'E', 'S', 'W']
                return count + coordinates[1] + abs( position.index('S') - position.index( coordinates[2] ))
            else:
                position = ['S', 'W', 'N', 'E']
                return count + abs(coordinates[1]) + abs(position.index('N') - position.index(coordinates[2]))
        elif coordinates[0] != 0 and coordinates[1] == 0:
            if coordinates[0] > 0:
                position = ['E', 'S', 'W', 'N']
                return count + coordinates[0] + abs( position.index('W') - position.index( coordinates[2] ))
            else:
                position = ['W', 'N', 'E', 'S']
                return count + abs(coordinates[0]) + abs(position.index('E') - position.index(coordinates[2]))
        else:
            if coordinates[0] > 0 and coordinates[1] > 0:
                position = ['W', 'N', 'E', 'S']
                if coordinates[2] == 'E' or coordinates[2] == 'S':
                    count = coordinates[1] + abs( position.index('S') - position.index( coordinates[2] ))
                    coordinates = coordinates[0], 0, 'S'
                else:
                    count = coordinates[0] + abs( position.index('W') - position.index( coordinates[2] ))
                    coordinates = 0, coordinates[1] , 'W'
            elif coordinates[0] > 0 and coordinates[1] < 0:
                position = ['W', 'S', 'E', 'N']
                if coordinates[2] == 'E' or coordinates[2] == 'N':
                    count = abs(coordinates[1]) + abs(position.index('N') - position.index(coordinates[2]))
                    coordinates = coordinates[0], 0, 'N'
                else:
                    count = coordinates[0] + abs(position.index('W') - position.index(coordinates[2]))
                    coordinates = 0, coordinates[1], 'W'
            elif coordinates[0] < 0 and coordinates[1] < 0:
                position = ['W', 'N', 'E', 'S']
                if coordinates[2] == 'W' or coordinates[2] == 'N':
                    count = abs(coordinates[1]) + abs(position.index('N') - position.index(coordinates[2]))
                    coordinates = coordinates[0], 0, 'N'
                else:
                    count = abs(coordinates[0]) + abs(position.index('E') - position.index(coordinates[2]))
                    coordinates = 0, coordinates[1], 'E'
            else:
                position = ['W', 'S', 'E', 'N']
                if coordinates[2] == 'E' or coordinates[2] == 'N':
                    count = abs(coordinates[0]) + abs(position.index('E') - position.index(coordinates[2]))
                    print(count)
                    coordinates = 0, coordinates[1], 'E'
                else:
                    count = abs(coordinates[1]) + abs(position.index('S') - position.index(coordinates[2]))
                    coordinates = coordinates[0], 0, 'S'

def RobotMoves():
    directions = input("A robot moves forward, turns left or right. Discover how many minimum moves you need to return to its original position "
                       "and give directions in terms of 'F', 'L', 'R':\n")
    coordinate = coordinates(directions.upper())
    print("Your coordinates are: ", coordinate)
    print("The minimum number of moves to return to its position: ", NumberOfMoves(coordinate))
    while True:
        answer = str(input("Would you like to start again? (y/n)\n"))
        if answer.lower() == 'y':
            directions = input("\nNew directions: ")
            coordinate = coordinates(directions.upper())
            print("Your coordinates are: ", coordinate)
            print("The minimum number of moves to return to its position: ", NumberOfMoves(coordinate))
        elif answer.lower() == 'n':
            print("Finished.")
            break
        else:
            pass
RobotMoves()