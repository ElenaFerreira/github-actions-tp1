#### 8. Accède à l'onglet "Actions" de ton repository sur GitHub. Que constates-tu ?

Statut success
"Hello World from GitHub Actions!"

#### 10. Commit et pousse ce nouveau workflow. Vérifie l'exécution dans l'onglet Actions. Que constates-tu ?

Statut success

#### 11. Modifie le fichier model.py pour introduire un bug (change le retour de "positive" à "positif" par exemple). Que se passe-t-il lors du prochain push ?

Erreur sur le test.yml
FAILED test_model.py::test_predict_positive - AssertionError: assert 'positif' == 'positive'
