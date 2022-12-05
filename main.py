"""Hangman Tic-Tac-Toe, Tu commences par jouer un jeux de hangman tu chouisis la catégorie et tu devine les lettres si tu a un elettre correctement la liste la change à un checkmark puis si tu l'a mal un X, si tu devine le mot tu gagne mais si tu perd tu va jouer le tic-tac-toe presque impossible, cest un tic-tac-toe mais l'ordi est capable de bouger deux fois (cest possible de le battre) si tu gagne le tic-tac-toe tu a la chance de rejouer si non le code arrete. Tout au long du code il utilise beaucoup des fonctions apprisent en classe. Il utilise Turtle, def function, tim package, random package, listes, join string, variables, du input, lower and upper built in function, while loop, if else elif built in functions, return, break, continue, du indexing, if elif else avec des mathematical operators; + = - > < =, du try and except built in functions,  """

#Où j'importe tout les packages d'extra nécéssaire pour le code
import random
import turtle as t
from turtle import Turtle
import time
#Où je configure l'écran
screen = t.Screen
wn = t.Screen()
wn.setup(640, 640)
#Où je configure la tortue #1
t.speed(0)
t.hideturtle()
t.pensize(2)
#Variable globale pour le temp
tim = 0
tim2 = 0
#Où je défini les règlements de tout le code
def rules():
  t6 = Turtle()
  t6.speed(0)
  t6.hideturtle()
  t6.write("""Here are the rules: 
  To start you will play Hangman,
  If you win, YOU WIN!!!
  If you lose you will play the 
  almost impossible Tic-Tac-Toe,
  If you win you replay Hangman, 
  If you lose, YOU LOSE :(,
  The rules may have been altered...""", font=('arial',20,'bold'), align='center')
  time.sleep(tim)
  t6.clear()
  t6.write("GOOD LUCK!!!", font=('arial',50,'bold'), align='center')
  time.sleep(tim2)
  t6.clear()
#Où je défini les règlements pour Hangman
def man_rules():
  t6 = Turtle()
  t6.speed(0)
  t6.penup()
  t6.hideturtle()
  t6.setposition(0, -100)
  t6.write("""Here are the rules: 
  Its regular Hangman,
  You will start by picking
  a category in the console,
  Then the code will take 
  a word from that category,
  You will have to enter
  a letter for your guess,
  If its wrong a body part
  will be added to the Hangman,
  If hes is completely there...
  YOU LOSE!!!""", font=('arial',20,'bold'), align='center')
  time.sleep(tim)
  t6.clear()
  t6.setposition(0,0)
  t6.write("GOOD LUCK!!!", font=('arial',50,'bold'), align='center')
  time.sleep(tim2)
  t6.clear()
#Où je défini les règlements pour Tic-Tac-Toe
def tic_rules():
  t6 = Turtle()
  t6.speed(0)
  t6.penup()
  t6.hideturtle()
  t6.setposition(0, -100)
  t6.write("""Here are the rules: 
  You play Tic-Tac-Toe,
  You will start as x,
  and will place your x
  in a certain coordinate using:
  Colum to start (Vertical)
  and Row (Horizontal)
  If you win, you can play
  Hangman again...
  The Game has a little twist,
  You'll find out soon enough...
  """, font=('arial',20,'bold'), align='center')
  time.sleep(tim)
  t6.clear()
  t6.setposition(0,0)
  t6.write("GOOD LUCK!!!", font=('arial',50,'bold'), align='center')
  time.sleep(tim2)
  t6.clear()
#Où je défini la totalité du code de Hangman
def man():
  man_rules()
#Où je défini le code pour déssiner le poteau
  def hang():
    t.setheading(0)
    t.penup()
    t.setposition(-150,-150)
    t.pendown()
    t.forward(75)
    t.penup()
    t.left(180)
    t.forward(37.5)
    t.right(90)
    t.pendown()
    t.forward(200)
    t.right(90)
    t.forward(75)
    t.right(90)
    t.forward(20)
