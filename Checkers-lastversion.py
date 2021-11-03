import random
# Différentes conversions de données qui seront utiles par la suite.
def conversion_board_matrice(matrice):
    L = [[2, 2, 2, 2, 2], [2, 2, 2, 2, 2], [2, 2, 2, 2, 2], [2, 2, 2, 2, 2], [2, 2, 2, 2, 2]]
    for i in range(5):
        for j in range(5):
            if matrice[i][j] == ' ':
                L[i][j] = -1
            elif matrice[i][j] == '●':
                L[i][j] = 1
            elif matrice[i][j] == '◯':
                L[i][j] = 0
    return L


def conversion_matrice_board(board):
    l = [['', '', '', '', ''], ['', '', '', '', ''], ['', '', '', '', ''], ['', '', '', '', ''], ['', '', '', '', '']]
    for i in range(5):
        for j in range(5):
            if board[i][j] == -1:
                l[i][j] = ' '
            elif board[i][j] == 1:
                l[i][j] = '●'
            elif board[i][j] == 0:
                l[i][j] = '◯'
    return l


def cases_vides_pleines(board):
    l_plein = []
    l_vide = []
    for i in range(5):
        for j in range(5):
            if board[i][j] == '●':
                l_plein.append((chr(97 + i), j+1))
            elif board[i][j] == '◯':
                l_vide.append((chr(97 + i), j+1))
    return l_vide, l_plein


# Affichage:
# '◯' '●' ' '

def est_dans_grille(ligne,colone):
    ligne=ligne.upper()
    if ligne=='A' or ligne=='B' or ligne=='C' or ligne=='D' or ligne=='E':
        if colone=='1' or colone=='2' or colone=='3' or colone=='4' or colone=='5':
            
            return True
        return False
    return False


def test_est_dans_grille():
    assert True == est_dans_grille('A',3), "Ces coordonnées sont valides!"
    assert False == est_dans_grille('Z','9'), "Ces coordonnées ne sont pas valides !"
    assert False == est_dans_grille('T','5'), "Ces coordonnées ne sont pas valides!"
    assert False == est_dans_grille('B','-5'), "Ces coordonnées ne sont pas valides!"
    assert False == est_dans_grille('X','22'), "Ces coordonnées ne sont pas valides!"

def affichage(board):
    print('    1   2   3   4   5 \n  ┌---┬---┬---┬---┬---┐')
    char_ligne = 65
    for i in range(5):
        print(chr(char_ligne), '│ ', end='')
        char_ligne += 1
        for j in range(5):
            print(board[i][j], '│ ', end='')
        print('')
        if i == 4:
            print('  └---┴---┴---┴---┴---┘')
        else:
            print('  ├---┼---┼---┼---┼---┤')
    print("Joueur n°1: ●\nJoueur n°2: ◯")


def input_tour():
    while True:
        move = input("Donnez la case de la pièece que vous voulez jouer. ")
        if len(move) == 2:
            if move[0].lower() in "abcde" and move[1] in "12345":
                return move[0].lower(), int(move[1])
        else:
            print("Saisie invalide.")


def moves_possibles(case, board):
    l_vide, l_plein = cases_vides_pleines(board)
    moves = []
    for i in (case[1]-1, case[1], case[1]+1):
        for b in (chr(ord(case[0])-1), chr(ord(case[0])), chr(ord(case[0])+1)):
            if 0 < i < 6 and b in "abcde" and (b, i) not in l_vide and (b, i) not in l_plein:
                moves.append((b, i))
    return moves


