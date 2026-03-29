class XO:
  def __init__(self):
    self.board = [[None,None,None],
                  [None,None,None],
                  [None,None,None]]
    
  def local_setup(self, p1, p2):
    self.p = [p1,p2]
    self.on=True
    self.turn=0
    
  
  def draw_checker(self):
    for i in self.board:
      for j in i:
          if j == None:
            return False
    return True
  
  def win_checker(self):
    a= [[(0,0),(1,1), (2,2)],
        [(0,0),(0,1), (0,2)],
        [(1,0),(1,1), (1,2)],
        [(2,0),(2,1), (2,2)],
        [(0,2),(1,1), (2,0)],
       ]
    for i in range(len(a)):
        if (self.board[a[i][0][0]][a[i][0][1]]==self.board[a[i][1][0]][a[i][1][1]]) and(
          self.board[a[i][1][0]][a[i][1][1]]==self.board[a[i][2][0]][a[i][2][1]]) and (
            self.board[a[i][0][0]][a[i][0][1]] != None):
            return self.board[a[i][1][0]][a[i][1][1]]
        if i >=1 and i<=3:
          if (self.board[a[i][0][1]][a[i][0][0]]==self.board[a[i][1][1]][a[i][1][0]]) and(
          self.board[a[i][1][1]][a[i][1][0]]==self.board[a[i][2][1]][a[i][2][0]]) and (
            self.board[a[i][0][1]][a[i][0][0]] !=None):
            return self.board[a[i][0][1]][a[i][0][0]]
    return False
  
  @staticmethod
  def render_board(board):
    rb=""
    rb+="\nX"+("-"*7)+"\n"
    b=1
    for i in board:
      rb+=str(b)+"|"
      for j in i:
        a = " "
        if j == 0:
          a="O"
        elif j == 1:
          a="X"
        rb+=a+"|"
      b+=1
      rb+="\n"
    rb+=" "+("-"*7)+ "\n"
    rb+=" 1  2  3 Y\n"
    return rb
  
  def clear(self):
    self.board = [[None,None,None],
                  [None,None,None],
                  [None,None,None]]
    
  @staticmethod
  def render_info():
    r = """
      rules:
      u will know\n
      Choose values b/w 1-3 for (x,y)
      eg: (1,3)\n
      press q: to quit
      press n: for new game \n
      """
    return r
  
  def input(self, j):
    try: 
      match j:
        case "q":
          return -1
        case "n":
          return -2
      self.update_board(eval(j))
      self.switch_p()
      return 1
    except:
      return -3
    
  def switch_p(self):
    if self.turn == 0:
      self.turn = 1
    else:
      self.turn = 0
      
  def update_board(self, val:tuple):
    match self.board[val[0]-1][val[1]-1]:
      case None:
        self.board[val[0]-1][val[1]-1] = self.turn
      case _:
        raise ValueError("already occupied")

  
  def game(self):
    print(self.render_info())
    
    while self.on:
      print(self.render_board(self.board))
      while True:
        m = "O"
        if self.turn == 1:
          m="X"
        print(f"{self.p[self.turn]}({m})", end=" ")
      
        match self.input(input("(x,y) : ")):
          case -1:
            print("\nbye ):")
            self.on=False
            break
          case -2:
            print("\nFresh start!!!")
            self.clear()
            self.turn=0
            break
          case -3:
            print("Enter Proper Value")
          case _:
            break
      
      a=self.win_checker()
      if a != False:
        print(self.p[a], "Won")
        self.on = False
      elif self.draw_checker():
        print("the match is a draw")
        self.on = False

        
if __name__ == "__main__":
  xo =XO()
  xo.local_setup("player 1", "player 2")
  xo.game()
