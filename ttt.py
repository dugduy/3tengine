class TicTacToe:
    def __init__(self,size=3,logs:list=[]) -> None:
        self.size=size
        self.logs=logs
        self.icons=['x','o']
        self.board_vector=[[' ' for j in range(size)] for i in range(size)]
        self.winner=None
        self.state='Pending'
        self.win_condition=self.win_conculate()
        self.is_gameover=self.is_gameovered()
    
    def win_conculate(self):
        row_win=[[(i,j) for j in range(self.size)] for i in range(self.size)]
        clumn_win=[[(j,i) for j in range(self.size)] for i in range(self.size)]
        l2r_cross=[[(i,i) for i in range(self.size)]]
        r2l_cross=[[(i,self.size-i-1) for i in range(self.size)]]
        return row_win+clumn_win+l2r_cross+r2l_cross

    def print_out(self):
        print('-'*20)
        for i in self.board_vector:
            print(i)
    
    def is_gameovered(self):
        for i in self.win_condition:
            cr_condit=[]
            for j in i:
                cr_condit.append(self.board_vector[j[0]][j[1]])
            winer=list(set(cr_condit))
            if len(winer)==1 and winer[0]!=' ':
                self.winner=winer[0]
                self.state=self.winner+' won!'
                return 1
        if len(self.logs)==self.size**2:
            self.state='Tie'
            return 1
        return 0
    
    def ticking(self,pos):
        x=pos[1]
        y=pos[0]
        if self.board_vector[x][y]==' ' and not self.is_gameover:
            self.board_vector[x][y]=self.icons[len(self.logs)%2]
            self.logs.append((x,y))
            self.is_gameover=self.is_gameovered()
            return 1
        else:
            return 0

    # loading from logs for faster coding
    def load_logs(self,logs):
        for i in logs:
            self.ticking(i)

# example

# my3t=TicTacToe()
# my3t.print_out()
# my3t.load_logs([(0,2),(1,1),(2,2),(1,2),(1,0),(0,0),(0,1),(2,1),(2,0)])
# my3t.print_out()
# # print(my3t.__dict__)
# print(my3t.is_gameover,my3t.winner,my3t.state)