def possible_eats(case, board):
    l_vide, l_plein = cases_vides_pleines(board)
    eats = []
    if case in l_vide:
        l_adverse = l_plein
    else:
        l_adverse = l_vide
    for i in (case[1]-1, case[1], case[1]+1):
        for b in (chr(ord(case[0])-1), chr(ord(case[0])), chr(ord(case[0])+1)):
            if 0 < i < 6 and b in "abcde" and (b, i) in l_adverse:
                if case[1] - 1 == i and case[1] - 2 > 0:
                    if chr(ord(case[0])-1) == b:
                        destination = (chr(ord(case[0])-2), case[1]-2)
                        cible = (chr(ord(case[0])-1), case[1]-1)
                        if destination not in l_vide and destination not in l_plein:
                            eats.append((cible, destination))
                    elif chr(ord(case[0])) == b:
                        destination = (b, case[1]-2)
                        cible = (b, case[1]-1)
                        if destination not in l_vide and destination not in l_plein:
                            eats.append((cible, destination))
                    elif chr(ord(case[0])+1) == b:
                        destination = (chr(ord(case[0])+2), case[1]-2)
                        cible = (chr(ord(case[0])+1), case[1]-1)
                        if destination not in l_vide and destination not in l_plein:
                            eats.append((cible, destination))
                elif case[1] == i:
                    if chr(ord(case[0])-1) == b:
                        destination = (chr(ord(case[0])-2), case[1])
                        cible = (chr(ord(case[0])-1), case[1])
                        if destination not in l_vide and destination not in l_plein:
                            eats.append((cible, destination))
                    elif chr(ord(case[0])+1) == b:
                        destination = (chr(ord(case[0])+2), case[1])
                        cible = (chr(ord(case[0])+1), case[1])
                        if destination not in l_vide and destination not in l_plein:
                            eats.append((cible, destination))
                elif case[1] + 1 == i and case[1] + 2 < 6:
                    if chr(ord(case[0])-1) == b:
                        destination = (chr(ord(case[0])-2), case[1]+2)
                        cible = (chr(ord(case[0])-1), case[1]+1)
                        if destination not in l_vide and destination not in l_plein:
                            eats.append((cible, destination))
                    elif chr(ord(case[0])) == b:
                        destination = (b, case[1]+2)
                        cible = (b, case[1]+1)
                        if destination not in l_vide and destination not in l_plein:
                            eats.append((cible, destination))
                    elif chr(ord(case[0])+1) == b:
                        destination = (chr(ord(case[0])+2), case[1]+2)
                        cible = (chr(ord(case[0])+1), case[1]+1)
                        if destination not in l_vide and destination not in l_plein:
                            eats.append((cible, destination))
    return eats


def mouvement_normal(pion, move, board):
    # On transforme le "board" en matrice, pour ensuite alterner ses valeurs, ainsi modifiant la position du pion qui
    # bouge à savoir, le supprimant de sa case de départ, et le mettant dans la case cible
    board = conversion_board_matrice(board)
    # i et j sont les informations positionelles du pion, avec lesquelles on accède à la matrice
    i = ord(pion[0]) - 97
    j = pion[1] - 1
    # On sauvegarde dans c le type de pion qu'il y avait dans la case de départ
    c = board[i][j]
    # On supprime le pion de la case de départ
    board[i][j] = -1
    # i et j sont les informations positionelles de la destination, avec lesquelles on accède à la matrice
    i = ord(move[0]) - 97
    j = move[1] - 1
    # On remet nore pion, à savoir c (qui sera ou vide ou plein, peu importe, cette information est précisément notre
    # variable "c", dans la destination, ainsi effectuant le mouvement
    board[i][j] = c
    # Dans le return suivant, on retransforme notre matrice, qui redevient notre nouvelle "board" avec le coup joué
    return conversion_matrice_board(board)


def mouvement_eat(pion, move, board):
    # On transforme le "board" en matrice, pour ensuite alterner ses valeurs, ainsi supprimant la pièce mangée, tout en
    # modifiant la position du pion qui mange, à savoir, le supprimant de sa case de départ, et le mettant dans la case
    # cible
    board = conversion_board_matrice(board)
    # i et j sont les informations positionelles du pion, avec lesquelles on accède à la matrice
    i = ord(pion[0]) - 97
    j = pion[1] - 1
    # On sauvegarde dans c le type de pion qu'il y avait dans la case de départ
    c = board[i][j]
    # On supprime le pion de la case de départ
    board[i][j] = -1
    cible = move[0]
    destination = move[1]
    # i et j sont les informations positionelles de la cible, avec lesquelles on accède à la matrice
    i = ord(cible[0]) - 97
    j = cible[1] - 1
    # On supprime la cible
    board[i][j] = -1
    # i et j sont les informations positionelles de la destination, avec lesquelles on accède à la matrice
    i = ord(destination[0]) - 97
    j = destination[1] - 1
    # On remet nore pion, à savoir c (qui sera ou vide ou plein, peu importe, cette information est précisément notre
    # variable "c", dans la destination, ainsi effectuant le mouvement
    board[i][j] = c
    # Dans le return suivant, on retransforme notre matrice, qui redevient notre nouvelle "board" avec le coup joué, on
    # retourne aussi la destination
    return conversion_matrice_board(board), destination

