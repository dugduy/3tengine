from ttt import TicTacToe
my3t=TicTacToe(logs=[(0,2),(1,1),(2,2),(1,2),(1,0),(0,0),(0,1),(2,1),(2,0)]) #use when init instead
my3t.print_out()
# my3t.load_logs([(0,2),(1,1),(2,2),(1,2),(1,0),(0,0),(0,1),(2,1),(2,0)])
# my3t.load_logs([(0,2),(1,1),(2,2),(1,2),(1,0),(0,0)])

# my3t.print_out()
# print(my3t.__dict__)
print(my3t.is_gameover,my3t.winner,my3t.state)
print(my3t.get_tickable())