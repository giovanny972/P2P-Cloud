import tkinter as tk
from pyp2p.net import *

class P2P_GUI:
    def __init__(self):
        self.p2p_network = None # Initialisation de l'objet pour le réseau P2P
        self.root = tk.Tk() # Création de la fenêtre principale
        self.root.title("P2P GUI") # Titre de la fenêtre
        # Ajout d'un cadre pour contenir les widgets
        self.frame = tk.Frame(self.root)
        
        # Widgets pour entrer l'adresse IP et le port
        self.ip_label = tk.Label(self.root, text="Adresse IP : ")
        self.ip_label.pack()
        self.ip_entry = tk.Entry(self.root)
        self.ip_entry.pack()
        self.port_label = tk.Label(self.root, text="Port : ")
        self.port_label.pack()
        self.port_entry = tk.Entry(self.root)
        self.port_entry.pack()
        
        # Bouton pour se connecter au réseau P2P
        self.connect_button = tk.Button(self.root, text="Se connecter", command=self.connect_to_p2p_network)
        self.connect_button.pack()
        
        # Widgets pour afficher les informations du réseau P2P
        self.network_info_label = tk.Label(self.root, text="Informations du réseau P2P")
        self.network_info_label.pack()
        self.peers_label = tk.Label(self.root, text="Pairs : ")
        self.peers_label.pack()
        self.files_label = tk.Label(self.root, text="Fichiers : ")
        self.files_label.pack()
        
        # Widgets pour rechercher et télécharger des fichiers
        self.search_label = tk.Label(self.root, text="Rechercher un fichier : ")
        self.search_label.pack()
        self.search_entry = tk.Entry(self.root)
        self.search_entry.pack()
        self.search_button = tk.Button(self.root, text="Rechercher", command=self.search_file)
        self.search_button.pack()
        self.download_label = tk.Label(self.root, text="Télécharger un fichier : ")
        self.download_label.pack()
        self.download_entry = tk.Entry(self.root)
        self.download_entry.pack()
        self.download_button = tk.Button(self.root, text="Télécharger", command=self.download_file)
        self.download_button.pack()
        
        self.root.geometry("600x400") # Determine la taille de la fenêtre
        self.root.mainloop() # Boucle principale
    
    # Fonction pour se connecter au réseau P2P
    def connect_to_p2p_network(self):
        ip = self.ip_entry.get() # Récupération de l'adresse IP
        port = int(self.port_entry.get()) # Récupération du port
        self.p2p_network = Net(passive_bind=str(ip), passive_port=port, node_type="passive") # Connexion au réseau P2P avec pyp2p
        self.p2p_network.start() # Démarrage du réseau P2P
        self.update_network_info() # Mise à jour des informations du réseau P2P
    
    # Fonction pour mettre à jour les informations du réseau P2P
    def update_network_info(self):
        peers = self.p2p_network.get_known_peers() # Récupération des pairs du réseau P2P
        files = self.p2p_network.get_shared_files() # Récupération des fichiers partagés sur le réseau P2P
        self.peers_label.config(text="Pairs : " + str(peers)) # Affichage des pairs
        self.files_label.config(text="Fichiers : " + str(files)) # Affichage des fichiers

    # Fonction pour rechercher un fichier sur le réseau P2P
    def search_file(self):
        filename = self.search_entry.get() # Récupération du nom de fichier saisi
        search_results = self.p2p_network.search(filename) # Recherche du fichier sur le réseau P2P
        if search_results:
            # Affichage des résultats de la recherche
            message = f"Résultats de la recherche pour {filename} : {search_results}"
        else:
            # Affichage d'un message si aucun fichier n'a été trouvé
            message = f"Aucun fichier trouvé pour {filename}"
        tk.messagebox.showinfo(title="Résultats de la recherche", message=message)
    
    def download_file(self):
        filename = self.download_entry.get() # Récupération du nom de fichier saisi
        download_results = self.p2p_network.search_download(filename) # Téléchargement du fichier
        if download_results:
            # Affichage d'un message si le fichier a été téléchargé avec succès
            message = f"Le fichier {filename} a été téléchargé avec succès"
        else:
            # Affichage d'un message si le fichier n'a pas été trouvé ou téléchargé
            message = f"Impossible de télécharger le fichier {filename}"
        tk.messagebox.showinfo(title="Résultat du téléchargement", message=message)

    # Fonction pour télécharger un fichier depuis le réseau P2P
    def download_file(self):
        filename = self.download_entry.get() # Récupération du nom de fichier saisi
        file_id = self.p2p_network.search_file(filename) # Recherche de l'ID du fichier sur le réseau P2P
        if file_id:
            # Téléchargement du fichier à partir de l'ID
            self.p2p_network.download_file(file_id)
            message = f"Le fichier {filename} a été téléchargé avec succès"
        else:
            # Affichage d'un message si aucun fichier n'a été trouvé
            message = f"Aucun fichier trouvé pour {filename}"
        tk.messagebox.showinfo(title="Téléchargement de fichier", message=message)
# Cette ligne vérifie que le script est exécuté en tant que programme principal et crée une instance de votre classe P2P_GUI pour afficher la fenêtre.    
if __name__ == '__main__':
    P2P_GUI()
