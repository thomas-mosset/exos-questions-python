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
    pass  # À compléter

# Crée une mini-calculatrice simple (addition, soustraction, multiplication, division)
def mini_calculatrice(a, b, operateur):
    pass  # À compléter


# 3. Boucles et itérations
# --------------------------------
# Affiche les nombres de 1 à 100 avec une boucle for
def affiche_1_a_100():
    pass  # À compléter

# Affiche uniquement les multiples de 3 entre 1 et 100
def affiche_multiples_de_3():
    pass  # À compléter

# Inverse une chaîne de caractères avec une boucle
def inverse_chaine(s):
    pass  # À compléter

# Défi : Affiche uniquement les nombres pairs entre 1 et 20
# 1. Avec une boucle for
def pairs_for():
    pass  # À compléter

# 2. Avec une boucle while
def pairs_while():
    pass  # À compléter


# 4. Fonctions
# --------------------------------
# Crée une fonction factorielle récursive
def factorielle_recursive(n):
    pass  # À compléter

# Crée une fonction factorielle avec boucle
def factorielle_boucle(n):
    pass  # À compléter

# Crée une fonction qui prend une liste de nombres et retourne la moyenne
def moyenne(liste):
    pass  # À compléter


# 5. Structures de données
# --------------------------------
# Trie une liste de nombres sans utiliser sorted()
def tri_personnalise(liste):
    pass  # À compléter

# Crée un dictionnaire qui compte les occurrences de chaque lettre dans une phrase
def compte_lettres(phrase):
    pass  # À compléter

# Écris une fonction qui retourne la clé avec la plus grande valeur dans un dictionnaire
def cle_max_valeur(dico):
    pass  # À compléter


# 6. Compréhension de liste et fonctions lambda
# --------------------------------
# Recrée la liste [0, 2, 4, 6, 8] avec une compréhension de liste
def liste_pairs():
    pass  # À compléter

# Utilise map() et filter() avec des fonctions lambda (exemple simple)
def map_filter_exemple():
    pass  # À compléter


# 7. Classes et programmation orientée objet
# --------------------------------
class CompteBancaire:
    banque = "OpenBank"

    def __init__(self, titulaire, solde=0):
        self.titulaire = titulaire
        self.solde = solde

    # méthode d’instance
    def afficher_solde(self):
        pass  # À compléter

    # méthode de classe
    @classmethod
    def nom_banque(cls):
        pass  # À compléter

    # méthode statique
    @staticmethod
    def taux_interet():
        pass  # À compléter


# Test de la classe
def test_compte_bancaire():
    c1 = CompteBancaire("Alice", 1500)
    c1.afficher_solde()
    CompteBancaire.nom_banque()
    CompteBancaire.taux_interet()


if __name__ == "__main__":
    # Ici, tu peux appeler tes fonctions pour tester ton code
    pass