def threatened(case,board):
    i = case[0]
    j = case[1]
    for k in range(-1,2):
              for l in range(-1,2):
                   if -1 < i+k < 5 and -1 < b+l < 5:
                       if board[i+k][j+l] in l_plein and board[i-l][j-l] not in l_plein and board[i-l][j-l] not in l_vide:
                             return True 
    return False

def iaintell(board):
    l_vide, l_plein = cases_vides_pleines(board)
    p=0
    r=0
    m=-34567
    n=-34567
    initial=board
    for i in l_vide:
        if possible_eats(i,board):
            for a in possible_eats(i,board):
                p+=3
                board,i= mouvement_eat(i, a, board)
                for j in l_vide:
                    if threatened(j,board):
                        p-=1
                for o in l_plein:
                    if threatened(j,board):
                        p+=2           
                if p>m:
                    m=p  
            
        else:
            for b in moves_possibles(i,board):
                r+=1
                board = mouvement_normal(i, b, board)
                for i in l_vide:
                    if threatened(i,board):
                        r-=1
                for y in l_plein:
                    if threatened(y,board):
                        r+=2
                if r>n:
                    n=r         
        board=initial

    if n>m:
        move=b
    else:
        move=a[1]
    return move
            
            
    

lol = [[-1, -1, -1, -1, -1], [-1, 0, 0, 0, -1], [-1, 0, 1, 0, -1], [-1, 0, 0, 0, -1], [-1, -1, -1, -1, -1]]
board_debut = [[1, 1, 1, 0, 0], [1, 1, 1, 0, 0], [1, 1, -1, 0, 0], [1, 1, 0, 0, 0], [1, 1, 0, 0, 0]]
board_milieu = [[0, -1, -1, -1, 1], [1, -1, 1, 0, -1], [1, 1, 0, -1, -1], [-1, 1, 0, 0, 1], [1, -1, 0, 0, 1]]
board_fin = [[-1, -1, -1, -1, -1], [-1, -1, 1, -1, -1], [-1, -1, 0, 0, -1], [-1, -1, -1, -1, -1], [-1, -1, -1, -1, -1]]
# affichage(conversion_matrice_board(lol))
# print(possible_eats(("c", 3), conversion_matrice_board(lol)))
# print(moves_possibles(("c", 2), conversion_matrice_board(lol)))



b = -1
while b != 0 and b != 1 and b != 2:
    print("BIENVENUE AU JEU ACORES:")
    print('\n')
    print("       MENU:")
    print("\n")
    print("Quelle disposition de grille voulez vous?")
    print("\n")
    print("   0 pour début de partie")
    print("\n")        
    print("   1 pour milieu de partie")
    print("\n")        
    print("   2 pour fin de partie")
    b = int(input())
if b == 0:
    board = board_debut
elif b ==1:
    board = board_milieu
else:
    board = board_fin

c = -1
while c != 0 and c != 1 and c !=2:
    print("Quel mode de jeu voulez-vous?")
    print("\n")
    print("   0 pour joueur vs. joueur")
    print("\n")
    print("   1 pour joueur vs. IA aléatoire")
    print("\n")
    print("   2 pour joueur vs. IA intelligente")
    c = int(input())
