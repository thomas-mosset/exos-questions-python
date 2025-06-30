# Exercices Python pour profil junior

# 1. Types de base et opérations
# --------------------------------
# Crée des variables de types int, float, str, bool, list, dict, tuple, set
# Affiche le type de chaque variable avec type()
# Convertis un float en int, une string en liste de caractères, etc.

var_int = 1
var_float = 0.3
var_str = "Hello World"
var_bool = True
var_list = ['Kiwi', 'Orange', 'Figue']
var_dict = {'name' : 'Jane', 'lastname' : 'Doe'}
var_tuple = ('Kiwi', 'Orange', 'Figue')
var_set = {'Kiwi', 'Orange', 'Figue'}

print("Type de var_int:", type(var_int))
print("Type de var_float:", type(var_float))
print("Type de var_str:", type(var_str))
print("Type de var_bool:", type(var_bool))
print("Type de var_list:", type(var_list))
print("Type de var_dict:", type(var_dict))
print("Type de var_tuple:", type(var_tuple))
print("Type de var_set:", type(var_set))

var_float_to_int = int(7.3)
var_str_to_list = list(var_str)

print(var_float_to_int, type(var_float_to_int))
print(var_str_to_list, type(var_str_to_list))


# 2. Opérateurs et conditions
# --------------------------------
# Écris une fonction qui vérifie si un nombre est pair ou impair.
def est_pair(n):
    if n % 2 == 0:
        print(f"{n} est pair.")
    else:
        print(f"{n} est impair.")

est_pair(10)
est_pair(21)

# Crée une mini-calculatrice simple (addition, soustraction, multiplication, division)
def mini_calculatrice(a, b, operateur):
    resultat = None
    operateur_ok = True
            
    if operateur == "+":
        resultat = a + b
    elif operateur == "-":
        resultat = a - b
    elif operateur == "/":
        if b != 0:
            resultat = a / b
        else:
            print("Erreur : division par zéro.")
            return
    elif operateur == "*":
        resultat = a * b
    else:
        operateur_ok = False
        print("Opérateur invalide. Utilisez uniquement '+', '-', '*', ou '/'.")
    
    if operateur_ok == True:
        print(f"Le résultat de {a} {operateur} {b} est : {resultat}")


mini_calculatrice(2, 4, "+")
mini_calculatrice(12, 4, "-")
mini_calculatrice(8, 4, "/")
mini_calculatrice(58, 4, "*")
mini_calculatrice(2, 4, "fail")

# 3. Boucles et itérations
# --------------------------------
# Affiche les nombres de 1 à 100 avec une boucle for
def affiche_1_a_100():
    for i in range(1, 101):
        print(i)

affiche_1_a_100()

# Affiche uniquement les multiples de 3 entre 1 et 100
def affiche_multiples_de_3():
    for i in range(1, 101):
        if i % 3 == 0:
            print(i)

affiche_multiples_de_3()

# Inverse une chaîne de caractères avec une boucle
def inverse_chaine(s):
    chaine_liste = list(s) # conversion en liste de la chaîne de caractères
    chaine_liste_inversee = [] # initialisation vide d'un tableau
    
    # boucle sur les caractères
    for caractere in reversed(chaine_liste):
        # ajout de chaque caractère
        chaine_liste_inversee.append(caractere)
    
    # conversion en chaîne de caractères
    chaine_inversee = "".join(chaine_liste_inversee)
    # affiche la chaine inversée
    print(chaine_inversee)

inverse_chaine("Hello World")

# Défi : Affiche uniquement les nombres pairs entre 1 et 20
# 1. Avec une boucle for
def pairs_for():
    for i in range(1, 21):
        if i % 2 == 0:
            print(i)

pairs_for()

# 2. Avec une boucle while
def pairs_while():
    i = 1
    
    while i < 21:
        if i % 2 == 0:
            print(i)
        i += 1

pairs_while()

# 4. Fonctions
# --------------------------------
# Crée une fonction factorielle récursive
def factorielle_recursive(n):
    if n == 0:
        return 1
    else:
        return n * factorielle_recursive(n -1)

print(factorielle_recursive(2))

# Crée une fonction factorielle avec boucle
def factorielle_boucle(n):
    resultat = 1
    for i in range(1, n + 1):
        resultat *= i
        
    return resultat

print(factorielle_boucle(2))

# Crée une fonction qui prend une liste de nombres et retourne la moyenne
def moyenne(liste):
    resultat = 0
    
    for n in liste:
        resultat += n
        
    print(resultat / len(liste))
        
moyenne([2, 5, 18, 20, 16])

# 5. Structures de données
# --------------------------------
# Trie une liste de nombres sans utiliser sorted()
def tri_personnalise(liste):
    for i in range(0, len(liste)):
        for j in range(i+1, len(liste)):
            if liste[i] >= liste[j]:
                liste[i], liste[j] = liste[j], liste[i]
                
    return liste

print(tri_personnalise([10, 48, 0, 23, 5, 4, 78]))

# Crée un dictionnaire qui compte les occurrences de chaque lettre dans une phrase
def compte_lettres(phrase):
    compteur = {}
    
    for lettre in phrase:
        if lettre != "":
            lettre = lettre.lower()
            
            if lettre in compteur:
                compteur[lettre] += 1
            else:
                compteur[lettre] = 1
    
    return compteur

print(compte_lettres("Hello World"))

# Écris une fonction qui retourne la clé avec la plus grande valeur dans un dictionnaire
def cle_max_valeur(dico):
    return max(dico, key=dico.get)
 
print(cle_max_valeur({"a": 12, "b": 88, "c": 42}))

# 6. Compréhension de liste et fonctions lambda
# --------------------------------
# Recrée la liste [0, 2, 4, 6, 8] avec une compréhension de liste
def liste_pairs(liste):
    # newlist = [expression for item in iterable if condition == True]
    nouvelle_liste = [n for n in liste if n % 2 == 0]
    
    return nouvelle_liste

print(liste_pairs([0, 1, 2, 3, 4, 5, 6, 7, 8]))

# Utilise map() et filter() avec des fonctions lambda
def map_filter_exemple():
    noms = [" Alice ", "Bob", "   Charlie", "Dave", "Eve  ", "Charlotte"]

    # Nettoyer les espaces + mettre en minuscule
    noms_nettoyes = list(map(lambda nom: nom.strip().lower(), noms))

    # Garder uniquement les noms qui commencent par la lettre "c" (minuscule /!\ sensible à la casse)
    noms_filtres = list(filter(lambda nom: nom.startswith("c"), noms_nettoyes))

    print("Noms nettoyés :", noms_nettoyes)
    print("Noms filtrés (commençant par 'c') :", noms_filtres)

map_filter_exemple()

# 7. Classes et programmation orientée objet
# --------------------------------
class CompteBancaire:
    banque = "OpenBank"

    def __init__(self, titulaire, solde=0):
        self.titulaire = titulaire
        self.solde = solde

    # méthode d’instance
    def afficher_solde(self):
        print(f"{self.titulaire} a un solde de {self.solde}€ sur son compte bancaire.")

    # méthode de classe
    @classmethod
    def nom_banque(cls):
        print(f"Ma banque s'appelle {cls.banque}.")

    # méthode statique
    @staticmethod
    def taux_interet():
        print("Les taux d'intérêts sont de 2%.")


# Test de la classe
def test_compte_bancaire():
    c1 = CompteBancaire("Alice", 1500)
    c1.afficher_solde()
    CompteBancaire.nom_banque()
    CompteBancaire.taux_interet()

if __name__ == "__main__":
    test_compte_bancaire()
