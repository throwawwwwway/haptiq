************
User Study A
************

Introduction
============
This reports describes briefly the procotol followed and presents the data collected with their results. This user study aims to compare different interaction techniques in order to evaluate which would be the most suited for graph exploration. Two sets of tactile signals has been developed: one is purely mapping what is under the device (M) when the second adds some guidance (G). These two sets - M and G, are the result of multiple enhancement after each iteration where the users have reported their struggles and where we have observed their difficulties in adopting these sets of tactile signals.


À propos du protocole B
Graphes
Les graphes partages les caractéristiques suivantes (à tester, à modifier, à itérer) :
- 7 noeuds
- 1 noeud à 4 connexions
- 2 noeuds à 3 connexions
- 2 noeuds à 2 connexions
- 2 noeuds à 1 connexion
- 2 connexions à 1 U
- 4 connexions à 2 U
- 2 connexions à 3 U
- tous les angles sont des multiples de 45°
- les noms attachés aux noeuds sont des noms de villes entre 5 et 8 caractères sans particule, sans tiret
- deux noeuds ne peuvent pas avoir le même nom
Interactions
HaptiQ avec guidage (avec annonce vocale des noeuds). Pour description, voir Exp1 (possible amélioration).
Pointage :
	- sur noeud, annonce le noeud et ses connexions (avec distance en U)
	- sur connexion, annonce les noeuds sur la connexion et l'axe de la connexion
	- sur rien, annonce le noeud le plus proche, direction et distance en U
	- coupe le son précédent si une nouvelle configuration est détectée
Clavier :
	- sur noeud, annonce le noeud et ses connexions (avec distance en U)
	- lorsque la direction est incorrecte annonce ("Impossible")
	- <espace> pour répéter
Tâches
Pour chaque interaction il y a deux blocs de tests. Chaque bloc se traduit de la manière suivante :
- Exploration libre de 5 min
- Tâche de recopie du graphe
- Classer du plus petit au plus grand les nconnexions suivantes : X, Y, Z,... (à définir le nombre)
- Quel serait le chemin le plus court entre x et y (à définir combien de fois le faire)
- NASA-TLX
Mesures
Online
- Nombre de fois qu'un noeud est revisité
- Nombre de temps passé sur chaque noeud
Offline
- Système de points pour le dessin du graphe
	- chaque noeud de bon (position relative au reste, nom) : 3 points
	- chaque connexion de bonne (angle relatif aux autres, entre les bons noeuds) : 2 points
	- chaque mise à l'échelle de bon : 1 points
- Score de justesse dans les questions de classement et du plus court chemin
- Mesure de satisfaction par le NASA-TLX
Discussion
Avantages
Le fait d'avoir un temps limité permet vraiment de faciliter la procédure de test, c'est aller au plus simple. Je pense que passé une heure d'expérience, la pénibilité biaise de beaucoup l'évaluation et arriver à gérer le temps de cette manière me paraît pertinent.
Désavantages
Le fait d'évaluer la justesse d'un graphe dessiné à la main peut paraître un peu compliqué, mais par un système de points positifs ça peut être relativement faisable.
Il est difficile de trouver des mesures qui soient adaptées aux trois interactions, poser les fameuses questions à la :
What is the minimum amount of node that are between x and y?
What is the minimum amount of node that need to be removed to prevent a connection between x and y?
What is the minimum amount of connection that need to be removed to prevent a connection between x and y?
serait intéressant. Cependant, j'ai peur que chaque graphe ait sa propre difficulté pour répondre à ses questions. Ou alors, il faudrait croiser chaque graphe avec les trois interactions entre les sujets (pour pouvoir comparer la même réponse avec les mêmes conditions hors l'interactions), pour ensuite faire des statistiques comparées HaptiQ vs Guidage, HaptiQ vs Keyboard. Remarque, cette solution me plaît aussi... mais on ne peut pas tout faire.

