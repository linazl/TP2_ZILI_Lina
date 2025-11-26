# TP2 DevOps – GitHub Actions & Tests Unitaires

**Auteure : ZILI Lina**

---

## 📌 Introduction

Dans le cadre du TP DevOps, l’objectif était d’automatiser l’intégration continue (CI) d’un projet Python grâce à Git, GitHub, GitHub Actions et des tests unitaires.  
Ce README décrit toutes les étapes réalisées, comme dans mon rapport de projet.

---

## 1️⃣ Étape 1 — Création du Workflow GitHub Actions

- Création du dépôt GitHub  
- Ajout du fichier `.github/workflows/main.yml`  
- Workflow configuré pour exécuter les tests unitaires à chaque push ou Pull Request  
- Vérification que le workflow passe en vert ✅

**📸 Capture d’écran : Création du fichier main.yml**  
<img width="2210" height="1260" alt="image" src="https://github.com/user-attachments/assets/884cc39e-a93d-42be-932d-85b8837768b8" />

**📸 Capture d’écran : Ouverture du repo sur VS Code**  
<img width="523" height="195" alt="Screenshot 2025-11-26 114031" src="https://github.com/user-attachments/assets/953c7b60-ca38-4d7b-a39a-554107db7a29" />


**📸 Capture d’écran : Exécution des tests unitaires** 
<img width="2256" height="1504" alt="Screenshot 2025-11-26 115256" src="https://github.com/user-attachments/assets/055daca0-b40f-4462-b41a-def56000edcb" />


---

## 2️⃣ Étape 2 — Création de l’Application Python

L’application contient trois fonctions principales :  
- `addition(a, b)`  
- `soustraction(a, b)`  
- `multiplication(a, b)`  

Les tests unitaires se trouvent dans `tests/test_app.py`.

**📸 Capture d’écran : Ajouter les fichiers de l'applicationn sur GitHub** 
<img width="1224" height="410" alt="Screenshot 2025-11-26 115427" src="https://github.com/user-attachments/assets/46263a5f-5266-4abd-8abd-b840d1a5a72d" />

**📸 Capture d’écran : Code de app.py**  
<img width="2230" height="1262" alt="Screenshot 2025-11-26 121259" src="https://github.com/user-attachments/assets/ebd2b71f-104c-4115-8c10-e116a9f7c0a1" />


**📸 Capture d’écran : Code de test_app.py**  
<img width="2222" height="1253" alt="image" src="https://github.com/user-attachments/assets/dce862f6-d0c2-4b23-b161-98e9922e190d" />


---

## 3️⃣ Étape 3 — Création d’une Branche et d’une Pull Request

- Création d’une branche `feature/ajout-multiplication`  
- Ajout des modifications  
- Push vers GitHub  
- Création d’une Pull Request  
- Vérification que le workflow s’exécute automatiquement sur la PR

**📸 Capture d’écran : Création de la branche**  
<img width="1494" height="306" alt="Screenshot 2025-11-26 121144" src="https://github.com/user-attachments/assets/230f0471-2207-4083-9235-7d2027324e87" />


**📸 Capture d’écran : Création de la Pull Request**  
<img width="1634" height="824" alt="Screenshot 2025-11-26 121445" src="https://github.com/user-attachments/assets/02bbaed8-4684-407d-9cc8-d3da5bd76a59" />

<img width="1645" height="1191" alt="Screenshot 2025-11-26 121526" src="https://github.com/user-attachments/assets/01454428-3e25-4838-b725-a228bde0c40c" />

<img width="1630" height="484" alt="Screenshot 2025-11-26 121623" src="https://github.com/user-attachments/assets/e356fcc0-afe3-4932-8056-a1e45a334386" />


**📸 Capture d’écran : Nouveau Code du fichier app.py**  
<img width="2225" height="1251" alt="Screenshot 2025-11-26 122506" src="https://github.com/user-attachments/assets/7e29ba74-c957-4649-94c2-9fd1a9a8acd3" />

---

## 4️⃣ Étape 4 — Test volontairement en échec

Un test a été volontairement modifié pour provoquer un échec du CI :

    assert addition(2, 2) == 5  # volontairement faux

**📸 Capture d’écran : Nouveau Code avec l'erreur volontaire**  
<img width="1349" height="737" alt="Screenshot 2025-11-26 123145" src="https://github.com/user-attachments/assets/fdad4e97-8831-4301-bd04-1530a202086f" />

<img width="1665" height="924" alt="Screenshot 2025-11-26 123417" src="https://github.com/user-attachments/assets/dc265130-d9ec-4531-b319-2f0a2c2741d0" />

<img width="1285" height="276" alt="Screenshot 2025-11-26 123539" src="https://github.com/user-attachments/assets/b05aae2d-eeb3-463c-8080-fcf1b66910a2" />

## 5️⃣ FIN.



