# Projet 15 : Descente de Gradient et Apprentissage Profond

Ce dépôt contient l'implémentation intégrale d'un réseau de neurones artificiels (Perceptron Multicouche), développé *from scratch* en Python. L'objectif de ce projet est d'identifier et de classer des caractères manuscrits issus de la base de données EMNIST, en s'appuyant exclusivement sur les mathématiques fondamentales de la descente de gradient et de la rétropropagation, sans recours à des bibliothèques de Machine Learning de haut niveau (telles que TensorFlow ou PyTorch).

## 📌 Fonctionnalités Principales

- **Modélisation Théorique :** Implémentation mathématique stricte de la propagation avant (*Feedforward*) et de la rétropropagation de l'erreur via la règle de la chaîne (*Chain Rule*).
- **Optimisation Algorithmique :** Vectorisation absolue des calculs matriciels via `NumPy` pour exploiter l'architecture SIMD du processeur, éliminant les boucles logicielles et réduisant les temps d'exécution de manière drastique.
- **Entraînement Avancé :** Comparaison et implémentation de plusieurs algorithmes d'optimisation. Utilisation de la descente de gradient par Mini-Batch couplée à la méthode du Moment pour assurer une convergence rapide et stable.
- **Pipeline de Prétraitement (Scénario) :** Module autonome de traitement photographique (Lissage Gaussien, Binarisation d'Otsu dynamique, Normalisation par Padding) transformant une image brute en signal d'entrée vectoriel exploitable.

## 🚀 Installation et Prérequis

### 1. Dépendances
Le projet requiert un environnement Python 3.x et les bibliothèques standards suivantes :
```bash
pip install numpy Pillow matplotlib
