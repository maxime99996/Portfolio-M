# Portfolio BTS SIO

Ce dépôt contient un modèle de portfolio statique pour les étudiants du BTS SIO (SLAM/SISR). Il est basé sur **[Pelican](https://blog.getpelican.com/)**, un générateur de site statique écrit en Python, et utilise **Bootstrap 5** pour la mise en page.

## 🎯 Objectifs pédagogiques

- Structurer son parcours, ses projets et ses compétences de manière professionnelle.
- Documenter sa veille technologique tout au long de l'année.
- Utiliser des outils du développement web modernes (Pelican, Jinja2, Markdown, Git).

---

## 🧰 Prérequis

- Python 3.10 ou supérieur
- Git
- Un éditeur de texte (VSCode recommandé)

---

## 🚀 Installation

```bash
# 1. Cloner le dépôt
git clone https://github.com/ljules/Portfolio-sio
cd Portfolio-SIO

# 2. Créer un environnement virtuel
python -m venv venv
source venv/bin/activate        # Linux/macOS
venv\Scripts\activate.bat       # Windows

# 3. Installer les dépendances
pip install pelican markdown --proxy http://IP_PROXY:PORT

# Remarque : Remplacer IP_PROXY par l'IP du serveur proxy (ex : 172.16.0.54 ou 172.16.0.51) et PORT par le numéro de port qui est toujours 8080.
```

---

## 🧪 Lancer le site en local

```bash
pelican -lr
```

Le site sera accessible sur : [http://localhost:8000](http://localhost:8000)

---

## 📁 Structure du projet

```
content/
├── pages/           → Pages statiques (parcours, projets, etc.)
├── veille/          → Articles de veille technologique
themes/
└── sio_portfolio/   → Thème personnalisé (Bootstrap 5 + Jinja2)
```

---

## 🧩 Modifier le contenu

### Modifier les pages

Les fichiers `.md` dans `content/pages/` contiennent vos pages statiques.

Exemple :

```markdown
Title: Mon parcours
Date: 2025-09-01
Save_as: pages/parcours.html
```

### Ajouter un article de veille

Créer un fichier `.md` dans `content/veille/` :

```markdown
Title: Lancement de GPT-5
Date: 2025-09-01
Tags: intelligence-artificielle, nlp
Summary: OpenAI annonce la sortie de GPT-5.
Category: Veille

Contenu complet de l’article...
```

---

## 🎨 Personnalisation

Le thème est situé dans `themes/sio_portfolio/` :

- Mise en page HTML : `templates/`
- Style CSS : `static/css/custom.css`
- Fichiers JS : `static/js/custom.js`
- Favicons : `static/logo/`

Tu peux modifier les fichiers dans `templates/` pour personnaliser le rendu de tes pages (`page.html`, `veille.html`, `article.html`, etc.).

---


---

## 📦 Générer la version finale pour la mise en production sur **GitHub IO**

```bash
pelican content -s publishconf.py
```

Les fichiers seront générés dans le dossier `docs/` avec les URLs configurées pour la mise en ligne.

Il faudra avant la publication sur **GitHub IO** :
1. Créer votre dépôt sur **GitHub** si cela n'est pas encore fait.
2. Activer la publication  de **GitHub IO** pour votre dépôt avec l'option `Deploy from a branch` et dans le dossier `docs` de la branche principale (_master_ ou _main_ selon votre choix ou stratégie).
3. Renseigner l'URL de votre page **GitHub IO** dans le fichier `publishconf.py` en renseignant la constante `SITEURL`.

---

Après l'exécution de la commande `pelican content -s publishconf.py`, votre portfolio pourra être _commité_ (`git commit -m "Message du commit"`) et poussé sur votre **GitHub** (`git push`) afin de le rendre accessible en production avec **GitHub IO**.


## 🧠 Ressources utiles

- [Documentation officielle de Pelican](https://docs.getpelican.com/en/latest/)
- [Guide Markdown rapide](https://www.markdownguide.org/cheat-sheet/)
- [Bootstrap 5](https://getbootstrap.com/)

---

## ✍️ Auteur

Développé dans le cadre du BTS SIO SLAM  
Modèle de base à adapter et personnaliser pour chaque étudiant.
