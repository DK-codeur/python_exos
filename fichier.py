try:
    with open('info.txt', 'r') as monFichier:
        for i in monFichier.readlines():
            print(i.strip())
except IOError as err:
    print("erreur de fichier", err)
except ValueError:
    print("erreur de  conversion")
except:
    print("erreur lors de l'execution")



