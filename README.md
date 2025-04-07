
# 📚 Gestionnaire de Bibliothèque (Console)

Ce projet est une application console en Python permettant de gérer une petite bibliothèque personnelle. Vous pouvez y ajouter des livres, les emprunter, les rendre, rechercher des titres, et sauvegarder l'état de la bibliothèque.

---

## ✨ Fonctionnalités

- Ajouter de nouveaux livres
- Emprunter / rendre un livre
- Afficher les livres disponibles
- Rechercher un livre (par titre, auteur, ou mot-clé)
- Sauvegarder et charger la bibliothèque (format JSON)
- Affectation d’un identifiant unique à chaque livre
- Interface en ligne de commande avec menu interactif

---

## 💻 Utilisation

1. **Lancer le programme** (Python 3 requis) :
   ```bash
   python3 nom_du_script.py
   ```

2. **Menu principal** :
   ```
   ____MENU____
   1 : Add new book.
   2 : Borrow a book.
   3 : Return a book.
   4 : Display available books.
   5 : Save library.
   6 : Load new library.
   7 : Quit.
   ```

---

## 📂 Format de sauvegarde

Les livres sont sauvegardés dans un fichier JSON (`lib1.json` par défaut) avec les informations suivantes :
- Titre
- Auteur
- Année
- Statut (disponible ou emprunté)
- ID unique

---

## ⚠️ Exceptions gérées

- `BookOut` : livre déjà emprunté
- `BookIn` : livre déjà rendu
- `UnknownBook` : livre non trouvé
- Gestion d’erreurs de lecture/écriture JSON

---

## 🛠️ Dépendances

Aucune ; le programme ne nécessite que Python 3 (pas de bibliothèques externes).

---

## 📌 À venir

- Interface graphique ? (Tkinter ou autre)
- Suivi des emprunts par utilisateur
- Statistiques de lecture / emprunts

---

## 👤 Auteur

Projet réalisé par LittlePinkSloth.

---