#Où je défini le code pour déssiner la tête
  def head():
    t.penup()
    t.setposition(-55, 10)
    t.pendown()
    t.circle(20)
#Où je défini le code pour déssiner le corp
  def body():
    t.penup()
    t.setposition(-35,-10)
    t.pendown()
    t.forward(70)
#Où je défini le code pour déssiner la première jambe
  def leg1():
    t.penup()
    t.setposition(-35, -80)
    t.right(45)
    t.pendown()
    t.forward(35)
#Où je défini le code pour déssiner la deuxième jambe
  def leg2():
    t.penup()
    t.setposition(-35, -80)
    t.left(90)
    t.pendown()
    t.forward(35)
#Où je défini le code pour déssiner le premier bras
  def arm1():
    t.setheading(90)
    t.penup()
    t.setposition(-35, -40)
    t.right(45)
    t.pendown()
    t.forward(35)
#Où je défini le code pour déssiner le deuxième bras
  def arm2():
    t.penup()
    t.setposition(-35, -40)
    t.left(90)
    t.pendown()
    t.forward(35)
#Où je défini le code pour déssiner le premier oeuil
  def eye1():
    t.setheading(0)
    t.penup()
    t.setposition(-40, 10)
    t.pendown()
    t.circle(5)
#Où je défini le code pour déssiner le deuxième oeuil
  def eye2():
    t.setheading(0)
    t.penup()
    t.setposition(-30, 10)
    t.pendown()
    t.circle(5)
#Où je défini le code pour déssiner la bouche
  def mouth():
    t.penup()
    t.setposition(-30, -2.5)
    t.setheading(135)
    t.pendown()
    t.circle(10, 90)
#Où je défini le code pour déssiner le nez
  def nose():
    t.penup()
    t.setposition(-35, 7.5)
    t.pendown()
    t.circle(2, 100, 2)
#Où je call pour déssiner le poteau
  hang()
#Où je met toutes les listes
  func_list = [head,body,leg1,leg2,arm1,arm2,eye1,eye2,mouth,nose]
  words1 = ["disavow", "pneumonoultramicroscopicsilicovolcanoconiosis"]
  words2 = ["beaker", "condensation", "coding"]
  words3 = ["brazil", "canada", "worcestershire"]
  words4 = ["literature", "grammar", "books"]
  words5 = ["painting", "canvas", "pencil"]
  words6 = ["football", "hockey", "soccer"]
  words7 = ["minecraft", "fortnite", "among us"]
#Où est la liste des lettres puis commande pour les mettre en string
  letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
  let = " ".join([str(item) for item in letters])
  index = 0
#Où je créé la tortue #2
  t2 = Turtle()
  t2.hideturtle()
  t2.speed(0)
  t2.penup()
  t2.setposition(0, 150)
#Où je créé la tortue #3
  t3 = Turtle()
  t3.hideturtle()
  t3.speed(0)
  t3.penup()
  t3.setposition(0, 260)
  t3.write("CATEGORIES", font=('arial',25,'bold'), align='center')
#Où je créé la tortue #4
  t4 = Turtle()
  t4.speed(0)
  t4.hideturtle()
  t4.penup()
  t4.setposition(0, 240)
  t4.write("Impossible, Science, Geography, English, Art, Sports, Gaming", font=('arial',10,'bold'), align='center')
#Où je créé la tortue #5
  t5 = Turtle()
  t5.hideturtle()
  t5.speed(0)
  t5.penup()
  t5.setposition(0, 100)
  t5.write(let, font=('arial',15,'bold'), align='center')
#Où l'utilisateur choisi une catégorie puis le met en lettres minuscules
  choice1 = input("Pick a category, (Impossible, science, Geography, english, art, sports, gaming): ")
  choice = choice1.lower()
#Où le code pour que si l'utilisateur ne met pas une des catégories il lui demande encore
  while choice not in ["impossible", "science", "geography", "english", "art", "sports", "gaming"]:
    choice1 = input("Pick a category, (Impossible, Science, Geography, English, Art, Sports, Gaming): ")
    choice = choice1.lower()
