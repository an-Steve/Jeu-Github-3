
"""
Jeu d'Aventure: La Quête du Cristal Perdu
Un jeu d'aventure textuel complet en Python
"""

import random
import time
import sys

class Joueur:
    def __init__(self, nom):
        self.nom = nom
        self.vie = 100
        self.vie_max = 100
        self.force = 10
        self.defense = 5
        self.niveau = 1
        self.experience = 0
        self.exp_prochain_niveau = 100
        self.gold = 50
        self.inventaire = ["Épée rouillée", "Potion de soin"]
        self.quetes_completees = []
        self.position = "village"
        
    def afficher_stats(self):
        print(f"\n{'='*50}")
        print(f"  {self.nom} - Niveau {self.niveau}")
        print(f"{'='*50}")
        print(f"  Vie: {self.vie}/{self.vie_max}")
        print(f"  Force: {self.force}")
        print(f"  Défense: {self.defense}")
        print(f"  Expérience: {self.experience}/{self.exp_prochain_niveau}")
        print(f"  Gold: {self.gold}")
        print(f"{'='*50}\n")
    
    def afficher_inventaire(self):
        print(f"\n{'='*50}")
        print("  INVENTAIRE")
        print(f"{'='*50}")
        if self.inventaire:
            for i, item in enumerate(self.inventaire, 1):
                print(f"  {i}. {item}")
        else:
            print("  Votre inventaire est vide.")
        print(f"{'='*50}\n")
    
    def gagner_experience(self, exp):
        self.experience += exp
        print(f"\n✨ Vous gagnez {exp} points d'expérience!")
        
        if self.experience >= self.exp_prochain_niveau:
            self.monter_niveau()
    
    def monter_niveau(self):
        self.niveau += 1
        self.experience = 0
        self.exp_prochain_niveau = int(self.exp_prochain_niveau * 1.5)
        
        gain_vie = random.randint(10, 20)
        gain_force = random.randint(2, 5)
        gain_defense = random.randint(1, 3)
        
        self.vie_max += gain_vie
        self.vie = self.vie_max
        self.force += gain_force
        self.defense += gain_defense
        
        print(f"\n{'*'*50}")
        print(f"  🎉 NIVEAU SUPÉRIEUR! Vous êtes maintenant niveau {self.niveau}!")
        print(f"{'*'*50}")
        print(f"  Vie max: +{gain_vie}")
        print(f"  Force: +{gain_force}")
        print(f"  Défense: +{gain_defense}")
        print(f"  Vie restaurée au maximum!")
        print(f"{'*'*50}\n")
        time.sleep(2)
    
    def utiliser_potion(self):
        if "Potion de soin" in self.inventaire:
            soin = random.randint(30, 50)
            self.vie = min(self.vie + soin, self.vie_max)
            self.inventaire.remove("Potion de soin")
            print(f"\n💚 Vous buvez une potion et récupérez {soin} points de vie!")
            print(f"   Vie actuelle: {self.vie}/{self.vie_max}")
            return True
        else:
            print("\n❌ Vous n'avez pas de potion de soin!")
            return False

class Ennemi:
    def __init__(self, nom, vie, force, defense, exp, gold):
        self.nom = nom
        self.vie = vie
        self.vie_max = vie
        self.force = force
        self.defense = defense
        self.exp = exp
        self.gold = gold

