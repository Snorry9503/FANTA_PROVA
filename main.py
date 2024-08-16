import tkinter as tk
import customtkinter as ctk


#from caricatore_giocatori import
# carica_giocatori_da_excel

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
# Configurazione base per customtkinter
ctk.set_appearance_mode("dark")  # Modalità scura
ctk.set_default_color_theme("blue")  # Tema colore blu

class FantaSavoiaApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Configurazione della finestra principale
        self.title("FANTASAVOIA TOOL")
        self.geometry("600x400")

        # Intestazione
        self.header_label = ctk.CTkLabel(self, text="FANTASAVOIA TOOL", font=("Arial", 36, "bold"))
        self.header_label.pack(pady=30)

        # Bottone Sezione Asta
        self.auction_button = ctk.CTkButton(self, text="Sezione Asta", font=("Arial", 18), command=self.open_auction_section, width=250, height=50)
        self.auction_button.pack(pady=20)

        # Bottone Sezione Admin
        self.admin_button = ctk.CTkButton(self, text="Sezione Admin", font=("Arial", 18), command=self.open_admin_section, width=250, height=50)
        self.admin_button.pack(pady=20)

    def open_auction_section(self):
    # Qui andrà il codice per aprire la sezione Asta
        # Creare una nuova finestra per la Sezione Asta
        auction_window = ctk.CTkToplevel(self)
        auction_window.title("Sezione Asta")
        auction_window.geometry("400x300")
        
        label = ctk.CTkLabel(auction_window, text="Benvenuto nella Sezione Asta", font=("Arial", 18))
        label.pack(pady=20)
        nome_utente= ctk.CTkEntry(auction_window, placeholder_text="Inserisci il nome utente")
        nome_utente.pack(pady=20)
        pass_word= ctk.CTkEntry(auction_window, placeholder_text="immetti password")
        pass_word.pack(pady=20)
        
        close_button = ctk.CTkButton(auction_window, text="Chiudi", command=auction_window.destroy)
        close_button.pack(pady=20)
        
        print('SezioneAsta')

    def open_admin_section(self):
        # Qui andrà il codice per aprire la sezione Admin
        admin_window = ctk.CTkToplevel(self)
        admin_window.title("Sezione Admin")
        admin_window.geometry("400x300")

        label = ctk.CTkLabel(admin_window, text="Benvenuto nella Sezione Admin", font=("Arial", 18))
        label.pack(pady=20)

        ingestdata_button = ctk.CTkButton(admin_window, text="Immetti Giocatori Anno corrente", font=("Arial", 18))
        ingestdata_button.pack(pady=20)
        ingestdata_buttonap = ctk.CTkButton(admin_window, text="Immetti Giocatori Anno precedente", font=("Arial", 18))
        ingestdata_buttonap.pack(pady=20)

        close_button = ctk.CTkButton(admin_window, text="Chiudi", command=admin_window.destroy)
        close_button.pack(pady=20)
        
        print('SezioneAdmin')

if __name__ == "__main__":
    app = FantaSavoiaApp()
    app.mainloop()


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
