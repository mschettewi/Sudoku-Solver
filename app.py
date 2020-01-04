from flask import Flask, redirect, request, render_template, send_from_directory, url_for
import json, ast
from board import Constraint
import copy
import os

app = Flask(__name__)


@app.route('/sample/', methods=['GET', 'POST'])
def sample():
    if (request.method == 'POST'):
        return redirect(url_for("main"), code=307)
    else:
        blue = [["" for i in range(9)] for j in range(9)]
        values = [[5, 3, -1, -1, 7, -1, -1, -1, -1],
                  [6, -1, -1, 1, 9, 5, -1, -1, -1],
                  [-1, 9, 8, -1, -1, -1, -1, 6, -1],
                  [8, -1, -1, -1, 6, -1, -1, -1, 3],
                  [4, -1, -1, 8, -1, 3, -1, -1, 1],
                  [7, -1, -1, -1, 2, -1, -1, -1, 6],
                  [-1, 6, -1, -1, -1, -1, 2, 8, -1],
                  [-1, -1, -1, 4, 1, 9, -1, -1, 5],
                  [-1, -1, -1, -1, 8, -1, -1, 7, 9]]

        return render_template('sudoku.html',
                               board=values,
                               blue=blue,
                               invalid=False,
                               disclaimer="")


@app.route('/', methods=['GET', 'POST'])
def main():
    blue = [["" for i in range(9)] for j in range(9)]
    if (request.method == 'GET'):
        values = [["" for i in range(9)] for j in range(9)]
        return render_template('sudoku.html',
                               board=values,
                               blue=blue,
                               invalid=False,
                               disclaimer="")

    else:
        data = ast.literal_eval(json.dumps(request.form))

        values = [[-1 for i in range(9)] for j in range(9)]
        for val in data:
            if (data[val] != " " and data[val] != ""):
                x, y = val.split(",")
                values[int(x)][int(y)] = int(data[val])
                blue[int(x)][int(y)] = "original"

        # c_values in case no solution
        c_values = copy.deepcopy(values)

        board = Constraint(values)
        board.print_board()

        if (not board.is_valid_board()):
            return render_template("sudoku.html",
                                   board=board.board,
                                   blue=blue,
                                   invalid=True,
                                   disclaimer="")

        board.solve()
        board.print_board()

        if (not board.is_full()):
            return render_template("sudoku.html",
                                   board=c_values,
                                   blue=blue,
                                   invalid=False,
                                   disclaimer="No Solution")

        if (board.backtracking):
            disclaimer = "Note: there may be more than one solution"
        else:
            disclaimer = ""
        return render_template("sudoku.html",
                               board=board.board,
                               blue=blue,
                               invalid=False,
                               disclaimer=disclaimer)


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'apple-touch-icon.png',
                               mimetype='image/vnd.microsoft.icon')


if __name__ == '__main__':
    app.run(port=5000)
