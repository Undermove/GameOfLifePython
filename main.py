import matplotlib.pyplot as plt
import numpy as np

from celluloid import Camera

file = open("gameOfLifeStart.csv")
# currentGen = np.loadtxt(file, delimiter=",").astype(int)
currentGen = np.random.randint(0, 2, size=(100, 100))
rows, columns = currentGen.shape
epochs = 300
nextGen = np.random.randint(0, 1, size=(rows, columns))

fig = plt.figure()
camera = Camera(fig)

for i in range(epochs):
    for row in range(rows):
        for column in range(columns):
            cell = currentGen[row, column]
            topCell = currentGen[row - 1 if row - 1 > 0 else rows - 1][column]
            topRightCell = currentGen[row - 1 if row - 1 > 0 else rows - 1][column + 1 if column + 1 < columns else 0]
            rightCell = currentGen[row][column + 1 if column + 1 < columns else 0]
            bottomRightCell = currentGen[row + 1 if row + 1 < rows else 0][column + 1 if column + 1 < columns else 0]
            bottomCell = currentGen[row + 1 if row + 1 < rows else 0][column]
            bottomLeftCell = currentGen[row + 1 if row + 1 < rows else 0][column - 1 if column - 1 > 0 else columns - 1]
            leftCell = currentGen[row][column - 1 if column - 1 > 0 else columns - 1]
            topLeftCell = currentGen[row - 1 if row - 1 > 0 else rows - 1][column - 1 if column - 1 > 0 else columns - 1]

            coLivers = topCell + topRightCell + rightCell + bottomRightCell + bottomCell + bottomLeftCell + leftCell + topLeftCell

            if cell == 0 and coLivers == 3:
                #     зародить жизнь
                nextGen[row][column] = 1

            if cell == 1 and (coLivers <= 1 or coLivers >= 4):
                #     прикончить клетку
                nextGen[row][column] = 0

            if cell == 1 and (coLivers == 2 or coLivers == 3):
                nextGen[row][column] = 1

    currentGen = nextGen
    nextGen = np.random.randint(0, 1, size=(rows, columns))
    plt.imshow(currentGen)
    camera.snap()

animation = camera.animate()
animation.save('gameOfLife.gif', writer='PillowWriter', fps=10)
