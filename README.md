# Conway_game_Kaggle_competitions

# Table of contents
You're sections headers will be used to refrence location of destination
- [Running](#Running)
- [How it's written](#How-it's-written)
- [Goals](#Goals)


# Running
To run Conway game of life:

Type input and output file name then type number of generation that you need

```bash
$ python Main.py input.txt output.txt 3
```


# How it's written

By opening Game_obj.py file you could undrestand that code have a class which name is Game. 
Game object initialize with two parameter N and T which demonstrate lenght of input matrix and number of generations that we need.
Other function is live_neighbours which can execute for each element of matrix which excat height and width.
Last function is play. In play function we call live_neighbours function for every elements in matrix to generate next state of game in every period.

Another python file is Main.py. In Main.py we call Game object to initiale the object with lenght of matrix and number of generation. 
Also we use sys.argv to read command line and initialize game object parameters and read input file.


# Goals

Ultimately, I'd like to participate in Kaggle competition which name is Conway's reverse Game of life.
For this code, this basically comes down to generate next state for each input matrix and result outpt matrix as a text file.