if c == 0:
    # Simple initialisation d'informations utiles par la suite
    board = conversion_matrice_board(board)
    l_vide, l_plein = cases_vides_pleines(board)
    j = 1
    while cases_vides_pleines(board)[0] and cases_vides_pleines(board)[1]:
        affichage(board)
        # Boucle qui ne s'arrête que lorsqu'il n'y a plus de pièces d'un certain type, i.e à la fin de la partie
        l_vide, l_plein = cases_vides_pleines(board)
        playable = False  # Indiquera si on peut jouer la pièce ou non.
        eats, moves, pion = 1, 1, 1  # Pour éviter un Warning (n'ajoute rien à la logique du code)
        # On identifie ici les pièces qu'on peut jouer dépendant du joueur actuel
        if j == 1:
            l_actuel = l_plein
            print("tour du joueur 1 (pièces pleines).")
        else:
            l_actuel = l_vide
            print("tour du joueur 2 (pièces vides).")
        while not playable:
            # On vérifie que le choix de l'utilisateur est jouable
            pion = input_tour()
            if pion not in l_actuel:
                print("Case sélectionnée non valable. Veuillez en sélectionner une autre.")
            else:
                # On cherche l'existence ou non de moves ou "eats" possibles
                moves = moves_possibles(pion, board)
                eats = possible_eats(pion, board)
                if not moves and not eats:
                    # Ici, on n'a trouvé aucune possibilité
                    print("Ce pion ne peut rien faire. Veuillez en sélectionner un autre.")
                else:
                    # Finalement ici, le pion est jouable
                    playable = True
        move = -1
        eats_destinations = []
        for i in eats:
            # Pour les eats, comme le joueur décide de son coup simplement en décrétant la destination, on
            # sauvegarde les destinations qu'on atteint pour chaque eat faisable, en sachant que chaque eat a sa
            # propre destination unique, on comparera ce que nous donne l'utilisateur avec ces derniers pour
            # ensuite déterminer la pièce mangée.
            eats_destinations.append(i[1])
        while move not in moves and move not in eats_destinations:
            # Boucle pour déterminer la validité du coup de l'utilisateur, on compare la destination qu'il nous
            # donne avec toutes celles possibles, à savoir celles dans moves et eats_destinations
            move = input("Donnez la destination de la pièece que vous voulez jouer. ")
            if len(move) == 2:
                if move[0].lower() in "abcde" and move[1] in "12345":
                    move = move[0].lower(), int(move[1])
                if move not in moves and move not in eats_destinations:
                    print("Mouvement invalide.")
            else:
                print("Saisie invalide.")
        if move in moves:
            # Si c'est un simple "move", on appelle la fonction créée pour celà, elle s'occupe de toute la suite,
            # à savoir même la mise à jour du "board"
            board = mouvement_normal(pion, move, board)
        elif move in eats_destinations:
            for i in eats:
                # Comme dit avant, ici on retrouve tout le coup, à savoir le pion mangé et la destination de celui
                # qui le mange à partir seulement de la destination, ces informations nous sont vitales après tout
                if move == i[1]:
                    move = i
                    break
            # Ici, nous avons un "eat", on appelle la fonction créée pour cela, elle s'occupe de toute la suite,
            # à savoir même la mise à jour du "board"
            board, pion = mouvement_eat(pion, move, board)
            while possible_eats(pion, board):
                # Avec la nouvelle "board", on recommence une boucle qui s'assure que tant qu'un enchaînement est
                # possible, on réitère le procédé pour manger les pièces, avec cette fois un choix pour
                # l'utilisateur, bien évidemment, comme on a déjà mis à jour le "board" à travers le premier "eat"
                # en utilisant "board" pour possible_eats, on utilise la nouvelle, à savoir celle après avoir mangé
                # ce qui est en accord avec notre logique.
                affichage(board)
                decision = input("Vous pouvez enchainer un coup! Voulez-vous le faire? Oui/Non: ")
                if decision.lower() == "oui":
                    eats_destinations = []
                    eats = possible_eats(pion, board)
                    for i in eats:
                        eats_destinations.append(i[1])
                        # Meme logique de sauvegarde des destinations possibles
                    move = -1
                    while move not in eats_destinations:
                        move = input("Donnez la destination de la pièece que vous voulez jouer. ")
                        if len(move) == 2:
                            if move[0].lower() in "abcde" and move[1] in "12345":
                                move = move[0].lower(), int(move[1])
                            if move not in eats_destinations:
                                print("Mouvement invalide.")
                        else:
                            print("Saisie invalide.")
                    for i in eats:
                        # encore une fois, on retrouve notre pion à travers les destinations
                        if move == i[1]:
                            move = i
                            break
                    # Et on réeffectue le eat, avec bien sûr une mise à jour du "board"
                    board, pion = mouvement_eat(pion, move, board)

        # Ici on change de joueur après que son coup soit effectué
        if j == 1:
            j = 2
        else:
            j = 1

    # Etant donné qu'on soit maintenant hors notre PREMIÈRE boucle, l'un des deux types de pièces a disparu, on
    # cherche ici lequel, et on déclare le gagnant accordèment
    affichage(board)
    if l_vide:
        print("Victoire des pièces pleines.")
    else:
        print("Victoire des pièces vides.")
