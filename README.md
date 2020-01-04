# Sudoku-Solver
Sudoku solver written with python backend     
Live version can be found here: [https://sudoku-solver-online.herokuapp.com/](https://sudoku-solver-online.herokuapp.com/)     
Note, it may take a moment to load as it is hosted on free tier of heroku that sleeps after 30 minutes of inactivity    


## Python run instructions 
`pip install -r requirements.txt`  
### Sudoku as a constraint problem
``` python
from board import Constraint
values = [[-1 for i in range(9)] for j in range(9)]   # 2x2 array, -1 representing empty cell
sudoku = Constraint(values)
sudoku.print_board()                                  # prints board
sudoku.solve()                                        # solves sudoku in-place
sudoku.print_board()                                  # prints board
...
```
### Sudoku as brute-force
``` python
from board import Board
values = [[-1 for i in range(9)] for j in range(9)]   # 2x2 array, -1 representing empty cell
sudoku = Board(values)
sudoku.print_board()                                  # prints board
sudoku.solve()                                        # solves sudoku in-place
sudoku.print_board()                                  # prints board
...
```

## Python Flask hosting instructions 
Run on localhost with following instructions   
1) `pip install -r requirements.txt`    
2) `python3 app.py`   

[https://sudoku-solver-online.herokuapp.com/](https://sudoku-solver-online.herokuapp.com/)
