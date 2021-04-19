

class Maze_solver():

    def __init__(self, mapa):
        self.mapa = mapa 
        self.current_position = 'S'
        self.is_solve = False
        self.current_row,self.current_column = self.find_start()
        self.step_counter = []
        self.counter = 0
        self.short_path = 100000
   
    def find_start(self):
        finded = False
        for row in range(len(self.mapa)):
            for column in range(len(self.mapa[row])):
              if self.mapa[row][column] == 'S':
                  finded = True
                  return row,column  
        raise 'No Start found'
    
    def can_move(self, current_row, current_column):
        return 0<= current_row < len(self.mapa) and  \
            0 <= current_column < len(self.mapa[0]) and \
                (self.mapa[current_row][current_column] == ' ' or
                self.mapa[current_row][current_column] == 'E')

    def solve(self):
        
        if self.mapa[self.current_row][self.current_column] == 'E':
            print(self)
            self.step_counter.append(self.counter)
            if self.short_path > self.counter:
                self.short_path = self.counter

        else:
            #Position mark
            self.mapa[self.current_row][self.current_column] = '#'
            self.counter += 1

            #up
            if self.can_move(self.current_row - 1, self.current_column):
                self.current_row -= 1
                self.solve()
                self.current_row += 1
                
            #down
            if self.can_move(self.current_row + 1, self.current_column):
                self.current_row += 1
                self.solve()
                self.current_row -= 1

            #left
            if self.can_move(self.current_row, self.current_column -1):
                self.current_column -= 1
                self.solve()
                self.current_column += 1

            #right
            if self.can_move(self.current_row, self.current_column +1):
                self.current_column += 1
                self.solve()
                self.current_column -= 1
        
        #undo postion marks
        self.mapa[self.current_row][self.current_column] = ' '
        self.counter -= 1

    def shortest_path(self):
        return min(self.step_counter)

    def __str__(self):
        return "\n".join(str(row) for row in self.mapa) + "\n"