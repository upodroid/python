
class Player1:
    ships = []
    def add(self, ships):
        pass

class Player2():
    ships = []
    def add(self, ships):
        pass

class ships:
    def __init__(self,row_size):
        self.row_size = row_size
class patrol_boat(ships):
    def __init__(self, column_size):
        ships.__init__(self,1)
        self.column_size = 2

class battleships(ships):
    def __init__(self, column_size):
        ships.__init__(self,1)
        self.column_size = 3


class submarine(ships):
    def __init__(self, column_size):
        ships.__init__(self, 1)
        self.column_size = 3


class destroyer(ships):
    def __init__(self, column_size):
        ships.__init__(self, 1)
        self.column_size = 4


class carrier(ships):
    def __init__(self, column_size):
        ships.__init__(self, 1)
        self.column_size = 5

player1 = Player1()
player1.add(patrol_boat("patrol"))
player1.add(patrol_boat("patrol"))
player1.add(battleships("battleship"))
player1.add(battleships("battleship"))
player1.add(submarine("submarine"))
player1.add(destroyer("destroyer"))
player1.add(carrier("carrier"))

player2 = Player2()
player2.add(patrol_boat("patrol"))
player2.add(patrol_boat("patrol"))
player2.add(battleships("battleship"))
player2.add(battleships("battleship"))
player2.add(submarine("submarine"))
player2.add(destroyer("destroyer"))
player2.add(carrier("carrier"))


grid = [['O' for i in range(10)] for j in range(10)]

def print_grid():
    print("  " + " ".join(str(i) for i in range(10))) # " ".join() puts the " " between each string in the list
    for y in range(10):
        print(str(y) + " " + " ".join(grid[y]))

print_grid()
#placing ships in grid
for turn in range(20):
    patrolr = int(input("pick row to place patrol ship: (0-9) "))
    patrolc = int(input("pick column to place patrol ship: (0-9) "))
    battleshipr = int(input("pick row to place battleship: (0-9) "))
    battleshipc = int(input("pick column to place battleship: (0-9) "))
    submariner = int(input("pick row to place submarine: (0-9) "))
    submarinec = int(input("pick column to place submarine: (0-9) "))
    destroyerr = int(input("pick row to place destroyer: (0-9) "))
    destroyerc = int(input("pick column to place destroyer: (0-9) "))
    carrierr = int(input("pick row to place carrier: (0-9) "))
    carrierc = int(input("pick column to place carrier: (0-9) "))
    grid[patrolr][patrolc] = "1"
    grid[patrolr][patrolc + 1] = "1"
    grid[battleshipr][battleshipc] = "1"
    grid[battleshipr][battleshipc + 1] = "1"
    grid[battleshipr][battleshipc + 2] = "1"
    grid[submariner][submarinec] = "1"
    grid[submariner][submarinec + 1] = "1"
    grid[submariner][submarinec + 1] = "1"
    grid[destroyerr][destroyerc] = "1"
    grid[destroyerr][destroyerc + 1] = "1"
    grid[destroyerr][destroyerc + 2] = "1"
    grid[destroyerr][destroyerc + 3] = "1"
    grid[carrierr][carrierc] = "1"
    grid[carrierr][carrierc + 1] = "1"
    grid[carrierr][carrierc + 2] = "1"
    grid[carrierr][carrierc + 3] = "1"
    grid[carrierr][carrierc + 4] = "1"
    print_grid()
#playing the game

for turn in range(1):
    row = int(input("guess row: (0-9) "))
    col = int(input("guess column: (0-9) "))


grid[row][col] = "X"
print_grid()