elif c==1:
    board = conversion_matrice_board(board)
    l_vide, l_plein = cases_vides_pleines(board)
    j = 1
    while cases_vides_pleines(board)[0] and cases_vides_pleines(board)[1]:
        # Boucle qui ne s'arrête que lorsqu'il n'y a plus de pièces d'un certain type, i.e à la fin de la partie
        affichage(board)
        l_vide, l_plein = cases_vides_pleines(board)
        playable = False  # Indiquera si on peut jouer la pièce ou non.
        eats, moves, pion = 1, 1, 1  # Pour éviter un Warning (n'ajoute rien à la logique du code)
        # On identifie ici les pièces qu'on peut jouer dépendant du joueur actuel
        if j == 1:
            l_actuel = l_plein
            print("tour du joueur 1 (pièces pleines).")
        else:
            l_actuel = l_vide
            print("tour de l'IA (pièces vides).")
        
        while not playable:
            # On vérifie que le choix de l'utilisateur est jouable
            if j==1:
                pion = input_tour()
            else:
                pion=random.choice(l_actuel)
                print('le pion choisi est',pion)
            
            if pion not in l_actuel:
                print("Case sélectionnée non valable. Veuillez en sélectionner une autre.")
            else:
                # On cherche l'existence ou non de moves ou "eats" possibles
                moves = moves_possibles(pion, board)
                eats = possible_eats(pion, board)
                if not moves and not eats:
                    # Ici, on n'a trouvé aucune possibilité
                    if j==1:
                        print("Ce pion ne peut rien faire. Veuillez en sélectionner un autre.")
                    else:
                        pion=random.choice(l_actuel)
                else:
                    # Finalement ici, le pion est jouable
                    playable = True
        move = -1
        eats_destinations = []
        for i in eats:
            eats_destinations.append(i[1])
        while move not in moves and move not in eats_destinations:
            # Boucle pour déterminer la validité du coup de l'utilisateur, on compare la destination qu'il nous
            # donne avec toutes celles possibles, à savoir celles dans moves et eats_destinations
            if j==1:
                move = input("Donnez la destination de la pièece que vous voulez jouer. ")
            else:
                liste=moves+eats
                move=random.choice(liste)
                print('le deplacement choisi est',move)
            if j==1:
                if len(move) == 2:
                    if move[0].lower() in "abcde" and move[1] in "12345":
                        move = move[0].lower(), int(move[1])
                    if move not in moves and move not in eats_destinations:
                        print("Mouvement invalide.")
                else:  
                    print("Saisie invalide.")
        if move in moves:
            # Si c'est un simple "move", on appelle la fonction créée pour celà, elle s'occupe de toute la suite,
            # à savoir même la mise à jour du "board"
            board = mouvement_normal(pion, move, board)  
        elif move in eats_destinations:
            for i in eats:
                # Comme dit avant, ici on retrouve tout le coup, à savoir le pion mangé et la destination de celui
                # qui le mange à partir seulement de la destination, ces informations nous sont vitales après tout
                if move == i[1]:
                    move = i
                    break    
            board, pion = mouvement_eat(pion, move, board)
            while possible_eats(pion, board):
                # Avec la nouvelle "board", on recommence une boucle qui s'assure que tant qu'un enchaînement est
                # possible, on réitère le procédé pour manger les pièces, avec cette fois un choix pour
                # l'utilisateur, bien évidemment, comme on a déjà mis à jour le "board" à travers le premier "eat"
                # en utilisant "board" pour possible_eats, on utilise la nouvelle, à savoir celle après avoir mangé
                # ce qui est en accord avec notre logique.
                affichage(board)
                decision = input("Vous pouvez enchainer un coup! Voulez-vous le faire? Oui/Non: ")
                if decision.lower() == "oui":
                    eats_destinations = []
                    eats = possible_eats(pion, board)
                    for i in eats:
                        eats_destinations.append(i[1])
                        # Meme logique de sauvegarde des destinations possibles
                    move = -1
                    while move not in eats_destinations:
                        move = input("Donnez la destination de la pièece que vous voulez jouer. ")
                        if len(move) == 2:
                            if move[0].lower() in "abcde" and move[1] in "12345":
                                move = move[0].lower(), int(move[1])
                            if move not in eats_destinations:
                                print("Mouvement invalide.")
                        else:
                            print("Saisie invalide.")
                    for i in eats:
                        # encore une fois, on retrouve notre pion à travers les destinations
                        if move == i[1]:
                            move = i
                            break
                    board, pion = mouvement_eat(pion, move, board)
                    # Et on réeffectue le eat, avec bien sûr une mise à jour du "board"
                    

        if j == 1:
            j = 2
        else:
            j = 1  
    affichage(board)
    if l_vide:
        print("Victoire des pièces pleines.")
    else:
        print("Victoire des pièces vides.")

