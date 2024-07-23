import re



#Function to check if the move is valid
def check_bishop_move(x1, y1, x2, y2):
    if x1 == x2 or y1 == y2:
        return "NO"
    elif abs(ord(x1) - ord(x2)) == abs(int(y1) - int(y2)):
        return "YES"
    else:
        return "NO"

def check_king_move(x1, y1, x2, y2):
    if abs(ord(x1) - ord(x2)) <= 1 and abs(int(y1) - int(y2)) <= 1:
        return "YES"
    else:
        return "NO"

def check_knight_move(x1, y1, x2, y2):
    if ((abs(ord(x1) - ord(x2)) == 2 and abs(int(y1) - int(y2)) == 1) or
        (abs(ord(x1) - ord(x2)) == 1 and abs(int(y1) - int(y2)) == 2)):
        return "YES"
    else:
        return "NO"

def check_rook_move(x1, y1, x2, y2):
    if x1 == x2 or y1 == y2:
        return "YES"
    else:
        return "NO"

def check_queen_move(x1, y1, x2, y2):
    return check_bishop_move(x1, y1, x2, y2) or check_rook_move(x1, y1, x2, y2)



#Main
try:
    #Piece entered by the user
    piece = input("Enter the piece (bishop|knight|rook|king|queen): ").lower()
    if piece not in ['bishop', 'knight', 'rook', 'king', 'queen']:
        raise ValueError("Invalid piece")
    
    #Cell coordinates entered by the user
    cell1 = input("Enter the first cell coordinate (e.g. A1): ").lower()
    cell2 = input("Enter the second cell coordinate (e.g. H8): ").lower()

    #Check of validity of the cell coordinates
    if cell1 == cell2:
        raise ValueError("Piece can't move to the same cell")
    match1 = re.match(r"([a-h])(\d)", cell1)
    match2 = re.match(r"([a-h])(\d)", cell2)
    if (not match1) or (not match2):
        raise ValueError("Invalid cell coordinates")
    x1, y1 = match1.groups()
    x2, y2 = match2.groups()
    if (x1 not in 'abcdefgh') or (x2 not in 'abcdefgh') or (int(y1) < 1) or (int(y1) > 8) or (int(y2) < 1) or (int(y2) > 8):
        raise ValueError("Invalid cell coordinates")

    #Check of validity of the piece move
    if piece == 'bishop':
        print(check_bishop_move(x1, y1, x2, y2))
    elif piece == 'king':
        print(check_king_move(x1, y1, x2, y2))
    elif piece == 'knight':
        print(check_knight_move(x1, y1, x2, y2))
    elif piece == 'rook':
        print(check_rook_move(x1, y1, x2, y2))
    else:
        print(check_queen_move(x1, y1, x2, y2))

#Execute the exceptions
except ValueError as e:
    print("Error:", str(e))
except KeyboardInterrupt:
    print("User interrupted the program. WHY BRO, WHY DID YOU DO THAT?")
except Exception as e:
    print("An error occurred:", str(e))