class Jeu:
    def __init__(self):
        self.joueur = None
        self.lieux = {
            "village": {
                "nom": "Village de Lumière",
                "description": "Un paisible village où vous avez grandi. Des maisons en bois bordent la place centrale.",
                "actions": ["explorer", "magasin", "auberge", "quitter_village"]
            },
            "foret": {
                "nom": "Forêt Sombre",
                "description": "Une forêt dense et mystérieuse. Des bruits étranges résonnent entre les arbres.",
                "actions": ["explorer", "combattre", "retour_village"]
            },
            "caverne": {
                "nom": "Caverne Profonde",
                "description": "Une caverne humide et sombre. Vous sentez une présence maléfique.",
                "actions": ["explorer", "combattre", "retour_foret"]
            },
            "donjon": {
                "nom": "Donjon du Seigneur des Ténèbres",
                "description": "Un donjon terrifiant d'où émane une aura de malveillance.",
                "actions": ["combattre_boss", "retour_village"]
            }
        }
        
        self.ennemis_foret = [
            Ennemi("Gobelin", 30, 8, 2, 25, 15),
            Ennemi("Loup Sauvage", 25, 10, 1, 30, 10),
            Ennemi("Bandit", 35, 12, 3, 40, 25)
        ]
        
        self.ennemis_caverne = [
            Ennemi("Chauve-souris Géante", 40, 15, 3, 50, 30),
            Ennemi("Squelette", 45, 18, 5, 60, 35),
            Ennemi("Araignée Venimeuse", 50, 20, 4, 70, 40)
        ]
        
        self.boss = Ennemi("Seigneur des Ténèbres", 150, 25, 10, 500, 1000)
        
    def afficher_texte_lent(self, texte, delai=0.03):
        """Affiche le texte caractère par caractère pour un effet dramatique"""
        for char in texte:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delai)
        print()
    
    def introduction(self):
        print("\n" + "="*70)
        self.afficher_texte_lent("          LA QUÊTE DU CRISTAL PERDU", 0.05)
        print("="*70 + "\n")
        time.sleep(1)
        
        self.afficher_texte_lent("Il y a longtemps, le Cristal de Lumière protégeait votre village...")
        time.sleep(0.5)
        self.afficher_texte_lent("Mais le Seigneur des Ténèbres l'a volé, plongeant le monde dans le chaos.")
        time.sleep(0.5)
        self.afficher_texte_lent("Vous êtes le seul espoir de récupérer le cristal et sauver votre peuple!\n")
        time.sleep(1)
        
        nom = input("👤 Entrez le nom de votre héros: ").strip()
        if not nom:
            nom = "Héros"
        
        self.joueur = Joueur(nom)
        print(f"\n⚔️  Bienvenue, {self.joueur.nom}! Votre aventure commence...\n")
        time.sleep(1)
    
    def afficher_lieu(self):
        lieu = self.lieux[self.joueur.position]
        print(f"\n{'='*70}")
        print(f"  📍 {lieu['nom']}")
        print(f"{'='*70}")
        print(f"  {lieu['description']}")
        print(f"{'='*70}\n")
    
    def menu_actions(self):
        lieu = self.lieux[self.joueur.position]
        print("Actions disponibles:")
        
        actions_texte = {
            "explorer": "1. Explorer les environs",
            "combattre": "2. Chercher un combat",
            "magasin": "3. Visiter le magasin",
            "auberge": "4. Se reposer à l'auberge (20 or)",
            "quitter_village": "5. Quitter le village",
            "retour_village": "6. Retourner au village",
            "retour_foret": "7. Retourner à la forêt",
            "combattre_boss": "8. Affronter le boss final",
            "stats": "s. Afficher vos statistiques",
            "inventaire": "i. Ouvrir l'inventaire",
            "potion": "p. Utiliser une potion",
            "quitter": "q. Quitter le jeu"
        }
        
        num = 1
        for action in lieu['actions']:
            if action in actions_texte:
                print(f"  {actions_texte[action]}")
        
        print(f"\n  {actions_texte['stats']}")
        print(f"  {actions_texte['inventaire']}")
        print(f"  {actions_texte['potion']}")
        print(f"  {actions_texte['quitter']}\n")
    
    def combat(self, ennemi):
        print(f"\n{'⚔️ '*20}")
        print(f"  UN {ennemi.nom.upper()} APPARAÎT!")
        print(f"{'⚔️ '*20}\n")
        time.sleep(1)
        
        tour = 1
        while self.joueur.vie > 0 and ennemi.vie > 0:
            print(f"\n--- Tour {tour} ---")
            print(f"Votre vie: {self.joueur.vie}/{self.joueur.vie_max}")
            print(f"{ennemi.nom}: {ennemi.vie}/{ennemi.vie_max}\n")
            
            print("1. Attaquer")
            print("2. Défendre")
            print("3. Utiliser une potion")
            print("4. Fuir")
            
            choix = input("\nVotre action: ").strip()
            
            if choix == "1":
                # Attaque du joueur
                degats = max(1, self.joueur.force + random.randint(-3, 5) - ennemi.defense)
                ennemi.vie -= degats
                print(f"\n⚔️  Vous attaquez {ennemi.nom} et infligez {degats} dégâts!")
                
                if ennemi.vie <= 0:
                    print(f"\n🎉 Victoire! Vous avez vaincu {ennemi.nom}!")
                    self.joueur.gagner_experience(ennemi.exp)
                    self.joueur.gold += ennemi.gold
                    print(f"💰 Vous gagnez {ennemi.gold} pièces d'or!")
                    
                    # Chance de trouver une potion
                    if random.random() < 0.3:
                        self.joueur.inventaire.append("Potion de soin")
                        print("💚 Vous trouvez une potion de soin!")
                    
                    time.sleep(2)
                    return True
                
                # Attaque de l'ennemi
                degats_ennemi = max(1, ennemi.force + random.randint(-2, 3) - self.joueur.defense)
                self.joueur.vie -= degats_ennemi
                print(f"💥 {ennemi.nom} vous attaque et inflige {degats_ennemi} dégâts!")
                
            elif choix == "2":
                print("\n🛡️  Vous vous mettez en position défensive!")
                degats_ennemi = max(0, (ennemi.force + random.randint(-2, 3) - self.joueur.defense) // 2)
                self.joueur.vie -= degats_ennemi
                print(f"💥 {ennemi.nom} attaque mais vous bloquez la plupart des dégâts! ({degats_ennemi} dégâts)")
                
            elif choix == "3":
                if self.joueur.utiliser_potion():
                    degats_ennemi = max(1, ennemi.force + random.randint(-2, 3) - self.joueur.defense)
                    self.joueur.vie -= degats_ennemi
                    print(f"💥 {ennemi.nom} profite de votre distraction et inflige {degats_ennemi} dégâts!")
                else:
                    continue
                
            elif choix == "4":
                if random.random() < 0.5:
                    print("\n🏃 Vous parvenez à fuir le combat!")
                    time.sleep(1)
                    return False
                else:
                    print("\n❌ Impossible de fuir!")
                    degats_ennemi = max(1, ennemi.force + random.randint(-2, 3) - self.joueur.defense)
                    self.joueur.vie -= degats_ennemi
                    print(f"💥 {ennemi.nom} vous attaque pendant votre fuite! ({degats_ennemi} dégâts)")
            
            if self.joueur.vie <= 0:
                print("\n💀 Vous avez été vaincu...")
                print("GAME OVER")
                return False
            
            tour += 1
            time.sleep(1)
        
        return True
    
    def explorer(self):
        if self.joueur.position == "village":
            evenements = [
                "Vous discutez avec les villageois. Ils vous parlent d'une forêt dangereuse au nord.",
                "Un vieil homme vous donne une amulette porte-bonheur.",
                "Vous entendez des rumeurs sur un trésor caché dans une caverne.",
                "Un forgeron vous parle d'armes légendaires."
            ]
        elif self.joueur.position == "foret":
            evenements = [
                "Vous trouvez un coffre contenant 50 pièces d'or!",
                "Vous découvrez des traces de créatures dangereuses.",
                "Un chemin secret mène vers une caverne sombre.",
                "Vous trouvez des herbes médicinales et gagnez une potion!"
            ]
        else:
            evenements = [
                "Vous trouvez des ossements anciens...",
                "Une inscription mystérieuse est gravée sur le mur.",
                "Vous sentez une présence maléfique tout près.",
                "Vous découvrez un passage vers le donjon du boss!"
            ]
        
        print(f"\n🔍 {random.choice(evenements)}\n")
        
        if "50 pièces d'or" in evenements[-1] and random.random() < 0.3:
            self.joueur.gold += 50
        
        if "potion" in evenements[-1] and random.random() < 0.3:
            self.joueur.inventaire.append("Potion de soin")
        
        time.sleep(2)
    
    def magasin(self):
        print(f"\n{'='*70}")
        print("  🏪 MAGASIN DU VILLAGE")
        print(f"{'='*70}")
        print(f"  Votre or: {self.joueur.gold}")
        print(f"{'='*70}")
        print("  1. Potion de soin (30 or)")
        print("  2. Épée en acier (+5 force) (100 or)")
        print("  3. Armure légère (+3 défense) (80 or)")
        print("  4. Retour")
        print(f"{'='*70}\n")
        
        choix = input("Que voulez-vous acheter? ").strip()
        
        if choix == "1" and self.joueur.gold >= 30:
            self.joueur.gold -= 30
            self.joueur.inventaire.append("Potion de soin")
            print("\n✅ Vous avez acheté une potion de soin!")
        elif choix == "2" and self.joueur.gold >= 100:
            self.joueur.gold -= 100
            self.joueur.force += 5
            self.joueur.inventaire.append("Épée en acier")
            print("\n✅ Vous avez acheté une épée en acier! Force +5")
        elif choix == "3" and self.joueur.gold >= 80:
            self.joueur.gold -= 80
            self.joueur.defense += 3
            self.joueur.inventaire.append("Armure légère")
            print("\n✅ Vous avez acheté une armure légère! Défense +3")
        elif choix == "4":
            return
        else:
            print("\n❌ Or insuffisant ou choix invalide!")
        
        time.sleep(2)
    
    def auberge(self):
        if self.joueur.gold >= 20:
            self.joueur.gold -= 20
            self.joueur.vie = self.joueur.vie_max
            print("\n🏨 Vous vous reposez à l'auberge et récupérez toute votre vie!")
            time.sleep(2)
        else:
            print("\n❌ Vous n'avez pas assez d'or! (20 or nécessaires)")
            time.sleep(2)
    
    def jouer(self):
        self.introduction()
        
        while self.joueur.vie > 0:
            self.afficher_lieu()
            self.menu_actions()
            
            choix = input("Votre choix: ").strip().lower()
            
            if choix == "q":
                print("\n👋 Merci d'avoir joué! À bientôt!")
                break
            
            elif choix == "s":
                self.joueur.afficher_stats()
            
            elif choix == "i":
                self.joueur.afficher_inventaire()
            
            elif choix == "p":
                self.joueur.utiliser_potion()
                time.sleep(1)
            
            elif choix == "1":
                self.explorer()
            
            elif choix == "2" and self.joueur.position in ["foret", "caverne"]:
                if self.joueur.position == "foret":
                    ennemi = random.choice(self.ennemis_foret)
                else:
                    ennemi = random.choice(self.ennemis_caverne)
                
                ennemi_copie = Ennemi(ennemi.nom, ennemi.vie, ennemi.force, ennemi.defense, ennemi.exp, ennemi.gold)
                self.combat(ennemi_copie)
            
            elif choix == "3" and self.joueur.position == "village":
                self.magasin()
            
            elif choix == "4" and self.joueur.position == "village":
                self.auberge()
            
            elif choix == "5" and self.joueur.position == "village":
                print("\n🌲 Vous entrez dans la Forêt Sombre...")
                self.joueur.position = "foret"
                time.sleep(1)
            
            elif choix == "6":
                print("\n🏘️  Vous retournez au village...")
                self.joueur.position = "village"
                time.sleep(1)
            
            elif choix == "7" and self.joueur.position == "caverne":
                print("\n🌲 Vous retournez à la forêt...")
                self.joueur.position = "foret"
                time.sleep(1)
            
            elif choix == "8" and self.joueur.position == "donjon":
                print("\n⚠️  Vous vous préparez à affronter le Seigneur des Ténèbres!")
                time.sleep(2)
                boss_copie = Ennemi(self.boss.nom, self.boss.vie, self.boss.force, 
                                   self.boss.defense, self.boss.exp, self.boss.gold)
                
                if self.combat(boss_copie):
                    print("\n" + "="*70)
                    print("  🎊 FÉLICITATIONS! 🎊")
                    print("="*70)
                    print("  Vous avez vaincu le Seigneur des Ténèbres!")
                    print("  Le Cristal de Lumière est récupéré!")
                    print("  Votre village est sauvé!")
                    print("="*70 + "\n")
                    break
            
            else:
                # Navigation cachée vers caverne et donjon
                if self.joueur.position == "foret" and choix == "caverne":
                    print("\n🗿 Vous découvrez l'entrée de la caverne...")
                    self.joueur.position = "caverne"
                    time.sleep(1)
                elif self.joueur.position == "caverne" and choix == "donjon" and self.joueur.niveau >= 5:
                    print("\n🏰 Vous trouvez le donjon du Seigneur des Ténèbres!")
                    self.joueur.position = "donjon"
                    time.sleep(1)
                else:
                    print("\n❌ Choix invalide!")
                    time.sleep(1)

# Lancement du jeu
if __name__ == "__main__":
    jeu = Jeu()
    jeu.jouer()