#Où le code choicis un mot aléatoirement par rapport à la catégorie choisise
  if choice == "impossible":
    t4.clear()
    t4.write("Impossible", font=('arial',10,'bold'), align='center')
    secret_word = random.choice(words1)
    if secret_word == "pneumonoultramicroscopicsilicovolcanoconiosis":
      font = 15
    else:
      font = 50
  elif choice == "science":
    t4.clear()
    t4.write("Science", font=('arial',10,'bold'), align='center')
    secret_word = random.choice(words2)
    font = 50
  elif choice == "geography":
    t4.clear()
    t4.write("Geography", font=('arial',10,'bold'), align='center')
    secret_word = random.choice(words3)
    font = 50
  elif choice == "english":
    t4.clear()
    t4.write("English", font=('arial',10,'bold'), align='center')
    secret_word = random.choice(words4)
    font = 50
  elif choice == "art":
    t4.clear()
    t4.write("Art", font=('arial',10,'bold'), align='center')
    secret_word = random.choice(words5)
    font = 50
  elif choice == "sports":
    t4.clear()
    t4.write("Sports", font=('arial',10,'bold'), align='center')
    secret_word = random.choice(words6)
    font = 50
  elif choice == "gaming":
    t4.clear()
    t4.write("Gaming", font=('arial',10,'bold'), align='center')
    secret_word = random.choice(words7)
    font = 50
#Où le code écrit le mot
  dashes = "-" * len(secret_word)
  t2.write(dashes, font=('arial', font,'bold'), align='center')
  guesses_left = 10
#Où l'utiisateur va essayer de choisir un lettre et si il écrit une mauvaise réponse il lui demande encore
  def get_guess():
      while True:
          guess = input("Guess: ")
          if guess.islower() == False:
              print("Your guess must be a lowercase letter!")
          else:
              if guess.islower():
                  if len(guess) == 1:
                      return guess
                  else: 
                      print("Your guess must have exactly one character!")
#Où les lettres devinés ce font ajouter au espace vides du mot et rafréchit
  def update_dashes(secret_word, dashes, guess):
      result = ""
      for i in range(len(secret_word)):
          if secret_word[i] == guess:
              result += guess
          else:
              result += dashes[i]
      return result
#Où le code met à jour la liste de lettres selon les lettres devinés si ils sont correctes ou mauvaises
  while True:
    guess = get_guess()
    if guess in secret_word:
      let = let.replace(guess, "✓")
      t5.clear()
      t5.setposition(0, 100)
      t5.write(let, font=('arial',15,'bold'), align='center')
      print("The letter is in the word.")
      dashes = update_dashes(secret_word, dashes, guess)
    else:
      let = let.replace(guess, "-")
      t5.clear()
      t5.setposition(0, 100)
      t5.write(let, font=('arial',15,'bold'), align='center')
      print("That letter is not in the word.")
      func_list[index]()
      index = index + 1
      guesses_left = guesses_left - 1
      if guesses_left == 0:
        x = "lose"
        break
#Où le code réécrit le mot avec les lettres devinés
    t2.clear()
    t2.write(dashes, font=('arial', font,'bold'), align='center')
    if dashes == secret_word:
      x = "win"
      break
#Où le code fait des choses par rapport à si l'utilisateur à deviné les lettres sans perdre ses 10 éssais si oui il donne un message qu'il a ganger sinon il lui fait joué tic-tac-toe
  if x == "lose":
    t.clear()
    t2.clear()
    t3.clear()
    t4.clear()
    t5.clear()
    t2.setposition(0,  50)
    t2.write("I will give you another chance, ",font=('arial',25,'bold'), align='center')
    t2.setposition(0,0)
    t2.write("If you beat my almost impossible",font=('arial',25,'bold'), align='center')
    t2.setposition(0, -50)
    t2.write("Tic Tac Toe you can play again...", font=('arial',25,'bold'), align='center')
    t5.write("You " + x + "! The word was: " + secret_word, font=('arial',25,'bold'), align='center')
    time.sleep(5)
    t.clear()
    t2.clear()
    t3.clear()
    t4.clear()
    t5.clear()
    tic()
  else:
    t.clear()
    t2.clear()
    t3.clear()
    t4.clear()
    t5.clear()
    t3.setposition(0,0)
    t3.write("YOU WIN!!!",font=('arial',70,'bold'), align='center')
