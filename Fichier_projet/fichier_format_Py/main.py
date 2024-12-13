#------------fichier Initiale-----------------------------------------------------------------
# avant toute execution tapez la commande suivante "pip install tqdm" 
#tqdm est le module responsable de barre de progres dans le terminal.
#Code simple de quiz qui utilise les fonctions definies dans le code precedent pour toute modifications
#Pour toutes modifications des questions veuillez respectez la synthaxe des fichiers et les regles ci dessous 
#-chaque questions doit avoir 4 options numerotees de a à d 
#-chaque questions doit se terminer par un point dinterrogation(?) suivi d'un espace ' ' et de la lettre de la reponse

import random
from tqdm import tqdm
import os
def printList(list:list):
    for elt in list:
        print(elt)


def getData(filename="Question"):#inserer le chemin du ficheier question
    data = []
    with open(filename, "r") as file:
        temp = []
        for line in file:
            temp.append(line.strip())
            if len(temp) == 5:
                data.append(temp)
                temp = []
    return data


def processData(data):
    dic = {}
    for elt in data:
        question = elt[0].split('?')[0]+'?'
        options = [opt.strip() for opt in elt[1:5]]
        answer = elt[0].split('?')[1].strip()
        dic[question] = {"reponse": answer, "options": options}
    return dic

def main():
    m_score = 0
    fileData = getData()
    m_dic = processData(fileData)
    keys = list(m_dic.keys())
    random.shuffle(keys)
    taille = len(m_dic)

    while True:
        for key in tqdm(keys, bar_format="{l_bar}{bar}{r_bar}", colour="green"):
            print()
            print(key)
            printList(m_dic[key]['options'])
            b = input("Entrez votre réponse (a, b, c ou d) : ")
            while b not in ['a', 'b', 'c', 'd']:
                print("Veuillez entrer une réponse valide (a, b, c ou d)")
                b = input("Entrez votre réponse (a, b, c ou d) : ")
            if b == m_dic[key]['reponse']:
                m_score += 1
                
            
            os.system('clear')

        print("Votre score est de : ", m_score, "/", taille)
        c = input("Voulez-vous continuer ? (O/N) ")
        if c.upper() == 'N':
            break
        else:
            random.shuffle(keys)
            m_score = 0
            os.system('clear')


if __name__ == "__main__":
    main()
