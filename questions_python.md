# Questions Python

- **Quelle est la différence entre une liste et un tuple ?**

Une liste est une collection ordonnée et modifiable (mutable) d’éléments de tout type. Elle est délimitée par des crochets ``[]``.

***Exemple : ma_liste = ['orange', 2, 'banana', 30.1 , 'kiwi']***

Un tuple est une collection ordonnée mais non modifiable (immutable). Il est délimité par des parenthèses ``()``.

***Exemple : mon_tuple = ('orange', 2, 'banana', 30.1 , 'kiwi')***

Les principales différences sont que les tuples ont une taille fixe, contrairement aux listes, que les tuples sont immutables, c'est à dire qu'ils ne sont pas modifiables, et que les tuples sont légèrement plus rapides que les listes.

---

- **Comment fonctionne ``*args`` et ``**kwargs`` dans une fonction ?**

Les paramètres ``*args`` et ``**kwargs`` agissent comme des arguments fourre-tout et indéfinis. Ils permettent de passer un nombre variable d’arguments à une fonction.

***Note : le ``*`` s'appelle opérateur splat.***

Le paramètre ``*args`` (dont le nom est une convention) est utilisé pour collecter plusieurs arguments non nommés et retourne un tuple. On peut les parcourir comme une liste. ``for arg in args:``

``` python

Exemple :

def foo(*args):
    print(args)

foo()                            # ()
foo(1)                           # (1,)
foo(1, 'Bonjour', True)          # (1, 'Bonjour', True)
```

Le paramètre ``**kwargs`` (dont le nom est une convention) est utilisé pour collecter plusieurs arguments nommés (clé = valeur | 'kw' = key word) et retourne un dictionnaire. On peut les parcourir comme un dict. ``for key, value in kwargs.items():``

``` python

Exemple :

def foo(**kwargs):
    print(kwargs)

foo()                                      # {}
foo(a=1)                                   # {'a': 1}
foo(a=1, mot='Bonjour', boolean=True)      # {'a': 1, 'mot': 'Bonjour', 'boolean': True}
```

Les ``*args`` et ``**kwargs`` peuvent être combinés, mais il faut respecter un ordre :

``` python
def ma_fonction(arg1, *args, **kwargs):
    pass
```

---

- Quelle est la différence entre ``is`` et ``==`` ?

L'opérateur ``==`` signifie "est égal à" et compare des valeurs (le contenu de 2 objets), tandis que l'opération ``is`` compare l'identité des objets.

``` python
x = [1, 2, 3]
y = [1, 2, 3]

print(x is y)  # False car x ne se réfère par à y. Les 2 ne pointent pas vers le même objet.
print(x == y)  # True car le contenu de x est égal au contenu de y.

z = x
print(x is z) # True car on est face au même objet.
```

---

- **À quoi sert ``elif`` au lieu de plusieurs ``if`` ?**

``elif`` (contraction de ``else if``) permet d'enchaîner plusieurs conditions exclusives après un ``if``.

Il est utilisé pour éviter de tester inutilement d'autres conditions une fois qu'une a été validée.

``` python
x = 10
if x == 5:
    print("Cinq")     # est testé
elif x == 10:
    print("Dix")      # est exécuté
elif x == 15:
    print("Quinze")   # n'est pas testé

```

---

- **Que fait la méthode ``split()`` sur une chaîne de caractères ?**

La méthode ``split()`` coupe la chaine de caractères (par défaut au niveau des espaces) et retourne une liste.

Si le séparateur ou aucun séparateur est trouvé, ``.split()`` retourne la chaîne de caractères entière dans une liste.

``` python
chaine = "Ma chaine de caractères"
chaine_splitee = chaine.split()
print(chaine_splitee)  # ['Ma', 'chaine', 'de', 'caractères']

date = "2025-06-23"
print(date.split("-")) # ['2025', '06', '23']

salutation = "Bonjour tout le monde"
print(salutation.split(",")) # ['Bonjour tout le monde']

```

---

- **Comment inverser une chaine de caractères en Python ?**

``` python
chaine = "Ma chaine de caractères"[::-1]
print(chaine) # sérétcarac ed eniahc aM

```

---

- **Comment inverser une liste en Python ?**

``` python
# Avec [::-1]
liste = [1, 2, 3, 4, 5]
liste_inversee = liste[::-1]

print(liste_inversee) # [5, 4, 3, 2, 1]

# Avec la méthode reverse()
liste.reverse()
print(liste) # [5, 4, 3, 2, 1]

```

---

- **Quelle est la différence entre une boucle ``for`` et une boucle ``while`` ?**

