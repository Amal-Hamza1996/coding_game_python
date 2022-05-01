'''
Ce script présente 25 algorithmes à résoudre allant de la manipulation des chaines de caractères
à celles de collections de données pour réussir les tests techniques.
'''

'''
1- La fonction suivante permet d'inverser un entier naturel.
Pour inverser une chaine de caratères, on utilise [::-1]. 
'''
 
def inverse_entier(n):
    sign = n // abs(n) # signe de l'entier
    return int(str(abs(n))[::-1]) * sign

#print(inverse_entier(3245))
#print(inverse_entier(-7670))


'''
2- Le jeu suivant consiste à retrouver dans une liste d’entiers, tous les triplets 
pythagoriciens possibles qui y sont.

'''
from math import gcd, sqrt
def list_pythagorien(L):
    n = len(L) # La longeur de la liste.
    # La liste doit contenir au moins 3 éléments.
    if n < 3:
        print("Il faut saisir une liste de longeur supérieures ou égale à 3. ")
    F = []
    for i in range(n-2):
        for j in range(1, n-1):
            for k in range(j+1, n):
                # Calculer le carré de chaque élément.
                x = L[i] ** 2
                y = L[j] ** 2
                z = L[k] ** 2
                if z == y + x or y == z + x or x == y + z:
                    F.append((L[i],L[j],L[k]))
    return F
L = [0, 3, -6, 1, -2, -4, 5]
#print(list_pythagorien(L))

'''
3- La fonction suivante permet de calculer la longuer moyennes des mots 
dans une phrase donnée.

'''
def average_words_lenght(sentence):
    for punctuation in "!?',;.":
        sentence = sentence.replace(punctuation, ' ') # remplacer les ponctuations par un espace;
    words = sentence.split() # diviser le texte en mots.
    return round(sum([len(word) for word in words])/len(words),2) # retourner la valeurs moyenne avec deux chiffres après la virgule.


sentence = " Cette fonction permet de calculer la valeur moyenne des mots d'une phrase."

#print(average_words_lenght(sentence))

'''
4-Le script suivant retourne les nombre de Fibonacci compris 
entre deux entiers positifs.
'''
# On utilise la fonction récursive de fibonacci
def fibonacci(n):
    if n == 0 or n == 1:
        return 1
    return (fibonacci(n-1) + fibonacci(n-2))

# Les nombres de fibonnaci compris entre x et y  
def fibonacci_number(x, y):
    L = []
    i = 0
    maximum = max(x,y)
    minimum = min(x,y)
    while fibonacci(i) <= maximum:
        if fibonacci(i) >= minimum:
            L.append(fibonacci(i))
        i+=1
    return L
#print(fibonacci_number(10, 22))

'''
5-La fonction suivante permet d'additionner deux chaines de caractères.

'''
def add_strings(x,y):
    return str(int(x) + int(y))
#print(add_strings('100', '150'))

'''
6- La fonction suivante permet de faire la recherche dichotomique 
d'un nombre dans une liste triée.

'''

def recherche_dichotomique(L,e):
    n = len(L)
    if n== 0: # La liste est vide.
        return False
    m = n//2  # L'index de l'élément au milieu.
    if L[m] == e:
        return L[m]
    elif e > L[m]:
        return recherche_dichotomique(L[m+1:], e)
    else:
        return recherche_dichotomique(L[0:m], e)
    return False

A = [1,2,3,5,8,9]
#print(recherche_dichotomique(A,10))

'''
7-Cette fonction retourne le premier caractère qui ne se répète pas 
dans une chaine de caractère.

'''
import collections

def first_unique_character(word):
    word = word.lower() # Mettre tout le mot en miniscule.
    count = collections.Counter(word) # Cette fonction retourne un dictionnaire des chaines de caractère du mot et leur occurences
    for idx, ch in enumerate(count):
        if count[ch] == 1:
            return (ch, idx)
             
#print(first_unique_character("coronavirus"))
#print(first_unique_character('Europe'))

'''
8- Cette fonction permet de vérifier si en supprimant une lettre
à un mot, on obtnient un palindrome (Le mot qu'on le lise dans les deux sens).
Cette fonction doit retourner True si le mot est un palindrome. 
'''

