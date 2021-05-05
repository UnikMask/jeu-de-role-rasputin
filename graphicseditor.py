import tkinter as tk
import csv
att_update=0
defense_update=0
agi_update=0
luck_update=0

def stats_edit_window():
    stats_edit = tk.Tk()
    stats_edit.configure(bg='#e9d49c')
    stats_edit.geometry("1080x720")
    title_stats_edit = tk.Label(stats_edit, text="Modification des stats", bg="#e9d49c", font=("Arial", 20, "bold"), fg="black")
    title_stats_edit.pack(side="top", pady=50)

    frame_edit_stats = tk.Frame(stats_edit, bg="orange")
    frame_edit_stats.pack()

    frame_update = tk.Frame(frame_edit_stats)
    frame_update.grid(row="5", column="0", ipady=50, padx=50, pady=50)
    update_text = tk.StringVar(frame_update)
    update_text.set(" ")
    tk.Label(frame_edit_stats, textvariable = update_text, font=("Arial", 12), fg="red").grid(row="5", column="0", ipady=50, padx=50, pady=50)

    def confirmation():
        #with open(../jeu_maingame/variables_saves.csv) as csvfile:
            #writer = csv.write(csvfile)
            #writer.writerow(att_update)
            #writer.writerow(defense_update)
            #writer.writerow(agi_update)
            #writer.writerow(luck_update)
        stats_edit.withdraw()
        editor.deiconify()

    confirm = tk.Button(frame_edit_stats, text="Confirmer vos points de stats ?", font=("Arial", 16), fg="green", command=confirmation)
    confirm.grid(row=5, column=1, ipady=50, padx=50, pady=50)

    def update(): #Update nbr des points restants a mettre dans les stats
        att_update = int(spinBox_att.get())
        defense_update = int(spinBox_def.get())
        agi_update = int(spinBox_agi.get())
        luck_update = int(spinBox_luck.get())
        nbr_restants = 50 - att_update - defense_update - agi_update - luck_update
        if nbr_restants < 0:
            update_text.set("Vous ne pouvez pas faire ca ! Le nombre de points maximum en tout est 50")
            confirm.config(state="disabled", takefocus=0)
        else:
            update_text.set("Il vous reste actuellement: " + str(nbr_restants) + " points")
            confirm.config(state="active")

    default = 10

    #Creation des spinbox pour les stats
    att = tk.Label(frame_edit_stats, text="Attaque", font=("Arial", 12), fg="black")
    att.grid(row="0", column="0", ipady=10, padx=10, pady=10)
    spinBox_att = tk.Spinbox(frame_edit_stats, from_=1, to=50, font=('arial', 12, 'normal'), bg='#F0F8FF', width=10, command=update)
    spinBox_att.grid(row="0", column="1", ipady=10, padx=10, pady=10)
    spinBox_att.delete(0)
    spinBox_att.insert(1, default)
    spinBox_att.config(state="readonly")

    defe = tk.Label(frame_edit_stats, text="Defense", font=("Arial", 12), fg="black")
    defe.grid(row="1", column="0", ipady=10, padx=10, pady=10)
    spinBox_def = tk.Spinbox(frame_edit_stats, from_=1, to=50, font=('arial', 12, 'normal'), bg='#F0F8FF', width=10, command=update)
    spinBox_def.grid(row="1", column="1", ipady=10, padx=10, pady=10)
    spinBox_def.delete(0)
    spinBox_def.insert(1, default)
    spinBox_def.config(state="readonly")

    agi = tk.Label(frame_edit_stats, text="Agilite", font=("Arial", 12), fg="black")
    agi.grid(row="2", column="0", ipady=10, padx=10, pady=10)
    spinBox_agi = tk.Spinbox(frame_edit_stats, from_=1, to=50, font=('arial', 12, 'normal'), bg='#F0F8FF', width=10, command=update)
    spinBox_agi.grid(row="2", column="1", ipady=10, padx=10, pady=10)
    spinBox_agi.delete(0)
    spinBox_agi.insert(1, default)
    spinBox_agi.config(state="readonly")

    luck = tk.Label(frame_edit_stats, text="Chance", font=("Arial", 12), fg="black")
    luck.grid(row="3", column="0", ipady=10, padx=10, pady=10)
    spinBox_luck = tk.Spinbox(frame_edit_stats, from_=1, to=50, font=('arial', 12, 'normal'), bg='#F0F8FF', width=10, command=update)
    spinBox_luck.grid(row="3", column="1", ipady=10, padx=10, pady=10)
    spinBox_luck.delete(0)
    spinBox_luck.insert(1, default)
    spinBox_luck.config(state="readonly")

    editor.withdraw()

def items_edit_window():
    items_edit = tk.Tk()
    items_edit.configure(bg="#e9d49c")
    items_edit.geometry("1080x720")
    tk.Label(items_edit, text="Ajouter des objets dans votre jeu", bg="#e9d49c", font=("Arial", 20, "bold"),fg="black").pack(side="top", pady=50)
    frame_items = tk.Frame(items_edit, bg="#e9d49c")
    frame_items.pack()

    def add_accessoires():
        accessoire_window = tk.Tk()
        accessoire_window.configure(bg='#e9d49c')
        accessoire_window.geometry("1080x720")
        title_accessoire_window = tk.Label(accessoire_window, text="Ajout accessoire", bg="#e9d49c", font=("Arial", 20, "bold"),fg="black")
        title_accessoire_window.pack(side="top", pady=50)

        frame_accessoire_window = tk.Frame(accessoire_window, bg="orange")
        frame_accessoire_window.pack()

    armes = tk.Button(frame_items, text="Ajouter des armes", bg="white", font=("Arial", 12, "normal"), fg="black") #, command=add_armes)
    armes.grid(row=0, column=0, ipady=50, padx=50, pady=50)

    accessoires = tk.Button(frame_items, text="Ajouter des accessoires", bg="white", font=("Arial", 12, "normal"), fg="black", command=add_accessoires)
    accessoires.grid(row=1, column=0, ipady=50, padx=50, pady=50)

    editor.withdraw()

# creation de la fenetre editor tkinter
editor = tk.Tk()
editor.configure(bg='#2e2b2a')  # Couleur du background en bleu clair
editor.geometry("1080x720")  # Taille page

title2 = tk.Label(text="Vous etes dans l'editeur du jeu", bg='#2e2b2a', font=("Arial", 20, "bold"), fg="white")
title2.pack(side="top", pady=50)

frame1 = tk.Frame(editor, bg='#fc9403')
frame1.pack()

photo_stats = tk.PhotoImage(file=r"./Plan-de-travail-6-150x150.png")

stats = tk.Button(frame1, text="Changer les valeurs des Stats", image=photo_stats, compound="top", command=stats_edit_window)
stats.grid(row="0", column="0", ipady=10, padx=10, pady=10)

items = tk.Button(frame1, text="Ajouter des items et definir l'inventaire dans votre jeu", command=items_edit_window)
items.grid(row="1", column="0", ipady=10, padx=10, pady=10)

dialogues = tk.Button(frame1, text="Ajouter les dialogues dans votre jeu")  # command=dialogues_edit_window
dialogues.grid(row="2", column="0", ipady=10, padx=10, pady=10)

editor.mainloop()
