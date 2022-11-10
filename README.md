# Scrapping League of Legends
Projet d'initiation à BeautifulSoup4 ayant pour but de récupérer les données des champions de League of Legends venant du site OP.gg afin de récupérer leurs statistiques de popularité, bannissements et leurs éventuels contres.  
Une analyse de données permettra de chercher des corrélations entre les différentes stats de chaque personnage.
## Versions du projet
### v0
La version 0 est un simple Jupyter Notebook allant sur la page OP.gg et qui va récupérer les données pour les champions allant sur la ligne du haut et print les résultats. </br>

Pour le faire fonctionner: </br>
`Exécuter les nodes Jupyter permettront d'afficher les données.`

### v1
La version 1 est un script python permettant de récupérer les champions allant sur la ligne du haut de la même manière que la version 0, sauf qu'il stocke les résultats dans une base de données.

Pour le faire fonctionner: </br>
1) Se positionner dans le dossier v1, et initialiser la base de données </br>
</t>`python_scrapping\v1> python .\create_database.py`
2) Toujours dans le dossier v1, exécuter le script de scrapping </br>
</t> `python .\scrapping.py`

### v2
La version 2 est un script permettant à l'utilisateur de définir pour quel rôle il souhaite récupérer les données grâce à un argument argparse, et le script effectuera le scrapping sur le rôle approprié et intègrera les résultats dans une table associée au rôle en question. Elle contient aussi une analyse de données sous la forme d'un jupyter notebook permettant de déterminer des corrélations entre les différentes statistiques des personnages.

Pour le faire fonctionner: </br>
1. Se positionner dans le dossier v2, et initialiser la base de données </br>
</t>`python_scrapping\v2> python .\create_database.py`
2. Toujours dans le dossier v2, exécuter le main en précisant un des arguments de rôles. </br>
`python .\main.py` suivi d'un des arguments suivants:  
    1. `-t` ou `--top` récupèrera les données associées aux top laners  
    2. `-j` ou `--jungle` récupèrera les données associées aux junglers  
    3. `-m` ou `--mid` récupèrera les données associées aux mid laners  
    4. `-a` ou `--adc` récupèrera les données associées aux ADC  
    5. `-s` ou `--support` récupèrera les données associées aux supports  
3. Pour faire fonctionner l'analyse de données, il faut avoir importé au moins la table "top" car c'est sur celle ci qu'elle se porte.
exemples :  
1. `python .\main.py -t`
2. `python .\main.py --top` 