La boucle ``for`` sert à parcourir une séquence (liste, chaîne, range, etc.) quand on connaît le nombre d’éléments à traiter, tandis que la boucle ``while`` répète un bloc de code tant qu'une condition est vraie. (Utile lorsqu'on ne sait pas à l’avance combien de fois il faut itérer.)

``` python

# Boucle for
liste = [1, 2, 3, 4, 5]

for x in liste:
    if x <= 3:
        print(x) # 1, 2, 3

# Boucle while
x = 0
while x <= 3:
    print(x) # 0, 1, 2, 3
    x += 1

```

---

- **Comment sortir d'une boucle prématurément ?**

L'opérateur ``break`` permet de sortir d'une boucle prématurément.

``` python

nb = 0

for nb in range(10):
    if nb == 5:
       break

    print('Number is ' + str(nb))

print('Out of loop')

# Number is 0
# Number is 1
# Number is 2
# Number is 3
# Number is 4
# Out of loop

```

A noter que ``continue`` permet de sauter le reste du code dans la boucle et de passer à l’itération suivante.

``` python

nb = 0

for nb in range(5):
    if nb == 2: # ici nb = 2 sera ignoré
       continue

    print('Number is ' + str(nb))


# Number is 0
# Number is 1
# Number is 3
# Number is 4

```

---

- **Quelle est la différence entre ``map()`` et une boucle ``for`` ?**

La fonction ``map()`` permet d'appliquer une fonction à chaque élément d'un ou plusieurs itérables. Elle retourne un objet ``map`` (qu’on convertit souvent en ``list()``). Elle est idéale pour les opérations simples et directes.

``` python

def multiplie(nb1, nb2):
    return nb1 * nb2

liste = [1, 2, 3, 4, 5]
liste2 = [10, 20, 30, 40, 50]
resultat = list(map(multiplie, liste, liste2))

print(resultat) # [10, 40, 90, 160, 250]

```

La boucle ``for`` est plus flexible (possibilité de faire des conditions, des filtres, plusieurs actions). Elle nécessite d’initialiser une nouvelle liste si on veut stocker un résultat. Elle est plus lisible pour les traitements complexes.

``` python

def multiplie(nb1, nb2):
    return nb1 * nb2

liste = [1, 2, 3, 4, 5]
liste2 = [10, 20, 30, 40, 50]
resultat = []

for nb1, nb2 in zip(liste, liste2):
    resultat.append(multiplie(nb1, nb2))

print(resultat)  # [10, 40, 90, 160, 250]

```

---

- **Qu'est-ce que ``zip()`` ?**
  
``zip()`` est une fonction intégrée qui permet de regrouper plusieurs listes ou itérables élément par élément. Elle associe les éléments en paires (ou tuples), selon leur position.

``` python

prenoms = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 22]

for nom, age in zip(prenoms, ages):
    print(nom, "a", age, "ans")

```

---

- **Comment trier une liste ? Quelle est la différence entre ``sort()`` et ``sorted()`` ?**
  
``sort()`` permet de trier une liste (et uniquement une liste) de manière alphabétique. Elle ne retourne pas de nouvelle liste (retourne ``None``) et modifie la liste initiale.

``` python

prenoms = ["Enzo", "Alice", "Charlie", "Bob"]
prenoms.sort()
print(prenoms) # ["Alice", "Bob", "Charlie", "Enzo"]

```

``sorted()`` permet de trier un tuple ou une liste de manière alphabétique tout en retournant une nouvelle liste triées. Elle ne modifie pas la liste ou le tuple original.

``` python

prenoms = ["Enzo", "Alice", "Charlie", "Bob"]
prenoms_tries = sorted(prenoms)
print(prenoms_tries)  # ['Alice', 'Bob', 'Charlie', 'Enzo']
print(prenoms)        # ['Enzo', 'Alice', 'Charlie', 'Bob'] — inchangé

```

---

- **Comment supprimer les doublons d’une liste tout en conservant l’ordre ?**

Les dictionnaires conservent l’ordre d’insertion. Avec ``dict.fromkeys(ma_liste)``, on crée un dictionnaire où les clés sont les éléments de la liste ```ma_liste```. Comme les clés d’un dict sont uniques, les doublons sont automatiquement éliminés. Transformer ce dictionnaire en liste avec ``list()`` donne la liste des clés dans l’ordre d’apparition.

``` python

names = ["James", "Bob", "James", "Mark", "Kate", "Sarah", "Kate"]
result = list(dict.fromkeys(names))
print(result) # ['James', 'Bob', 'Mark', 'Kate', 'Sarah']

```

---

- **Quelle est la différence entre une liste (``list``), un dictionnaire (``dict``), un ensemble (``set``) et une chaîne (``str``) ?**

Une liste ``list`` est une collection ordonnée et modifiable qui autorise les éléments en double.

Un dictionnaire ``dict`` est une collection ordonnée (à partir de python 3.7) de paires key-value (clé-valeur). Les clés sont uniques.

