import tkinter as tk
#a verifier

def stats_edit_window():
    stats_edit = tk.Tk()
    stats_edit.configure(bg='blue')
    stats_edit.geometry("1080x720")
    title_stats_edit = tk.Label(stats_edit, text="Modification des stats", bg="blue", font=("Arial", 20, "bold"),
                                fg="black")
    title_stats_edit.pack(side="top", pady=50)

    frame_edit_stats = tk.Frame(stats_edit, bg="orange")
    frame_edit_stats.pack()

    default = 10
    att = tk.Label(frame_edit_stats, text="Attaque", font=("Arial", 12), fg="black")
    att.grid(row="0", column="0", ipady=10, padx=10, pady=10)
    spinBox_att = tk.Spinbox(frame_edit_stats, from_=1, to=50, font=('arial', 12, 'normal'), bg='#F0F8FF', width=10)
    spinBox_att.grid(row="0", column="1", ipady=10, padx=10, pady=10)
    spinBox_att.delete(0)
    spinBox_att.insert(1, default)

    defe = tk.Label(frame_edit_stats, text="Defense", font=("Arial", 12), fg="black")
    defe.grid(row="1", column="0", ipady=10, padx=10, pady=10)
    spinBox_def = tk.Spinbox(frame_edit_stats, from_=1, to=50, font=('arial', 12, 'normal'), bg='#F0F8FF', width=10)
    spinBox_def.grid(row="1", column="1", ipady=10, padx=10, pady=10)
    spinBox_def.delete(0)
    spinBox_def.insert(1, default)

    agi = tk.Label(frame_edit_stats, text="Agilite", font=("Arial", 12), fg="black")
    agi.grid(row="2", column="0", ipady=10, padx=10, pady=10)
    spinBox_agi = tk.Spinbox(frame_edit_stats, from_=1, to=50, font=('arial', 12, 'normal'), bg='#F0F8FF', width=10)
    spinBox_agi.grid(row="2", column="1", ipady=10, padx=10, pady=10)
    spinBox_agi.delete(0)
    spinBox_agi.insert(1, default)

    luck = tk.Label(frame_edit_stats, text="Chance", font=("Arial", 12), fg="black")
    luck.grid(row="3", column="0", ipady=10, padx=10, pady=10)
    spinBox_luck = tk.Spinbox(frame_edit_stats, from_=1, to=50, font=('arial', 12, 'normal'), bg='#F0F8FF', width=10)
    spinBox_luck.grid(row="3", column="1", ipady=10, padx=10, pady=10)
    spinBox_luck.delete(0)
    spinBox_luck.insert(1, default)

    texte = tk.Frame(frame_edit_stats, bg="white")
    texte.grid(row=5, column=0, ipady=50, padx=50, pady=50, columnspan=4)

    mytext = tk.StringVar()
    mytext.set("dsgfsgsfgfgfgfgfd")
    mylab1 = tk.Label(texte, text="mytext", font=("Arial", 12), fg="red")
    mylab = tk.Label(stats_edit, textvariable=mytext, font=("Arial", 12), fg="red")
    mylab1.pack()
    mylab.pack()

    # def update():
    #     att_update = int(spinBox_att.get())
    #     defense_update = int(spinBox_def.get())
    #     agi_update = int(spinBox_agi.get())
    #     luck_update = int(spinBox_luck.get())
    #     nbr_restants = 50 - att_update - defense_update - agi_update - luck_update
    #     if nbr_restants < 0:
    #         mytext.set("Vous ne pouvez pas faire ca ! Le nombre de points maximum en tout est 50")
    #     else:
    #         mytext.set( "Il vous reste actuellement:" + str(nbr_restants ) + "points")
    #
    #
    # mise_a_jour = tk.Button(frame_edit_stats, text="Mettre a jour le nombre de points restants", command=update)
    # mise_a_jour.grid(row="4", column="1", ipady=10, padx=10, pady=10)
    #
    # editor.destroy()

# creation de la fenetre editor tkinter
editor = tk.Tk()
editor.configure(bg='#92cbf7')  # Couleur du background en bleu clair
editor.geometry("1080x720")  # Taille page

title2 = tk.Label(text="Vous etes dans l'editeur du jeu", bg='#92cbf7', font=("Arial", 20, "bold"), fg="black")
title2.pack(side="top", pady=50)

frame1 = tk.Frame(editor, bg='#fc9403')
frame1.pack()

photo_stats = tk.PhotoImage(file=r"./Plan-de-travail-6-150x150.png")

stats = tk.Button(frame1, text="Changer les valeurs des Stats", image=photo_stats, compound="top",
                  command=stats_edit_window)
stats.grid(row="0", column="0", ipady=10, padx=10, pady=10)

items = tk.Button(frame1, text="Ajouter des items et definir l'inventaire dans votre jeu")  # command=items_edit_window
items.grid(row="1", column="0", ipady=10, padx=10, pady=10)

dialogues = tk.Button(frame1, text="Ajouter les dialogues dans votre jeu")  # command=dialogues_edit_window
dialogues.grid(row="2", column="0", ipady=10, padx=10, pady=10)

editor.mainloop()
