# Questions Python

- **Quelle est la différence entre une liste et un tuple ?**

Une liste est une collection ordonnée et modifiable (mutable) d’éléments de tout type. Elle est délimitée par des crochets [].

***Exemple : ma_liste = ['orange', 2, 'banana', 30.1 , 'kiwi']***

Un tuple est une collection ordonnée mais non modifiable (immutable). Il est délimité par des parenthèses ().

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
# Avec [::1]
liste = [1, 2, 3, 4, 5]
liste_inversee = liste[::1]

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

A noter que ``contine`` permet de sauter le reste du code dans la boucle et de passer à l’itération suivante.

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
  
``zip()`` est une fonction intégrée qui permet de regrouper plusieurs listes ou itérables élément par élément. Elle associeles éléments en paires (ou tuples), selon leur position.

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

Les dictionnaires conservent l’ordre d’insertion. Avec ``dict.fromkeys(ma_liste)``, on crée un dictionnaire où les clés sont les éléments de la liste ```ma_liste``. Comme les clés d’un dict sont uniques, les doublons sont automatiquement éliminés. Transformer ce dictionnaire en liste avec ``list()`` donne la liste des clés dans l’ordre d’apparition.

``` python

names = ["James", "Bob", "James", "Mark", "Kate", "Sarah", "Kate"]
result = list(dict.fromkeys(names))
print(result) # ['James', 'Bob', 'Mark', 'Kate', 'Sarah']

```

---

- **Quelle est la différence entre une liste, un dictionnaire, un ensemble (``set``) et une chaîne (``str``) ?**


- Quelle est la différence entre une fonction et une méthode ?


- Que signifie la portée d’une variable (``global`` vs ``local``) ?


- Qu'est-ce qu'une fonction lambda ?


- Qu’est-ce qu’une classe et un objet ?


- À quoi sert ``__init__()`` ?


- Quelle est la différence entre une méthode de classe, de classe statique, et une méthode d’instance ?


- Que signifie l’héritage en Python ?


- Comment gérer les exceptions en Python ?


- Quelle est la différence entre ``try/except`` et ``try/except/finally`` ?


- Les dictionnaires sont-ils ordonnés en Python 3.9+ ?
