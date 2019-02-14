###OTHELLO_GUI
# import point
# import spots_model
import tkinter
import math
import Othello_Logic


default_font = ('Helvetica', 15)
class end_window:
    '''
Creates the ending window of the game
    '''
    def __init__(self, gs):
        self._the_end = tkinter.Toplevel()
        self._othello_state = gs
        self._ending_label = tkinter.Label(master = self._the_end, text ='{} WINS!'.format(self._othello_state.winner, font = default_font))

        self._ending_label.grid(row = 0, column = 0, columnspan = 1, padx = 10, pady = 10,
            sticky = tkinter.N + tkinter.E + tkinter.S + tkinter.W)

        self._start_again_label = tkinter.Label(
            master = self._the_end, text = 'press ok to exit this window, then press start to start a new game',
            font = default_font)
        self._start_again_label.grid(
            row = 1, column = 0, columnspan = 1, padx = 10, pady = 10,
            sticky = tkinter.N + tkinter.E + tkinter.S + tkinter.W)

        self.the_buttons = tkinter.Frame(master = self._the_end)
        self.the_buttons.grid(
            row = 2, column = 0, padx = 10, pady = 10)
        
        self.ok_button = tkinter.Button(
            master = self.the_buttons, text = 'OK', font = default_font,
            command = self.exit_it)
        self.ok_button.grid(row = 0, column = 0, padx = 10, pady = 10)

        self.ok_pressed = False


    def show_self(self):
        self._the_end.grab_set()
        self._the_end.wait_window()


    def exit_it(self):
        self._the_end.destroy()

            
            
class start_dialog:
    '''
creates the starting game set up window
    '''
    def __init__(self):
        self._dialog_window = tkinter.Toplevel()

        self.label_for_rows = tkinter.Label(
            master = self._dialog_window, text = 'How many rows do you want?', font = default_font)
        self.label_for_rows.grid(
            row = 0, column = 0, columnspan = 2, padx = 10, pady = 10,
            sticky = tkinter.W)
        
        self.entry_for_rows = tkinter.Entry(
            master = self._dialog_window, width = 10, font = default_font)
        self.entry_for_rows.grid(
            row = 0, column = 1, padx = 100, pady = 10,
            sticky = tkinter.W + tkinter.E)
        

        self.label_for_columns = tkinter.Label(
            master = self._dialog_window, text = 'How many columns do you want?',
            font = default_font)
        self.label_for_columns.grid(
            row = 1, column = 0, columnspan = 2, padx = 10, pady = 10,
            sticky = tkinter.W)
        self.entry_for_columns = tkinter.Entry(
            master = self._dialog_window, width = 10, font = default_font)
        self.entry_for_columns.grid(
            row = 1, column = 1, padx = 100, pady = 10,
            sticky = tkinter.W + tkinter.E)


        self.whose_first_label = tkinter.Label(
            master = self._dialog_window, text = 'Who will go first? B or W?',
            font = default_font)
        self.whose_first_label.grid(
            row = 2, column = 0, padx = 10, pady = 10,
            sticky = tkinter.W)
        
        self.whose_first_entry = tkinter.Entry(
            master = self._dialog_window, width = 10, font = default_font)
        self.whose_first_entry.grid(
            row = 2, column = 1, padx = 100, pady = 10,
            sticky = tkinter.W + tkinter.E)


        self.orientation_label = tkinter.Label(
            master = self._dialog_window, text = 'Select orientation order: B or W',
            font = default_font)
        self.orientation_label.grid(
            row = 3, column = 0, padx = 10, pady = 10,
            sticky = tkinter.W)
        
        self.orientation_entry = tkinter.Entry(
            master = self._dialog_window, width = 10, font = default_font)
        self.orientation_entry.grid(
            row = 3, column = 1, padx = 100, pady = 10,
            sticky = tkinter.W + tkinter.E)



        self.winning_label = tkinter.Label(
            master = self._dialog_window, text = 'input > or < to specify winning condition',
            font = default_font)
        self.winning_label.grid(
            row = 4, column = 0, padx = 10, pady = 10,
            sticky = tkinter.W)
        
        self.winning_entry = tkinter.Entry(
            master = self._dialog_window, width = 10, font = default_font)
        self.winning_entry.grid(
            row = 4, column = 1, padx = 100, pady = 10,
            sticky = tkinter.W + tkinter.E)
        
        

        self.frame_buttons = tkinter.Frame(master = self._dialog_window)
        self.frame_buttons.grid(
            row = 5, column = 0, padx = 10, pady = 10)
        

        self.ok_button = tkinter.Button(
            master = self.frame_buttons, text = 'OK', font = default_font,
            command = self.on_ok_button_pressed)
        self.ok_button.grid(row = 0, column = 0, padx = 10, pady = 10)


        self.cancel_button = tkinter.Button(
            master = self.frame_buttons, text = 'Cancel', font = default_font,
            command = self.on_cancel_button_pressed)
        self.cancel_button.grid(row = 0, column = 1, padx = 10, pady = 10)


        self.ok_pressed = False
        self.rows = 0
        self.columns = 0
        self.first = ''
        self.orientation = ''
        self.condition = ''

    def show_yo_self(self):
        '''
shows the starting window
        '''
        self._dialog_window.grab_set()
        self._dialog_window.wait_window()

    def was_ok_button_pressed(self):
        '''
returns true if ok was pressed
        '''
        return self.ok_pressed

    def on_ok_button_pressed(self):
        '''
creates set of tasks to be done once ok is pressed 
        '''
        self.ok_pressed = True
        self.rows = self.entry_for_rows.get()
        self.columns = self.entry_for_columns.get()
        self.first = self.whose_first_entry.get()
        self.orientation = self.orientation_entry.get()
        self.condition = self.winning_entry.get()
        self._dialog_window.destroy()

    def on_cancel_button_pressed(self):
        '''
dictates what is to be done when cancel is pressed 
        '''
        self._dialog_window.destroy()
    

