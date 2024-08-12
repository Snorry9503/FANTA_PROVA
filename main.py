import customtkinter as Ctk
#from caricatore_giocatori import carica_giocatori_da_excel

# 1. Caricamento della Lista dei Giocatori
#file_pathAP = 'c:/Users/GAR/Documents/FANTA_PROVA/'
#file_pathAC = 'c:/Users/GAR/Documents/FANTA_PROVA/'
#lista_giocatoriAC = carica_giocatori_da_excel(file_pathAC)
#lista_giocatoriAP = carica_giocatori_da_excel(file_pathAP)
# 2. Funzione per Avviare l'Asta
#def start_auction():
#    print("L'asta è iniziata!")
    # Puoi aggiungere qui la logica per visualizzare la lista dei giocatori nell'interfaccia

# 3. Creazione della Finestra Principale della GUI
root = Ctk.CTk()
root.title("Savoia Tool - By Gabbo")

## Creazione di un'etichetta e un pulsante
#label = tk.Label(root, text="Lista Giocatori")
#label.pack(pady=20)
# Add a Treeview widget
#tree = ttk.Treeview(root, column=("c1", "c2", "c3", "c4"), show='headings', height=25)

#tree.column("# 1", anchor=tk.CENTER)
#tree.heading("# 1", text="Giocatore")
#tree.column("# 2", anchor=tk.CENTER)
#tree.heading("# 2", text="Squadra")
#tree.column("# 3", anchor=tk.CENTER)
#tree.heading("# 3", text="Ruolo")
#tree.column("# 4", anchor=tk.CENTER)
#tree.heading("# 4", text="FantaMilioni")

#for giocatore in lista_giocatoriAC:
# Insert the data in Treeview widget
#    tree.insert('', 'end', text="1", values=(f"{giocatore['Nome']}", f"{giocatore['Squadra']}", f"{giocatore['RuoloMantra']}",f"{giocatore['FVM_M']}"))

#tree.pack()

# Creazione del pulsante per avviare l'asta
#start_button = tk.Button(root, text="Inizia Asta", command=start_auction)
#start_button.pack(pady=20)

# 4. Avvio del Loop Principale dell'Interfaccia
root.mainloop()