def almost_palidromc(word):
    word = word.lower()
    for i in range(len(word)):
        ch = word[0:i] + word[i+1:]
        if ch == ch[::-1]:
            return (word[i], True, ch)
    return  word == word[::-1]

#print(almost_palidromc("Katyak"))
#print(almost_palidromc("Hannah"))

'''
9- La fonction suivante permet le chemin d'accès d'un fichier 
à partir de la racine.
L'algorithme prend en entrée la racine et le nom du fichier à trouver
et retourne en sortie le chemin

'''
import os
def find_files(filename, search_path):
    res= []
    for root, dir, files in os.walk(search_path):
        if filename in files:
            res.append(os.path.join(root, filename))
        
'''
9 - Cette fonction permet de dire si une liste est monotone ou non, c’est-à-dire si notre liste de nombres 
(entiers) est triée dans un ordre croissant ou décroissant.
On utilise la fonction all() de python qui renvoie True si 
tous les éléments de iterable sont vrais (ou s'il est vide) 

'''

def monotonic_array(L):
    return (all(L[i] <= L[i+1] for i in range(0,len(L)-1)) or  all(L[i] >= L[i+1] for i in range(0,len(L)-1)))

E = [6, 5, 4, 4] 
F = [1,1,1,3,3,4,3,2,4,2]

#print(monotonic_array(E))
#print(monotonic_array(F))

'''
10- Cette fonction permet d'inverser une chaîne de caractères sans modifier la position des caractères spéciaux : !@#$%^&*()-_=+~
'''

def inverser_special_char(word):
    res_list = []
    res = ""
    n = len(word)
    list_word = [word[i] for i in range(n)]
    carac_special_index = [i for i in range(0, n) if not(word[i].isalnum())]
    for i in range(n):
        if (n-1-i) not in carac_special_index:
            res_list.append(word[n-1-i])
    for e in carac_special_index:
        res_list.insert(e, word[e]) 
    for elt in res_list:
        res+=elt
    return res

    

word_ = "Alo*etui@l)ios82?"
#L= inverser_special_char(word_)
#print(L)
# expected : "28s*oili@u)teolA?"

'''
11- Cette fonction retourne les nombres premiers inférieurs 
ou égles à un entier n:

'''

def prime_numbers(n):
    primes = []
    if n== 0 or n==1:
        return []
    for i in range(2,n):
        divieurs = [p for p in range(1,i+1) if i%p == 0]
        if len(divieurs) == 2:
            primes.append(i)
    return primes
#print(prime_numbers(10))
#print(prime_numbers(21))

'''
12- La fonction suivante réalise le Tri par insertion d'une liste.

'''
def tri_insertion(L):
    n = len(L)
    print("********** Tri par insertion *************")
    print("En entree :", L)
    print("Nous aurons les etapes suivantes :\n")
    for i in range(1,n):
        sttr = "-Iteration " +str(i)+" (insertion de " + str(L[i]) + ") :" 
        cle = i
        while cle > 0:
            if L[cle] < L[cle-1]:
                L[cle], L[cle-1] = L[cle-1], L[cle]
            cle = cle -1
        print(sttr, L)
    return L
#L = [98, 23, 1, 4, 10]
#tri_insertion(L)

'''
13- La fonction suivante permet de faire le tri à bulles d'une liste.

'''

def tri_bulles(L):
    n = len(L)
    inversion = True
    while inversion:
        inversion = False
        for i in range(0,n-1):
            if L[i] > L[i+1]:
                L[i], L[i+1] = L[i+1], L[i]
                inversion = True
    return L
#print(tri_bulles([1,6,9,5,7,2,0,8,29,1,100]))

'''
14- La fonction suivante permet d'afficher plusieurs listes comme des chemins croissante:
L’idée est de prendre deux listes U et V, de faire un chemin croissant à partir d’un élément 
de U et des autres éléments de V.

'''

def growing_path(U, V):
    # Trier les deux listes de façon croissante.
    U.sort()
    V.sort()
    
    # Parcourir la première liste
    # et comparer chaque élément avec ceux de la seconde liste
    for i in range(len(U)):
        # Initialiser la liste
        L = [U[i]]
        # Comparer l'élément avec chaque élément de la seconde liste
        for j in range(len(V)):
            if U[i] < V[j]:
                L.append(V[j])
                print(L)
        print(L)
