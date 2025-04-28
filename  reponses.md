#### 8. Accède à l'onglet "Actions" de ton repository sur GitHub. Que constates-tu ?

Statut success
"Hello World from GitHub Actions!"

#### 10. Commit et pousse ce nouveau workflow. Vérifie l'exécution dans l'onglet Actions. Que constates-tu ?

Statut success

#### 11. Modifie le fichier model.py pour introduire un bug (change le retour de "positive" à "positif" par exemple). Que se passe-t-il lors du prochain push ?

Erreur sur le test.yml
FAILED test_model.py::test_predict_positive - AssertionError: assert 'positif' == 'positive'

#### 14. Que constates-tu après le push ?

Statut success


#### 27. Commit et pousse ces modifications. Vérifie l'onglet Actions et télécharge l'artifact généré. Que contient-il ?
{
  "accuracy": 0.884,
  "precision": 0.915,
  "recall": 0.929,
  "f1_score": 0.974
}

#### 30. Pousse plusieurs fois les modifications et observe les résultats. Que constates-tu ?
Run ACCURACY=$(python -c "import json; f=open('metrics.json');
Model accuracy: 0.888
❌ Model accuracy below threshold (0.9)
Error: Process completed with exit code 1.

-> Ce qu'on veut


#### 36. Vérifie dans l'onglet "Releases" de ton repository. Que constates-tu ?
J'ai ma release avec deux fichiers à télécharger
code source
un zip et un tar.gz


#### 38. Ajoute plus de commentaires à ton fichier model.py et pousse-le. Vérifie l'artifact de documentation. Que contient-il ?
<a id="model"></a>
# model
<a id="model.predict_sentiment"></a>
#### predict\_sentiment
```python
def predict_sentiment(text)
```
Predict the sentiment of a given text.
**Arguments**:
- `text` _str_ - The input text to analyze.
**Returns**:
- `str` - The predicted sentiment ('positive', 'negative', or 'neutral').


#### 40. Ajoute une nouvelle dépendance à requirements.txt et pousse-la. Exécute ce workflow deux fois. Que constates-tu au niveau du temps d'exécution ?