class the_canvas(tkinter.Canvas):
    '''
Creates and deals with the main game canvas
    '''
    def __init__(self, parent, gs, oa, **kwargs):
        tkinter.Canvas.__init__(self,parent,**kwargs)
        self.bind("<Configure>", self._resize)
        self.width = 600
        self.height = 600
        self._othello_state = gs
        self._othello_app = oa
        self._turn_color = ''
        
    def _resize(self, event):
        '''
handles resizing
        '''
        horizon_scale = event.width/self.width
        vertical_scale = event.height/self.height
        self.width = event.width
        self.height = event.height
        self.configure(width = self.width, height = self.height)
        self.scale('all', 0,0,horizon_scale,vertical_scale)

    def _assemble_horizontal(self):
        '''
creates the horizontal gridlines
        '''
        self._hori = self.height/self._othello_state.rows
        for amount in range(self._othello_state.rows+1):
            self.create_line(0, self._hori*amount, self.width, self._hori*amount, fill = 'black')

    def _assemble_vertical(self):
        '''
creates the vertical gridlines
        '''
        self._vert = self.width/self._othello_state.columns
        for amount in range(self._othello_state.columns+1):
            self.create_line(self._vert*amount, 0, self._vert*amount, self.height, fill = 'black')
        


    def _update_canvas(self):
        '''
updates the canvas
        '''
        if self._othello_state.turn == 'W':
            self._turn_color = 'white'
        elif self._othello_state.turn == 'B':
            self._turn_color = 'black'
        self.delete(tkinter.ALL)
        self._assemble_horizontal()
        self._assemble_vertical()
        self._set_pieces()
            

    def make_piece(self,x1,x2,y1,y2):
        '''
makes a game tile
        '''
        self.create_oval(x1,x2,y1,y2,outline = 'black', fill = self._turn_color) 

    def _place_piece(self, event):
        '''
handles the placing of a valid tile on the canvas board
        '''
        coordinates = (event.x,event.y)
        column_weight = self.width/self._othello_state.columns
        row_weight = self.height/self._othello_state.rows
        row = int(event.y/row_weight)
        col = int(event.x/column_weight)
        self._othello_state.make_move(col,row)
##        print(col,row)
        self._update_canvas()
        self._othello_state.game_over()
        self._othello_state.game_over()
        if self._othello_state.counter == 2:
            self._othello_app._update_scores()
            self._on_game_over()
            