#Où je défini tout le code du Tic-Tac-Toe
def tic():
  tic_rules()
#Où le code va prendre la saisie de l'utilisateur et va faire sure que c'est possible de le placer à n'importe qu'elle place
  def get_valid_index(prompt):
      while True:
          try:
              index = int(input(prompt))
              if index >= 1 and index <= 3:
                  index = index - 1
                  return index
              print("Must be 1 - 3 inclusive!")
          except ValueError:
              print("Must be an integer!")
#Où tout les façons de ganger son stocker
  def game_is_over(board):
    for i in range(3):
#If statement si quelqu'un gagne au coordonnées spécifiques
          if board[i][0] == board[i][1] == board[i][2] and board[i][0] != "-":
              print(board[i][0] + " wins!")
              global w
              w = board[i][0]
              return True
#If statement si quelqu'un gagne au coordonnées spécifiques
          if board[0][i] == board[1][i] == board[2][i] and board[0][i] != "-":
              print(board[0][i] + " wins!")
              w = board[0][i]
              return True
#If statement si quelqu'un gagne au coordonnées spécifiques
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != "-":
          print(board[0][0] + " wins!")
          w = board[0][0]
          return True
#If statement si quelqu'un gagne au coordonnées spécifiques
    if board[2][0] == board[1][1] == board[0][2] and board[2][0] != "-":
          print(board[2][0] + " wins!")
          w = board[2][0]
          return True
#If statement si quelqu'un gagne au coordonnées spécifiques
    if "-" not in board[0] and "-" not in board[1] and "-" not in board[2]:
          print("Tie game!")
          w = "a"
          return True
    return False
#Où la liste "board" est créé pour le tableau et où il se fait transformer en string
  board = []
  board = [['-', '-', '-'],
  ['-', '-', '-'],
  ['-', '-', '-']]
  board1 = "  |  ".join([str(item) for item in board[0]])
  board2 = "  |  ".join([str(item) for item in board[1]])
  board3 = "  |  ".join([str(item) for item in board[2]])
#Où toutes les choses nécéssairespour commencer le code se font mettres en place
  turn = "o"
  t2 = Turtle()
  t2.hideturtle()
  t2.speed(0)
  t2.penup()
  t2.clear()
  board1 = "  |  ".join([str(item) for item in board[0]])
  board2 = "  |  ".join([str(item) for item in board[1]])
  board3 = "  |  ".join([str(item) for item in board[2]])
  t2.setposition(0,50)
  t2.write(board1, font=('arial',25,'bold'), align='center')
  t2.setposition(0, 0)
  t2.write(board2, font=('arial',25,'bold'), align='center')
  t2.setposition(0, -50)
  t2.write(board3, font=('arial',25,'bold'), align='center')
