board = {'tL': " ", 'tM': " ", 'tR': " ",
         'mL': " ", 'mM': " ", 'mR': " ",
         'bL': " ", 'bM': " ", 'bR': " "}
bmoves = {'bL': " ",'tR': " ", 'bR': " "}
boardd = ['tL', 'tM', 'tR',
          'mL','mM', 'mR',
          'bL', 'bM', 'bR']
Row = ['t', 'm', 'b']
Column = ['L', 'M', 'R']

def Theboard(B0ard):
    print('t' + '| ' + B0ard['tL'] + '|' + B0ard['tM'] + "|" + B0ard['tR'])
    print("-  -+-+-")
    print('m' + '| ' + B0ard['mL'] + '|' + B0ard['mM'] + "|" + B0ard['mR'])
    print("-  -+-+-")
    print('b' + '| ' + B0ard['bL'] + '|' + B0ard['bM'] + "|" + B0ard['bR'])
    print("-  -----")
    print(" | L-M-R")

def movecheck(m0ve):
    for i in board.keys():
        if m0ve == i:
            if (board[i] == 'O') or (board[i] == 'X'):
                return "Occupied"
            return "free"
            
def playerMove(B0ard):
    while True:
        move = input("What is your move? ")
        if movecheck(move) == "Occupied" or move not in boardd: 
            print("Invalid move or occupied.")
            print()
            continue
        B0ard[move] = "O"
        return

someDict = {}
def valChecker(f, l):
    for x in valPos:
        if boardd[f][0] not in x:
            continue
        x.remove(boardd[f][0])
        if boardd[l][0] not in x:
            continue
        x.remove(boardd[l][0])
        if someDict[boardd[f] + boardd[l]][0] not in x:
            x.extend((boardd[f][0], boardd[l][0]))
            continue
        return True
    return False
def alter(x, y):
    try:
        someDict[boardd[x] + boardd[y]] = boardd[int(y * 2 - x)]
        if valChecker(x, y):
            return
        someDict[boardd[x] + boardd[y]] = boardd[int(x * 2 - y)]
        if valChecker(x, y):
            return
        del someDict[boardd[x] + boardd[y]]
    except IndexError:
        del someDict[boardd[x] + boardd[y]]
        return
    
for i in range(9):
    for o in range(i + 1, 9):
        valPos = [['t', 't', 't'], ['m', 'm', 'm'], ['b', 'b', 'b'], ['t', 'm', 'b']]
        a = (i + o) / 2
        if (i == 0 and o == 7) or (i == 1 and o == 3) or (i == 2 and o == 7):
            continue
        if a % 1 == 0:
            someDict.setdefault(boardd[i] + boardd[o], boardd[int((i + o) / 2)])
            if not valChecker(i, o):
                alter(i, o)
        else:
            someDict.setdefault(boardd[i] + boardd[o], boardd[(int(o * 2 - i)) % 9])
            if not valChecker(i, o):
                alter(i, o)
    
def middleBotMove():
    for i in range(9):
        if movecheck(boardd[i]) == "free":
            continue
        for o in range(i + 1, 9):
            if (movecheck(boardd[o]) == 'free') or (board[boardd[o]] != board[boardd[i]]):
                continue
            try:
                if movecheck(someDict[boardd[i] + boardd[o]]) == 'Occupied':
                    continue
                board[someDict[boardd[i] + boardd[o]]] = 'X'
                return True
            except KeyError:
                continue
def winCheck():
    for i in Row:
        win = ""
        for o in Column:
            win += board[i + o]
            if win == 'XXX':
                print('Bot Wins!')
                return True
    for o in Column:
        win = ''
        for i in Row:
            win += board[i + o]
            if win == 'XXX':
                print('Bot Wins!')
                return True
    if board['tL'] == board['mM'] == board['bR'] == 'X':
        print('Bot Wins!')
        return True
    if board['tR'] == board['mM'] == board['bL'] == 'X':
        print('Bot Wins!')
        return True
def gameDraw():
    idk = 0
    for i in board.values():
        if i != ' ':
            idk += 1
    if idk == 9:
        print('Draw!')
        return True
            
def botMove(B0ard):
    while True:
        print()
        Theboard(board)
        if winCheck() == True:
            return
        if gameDraw() == True:
            return
        playerMove(B0ard)
        for i in bmoves.keys():
            if middleBotMove() == True:
                break
            if movecheck('mM') == 'free':
                board['mM'] = 'X'
                break
            if movecheck(i) == "free":
                board[i] = 'X'
                bmoves[i] = 'X'
                break
       
def botFirst(B0ard):
    B0ard['tL'] = "X"
    botMove(B0ard)
    return
def playerFirst(B0ard):
    botMove(B0ard)
    return
   
def main():
    Theboard(board)
    while True:
        idk = input("\nWho goes first?\nType 'Player' if player\nType 'Bot' if bot\n: ")
        if idk.lower() == 'player':
            playerFirst(board)
            break
        elif idk.lower() == 'bot':
            botFirst(board)
            break
        else:
            print("\nMake sure you typed correctly!")
main()