##                   self.make_piece(column_weight*col, row_weight*row,column_weight*col+column_weight,row_weight*row+row_weight)
##                   print((col,row))


    def _on_game_over(self):
        '''
handles what is to be done once game ends
        '''
        ending_game = end_window(self._othello_state)
        ending_game.show_self()
        
    
    def _set_pieces(self):
        '''
draws all necessary pieces on the board
        '''
        for stuff in range(self._othello_state.columns):
            for amount in range(self._othello_state.rows):
                coordinates = (stuff,amount)
                column_weight = self.width/self._othello_state.columns
                row_weight = self.height/self._othello_state.rows
                canvasx = stuff*column_weight
                canvasy = amount*row_weight
                spot = self._othello_state.board[stuff][amount]
                if spot != self._othello_state.NONE:
                    
                    oline = 'black'
                    color = 'white'
                    
                    if spot == self._othello_state.player_black:
                        oline = 'white'
                        color = 'black'
                    self.create_oval(canvasx,canvasy,canvasx+column_weight,canvasy+row_weight,outline = oline, fill = color)

        
        
        
        
        
        

class Othello_app:
    def __init__(self):
        self._root_window = tkinter.Tk()

        
        self._title_text = tkinter.StringVar()
        self._title_text.set("welcome to Othello")

        self._title_label = tkinter.Label(
            master = self._root_window, textvariable = self._title_text,
            font = ('Helvetica', 14))

        self._title_label.grid(
            row= 0, column = 0, columnspan = 2, padx = 5, pady = 1,
            sticky = tkinter.N)

        self._othello_state = Othello_Logic.Othello_state()

        self._first_player = self._othello_state.first_player

        self._turn = self._othello_state.turn
 

        self._columns = self._othello_state.columns
        self._rows = self._othello_state.rows

        self._white_score_text = tkinter.StringVar()


        self._white_score_label = tkinter.Label(
            master = self._root_window, textvariable = self._white_score_text,
            font = ('Helvetica', 14))

        self._white_score_label.grid(
            row= 2, column = 0, columnspan =1, padx = 1, pady = 1,
            sticky = tkinter.W)

        self._black_score_text = tkinter.StringVar()


        self._black_score_label = tkinter.Label(
            master = self._root_window, textvariable = self._black_score_text,
            font = ('Helvetica', 14))

        self._black_score_label.grid(
            row= 2, column = 0, columnspan =1, padx = 1, pady = 1,
            sticky = tkinter.E)

        self.width = 600
        self.height = 600

        self._start_button = tkinter.Button(
            master = self._root_window, text = 'Click to Start',
            font = default_font, command = self._on_start_clicked)

        self._start_button.grid(
            row = 2, column = 0, columnspan = 1, padx = 10,
            pady = 10, sticky = tkinter.S)

        self._main_canvas = the_canvas(self._root_window, self._othello_state,self,height = self.height,
        width = self.width, background = '#2EB82E', highlightthickness = 0)
        
        self._main_canvas.grid(
        row = 0, column = 0, padx = 30, pady = 20,
        sticky = tkinter.N +tkinter.E + tkinter.S + tkinter.W)
        
        self._main_canvas.bind("<Button-1>",self._canvas_clicked)

        self._root_window.rowconfigure(0, weight = 1)
        self._root_window.columnconfigure(0, weight = 1)

        self._main_loop_start()

    def _canvas_clicked(self, event):
        self._update_scores()
        self._update_scores()
        self._main_canvas._place_piece(event)
        self._update_scores()

    def _update_scores(self):
        self._othello_state.get_score()
        
        self._white_score_text.set("White Score: {}".format(str(self._othello_state.score_white)))
        self._black_score_text.set("Black Score: {}".format(str(self._othello_state.score_black)))

        self._title_text.set("{} TURN".format(self._othello_state.turn))
    def _main_loop_start(self):
        self._root_window.mainloop()

    def _on_start_clicked(self):
        starting_game = start_dialog()
        starting_game.show_yo_self()
        if starting_game.was_ok_button_pressed():
##            self._rows = int(starting_game.rows)
##            self._columns = int(starting_game.columns)
##            self._first_player = starting_game.first
##            self._orientation = starting_game.orientation
            self._othello_state.create_row_amount(int(starting_game.rows))
            self._othello_state.create_column_amount(int(starting_game.columns))
            self._othello_state.create_first_player(starting_game.first)

            self._rows = self._othello_state.rows
            self._columns = self._othello_state.columns

            self._othello_state.create_game_board()
            self._othello_state.starting(str(starting_game.orientation))
            self._othello_state.create_winning_condition(str(starting_game.condition))
            self._othello_state.counter = 0
            self._main_canvas._update_canvas()
        
     

        pass

    
        
    

     