#Où le "rigging" du Tic-Tac-Toe presque impossible arrive, chaque if elif démontre une chose à faire si il y a deux x à une position qui pourrait faire un Tic-Tac-Toe
  while not game_is_over(board):
    if turn == 'x':
      if board[0][0] == board[0][1] == "x":
        board[0][2] = "o"
      elif board[0][1] == board[0][2] == "x":
        board[0][0] = "o"
      elif board[0][0] == board[0][2] == "x":
        board[0][1] = "o"
      elif board[1][0] == board[1][1] == "x":
        board[1][2] = "o"
      elif board[1][1] == board[1][2] == "x":
        board[1][0] = "o"
      elif board[1][0] == board[1][2] == "x":
        board[1][1] = "o"
      elif board[2][0] == board[2][1] == "x":
        board[2][2] = "o"
      elif board[2][1] == board[2][2] == "x":
        board[2][0] = "o"
      elif board[2][0] == board[2][2] == "x":
        board[2][1] = "o"
      elif board[0][0] == board[2][2] == "x":
        board[1][1] = "o"
      elif board[0][2] == board[2][0] == "x":
        board[1][1] = "o"
      elif board[0][0] == board[1][1] == "x":
        board[2][2] = "o"
      elif board[1][1] == board[2][2] == "x":
        board[0][0] = "o"
      elif board[2][0] == board[1][1] == "x":
        board[0][2] = "o"
      elif board[0][2] == board[1][1] == "x":
        board[2][0] = "o"
      elif board[0][0] == board[1][0] == "x":
        board[2][0] = "o"
      elif board[1][0] == board[2][0] == "x":
        board[0][0] = "o"
      elif board[0][0] == board[2][0] == "x":
        board[1][0] = "o"
      elif board[0][1] == board[1][1] == "x":
        board[2][1] = "o"
      elif board[1][1] == board[2][1] == "x":
        board[0][1] = "o"
      elif board[0][1] == board[2][1] == "x":
        board[1][1] = "o"
      elif board[0][2] == board[1][2] == "x":
        board[2][2] = "o"
      elif board[1][2] == board[2][2] == "x":
        board[0][2] = "o"
#Choisis aléatoirement une coordonnée
      row = random.randint(0,2)
      col = random.randint(0,2)
#Où l'ordinateur choisi où jouer aléatoirement
      if board[col][row] == "-":
        board[col][row] = "o"
        board1 = "  |  ".join([str(item) for item in board[0]])
        board2 = "  |  ".join([str(item) for item in board[1]])
        board3 = "  |  ".join([str(item) for item in board[2]])
        t2.clear()
        t2.setposition(0, 50)
        t2.write(board1, font=('arial',25,'bold'), align='center')
        t2.setposition(0, 0)
        t2.write(board2, font=('arial',25,'bold'), align='center')
        t2.setposition(0, -50)
        t2.write(board3, font=('arial',25,'bold'), align='center')
        turn = "o"
      else:
        continue
#Où les commandes du début vont tousses ce réunires pour imprimer le choix des coordonnées de l'utilisateur
    elif turn == "o":
      print("It's your turn.")
      row = get_valid_index("Column: ")
      col = get_valid_index("Row: ")
      if board[col][row] == '-':
        board[col][row] = "x"
        board1 = "  |  ".join([str(item) for item in board[0]])
        board2 = "  |  ".join([str(item) for item in board[1]])
        board3 = "  |  ".join([str(item) for item in board[2]])
        t2.clear()
        t2.setposition(0, 50)
        t2.write(board1, font=('arial',25,'bold'), align='center')
        t2.setposition(0, 0)
        t2.write(board2, font=('arial',25,'bold'), align='center')
        t2.setposition(0, -50)
        t2.write(board3, font=('arial',25,'bold'), align='center')
        turn = 'x'
      else:
        print("Choose a different spot")
        continue
#Si la variable w (win) est "x" il laisse l'utilisateur rejouer
  if w == "x":
    t.clear()
    t2.clear()
    global tim
    global tim2
    tim = 0
    tim2 = 0
    man()
#Si la variable w (win) est "o" il donne un message que l'utilisateur à perdu et ferme le programme
  elif w == "o":
    t.clear()
    t2.clear()
    t.penup()
    t2.penup()
    t2.setposition(0,0)
    t2.write("You lose :(", font=('arial',70,'bold'), align='center')
#Si le code à déterminé une égalité il donne un message que c'était un égalité puis sort du code
  else:
    t.clear()
    t2.clear()
    t.penup()
    t2.penup()
    t2.setposition(0,0)
    t2.write("TIE...", font=('arial',70,'bold'), align='center')
    t2.setposition(0, -100)
    t2.write("Still LOST :(", font=('arial',70,'bold'), align='center')
#Où le code call les fonctions pour qu'ils se run
rules()
man()