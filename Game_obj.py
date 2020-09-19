import sys
import numpy
import pylab

class GameOfLife:
    def __init__(self, N, T):
        """ Set up Conway's Game of Life. """
        # Here we create two grids to hold the old and new configurations.
        # This assumes an N*N grid of points.
        # Each point is either alive or dead, represented by integer values of 1 and 0, respectively.
        self.N = N
        self.old_grid = numpy.zeros(N * N, dtype='i').reshape(N, N)
        self.new_grid = numpy.zeros(N * N, dtype='i').reshape(N, N)
        self.T = T  # The maximum number of generations
        # print('old grid : ')
        # print(self.old_grid)
        sys_arg = sys.argv
        # print(sys_arg)
        # outpt_file = sys_arg[2]
        with open(sys_arg[1], 'r') as f:
            context = [[int(num) for num in line.split(' ')] for line in f]
        # Set up a random initial configuration for the grid.

        for i in range(0, self.N):
            for j in range(0, self.N):
                self.old_grid[i][j] = context[i][j]

    def live_neighbours(self, i, j):
        """ Count the number of live neighbours around point (i, j). """
        s = 0  # The total number of live neighbours.
        # Loop over all the neighbours.
        for x in [i - 1, i, i + 1]:
            for y in [j - 1, j, j + 1]:
                if (x == i and y == j):
                    continue  # Skip the current point itself - we only want to count the neighbours!
                if (x != self.N and y != self.N):
                    s += self.old_grid[x][y]
                # The remaining branches handle the case where the neighbour is off the end of the grid.
                # In this case, we loop back round such that the grid becomes a "toroidal array".
                elif (x == self.N and y != self.N):
                    s += self.old_grid[0][y]
                elif (x != self.N and y == self.N):
                    s += self.old_grid[x][0]
                else:
                    s += self.old_grid[0][0]
        return s

    def play(self):
        """ Play Conway's Game of Life. """

        # Write the initial configuration to file.
        # pylab.pcolormesh(self.old_grid)
        # pylab.colorbar()
        # pylab.savefig("generation0.png")
        t = 1  # Current time level
        write_frequency = 5  # How frequently we want to output a grid configuration.
        while t <= self.T:  # Evolve!
            # print("Next state %d" % t)

            # Loop over each cell of the grid and apply Conway's rules.
            for i in range(self.N):
                for j in range(self.N):
                    live = self.live_neighbours(i, j)
                    if (self.old_grid[i][j] == 1 and live < 2):
                        self.new_grid[i][j] = 0  # Dead from starvation.
                    elif (self.old_grid[i][j] == 1 and (live == 2 or live == 3)):
                        self.new_grid[i][j] = 1  # Continue living.
                    elif (self.old_grid[i][j] == 1 and live > 3):
                        self.new_grid[i][j] = 0  # Dead from overcrowding.
                    elif (self.old_grid[i][j] == 0 and live == 3):
                        self.new_grid[i][j] = 1  # Alive from reproduction.
            # Output the new configuration.
            # if (t % write_frequency == 0):
            #     print('New grids : ')
            #     print(self.new_grid)
            # pylab.pcolormesh(self.new_grid)
            # pylab.savefig("generation%d.png" % t)

            # The new configuration becomes the old configuration for the next generation.
            self.old_grid = self.new_grid.copy()
            # print('last old grid : : : ')
            # print(self.old_grid)

            # Move on to the next time level
            t += 1
        ###################################
        sys_arg = sys.argv
        # print(sys_arg)
        f = open(str(sys_arg[2]), 'w')
        for i in range(self.N):
            for j in range(self.N):
                # print(self.new_grid[i][j])
                f.write(str(self.new_grid[i][j]) + ' ')
            f.write('\n')

#
# if (__name__ == "__main__"):