elif c==2:
    board = conversion_matrice_board(board)
    l_vide, l_plein = cases_vides_pleines(board)
    j = 1
    while cases_vides_pleines(board)[0] and cases_vides_pleines(board)[1]:
        # Boucle qui ne s'arrête que lorsqu'il n'y a plus de pièces d'un certain type, i.e à la fin de la partie
        affichage(board)
        l_vide, l_plein = cases_vides_pleines(board)
        playable = False  # Indiquera si on peut jouer la pièce ou non.
        eats, moves, pion = 1, 1, 1  # Pour éviter un Warning (n'ajoute rien à la logique du code)
        # On identifie ici les pièces qu'on peut jouer dépendant du joueur actuel
        if j == 1:
            l_actuel = l_plein
            print("tour du joueur 1 (pièces pleines).")
        else:
            l_actuel = l_vide
            print("tour de l'IA (pièces vides).")
        
        while not playable:
            # On vérifie que le choix de l'utilisateur est jouable
            if j==1:
                pion = input_tour()
               
                if pion not in l_actuel:
                    print("Case sélectionnée non valable. Veuillez en sélectionner une autre.")
                else:
                    # On cherche l'existence ou non de moves ou "eats" possibles
                    moves = moves_possibles(pion, board)
                    eats = possible_eats(pion, board)
                    if not moves and not eats:
                        # Ici, on n'a trouvé aucune possibilité
                        print("Ce pion ne peut rien faire. Veuillez en sélectionner un autre.")
                    else:
                        # Finalement ici, le pion est jouable
                        playable = True   
            else:
                playable=True
        move = -1
        eats_destinations = []
        for i in eats:
            eats_destinations.append(i[1])
        while move not in moves and move not in eats_destinations:
            # Boucle pour déterminer la validité du coup de l'utilisateur, on compare la destination qu'il nous
            # donne avec toutes celles possibles, à savoir celles dans moves et eats_destinations
            if j==1:
                move = input("Donnez la destination de la pièece que vous voulez jouer. ")
 
            if j==1:
                if len(move) == 2:
                    if move[0].lower() in "abcde" and move[1] in "12345":
                        move = move[0].lower(), int(move[1])
                    if move not in moves and move not in eats_destinations:
                        print("Mouvement invalide.")
                else:  
                    print("Saisie invalide.")
        if j!=1:
            move=iaintell(board)
        if move in moves:
            # Si c'est un simple "move", on appelle la fonction créée pour celà, elle s'occupe de toute la suite,
            # à savoir même la mise à jour du "board"
            board = mouvement_normal(pion, move, board)  
        elif move in eats_destinations:
            for i in eats:
                # Comme dit avant, ici on retrouve tout le coup, à savoir le pion mangé et la destination de celui
                # qui le mange à partir seulement de la destination, ces informations nous sont vitales après tout
                if move == i[1]:
                    move = i
                    break    
            board, pion = mouvement_eat(pion, move, board)
            while possible_eats(pion, board):
                # Avec la nouvelle "board", on recommence une boucle qui s'assure que tant qu'un enchaînement est
                # possible, on réitère le procédé pour manger les pièces, avec cette fois un choix pour
                # l'utilisateur, bien évidemment, comme on a déjà mis à jour le "board" à travers le premier "eat"
                # en utilisant "board" pour possible_eats, on utilise la nouvelle, à savoir celle après avoir mangé
                # ce qui est en accord avec notre logique.
                affichage(board)
                decision = input("Vous pouvez enchainer un coup! Voulez-vous le faire? Oui/Non: ")
                if decision.lower() == "oui":
                    eats_destinations = []
                    eats = possible_eats(pion, board)
                    for i in eats:
                        eats_destinations.append(i[1])
                        # Meme logique de sauvegarde des destinations possibles
                    move = -1
                    while move not in eats_destinations:
                        move = input("Donnez la destination de la pièece que vous voulez jouer. ")
                        if len(move) == 2:
                            if move[0].lower() in "abcde" and move[1] in "12345":
                                move = move[0].lower(), int(move[1])
                            if move not in eats_destinations:
                                print("Mouvement invalide.")
                        else:
                            print("Saisie invalide.")
                    for i in eats:
                        # encore une fois, on retrouve notre pion à travers les destinations
                        if move == i[1]:
                            move = i
                            break
                    board, pion = mouvement_eat(pion, move, board)

        if j == 1:
            j = 2
        else:
            j = 1  
    affichage(board)
    if l_vide:
        print("Victoire des pièces pleines.")
    else:
        print("Victoire des pièces vides.")
                   