E = [9, 1, 23, 4]
F = [10, 20, 7]
#growing_path(E, F)
'''
14- La fonction suivante permet de déplacer tous les zéros à la fin de notre
liste

'''

def move_zeros(L):
    for i in L:
        if 0 in L:
            L.remove(0) # supprimer le premier zéro de la liste.
            L.append(0) # ajouter 0 à la fin de la liste
    return L
#array1 = [0, 1, 0, 3, 12]
#array2 = [1, 7, 0, 0, 8, 0, 10, 12, 0, 4]
#print(move_zeros(array1))
#print(move_zeros(array2))

'''
15- La fonction suivante permet de vérifier si une adresse e-mail
est valide ou non.

'''

from re import match

def is_email_valid(email):
    # Écrivons l'expression régulière d'une adresse email selon RFC 5322
    email_regex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
    
    # Vérifions que notre adresse email respecte ou non l'expression régulière
    valide_email = match(email_regex, email)
    if valide_email is None:
        return False
    return valide_email[0]

# U = "prenom.nom@contact.fr"
# V = "123prenom,nom@contact.org.fr"
# print(is_email_valid(U))
# print(is_email_valid(V))

'''
16- La fonction suivante permet de remplacer les valeur None d'une liste avec
la valeur qui précède.

Il est fréquent pour les Data Scientists de faire cette opération : remplir les valeurs 
None par d’autres valeurs grâce à des fonctions de la librairie Pandas. 

'''
def fill_blanks(L):
    res = []
    precedent = 0
    for i in L:
        if i is not None:
            res.append(i)
            precedent = i
        else:
            res.append(precedent)

    return res

# array1 = [1, None, 2, 3, None, None, 5, None]
# array2 = [None, 7, 0, 0, 8, None, 10, None, None, None]
 
# print(fill_blanks(array1))
# print(fill_blanks(array2))

'''
17- La fonction suivante permet de trier une liste d'entiers en 
mettant les nombres pairs triés de façon croissante en début et à la fin
les impairs triés de façon décroissante.

'''

def even_odd_sort(L):
    res = []
    pair = [L[i] for i in range(len(L)) if L[i]%2 == 0] # Pour stocker les nombres pairs.
    impair = [L[i] for i in range(len(L)) if L[i]%2 == 1] # Pour stocker les nombres impairs.
    pair.sort()
    impair.sort(reverse=True)
    res = pair + impair
    return res


# numbers = [93, 24, 38, 1, 96, 87, 100]
# print(even_odd_sort(numbers))

'''
18- La fonction suivante prend en paramètre deux textes, et permet
de repérer leur différence et leur intersection.

Différence : liste de mots présents dans un texte et pas dans l’autre.
Intersection : liste de mots présents dans les deux textes.

'''

def matching_words(sentence1, sentence2):
    sentence1 = sentence1.lower()
    sentence2 = sentence2.lower()

    set1 = set(sentence1.split())
    set2 = set(sentence2.split())
     
    return sorted(list(set1^set2)), sorted(list(set1&set2)) # ^ A.symmetric_difference(B), & A.intersection(B)

# sentence1 = "le blog 'ledatascientist' est le blog français de référence en data science"
# sentence2 = "parmi tous les blogs de data science j'aime 'ledatascientist'"

# print(matching_words(sentence1, sentence2))

'''
19- La fonction suivante permet de retourner la médiane d'une liste de valeurs
Cette fonction met en côté une moitié des valeurs qui sont toutes infénieures ou égales à x (la médiane)
et de l'autre côté l'autre moitié des valeurs qui en sont supérieurs

'''

def median(X):
    n = len(X)
    if n%2 == 0:
        return (X[int(n/2)] + X[int((n-1)/2)])/2
    else:
        return X[int((n+1)/2)]

# A = [1, 92, 25, 30, 12, 1]
# print(median(A))

