from tkinter import *
from grille_de_jeu import *
from pieces_etats import *
from fonctions_jeu import *
import operator


users_scores=[('a',10),('b',20),('c',30)]

def affichage_grille():

    global score
    global nombre_lignes_supprimees
    score = 0
    nombre_lignes_supprimees = 0
    root = Tk()
    root.title("Tetris")
    top = Toplevel()
    root.config(bg = 'grey')
    label_choix_niveau=LabelFrame(root, text="CHOOSE YOUR LEVEL:", bg = 'grey', fg = '#424949', font=("Helvetica", "10", "bold"))
    label_choix_niveau.grid()
    set_niveau= Listbox(label_choix_niveau, height=7, fg='white', bg='#424949', selectmode='SINGLE', selectbackground = 'grey')
    set_niveau.insert(1,"Level 0")
    set_niveau.insert(2,"Level 1")
    set_niveau.insert(3,"Level 2")
    set_niveau.insert(4,"Level 3")
    set_niveau.insert(5,"Level 4")
    set_niveau.insert(6,"Level 5")
    set_niveau.insert(7,"Level 6")
    set_niveau.grid()

    global niveau
    niveau = 0

    global grille
    grille = cree_grille()
    global grille_graphique
    grille_graphique = [[0 for _ in range(10)] for _ in range(22)]

    for i in range(22):
            for j in range(10):
                case = Frame(top, bg = 'black', relief = 'raised', bd = 0.5, width = 30, height = 30)
                case.grid(row = i, column = j)
                grille_graphique[i][j] = case

    global piece
    piece = generer_piece()

    #Fenetre score
    left_frame = Toplevel()
    font_tetrix = 'Helvetica'
    width_num=10
    height_num=1
    number_background_color="#424949"
    frame_background_color="grey"

    left_frame.config(background=frame_background_color, highlightthickness=1,)

    label_score = Label(left_frame, text="SCORE", fg="#424949", font=font_tetrix, background="grey",width=width_num+3, height=height_num)
    label_score.grid(row=0,column=0)

    label_score_num = Label(left_frame, text=str(score), fg="white", background=number_background_color,width=width_num, height=height_num)
    label_score_num.grid(row=1,column=0)


    label_level = Label(left_frame, text="LEVEL", fg="#424949", font=font_tetrix, background=frame_background_color,width=width_num+3, height=height_num)
    label_level.grid(row=2,column=0)

    label_level_num = Label(left_frame, text=str(niveau), fg="white", background=number_background_color,width=width_num, height=height_num)
    label_level_num.grid(row=3,column=0)


    label_line = Label(left_frame, text="LINES", fg="#424949", font=font_tetrix, background=frame_background_color,width=width_num+3, height=height_num)
    label_line.grid(row=4,column=0)

    label_line_num = Label(left_frame, text=str(nombre_lignes_supprimees), fg="white", background=number_background_color,width=width_num, height=height_num)
    label_line_num.grid(row=5,column=0)

    label_vide = Label(left_frame, text="", background=frame_background_color)
    label_vide.grid(row=6,column=0)

    ##Fonctions
    def mise_a_jour_grille_graph():
            global piece
            global grille_graphique
            global grille

            grille_provisoire = copy.deepcopy(grille)
            forme = piece[2]
            for c in coordonees(piece):
                grille_provisoire[c[0]][c[1]] = forme + 1
            for i in range(22):
                for j in range(10):
                    grille_graphique[i][j].config(bg = piece_coleur[grille_provisoire[i][j]])

    def KeyPressed(event):
        global piece
        global grille_graphique
        d = event.keysym
        piece = deplacement_piece(grille, piece, d)
        mise_a_jour_grille_graph()

    def display_score_board():
        # permet d'ouvrir la fenêtre des scores
        # parametres: None
        # renvoie: None
        score_board_window=Toplevel(root,bg='grey')
        score_board_window.geometry()
        score_board=Message(score_board_window,bg='grey', fg='white', text="Score Board",font=("Times", "24", "bold"))
        score_board.grid(row=0, column=1)
        score_board.config(anchor=N)
        users_scores.sort(key=operator.itemgetter(1))
        n_1_user=Message(score_board_window,bg='grey', fg="#72f1f1",text= "First: "+str(users_scores[len(users_scores)-1][0]))
        n_1_score=Message(score_board_window,bg='grey', fg="#72f1f1",text= users_scores[len(users_scores)-1][1])
        n_2_score=Message(score_board_window,bg='grey',fg="#2046f0",text= users_scores[len(users_scores)-2][1])
        n_2_user=Message(score_board_window,bg='grey',fg='#2046f0',text= "Second: "+str(users_scores[len(users_scores)-2][0]))
        n_3_score=Message(score_board_window,bg='grey',fg="#e2972f",text= users_scores[len(users_scores)-3][1])
        n_3_user=Message(score_board_window,bg='grey',fg="#e2972f",text= "Third: "+str(users_scores[len(users_scores)-3][0]))
        n_1_user.grid(row=2,column=1)
        n_1_score.grid(row=3,column=1)
        n_2_user.grid(row=4,column=0)
        n_2_score.grid(row=5,column=0)
        n_3_user.grid(row=4,column=2)
        n_3_score.grid(row=5,column=2)
        score_board_window.grid()

    global next_piece
    next_piece = generer_piece()

    right_frame = Toplevel()


    right_frame.config(background="#424949", relief ='raised', highlightthickness=1)

    label_next = LabelFrame(right_frame, text="NEXT", labelanchor = 'n', fg="white", font='Helvetica', background="#424949")
    label_next.grid(row=0,column=0)

    global grille_graphique2
    global grille_provisoire2
    grille_graphique2 = [[0 for _ in range(4)] for _ in range(4)]
    grille_provisoire2 = [[0 for _ in range(4)] for _ in range(4)]


    for i in range(4):
        for j in range(4):
            case = Frame(label_next, bg = "#424949", width = 40, height = 40)
            case.grid(row = i+1, column = j)
            grille_graphique2[i][j] = case

    def update_next_piece():
        global next_piece
        global grille_graphique2
        global grille_provisoire2
        forme=next_piece[2]
        for i in range(4):
            for j in range(4):
                grille_provisoire2[i][j] = 0
        for c in coordonees(next_piece):
             grille_provisoire2[c[0]][c[1]-3] = forme+1
        for i in range(4):
            for j in range(4):
                grille_graphique2[i][j].config(bg = '#424949', bd = 0)
                if grille_provisoire2[i][j]!=0:
                    grille_graphique2[i][j].config(bg = piece_coleur[grille_provisoire2[i][j]],relief = 'groove',bd = 0.5)

    update_next_piece()

    def game_over():
        Label(left_frame, text = 'GAME OVER', bg = 'grey', fg = 'red', font = ('Helvetica', 20, 'bold')).grid()
        if user_name.get()!='':
                users_scores.append((user_name.get(),score))

    def start_game():
        global grille
        global piece
        global niveau
        global nombre_lignes_supprimees
        global score
        global next_piece
        niveau_initial = set_niveau.curselection()[0]

        if not test_fin_jeu(grille):
            mise_a_jour_grille_graph()
            piece=deplacement_piece(grille,piece,'Down')
            mise_a_jour_grille_graph()
            if collision(piece, grille)[0]:
                grille = collision(piece, grille)[1]
                traitement = traitement_grille(grille, score, nombre_lignes_supprimees)
                grille = traitement[0]
                score = traitement[1]
                nombre_lignes_supprimees = traitement[2]
                piece = copy.deepcopy(next_piece)
                next_piece = generer_piece()
                update_next_piece()
                mise_a_jour_grille_graph()
                label_line_num.config(text = str(nombre_lignes_supprimees))
                label_score_num.config(text = str(score))
                label_level_num.config(text = str(niveau))
            niveau = niveau_initial + nombre_lignes_supprimees // 10
            top.after(horloge(niveau), start_game)
        else:
            game_over()



    start = Button(root, text = 'START GAME', activebackground = "blue", command = start_game, bg = 'grey')
    start.grid(row = 2)
    quit_button = Button(root, text="QUIT", activebackground = "blue", fg="#8D021F",command=quit, bg = 'grey')
    quit_button.grid(row = 3)
    user_name_title=Message(root, bg='grey', fg='white', text="Please enter a username if you want to save your score: ", anchor="e")
    user_name=Entry(root, textvariable= StringVar)
    Score_button=Button(root, text="Show Scoreboard", bg='grey', fg='white', relief= "raised", anchor="center",command=display_score_board)
    user_name_title.grid(row=4)
    user_name.grid(row=5)
    Score_button.grid(row=6)
    top.bind('<Key>', KeyPressed)
    root.mainloop()
    top.mainloop()
    left_frame.mainloop()
    right_frame.mainloop()



affichage_grille()

def Save() :
        ###Fonction pour sauvegarder la grille
        file=open("Save.txt","w+")
        file.seek(0)
        file.truncate()
        file.write(str(game_grid))
def Load() :
    ### Fonction pour charger la sauvegarde
    global game_grid
    file=open("Save.txt","r+")
    game_grid=str_to_list(file.read())
    display_and_update_graphical_grid()

def Cancel() :
    ### Fonction pour annuler le dernier coup joué
    global game_grid
    global game_grid_copy
    game_grid= copy.deepcopy(game_grid_copy)
    display_and_update_graphical_grid()