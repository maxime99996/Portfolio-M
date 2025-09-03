# Notes sur le fonctionnement Pelican

## Chaîne de génération

La structure des dossiers (content, pages et veille) sont définis dans **pelicanconf.py** par les constantes : 
- `PATH` : dossier `content`
- `ARTICLE_PATHS` : dossier `veille`
- `PAGE_PATHS` : dossier `pages`

Les fichiers sont générés dans le dossier défini par la constante `OUTPUT_PATH` (défini à `output` par défaut).

Le nom des fichiers générés s'appuie sur la valeur associé à la clé `Title` du fichier **Markdown**.