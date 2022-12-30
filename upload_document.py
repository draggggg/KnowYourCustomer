import tkinter as tk
from tkinter import filedialog

# Créer une fenêtre principale
root = tk.Tk()

# Créer une fonction pour ouvrir une boîte de dialogue de sélection de fichier
def open_file_dialog():
  file_path = filedialog.askopenfilename()
  print("Chemin du fichier sélectionné:", file_path)

# Créer un bouton qui appelle la fonction "open_file_dialog" lorsqu'il est cliqué
button = tk.Button(root, text="Sélectionner une photo", command=open_file_dialog)
button.pack()

# Démarrer la boucle d'événements Tkinter
root.mainloop()
