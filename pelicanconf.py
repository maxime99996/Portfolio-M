#####################################################################
#                                                                   #
#                     FICHIER DE CONFIGURATION                      #
#                          DU PORTFOLIO                             #
#                                                                   #
#####################################################################

# IMPORTS :
# ---------
from datetime import datetime

SITENAME = 'Portfolio BTS SIO SLAM'
SITESUBTITLE = "Mon parcours de formation"
AUTHOR = 'Maxime GALLI'
SITEURL = "" 
TIMEZONE = 'Europe/Paris'
DEFAULT_LANG = 'fr'
CURRENT_YEAR = datetime.now().year
RELATIVE_URLS = True

PATH = "content"
THEME = 'themes/sio_portfolio'
ARTICLE_PATHS = ['veille']
PAGE_PATHS = ['pages']

STATIC_PATHS = ['images', 'pdfs']  # adapte selon tes besoins
OUTPUT_PATH = 'docs'

ARTICLE_URL = 'veille/{slug}.html'
ARTICLE_SAVE_AS = 'veille/{slug}.html'

PAGE_URL = 'pages/{slug}.html'
PAGE_SAVE_AS = 'pages/{slug}.html'

MENUITEMS = (
    ("Accueil", "/", "house", None, "Page d'accueil du portefolio", None),
    ("Mon parcours", "/pages/parcours", "mortarboard", None, "Découvrez mon parcours scolaire.", "primary"),
    ("Réalisations", "/pages/realisations", "check2-square", None, "Accédez aux projets et TP.", "success"),
    ("Veille techno.", "/ma-veille", "broadcast-pin", None, "Consultez mes articles de veille.", "warning"),
    ("Engagement", "/pages/engagement-etudiant", "people-fill", None, "Présentation de mon engagement étudiant.", None),
)

MAINITEMS = MENUITEMS[1:4]

PLUGIN_PATHS = ['plugins']
PLUGINS = []

SUMMARY_MAX_LENGTH = 100
DEFAULT_PAGINATION = 10

FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
TAG_FEED_ATOM = None
