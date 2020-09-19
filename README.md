# Conway_game_Kaggle_competitions

# Table of contents
Sections headers will be used to reference the location of destination
- [Running](#Running)
- [How it's written](#How-it's-written)
- [Goals](#Goals)


# Running
To run the Conway game of life:

Type input and output file name then type number of generation that you need

```bash
$ python Main.py input.txt output.txt 3
```
Alternatively, a general-purpose neighbor-oriented state transition function is also available as play function. This will take an array encoding the current state along with a game object, and outputs the next state for all cells. Game_obj.py shows how to use this.

# How it's written
The game grid is encoded as a simple n by n array (in input.txt is 20x20) of zeros and ones. In each program, a state transition is determined for each pixel by looking at the 8 pixel values all around it, and counting how many of them are "alive", then applying game rules based that number. Since the "alive" or "dead" states are just encoded as 1 or 0, this is equivalent to summing up the values of all 8 neighbors.
In Game_obj.py you can see live_neighbours function which determine neighbours all around a pixel. Then we want to do this for all pixels in a single shot and generate next state, for this goal we use play function wich called live_neighbours function for all neighbours.

In Main.py we call Game object. Game object initialize with two parameter N and T which demonstrate lenght of input matrix and number of generations that we need.
When you initialize T you can execute play function in game object for T step and store result in output.txt.
Also we use sys.argv to read command line and initialize game object parameters and read input file.

```

# Goals

Ultimately, I'd like to participate in Kaggle competition which name is Conway's reverse Game of life.
For this code, this basically comes down to generate next state for each input matrix and result outpt matrix as a text file.
