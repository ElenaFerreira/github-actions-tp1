#### 8. Accède à l'onglet "Actions" de ton repository sur GitHub. Que constates-tu ?

`"Hello World from GitHub Actions!"`

Le workflow hello.yml s'est bien déclenché automatiquement suite à au push. Il s'est exécuté avec succès (Statut : success) et le log affiche bien le message :
"Hello World from GitHub Actions!". GitHub Actions est bien configuré. Dès qu'un push est fait, il déclenche un workflow défini dans .github/workflows/.

#### 10. Commit et pousse ce nouveau workflow. Vérifie l'exécution dans l'onglet Actions. Que constates-tu ?

Le nouveau workflow test.yml s'exécute automatiquement et son statut est success.
Tous les tests définis avec pytest dans test_model.py sont passés sans erreur. GitHub Actions est capable d'installer les dépendances (pip install) et d'exécuter des tests unitaires automatiquement.

#### 11. Modifie le fichier model.py pour introduire un bug (change le retour de "positive" à "positif" par exemple). Que se passe-t-il lors du prochain push ?
Le workflow test.yml échoue. Dans les logs, on voit une erreur sur test_model.py :

`FAILED test_model.py::test_predict_positive - AssertionError: assert 'positif' == 'positive'`

#### 14. Que constates-tu après le push ?

Le workflow test.yml fonctionne correctement pour plusieurs versions de Python (3.8, 3.9, 3.10) grâce à la matrice de test.
Notre projet est compatible avec plusieurs versions de Python.

#### 27. Commit et pousse ces modifications. Vérifie l'onglet Actions et télécharge l'artifact généré. Que contient-il ?
`{
  "accuracy": 0.884,
  "precision": 0.915,
  "recall": 0.929,
  "f1_score": 0.974
}`

L'artifact stocke les résultats de l'évaluation du modèle. GitHub Actions peut produire et conserver des fichiers intermédiaires pour analyse ou usage ultérieur.


#### 30. Pousse plusieurs fois les modifications et observe les résultats. Que constates-tu ?
Lorsque accuracy est inférieure à 0.9, le workflow échoue avec un message d'erreur :

`❌ Model accuracy below threshold (0.9)`

Le workflow ne valide un modèle que s'il atteint un certain niveau de qualité (ici accuracy > 0.9).

#### 36. Vérifie dans l'onglet "Releases" de ton repository. Que constates-tu ?
Elle contient deux fichiers téléchargeables : un .zip et un .tar.gz du code source.


#### 38. Ajoute plus de commentaires à ton fichier model.py et pousse-le. Vérifie l'artifact de documentation. Que contient-il ?
L'artifact contient une documentation générée du fichier model.py, extraite automatiquement des docstrings, sous forme de markdown docs/model.md


#### 40. Ajoute une nouvelle dépendance à requirements.txt et pousse-la. Exécute ce workflow deux fois. Que constates-tu au niveau du temps d'exécution ?
Lors du premier push, l'installation des dépendances prend du temps (`pip install` classique). 

Lors du second push, l'installation est plus rapide grâce à la mise en cache automatique.
En utilisant `actions/cache`, on évite de réinstaller à chaque fois toutes les dépendances. 