Un ensemble ``set`` est une collection non-ordonnée, non indexée et qui ne contient que des éléments uniques (pas de doublons).

Une chaîne ``str`` est une séquence immuable (qui ne change pas) de caractères qui peut être parcourue comme une liste. (Chaque élément est un caractère.)

``` python

list_ex = [1, 2, 2, 3] # doublon possible

dict_ex = {"nom": "Alice", "âge": 25} # key - value pair

set_ex = {1, 2, 3} # pas de doublon

str_ex = "Hello world"

```

---

- **Quelle est la différence entre une fonction et une méthode ?**

Une méthode est une fonction liée à un objet (comme une liste, une chaîne, etc.)  qui est appelée avec la syntaxe ``objet.methode()``, tandis qu'une fonction est un bloc de code réutilisable qui accepte des arguments. Cette dernière peut être appelée seule : ***Exemple : print(), len(), ou une fonction créée avec def.***

``` python

def func_example ():
    print("coucou")

func_example() # appel de la fonction

my_method_text = "example"
print(my_method_text.upper()) # appel de la méthode

```

---

- **Que signifie la portée d’une variable (``global`` vs ``local``) ?**

Une variable ``global`` est déclarée en dehors d'une fonction et est disponible dans toutes les fonctions et méthodes du fichier dans lequel elle a été déclarée. Elle ne peut être modifiée dans une fonction que si on utilise le mot-clé ``global``.

Une variable ``local`` est disponible, cloisonnée et exploitable uniquement dans la fonction dans laquelle elle a été déclarée. (Cela vaut pour les variables en tant que paramètre de la fonction et celles déclarées dans la fonction.)

``` python

compteur = 0  # variable globale

def incrementer():
    global compteur  # on indique qu'on veut modifier la variable globale grâce à "global"
    compteur += 1
    local_message = "Compteur incrémenté"  # variable locale
    print(local_message)

incrementer()
print("Valeur globale de compteur :", compteur)



x = "global"

def ma_fonction():
    x = "local"
    print("Dans la fonction :", x) # Dans la fonction : local

ma_fonction()
print("En dehors de la fonction :", x) # En dehors de la fonction : global

```

---

- **Qu'est-ce qu'une fonction lambda ?**

Une fonction ``lambda`` est une fonction anonyme, c'est-à-dire qui n'est pas nommée. Elle s’écrit en une seule ligne, et est utile pour des opérations simples et courtes.

***Syntaxe : lambda arguments: expression***

``` python

# Avec def
def addition(x, y):
    return x + y

# Avec lambda
addition = lambda x, y: x + y # Fonction lambda qui additionne 2 nombres

print(addition(2, 3))  # Affiche 5

```

---

- **Qu’est-ce qu’une classe et un objet ?**

Python est un langage en POO (Programmation Orientée Objet).

Une classe est un modèle pour créer un objet. Elle définit des attributs (données) et des méthodes.

Un objet est une instance de classe qui vient utiliser, avec ses propres valeurs, les proprités (attributs) et les actions / comportements (méthodes) mises à disposition par la classe.

``` python

# Classe
class Animal:
    def __init__(self, animal_type, nom, age, son): # __init__ -> constructeur
        self.animal_type = animal_type  # attribut de classe
        self.nom = nom                  # attribut de classe
        self.age = age                  # attribut de classe
        self.son = son                  # attribut de classe
    
    def presentation(self): # méthode
        print(f"Voici mon {self.animal_type} {self.nom} qui a {self.age} ans.")
    
    def bruit(self): # self fait référence à l'instance actuelle
        print(self.son)

# Création d'objet
mon_objet_chat = Animal("chat", "Isis", 6, "Miaou !")
mon_objet_chien = Animal("chien", "Pepsi", 5, "Wouaf !")

# Utilisation des méthodes de la classe Animal()
mon_objet_chat.presentation() # Voici mon chat Isis qui a 6 ans.
mon_objet_chat.bruit() # Miaou !

mon_objet_chien.presentation() # Voici mon chien Pepsi qui a 5 ans.
mon_objet_chien.bruit() # Wouaf !

```

---

- **Que signifie l’héritage en Python ?**

L'héritage en Python permet à une classe enfant d'hériter des propriétés et méthodes d'une classe parent. C'est utilisé en POO (Programmation Orientée Objet).

``` python

# classe parent
class Animal:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

# classe enfant Chat qui hérite des propriétés et méthodes de la classe parent Animal
class Chat(Animal): 
    def __init__(self, nom, age, type):
        super().__init__(nom, age) # appel du constructeur de la classe parent
        self.type = type
    
    def miauler(self):
        print("Miaou !")

animal1 = Animal("Gizmo", 3)
chat1 = Chat("Bubble", 5, "chat") # on passe "nom", "age" et "type" à l'instance Chat
chat1.miauler()   # Miaou !
print(chat1.nom)  # Bubble
print(chat1.age)  # 5
print(chat1.type) # chat

```

