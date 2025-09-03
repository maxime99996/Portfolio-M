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
git clone https://github.com/ton-utilisateur/portfolio-bts-sio.git
cd portfolio-bts-sio

# 2. Créer un environnement virtuel
python -m venv venv
source venv/bin/activate        # Linux/macOS
venv\Scripts\activate.bat     # Windows

# 3. Installer les dépendances
pip install pelican markdown
```

---

## 🧪 Lancer le site en local

```bash
make devserver
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

## 🧼 Nettoyer la génération

```bash
make clean
```

---

## 📦 Générer la version finale

```bash
make publish
```

Les fichiers seront générés dans le dossier `output/` avec les URLs configurées pour la mise en ligne.

---

## 🧠 Ressources utiles

- [Documentation officielle de Pelican](https://docs.getpelican.com/en/latest/)
- [Guide Markdown rapide](https://www.markdownguide.org/cheat-sheet/)
- [Bootstrap 5](https://getbootstrap.com/)

---

## ✍️ Auteur

Développé dans le cadre du BTS SIO SLAM  
Modèle de base à adapter et personnaliser pour chaque étudiant.
