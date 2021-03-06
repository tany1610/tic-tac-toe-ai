board = [["", "", ""],["", "", ""], ["", "", ""]]
player = "X"
ai = "O"
current_player = player
avaliable = []
scores = {'O': 1, 'X': -1, 'tie': 0}
game_has_ended = False

w = None
h = None

def setup():
    global w, h
    size(800, 800)
    w = width / 3
    h = height / 3
    
def draw():
    global w, h, game_has_ended
    
    if not game_has_ended:
        background(255, 255, 255)
        
        strokeWeight(6)
        line(w, 0, w, height)
        line(w*2, 0, w*2, height)
        line(0, h, width, h)
        line(0, h*2, width, h*2)
        
        if current_player == ai:
            ai_turn()
        
        for i in range(3):
            for j in range(3):
                spot = board[i][j]
                x = w * i + w / 2
                y = h * j + h / 2
                textAlign(CENTER, CENTER)
                textSize(100)
                fill(0)
                if spot == player:                
                    text("X", x, y)
                elif spot == ai:
                    text("O", x, y)
    
        if has_won("O"):
            draw_score("The AI won!")
            game_has_ended = True
            
        elif has_won("X"):
            draw_wcore("You won!")
            game_has_ended = True
            
        elif is_tie():
            draw_score("Tie!")
            game_has_ended = True
    
                
def has_won(current):
    global board
    
    if board[0][0] == board[0][1] == board[0][2] == current:
        return True
    elif board[1][0] == board[1][1] == board[1][2] == current:
        return True
    elif board[2][0] == board[2][1] == board[2][2] == current:
        return True
    elif board[0][0] == board[1][0] == board[2][0] == current:
        return True
    elif board[0][1] == board[1][1] == board[2][1] == current:
        return True
    elif board[0][2] == board[1][2] == board[2][2] == current:
        return True
    elif board[0][0] == board[1][1] == board[2][2] == current:
        return True
    elif board[0][2] == board[1][1] == board[2][0] == current:
        return True
    
def is_tie():
    return all(x != "" for y in board for x in y)
              
def minimax(board, depth, is_maximazing):
    global scores
    result = None
    
    if has_won("X"):
        result = "X"
    elif has_won("O"):
        result = "O"
    elif is_tie():
        result = "tie"

    if result:
        return scores[result]
    
    if is_maximazing:
        best_score = -10000
        for i in range(3):
            for j in range(3):
                if board[i][j] == "":
                    board[i][j] = "O"
                    score = minimax(board, depth + 1, False)
                    board[i][j] = ""
                    if score > best_score:
                        best_score = score
        return best_score
    
    else:
        best_score = 10000
        for i in range(3):
            for j in range(3):
                if board[i][j] == "":
                    board[i][j] = "X"
                    score = minimax(board, depth + 1, True)
                    board[i][j] = ""
                    if score < best_score:
                        best_score = score
        return best_score
    

def ai_turn():
    global board, current_player, player
    
    best_score = -10000
    best_move = []
    
    for i in range(3):
        for j in range(3):
            if board[i][j] == "":
                board[i][j] = "O"
                score = minimax(board, 0, False)
                board[i][j] = ""
                if score > best_score:
                    best_score = score
                    best_move = [i, j]
    if is_tie():
        return
    
    board[best_move[0]][best_move[1]] = "O"
    current_player = player
    
def draw_score(message):
    background(0)
    textAlign(CENTER, CENTER)
    textSize(100)
    fill(255)
    text(message, width / 2, height / 2)
    textSize(40)
    textAlign(LEFT, LEFT)
    text("(Press left mouse button to restart)", width * 0.1, height / 1.5)
    
def reset_game():
    global board, game_has_ended, current_player
    board = [["", "", ""],["", "", ""], ["", "", ""]]
    current_player = player
    game_has_ended = False
    
def mousePressed():
    global board, current_player, ai, player, w, h, game_has_ended
    
    if current_player == player:
        player_row = floor(mouseX / w)
        player_col = floor(mouseY / h)
        if board[player_row][player_col] != "X" and board[player_row][player_col] != "O":
            board[player_row][player_col] = "X"
            current_player = ai
            
    if game_has_ended:
        reset_game()
            
