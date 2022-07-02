import random



class TicTacToe:
        def __init__(self):
                self.board=[]
        
        def create_board(self):
                for i in range(3):
                        row=['_','_','_']
                        self.board.append(row)

        def isfull(self):
                for row in self.board:
                        for cell in row:
                                if cell=='_':
                                        return False
                return True

        def fill_board(self,row,col,player):
                self.board[row][col]=player

        def get_player(self):
                return random.randint(0,1)

        def swap_player(self,player):
                if player=="X":
                        return "O"
                else:
                        return "X"

        def is_winner(self,player):
                #horizonttally
                for i in range(3):
                        win=True
                        for j in range(3):
                                if self.board[i][j]!=player:
                                        win=False
                
                #vertically
                for i in range(3):
                        win=True
                        for j in range(3):
                                if self.board[j][i]!=player:
                                        win=False
                
                #diagonally
                win=True
                for i in range(3):
                        if self.board[i][i]!=player:
                                win=False

                for i in range(-1,-4,-1):
                        if self.board[i][i]!=player:
                                win=False

                return win
        def show(self):
                for row in self.board:
                        print('\n')
                        for cell in row:
                                print(cell,end=' ')
        def start(self):
                self.create_board()

                if self.get_player()==1:
                        player='X'
                else:
                        player='O'
        
                while True:
                        print(f'PLAYER {player} TURN')

                        self.show()

                        row, col = list(map(int, input("\nEnter row and column number: \n").split()))

                        print('\n')

                        self.fill_board(row-1,col-1,player)

                        if self.is_winner(player):
                                print(f"player {player} won")
                                break

                        elif self.isfull():
                                print('DRAW!')
                                break

                        player=self.swap_player(player)

                self.show()


x=TicTacToe()
x.start()




