
def print_board( lst):
    lst = reverse_lst(lst)
    print("\n")
    for r in range(len(lst[0])):
        print(f" ({r + 1})", end="")
    print("\n")
    # Afficher la grille
    for r in range(len(lst)-1,-1,-1):
        print('|', end="")
        for c in range(len(lst[0])):
            print(f"  {lst[r][c]} |", end="")
        print("\n")
    print(f"{'-' * 42}\n")

def reverse_lst(lst):
    nLst = []
    for i in lst:
        nLst.insert(0,i)

    return nLst

def check_if_winner(val1 , val2 , lst):
    lst = reverse_lst(lst)
    
    val1 = len(lst)-val1-1
    
    val = lst[val1][val2]
    if(val=='-'):
        return False
    t1 = val1
    t2 = val2
 
    count = -1
    #vérifier la colonne ci-dessous
    while val1<len(lst):
        if(val==lst[val1][val2]):
            
            count+=1
        else:
            break
        val1+=1

    if(count==3):
        return True
    else:
        count = -1
    #vérifier la colonne ci-dessus
    val1 = t1 
    val2 = t2
    while val1>=0:
        if(val==lst[val1][val2]):
            count+=1
        else:
            break
        val1-=1
   
    if(count==3):
        return True
    else:
        count = -1
    #vérifier la rangée en avant
    val1 = t1 
    val2 = t2
    while val2<len(lst[0]):
        if(val==lst[val1][val2]):
            count+=1
        else:
            break
        val2+=1
  
    if(count==3):
        return True
    else:
        count = -1
    #vérifier la rangée en arrière
    val1 = t1 
    val2 = t2
    while val1<len(lst):
        if(val==lst[val1][val2]):
            count+=1
        else:
            break
        val2-=1
    
    if(count==3):
        return True
    else:
        count = -1
    val1 = t1 
    val2 = t2
    #diagonal vers le coin gauche
    while val1>=0 and val2>=0:
        if(val==lst[val1][val2]):
            count+=1
        else:
            break
        val1-=1
        val2-=1
    if(count==3):
        return True
    else:
        count = -1
    val1 = t1
    val2 = t2
    
    #diagonal vers le coin gauche
    while val1>=0 and 0<=val2<len(lst) :
        
        if(val==lst[val1][val2]):
            count+=1
        else:
            break
        val1-=1
        val2+=1
    if(count==3):
        return True
    else:
        count = -1
    val1 = t1
    val2 = t2
    #diagonal vers le coin droit
    while val1<len(lst[0]) and val2<len(lst[0]):
        if(val==lst[val1][val2]):
            count+=1
        else:
            break
        val1+=1
        val2+=1
    if(count==3):
        return True
    else:
        count = -1
    val1 = t1
    val2 = t2

    while val1<len(lst) and val2<len(lst):
        if(val==lst[val1][val2]):
            count+=1
        else:
            break
        val1+=1
        val2-=1
    if(count==3):
        return True
    else:
        count = -1
    return False



def turn(column , lst , t , last_move ) :
        # Colonne du jeton (vérifie si la colonne est libre)
        for i in range(len(lst)-1, -1, -1):
            if lst[i][column] == '-':
                lst[i][column] = which_turn(t)
                last_move = [i, column]

                t += 1
                return True , t , last_move

        return False , t , last_move

def which_turn(turns):
        players = ['X', 'O']
        return players[turns % 2]

lst = [['-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-'],['-', '-', '-', '-', '-']]
def play():
    turns = 0
    last_move = [1,1]
    game_over = False
    while not game_over:
        
        

        valid_move = False
        print_board(lst)
        while not valid_move:
            user_move = input(f"{which_turn(turns)}'s turn - pick a column (1-{len(lst)}): ")
        
            try:
                valid_move , turns , last_move  = turn(int(user_move) - 1 , lst , turns , last_move)
            except:
                print(f"please choose number between 1 and {len(lst[0])}")
        
        game_over = check_if_winner(last_move[0] ,last_move[1] , lst)
    print_board(lst)
    print(lst[last_move[0]][last_move[1]],"is Winner ")



if __name__ == '__main__':
    play()