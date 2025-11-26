# TP2 DevOps – GitHub Actions & Tests Unitaires

**Auteure : ZILI Lina**

---

## 📌 Introduction

Dans   le cadre du TP DevOps, l’objectif était d’automatiser l’intégration continue (CI) d’un projet Python grâce à Git, GitHub, GitHub Actions et des tests unitaires.  
Ce README décrit toutes les étapes réalisées, comme dans mon rapport de projet.

---

## 1️⃣ Étape 1 — Création du Workflow GitHub Actions

- Création du dépôt GitHub  
- Ajout du fichier `.github/workflows/main.yml`  
- Workflow configuré pour exécuter les tests unitaires à chaque push ou Pull Request  
- Vérification que le workflow passe en vert ✅

**📸 Capture d’écran : création du workflow**  

**📸 Capture d’écran : workflow en vert**  
[Insérer screenshot ici]

---

## 2️⃣ Étape 2 — Création de l’Application Python

L’application contient trois fonctions principales :  
- `addition(a, b)`  
- `soustraction(a, b)`  
- `multiplication(a, b)`  

Les tests unitaires se trouvent dans `tests/test_app.py`.

**📸 Capture d’écran : code de app.py**  
[Insérer screenshot ici]

**📸 Capture d’écran : code de test_app.py**  
[Insérer screenshot ici]

---

## 3️⃣ Étape 3 — Création d’une Branche et d’une Pull Request

- Création d’une branche `feature/ajout-multiplication`  
- Ajout des modifications  
- Push vers GitHub  
- Création d’une Pull Request  
- Vérification que le workflow s’exécute automatiquement sur la PR

**📸 Capture d’écran : création de la branche**  
[Insérer screenshot ici]

**📸 Capture d’écran : création de la Pull Request**  
[Insérer screenshot ici]

**📸 Capture d’écran : workflow lancé automatiquement**  
[Insérer screenshot ici]

---

## 4️⃣ Étape 4 — Ajout des Tests Unitaires dans le Workflow

Les tests sont déjà intégrés dans le fichier `main.yml` et s’exécutent automatiquement avec `pytest`.

**📸 Capture d’écran : pytest dans le workflow**  
[Insérer screenshot ici]

---

## 5️⃣ Étape 5 — Test volontairement en échec

Un test a été volontairement modifié pour provoquer un échec du CI :

```python
def test_addition():
    assert addition(2, 2) == 5  # volontairement faux
