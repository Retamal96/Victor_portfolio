

class Sudoku_Solver():

    def __init__(self, board):
        self.board = board
        

    def __str__(self):
        return "\n".join(str(row) for row in self.board) + "\n"

    def solve(self):
        current_row, current_column = self.next_open_position()
        for number in range(1,10):
            if self.is_not_solve() and self.can_put_number(number,current_row, current_column):
                self.board[current_row][current_column] = number
                self.solve()
                if self.is_not_solve():     
                    self.board[current_row][current_column] = ' '
    
    def is_not_solve(self):
        for row in self.board:
            if ' ' in row:
                return True
        return False
            
    def next_open_position(self):
        for row in range(len(self.board)):
            for column in range(len(self.board[row])):
                if self.board[row][column] == ' ':
                    return row, column
        return -1,-1 # since you have row,col = this func, if returning -1 --> row,col =- 1


    def can_put_number(self,number,current_row, current_column):
        return self.number_in_row(number,current_row) and\
            self.number_in_column(number,current_column) and \
                self.number_in_square(number,current_row, current_column)


    def number_in_row(self,number,current_row):
        """for place in self.board[self.current_row]:
            if number == place:
                return False
        return True"""
        return number not in self.board[current_row] #Easier and avoiding the loop

    def number_in_column(self, number,current_column):
        for row in self.board:
            if number == row[current_column]:
                return False
        return True

    def number_in_square(self,number,current_row,current_column):
        square_row = (current_row // 3)*3
        square_column = (current_column // 3)*3
        for row in range(square_row, square_row + 3 ):
            for column in range(square_column, square_column + 3):
                if number == self.board[row][column]:
                    return False
        return True
