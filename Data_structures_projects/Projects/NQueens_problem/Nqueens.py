class Nqueens():

    def __init__(self, size):
        self.board = []
        self.size = size
        for row in range(self.size):
            self.board.append([])
            for column in range(self.size):
                self.board[row].append(' ')

        self.numbers_of_queens_on_board = 0       
        self.is_solve = False


    def solve(self):
        #print(self)
        if self.numbers_of_queens_on_board == self.size:
            self.is_solve = True
            print(self)
        if not self.is_solve:
            for row in range(self.size):
                if self._can_put_queen(row):
                    self.board[row][self.numbers_of_queens_on_board] = 'Q' #this works bc we dont need to check columns where we alredy place one Q
                    self.numbers_of_queens_on_board += 1
                    self.solve()
                    self.numbers_of_queens_on_board -= 1
                    self.board[row][self.numbers_of_queens_on_board] = ' ' #this works bc we dont need to check columns where we alredy place one Q                


    def _can_put_queen(self, row):
        return self._row_is_clear(row) and \
            self._diagonal_up_is_clear(row) and \
            self._diagonal_down_is_clear(row)

    def _row_is_clear(self, row):
        return 'Q' not in self.board[row]
    

    """
    We are only checking the parts were we already place a queen, since its impossible to have a Q further
    """
    def _diagonal_up_is_clear(self, row):
        current_row = row -1
        current_column = self.numbers_of_queens_on_board - 1

        while current_column >= 0 and current_row >= 0:
            if self.board[current_row][current_column] == 'Q': #Remeber we can only place Q in unique columns
                return False
            current_column -= 1
            current_row -=1
            
        return True

    def _diagonal_down_is_clear(self, row):
        current_row= row +1
        current_column = self.numbers_of_queens_on_board - 1 

        while current_column >=0 and current_row < len(self.board):
            if self.board[current_row][current_column] =='Q':
                return False
            current_row += 1 
            current_column -= 1
        return True



    def __str__(self):
        result = ""
        for row in self.board:
            result += str(row) + '\n'
        return result