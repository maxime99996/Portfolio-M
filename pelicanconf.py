#####################################################################
#                                                                   #
#                     FICHIER DE CONFIGURATION                      #
#                          DU PORTFOLIO                             #
#                                                                   #
#####################################################################

# IMPORTS :
# ---------
from datetime import datetime



# CONFIGURATION & INFORMATIONS GENERALES :
# ----------------------------------------
# Cette section contient les variables générales associé au site/portefolio.

SITENAME = 'Portfolio BTS SIO SLAM'
SITESUBTITLE = "Mon parcours de formation"
AUTHOR = 'John DOE'
SITEURL = "" # Est surchargé par l'url du serveur dans le fichier publishconf.py
TIMEZONE = 'Europe/Rome'
DEFAULT_LANG = 'fr'
CURRENT_YEAR = datetime.now().year
RELATIVE_URLS = True # Est surchargé par la valeur False dans le fichier publishconf.py


# CONFIGURATION DES DOSSIERS :
# ----------------------------
# Cette section définit la structure des dossiers

PATH = "content"                # Dossier des contenus (pages et articles)
THEME = 'themes/sio_portfolio'  # Dossier du thème
ARTICLE_PATHS = ['veille']      # Sous-dossier de PATH qui contient les articles de veille.
PAGE_PATHS = ['pages']          # Sous-dossier de PATH qui contient les pages statiques du site. 


# Pour les fichiers statiques :
STATIC_PATHS = []

# Dossier de sortie pour la publication :
OUTPUT_PATH = 'docs'           # Attention, pour la publication sur GitHub Pages le dossier doit être "/docs"



# URL & FICHIERS GENERES :
# ------------------------
# Cette section définit les constante utilisée par Pelican pour générer les url et nom des fichiers
# articles (veille) et pages.

ARTICLE_URL = 'veille/{slug}.html'
ARTICLE_SAVE_AS = 'veille/{slug}.html'

PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = 'pages/{slug}.html'



# STRUCTURE DU MENU DE NAVIGATION:
# --------------------------------

# ((nom, url, icone, (nom, url, icone),description, couleur)...)
MENUITEMS = (
    ("Accueil", "/", "house", None, "Page d'accueil du portefolio", None),

    ("Mon parcours", "/pages/parcours", "mortarboard",
        (
            ("Parcours scolaire", "/pages/parcours-scolaire"),
            ("Le BTS SIO", "/pages/bts-sio")
        ),
        "Découvrez mon parcours scolaire et professionnel.", "primary"
    ),

    ("Réalisations", "/pages/realisations", "check2-square",
        (
            ("TP majeurs", "/pages/tp-majeurs"),
            ("Stage de 1ère année", "/pages/stage-sio1"),
            ("Stage de 2e année", "/pages/stage-sio2"),
            ("Projets scolaires", "/pages/projets-scolaires"),
            ("Projets personnels", "/pages/projets-personnels"),                             # Optionnel
            ("Certifications complémentaires", "/pages/certifications-complementaires") # Optionnel
        ),
        "Accédez aux projets et TP réalisés pendant ma formation et à mes projets personnels.", "success"
     ),

    ("Veille techno.", "/ma-veille", "broadcast-pin",
        (
        ("Ma veille technologique", "/ma-veille"),
        ("Archive des articles", "/archives"),
        ("Liste des catégories", "/categories"),
        ("Liste des auteurs", "/authors"),
        ("Liste des mots clés", "/tags")
        ),
        "Consultez les articles de veille technologique que j’ai suivis durant cette année.", "warning"
    ),

    ("Engagement", "/pages/engagement-etudiant", "people-fill", None, "Présention de mon engagement étudiant.", None),    # Optionnel

)

MAINITEMS = MENUITEMS[1:4] # Récupération de PARCOURS, REALISATION & VEILLE pour afficage dans index.html



# PLUGINS :
# ---------
PLUGIN_PATHS = ['plugins']
PLUGINS = []



# ARTICLES & PAGINATION :
# -----------------------
# Options associée à la génération et pagination des articles (veille).

# Résumé des articles
SUMMARY_MAX_LENGTH = 100

# Pagination
DEFAULT_PAGINATION = 10


# RELATIVE_URLS = True



# Flux RSS/Atom :
# ---------------
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
TAG_FEED_ATOM = None
