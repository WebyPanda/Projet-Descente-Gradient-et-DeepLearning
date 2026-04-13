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
```

(Note : Pillow est utilisé pour l'acquisition d'images dans le pipeline Scénario, matplotlib pour la visualisation des courbes d'erreur).

### 2. Clonage du dépôt
```bash
git clone [https://github.com/WebyPanda/Projet-Descente-Gradient-et-DeepLearning.git](https://github.com/WebyPanda/Projet-Descente-Gradient-et-DeepLearning.git)
cd Projet-Descente-Gradient-et-DeepLearning
```

### 3. Téléchargement du Dataset (EMNIST)
En raison de sa taille volumineuse, la base de données EMNIST n'est pas versionnée sur ce dépôt. Un script d'automatisation est fourni pour la récupérer depuis les serveurs officiels du NIST.
Exécutez la commande suivante à la racine du projet :
```Bash
python download_emnist.py
```

Le script créera automatiquement un dossier gzip/ contenant les fichiers requis pour l'entraînement de l'algorithme.

## ⚙️ Structure du Projet
```Plaintext
📁 Projet-Descente-Gradient-et-DeepLearning/
├── 📄 download_emnist.py    # Script de récupération sécurisée du dataset
├── 📄 reseau_neurones.py    # Cœur mathématique du perceptron (Architecture, Forward, Backward)
├── 📄 entrainement.py       # Algorithmes d'optimisation (Batch, Stochastique, Mini-Batch, Moment)
├── 📄 scenario.py           # Pipeline de vision par ordinateur (Binarisation, Rognage, Inférence)
├── 📁 data/                 # Dossier local généré contenant EMNIST (ignoré par Git)
├── 📁 images_test/          # Répertoire destiné aux photographies à analyser
└── 📄 README.md             # Documentation
```

## 📊 Performances Expérimentales
Afin d'éviter les phénomènes de goulot d'étranglement de l'information sur le dataset EMNIST Balanced (47 classes : chiffres, lettres majuscules et minuscules), l'architecture finale retenue possède deux couches cachées de dimension [512, 256].
Paramètres synaptiques ajustés : > $5,4 \times 10^5$ poids et biais.Méthode d'entraînement : Gradient stochastique par Mini-Batch (lots de 50).Taux de réussite final : 85,2 % en généralisation. (Sur un set réduit aux chiffres uniquement, la précision dépasse les 96 %).

## 👥 Contributeurs (Prépa Toulouse Transitions)
Thomas Mauline : Optimisation algorithmique (Vectorisation NumPy, typage strict) et conception du pipeline de traitement d'images (Scénario).
Thomas Stapelfeld : Structure des couches intermédiaires, modélisation théorique et implémentation de la rétropropagation.
Albert Tellia : Modélisation mathématique des neurones, recherche sur l'architecture réseau et implémentation des algorithmes de descente de gradient.
Sacha Garrouste : Intégration et manipulation des structures de la base de données EMNIST.
Jeanne Reberga : Intégration globale du code, gestion des présentations et mise au propre des architectures algorithmiques.