---

- **À quoi sert ``__init__()`` ?**

``__init__()`` est une méthode constructeur appelée automatiquement à la création d'un objet. Elle sert à assigner des valeurs aux propriétés de l'objet qui sera créer à partir de la classe.

``` python

class Personne:
    def __init__(self, nom, age):
        self.nom = nom   # attribut d'instance
        self.age = age   # attribut d'instance

personne1 = Personne("Thomas", 30)
print(personne1.nom) # Thomas
print(personne1.age) # 30

```

---

- **Quelle commande utiliser pour lire un fichier Python ?**

On utilise la commande ``python nom_du_fichier.py`` pour lire un fichier Python dans le terminal.

---

- **Quelle est la différence entre une méthode de classe,  statique, et d’instance ?**

Une méthode de classe est liée à la classe elle-même. Elle utilise ``@classmethod`` et reçoit ``cls`` en premier argument. On l'utilise lorsqu'on veut travailler avec la classe elle-même, non un objet spécifique. Ex : modification des variables partagées par toutes les instances (objets) de la classe.

Une méthode d'instance est liée à un objet instancié de la classe. Elle utilise ``self`` pour accéder aux attributs de l'objet. On l'utilise lorsqu'on a besoin d'accéder ou de modifier les données propres à une objet (instance). Ex : modification du nom d'une personne ou le solde d'un compte bancaire.

Une méthode statique n'accède si à l'instance ``self`` ni à la classe ``cls``. Elle est indépendante du contexte de classe et s’utilise avec ``@staticmethod``. On l'utilise lorsqu'on a besoin d'une fonction utilitaire liée à la classe, mais qui ne dépends ni de la classe ni de l'objet.

``` python

class Exemple:
    nom_de_la_classe = "Exemple"

    def __init__(self, nom):
        self.nom = nom
    
    def methode_instance(self):
        print(f"Je suis {self.nom}") # utilise self

    @classmethod
    def methode_de_classe(cls):
        print(f"Nom de la class : {cls.nom_de_la_classe}") # utilise cls
    
    @staticmethod
    def methode_statique():
        print("Je suis une méthode statique") # ne dépend ni de self ni de cls
    
obj = Exemple("Objet 1")
obj.methode_instance() # Je suis Objet 1
Exemple.methode_de_classe() # Nom de la classe : Exemple
Exemple.methode_statique() # Je suis une méthode statique -> juste une fonction.


class Voiture:
    nb_voitures = 0

    def __init__(self):
        Voiture.nb_voitures += 1

    @classmethod
    def combien_de_voitures(cls):
        print(f"Il y a {cls.nb_voitures} voitures")

Voiture.combien_de_voitures()

```

---

- **Comment gérer les exceptions en Python ?**

Les exceptions sont gérées avec un bloc ``try / except``. Le block ``try`` permet de tester si un bloc de code a des erreurs. Si c'est le cas et qu'une erreur survient, le bloc ``except`` permet de capturer l'erreur et d'executer une code de gestion.

On est sur la même logique qu'un' ``try / catch`` en Javascript.

``` python
try:
    print(x) # ici x n'est pas défini, ce qui va donc générer une erreur
except NameError:
    print("Variable non définie")
except Exception as error
    print(f"Une erreur est survenue : {error}")

```

---

- **Quelle est la différence entre ``try/except`` et ``try/except/finally`` ?**

Un bloc ``try/except`` permet de gérer une erreur survenue dans un bloc de code. 

Un bloc ``try/except/finally`` ajoute un bloc ``finally`` qui permet de toujours exécuter le bloc de code, qu'il y ait eu une erreur ou non.

A noter qu'un bloc ``else`` est aussi possible. Il permet d'executer du code si aucune erreur n'est survenue.

``` python
def lire_fichier(nom_fichier):
    # on essaie d'ouvrier en lecture le fichier et de le lire
    try:
        fichier = open(nom_fichier, 'r')
        contenu = fichier.read()
    # Si le fichier n’existe pas, on affiche un message d’erreur
    except FileNotFoundError:
        print("Erreur : fichier non trouvé.")
    # Sinon, on affiche son contenu
    else:
        print("contenu du fichier :")
        print(contenu)
    # Enfin, on ferme le fichier s'il a été ouvert (même si une erreur est survenue)
    finally:
        try:
            fichier.close()
            print("Fichier fermé.")
        # le fichier n'a jamais été ouvert
        except UnboundLocalError:
            pass

lire_fichier("exemple.txt")

```

---
