import os
import os.path

# os.chdir('chemin') #specifier le chemin
print(os.getcwd()) #chemin actu

myFile = open("info2.txt", "w")

texte = "salut j'ecris dans un fichier avec python !" 
myFile.write(texte)
myFile.close()