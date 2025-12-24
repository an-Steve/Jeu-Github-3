# 🗡️ La Quête du Cristal Perdu

Un jeu d'aventure textuel RPG complet développé en Python. Incarnez un héros légendaire dans une quête épique pour sauver votre village du Seigneur des Ténèbres !

![Python](https://img.shields.io/badge/Python-3.6+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Status-Complete-success.svg)

## 📖 Histoire

Il y a longtemps, le Cristal de Lumière protégeait votre village... Mais le Seigneur des Ténèbres l'a volé, plongeant le monde dans le chaos. Vous êtes le seul espoir de récupérer le cristal et sauver votre peuple !

## ✨ Fonctionnalités

### 🎮 Système de Jeu
- **Système RPG complet** avec statistiques (Vie, Force, Défense)
- **Progression par niveaux** avec gain d'expérience
- **Inventaire dynamique** pour gérer vos objets
- **Système monétaire** pour acheter équipement et potions

### 🗺️ Exploration
- **4 zones à explorer** :
  - 🏘️ Village de Lumière (point de départ)
  - 🌲 Forêt Sombre (ennemis de niveau moyen)
  - 🗿 Caverne Profonde (ennemis difficiles)
  - 🏰 Donjon du Seigneur des Ténèbres (boss final)
- **Événements aléatoires** lors de l'exploration
- **Trésors cachés** à découvrir

### ⚔️ Combat
- **Système de combat tactique** avec 4 actions :
  - Attaquer
  - Défendre (réduit les dégâts)
  - Utiliser une potion
  - Fuir (avec chance d'échec)
- **Variété d'ennemis** : Gobelins, Loups, Bandits, Squelettes, Araignées géantes
- **Boss final épique** : Le Seigneur des Ténèbres

### 🏪 Commerce
- **Magasin du village** pour acheter :
  - Potions de soin (30 gold)
  - Épée en acier - +5 Force (100 gold)
  - Armure légère - +3 Défense (80 gold)
- **Auberge** pour restaurer votre santé (20 gold)

### 🎨 Interface
- Interface textuelle soignée avec emojis
- Effets de texte progressif pour une ambiance immersive
- Menus clairs et intuitifs
- Statistiques détaillées du joueur

## 🚀 Installation

### Prérequis
- Python 3.6 ou supérieur

### Installation simple

1. **Clonez le dépôt**
```bash
git clone https://github.com/votre-username/quete-cristal-perdu.git
cd quete-cristal-perdu
```

2. **Lancez le jeu**
```bash
python3 jeu_aventure.py
```

Aucune dépendance externe n'est requise ! Le jeu utilise uniquement la bibliothèque standard Python.

## 🎯 Comment Jouer

### Commandes de base
- **Chiffres (1-8)** : Sélectionner une action spécifique au lieu
- **s** : Afficher vos statistiques
- **i** : Ouvrir votre inventaire
- **p** : Utiliser une potion de soin
- **q** : Quitter le jeu

### Conseils de gameplay

#### 🌟 Débuter
1. Explorez le village pour vous familiariser avec l'interface
2. Visitez le magasin pour voir l'équipement disponible
3. Partez dans la Forêt Sombre pour vos premiers combats

#### ⚔️ Combat
- **Attaquez** pour infliger des dégâts maximaux
- **Défendez** quand votre vie est basse pour réduire les dégâts
- **Utilisez des potions** stratégiquement
- **Fuyez** si le combat devient trop difficile (50% de chance)

#### 📈 Progression
- Combattez des ennemis pour gagner de l'expérience et de l'or
- Montez en niveau pour améliorer vos statistiques
- Achetez de l'équipement au magasin pour devenir plus puissant
- Explorez pour trouver des trésors et des potions

#### 🏆 Objectif final
- Atteignez **niveau 5** minimum
- Explorez la **Caverne** puis trouvez le **Donjon**
- Affrontez le **Seigneur des Ténèbres** et récupérez le Cristal !

## 📊 Caractéristiques Techniques

### Structure du Code
```
jeu_aventure.py
├── Classe Joueur
│   ├── Gestion des statistiques
│   ├── Système d'inventaire
│   └── Progression de niveau
├── Classe Ennemi
│   └── Comportement des adversaires
└── Classe Jeu
    ├── Gestion des lieux
    ├── Système de combat
    ├── Commerce (magasin/auberge)
    └── Boucle principale
```

### Statistiques du jeu
- **Lignes de code** : ~500
- **Classes** : 3 (Joueur, Ennemi, Jeu)
- **Lieux** : 4 zones explorables
- **Ennemis** : 6 types + 1 boss
- **Objets** : 5 types d'équipement/consommables

## 🎮 Captures d'écran

### Écran de démarrage
```
======================================================================
          LA QUÊTE DU CRISTAL PERDU
======================================================================

Il y a longtemps, le Cristal de Lumière protégeait votre village...
Mais le Seigneur des Ténèbres l'a volé, plongeant le monde dans le chaos.
Vous êtes le seul espoir de récupérer le cristal et sauver votre peuple!

👤 Entrez le nom de votre héros: 
```

### Interface de combat
```
⚔️ ⚔️ ⚔️ ⚔️ ⚔️ ⚔️ ⚔️ ⚔️ ⚔️ ⚔️ ⚔️ ⚔️ ⚔️ ⚔️ ⚔️ ⚔️ ⚔️ ⚔️ ⚔️ ⚔️ 
  UN GOBELIN APPARAÎT!
⚔️ ⚔️ ⚔️ ⚔️ ⚔️ ⚔️ ⚔️ ⚔️ ⚔️ ⚔️ ⚔️ ⚔️ ⚔️ ⚔️ ⚔️ ⚔️ ⚔️ ⚔️ ⚔️ ⚔️ 

--- Tour 1 ---
Votre vie: 100/100
Gobelin: 30/30

1. Attaquer
2. Défendre
3. Utiliser une potion
4. Fuir
```

### Statistiques du joueur
```
==================================================
  Héros - Niveau 3
==================================================
  Vie: 120/140
  Force: 16
  Défense: 9
  Expérience: 75/225
  Gold: 175
==================================================
```

## 🛠️ Personnalisation

Le jeu est facilement modifiable pour ajouter :
- De nouveaux ennemis
- D'autres zones d'exploration
- Plus d'objets et d'équipements
- Des quêtes secondaires
- Des compétences spéciales

Consultez le code source pour voir comment étendre le jeu !

## 🤝 Contribution

Les contributions sont les bienvenues ! N'hésitez pas à :
1. Fork le projet
2. Créer une branche pour votre fonctionnalité (`git checkout -b feature/NouvelleFonctionnalite`)
3. Commit vos changements (`git commit -m 'Ajout d'une nouvelle fonctionnalité'`)
4. Push vers la branche (`git push origin feature/NouvelleFonctionnalite`)
5. Ouvrir une Pull Request

## 📝 Idées d'améliorations

- [ ] Système de sauvegarde/chargement
- [ ] Plus de classes de personnages (Guerrier, Mage, Voleur)
- [ ] Système de compétences et sorts
- [ ] Quêtes secondaires
- [ ] Crafting d'objets
- [ ] Système d'alliés/compagnons
- [ ] Mode multijoueur
- [ ] Interface graphique (Pygame)

## 📜 License

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.

## 👤 Auteur

Créé avec ❤️ par [Votre Nom]

## 🌟 Remerciements

- Merci à la communauté Python
- Inspiré par les jeux d'aventure textuels classiques
- Émojis fournis par Unicode

---

**Amusez-vous bien et bonne chance dans votre quête ! ⚔️🛡️✨**

*Si vous aimez ce projet, n'hésitez pas à lui donner une ⭐ !*
