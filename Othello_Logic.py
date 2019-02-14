###Othello_Logic.py
### Jonathan Navarro 83144130
from collections import namedtuple

class Othello_state:
    def __init__(self):
        self.columns = 0
        self.rows = 0
        self.first_player = ''
        self.NONE = ''
        self.board = ''
        self.player_white = 'W'
        self.player_black = 'B'
        self.score_black = 0
        self.score_white = 0
        self.turn = ''
        self.opposite = ''
        self.counter = 0
        self.orientation = ''
        self.winner = ''
        self.condition = ''
    


    def create_column_amount(self,new_amount):
        '''
creates columns
        '''
        self.columns = new_amount

    def create_row_amount(self,new_amount):
        '''
creates rows
        '''
        self.rows = new_amount

    def create_first_player(self,first):
        '''
creates first player
        '''
        print("first: ",first)
        if first.upper() == 'W':
            self.first_player = self.player_white
            self.turn = self.player_white
            self.opposite = self.player_black
        elif first.upper() == 'B':
            self.first_player = self.player_black
            self.turn = self.player_black
            self.opposite = self.player_white
        # else:
        #     return create_first_player()
            

    def starting(self,starting_player):
        '''
Creates starting positions for center pieces
        '''
##        starting_player = input().upper()
        self.orientation = starting_player.upper()
        if starting_player.upper() == 'W':
            self.board[int((len(self.board)/2)-1)][int((len(self.board[0])/2)-1)] = self.player_black
            self.board[int(len(self.board)/2)][int((len(self.board[0])/2)-1)] = self.player_white
            self.board[int(len(self.board)/2)][int(len(self.board[0])/2)] = self.player_black
            self.board[int((len(self.board)/2)-1)][int(len(self.board[0])/2)] = self.player_white
        elif starting_player.upper() == 'B':
            self.board[int((len(self.board)/2)-1)][int((len(self.board[0])/2)-1)] = self.player_white
            self.board[int(len(self.board)/2)][int((len(self.board[0])/2)-1)] = self.player_black
            self.board[int(len(self.board)/2)][int(len(self.board[0])/2)] = self.player_white
            self.board[int((len(self.board)/2)-1)][int(len(self.board[0])/2)] = self.player_black
        else:
            pass

    def create_winning_condition(self, condition_selection):
        '''
creates winning condition
        '''
        self.condition = condition_selection


    def is_valid_move(self):
        directions = [(-1,-1),
                       (0,1),
                       (1,-1),
                       (1,0),
                       (0,-1),
                       (-1,0),
                       (-1,1),
                       (1,1)]
        valid = []
        for amount in range(self.columns):
            for place in range(self.rows):
                if self.board[amount][place] != '':
                    continue 
                for direction in directions:
                    #first increment checks one next to it
                    x = amount+direction[0]
                    y = place +direction[1]
                    if not self.On_the_Board(x,y):
                        continue
                    if self.board[x][y] != self.opposite:
                        continue
                    #second for one next to first 
                    x += direction[0]
                    y += direction[1]
                    while x in range(self.columns)and y in range(self.rows):
                        if self.board[x][y] == self.turn:
                            valid.append((amount,place))
                            break
                        if self.board[x][y] == '':
                            break
                        #increment until we find another like tile or end of board
                        x+= direction[0]
                        y+= direction[1]
        return valid
                    
        
        
    def Flip_em(self,coord):
        moves_to_flip = []
        flipped = []
        directions = [(-1,-1),
                       (0,1),
                       (1,-1),
                       (1,0),
                       (0,-1),
                       (-1,0),
                       (-1,1),
                       (1,1)]
        for direction in directions:
            x = coord[0] +direction[0]
            y = coord[1] +direction[1]
            if not self.On_the_Board(x,y):
                        continue
            if self.board[x][y] != self.opposite:
                        continue
            x += direction[0]
            y += direction[1]
            while x in range(self.columns)and y in range(self.rows):
                    if self.board[x][y] == self.turn:
                        moves_to_flip.append((x,y))
                        dir = direction
##                        print(dir)
                        for amount in range(self.columns):
##                            print((x-dir[0],y-dir[1]))
                            if self.board[x-dir[0]][y-dir[1]]== self.opposite:
                                flipped.append((x-dir[0],y-dir[1]))
                                x-=dir[0]
                                y-=dir[1]
                            
                        break
                    if self.board[x][y] == '':
                        break
                    #increment until we find another like tile or end of board
                    x+= direction[0]
                    y+= direction[1]
##        print(moves_to_flip)
        return  flipped


    def get_score(self):
        self.score_black = 0
        self.score_white = 0
        for amount in self.board:
            for place in amount:
                if place == self.player_black:
                    self.score_black+= 1
                elif place == self.player_white:
                    self.score_white+= 1
##        print('Black Score: ', self.score_black,'     White Score:', self.score_white)
        
                
                
        
        
    def game_over(self):
        moves = self.is_valid_move()

        if self.condition == '>':
            if len(moves) == 0:
                self.turn == self.opposite
                self.counter+=1
                if self.counter == 2:
##                    print('GAME OVER')
                    if self.score_black > self.score_white:
##                        print('BLACK WINS')
                        self.winner = 'Black'
                        return False               
                    elif self.score_white > self.score_black:
##                        print('WHITE WINS')
                        self.winner = 'White'
                        return False
                    elif self.score_black == self.score_white:
##                        print('STALEMATE: NO WINNER')
                        self.winner = 'NOBODY'
                        return False
        if self.condition == '<':
            if len(moves) == 0:
                self.turn = self.opposite
                self.counter+=1
                if self.counter == 2:
##                    print('GAME OVER')
                    if self.score_black < self.score_white:
##                        print('BLACK WINS')
                        self.winner = 'Black'
                        return False               
                    elif self.score_white < self.score_black:
##                        print('WHITE WINS')
                        self.winner = 'White'
                        return False
                    elif self.score_black == self.score_white:
##                        print('STALEMATE: NO WINNER')
                        self.winner = 'NOBODY'
                        return False 
       


    
    def On_the_Board(self,x, y):
    # Returns True if the coordinates are located on the board.
        return x >= 0 and x < self.columns and y >= 0 and y < self.rows

                            
                       
        




         

    def make_move(self,x_coordinate,y_coordinate):
        moves = self.is_valid_move()

        if len(moves) == 0:
            self.turn = self.opposite
##            print("No Available move, next player's turn")
            self.counter +=1 
        if len(moves) > 0:
            while True:
##                x_coordinate = int(input())-1
##                y_coordinate = int(input())-1

                if (x_coordinate,y_coordinate) not in moves:
                    break
                else:
                
                    if self.turn == 'W':
                        self.board[x_coordinate][y_coordinate] = self.player_white
##                        print(x_coordinate,y_coordinate)
                        flip = self.Flip_em((x_coordinate,y_coordinate))
##                        print(flip)
##                        print('x')
                        for tile in flip:
                            self.board[tile[0]][tile[1]] = self.player_white
                        self.turn = self.player_black
                        self.opposite = self.player_white
                        break
                        
                    elif self.turn == 'B':
                        self.board[x_coordinate][y_coordinate] = self.player_black
                        flip = self.Flip_em((x_coordinate,y_coordinate))
                        for tile in flip:
                            self.board[tile[0]][tile[1]] = self.player_black
                        self.turn = self.player_white
                        self.opposite = self.player_black
                        break
                    else:
                        break       


    def create_game_board(self):
        new_board = []
        for amount in range(self.columns):
            new_board.append([])
            for slot in range(self.rows):
                new_board[-1].append(self.NONE)
        self.board = new_board
##        for x in new_board:
##            print(x)
     

    def print_game_board(self):
        board = self.board
        for row in range(self.rows):
            for col in range(self.columns):
                if board[col][row] == '':
                    print('. ', end = ' ')
                else:
                    print(board[col][row] + ' ', end = ' ')
            print('\n')






###TO PRINT INDIVIDUAL LISTS FROM BOARD###
##for stuff in x.board:
##	print(stuff)






##x.board[int((len(x.board)/2)-1)][int((len(x.board[0])/2)-1)] = 'B'
##>>> for stuff in x.board:
##	print(stuff)
##
##	
##['', '', '', '', '', '']
##['', '', '', '', '', '']
##['', '', '', '', '', '']
##['', '', 'B', '', '', '']
##['', '', '', '', '', '']
##['', '', '', '', '', '']
##['', '', '', '', '', '']
##['', '', '', '', '', '']

##x.board[int(len(x.board)/2)][int((len(x.board[0])/2)-1)] = 'W'
##>>> for stuff in x.board:
##	print(stuff)
##
##	
##['', '', '', '', '', '']
##['', '', '', '', '', '']
##['', '', '', '', '', '']
##['', '', 'B', '', '', '']
##['', '', 'W', '', '', '']
##['', '', '', '', '', '']
##['', '', '', '', '', '']
##['', '', '', '', '', '']
##
##
##x.board[int(len(x.board)/2)][int(len(x.board[0])/2)] = 'B'
##>>> for stuff in x.board:
##	print(stuff)
##
##	
##['', '', '', '', '', '']
##['', '', '', '', '', '']
##['', '', '', '', '', '']
##['', '', 'B', '', '', '']
##['', '', 'W', 'B', '', '']
##['', '', '', '', '', '']
##['', '', '', '', '', '']
##['', '', '', '', '', '']

##x.board[int((len(x.board)/2)-1)][int(len(x.board[0])/2)] = 'W'
##>>> for stuff in x.board:
##	print(stuff)
##
##	
##['', '', '', '', '', '']
##['', '', '', '', '', '']
##['', '', '', '', '', '']
##['', '', 'B', 'W', '', '']
##['', '', 'W', 'B', '', '']
##['', '', '', '', '', '']
##['', '', '', '', '', '']
##['', '', '', '', '', '']

         