'''
20- La fonction suivante permet de connaître le nombre de bits dans la 
représentation binaire d’un entier n qu’il faut changer pour obtenir l’entier m.
On commence par définir la fonction qui permet de représenter un entier en base 2.

'''
def toBinary(n):
    res = []
    while n != 0:
        res.append(n%2)
        n = n//2
    res.sort(reverse=True)
    return res

#print(toBinary(16))

def count_flipped(n,m):
    xor = n^m # OU Exclusif
    xor_binary = str(bin(xor)) # Petit tweat pour convertir la valeur en binaire qu'on convertit en string
    return xor_binary.count('1') # On compte le nombre de bits à 1
#print(count_flipped(8, 6))

'''
21- La fonction suivante permet de retourner le plus grand commun diviseur de deux entier.

'''

def pgcd(x, y):
    if x == 0:
        return y, 0, 1
    gcd, u, v = pgcd(y%x, x)
    u2 = v -(y//x)*u
    v2 = u

    return gcd, u2, v2
#print(pgcd(45, 60))

'''
22- La fonction suivante permet détecter pour deux mots données, la plus grande
séquence qu'ils ont en commun.
'''

def plus_longue_sequence_commune(word1, word2):
    pass
'''
23- La fonction suivante permet de vérifier si une phrase respecte l'ordre des parenthèses,
accolades, crochets ouvrants et fermants.
'''

def est_valid(sentence):
    carac_special = ["{", "}", "(", ")", "[", "]"]
    ouvrant_fermant = {"{": "}", "(": ")", "[":"]"}
    L = [sentence[i] for i in range(len(sentence)) if sentence[i] in carac_special]
    n = len(L)
    if n % 2 != 0:
        return False
    for i in range(int(n/2)):
        if L[n-i-1] != ouvrant_fermant[L[i]]:
            return False
    return True
    
# sentence1 = "{Je suis un ingénieur data scientist. J'ai participé à plusieurs projet qui s'incrivent dans ce cadre (Détection des anomalies, Reinforecment Learning, NLP [Analyse des semtiements, Extraction des informations clés d'un document.])} "
# sentence2 = "{J'aime la programmation, et les mathématiques (Probabilité, statistiques})"

# print(est_valid(sentence1))
# print(est_valid(sentence2))

'''
La classe suivante permet de manipuler un arbre binaire, 
nous voulons supprimer toutes les feuilles qui ont profondeur infénieure à k.

'''

# Créons une classe pour ajouter un noued dans l'arbre.
class newNode():
    # constructeur de la classe.
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    
# Afficher notre arbre.
def print_tree(root):
    if root:
        print_tree(root.left)
        print(root.val, end = " ")
        print_tree(root.right)
    
def remove_leafs(root, k):
    # Fonction de suppression des feuilles dont la profondeur est inférieure à k.
    def remove_leafs_from_short_depth(root, depth, k):
        if root == None:
            return None
        # on descend de la racine aux noeuds descencdants.
        root.left = remove_leafs_from_short_depth(root.left, depth + 1, k)
        root.right = remove_leafs_from_short_depth(root.right, depth+1, k)

        if root.left == None and root.right == None and depth < k:
            return None
        return root
    # Notre fonction finale utilise la fonction remove_leafs_from_short_depth
    new_tree = remove_leafs_from_short_depth(root, 1, k)
    return new_tree
if __name__ == "__main__":
    
    #Construisons notre arbre ci-dessus
    root = newNode(1)
    root.left, root.right = newNode(2), newNode(3)
    root.left.left = newNode(4)
    root.right.left, root.right.right = newNode(5), newNode(6)
    root.left.left.left, root.left.left.right = newNode(7), newNode(8)
    root.right.left.right = newNode(9)
    root.left.left.left.left = newNode(10)
    root.right.left.right.left, root.right.left.right.right = newNode(11), newNode(12)
    # Affichons l'arbre avant la suppression
    print("Notre arbre avant suppression")
    print_tree(root)
    print()
    print('-'*100)
    # Supprimons les feuilles de longueur inférieur à 4
    new_tree = remove_leafs(root, 4)
    # Affichons notre arbre après suppression
    print("Nouvel arbre obtenu")
    print_tree(new_tree)



        
            
    
    







   


