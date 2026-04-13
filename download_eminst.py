import os
import urllib.request
import zipfile
import shutil

def download_and_extract_emnist():
    """
    Télécharge et extrait la base de données EMNIST au format binaire (gzip).
    Intègre un User-Agent pour contourner les erreurs HTTP 403.
    """

    # URL officielle hébergée par le NIST
    url = "https://biometrics.nist.gov/cs_links/EMNIST/gzip.zip"
    zip_path = "emnist-gzip.zip"

    # Étape 1 : Téléchargement avec usurpation d'identité (User-Agent)
    print(f"Début du téléchargement depuis {url}...")
    print("Cette opération peut prendre quelques minutes (environ 500 Mo).")
    try:
        # Création d'une requête spécifique simulant un navigateur Chrome sur Windows
        req = urllib.request.Request(
            url, 
            headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}
        )
        
        # Exécution de la requête et écriture du fichier par blocs
        with urllib.request.urlopen(req) as response, open(zip_path, 'wb') as out_file:
            shutil.copyfileobj(response, out_file)
            
        print("Téléchargement terminé avec succès.")
    except Exception as e:
        print(f"Erreur lors du téléchargement : {e}")
        return

    # Étape 2 : Extraction
    print("Extraction des fichiers en cours...")
    try:
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall()
        print(f"Extraction terminée. Les fichiers bruts sont disponibles dans 'gzip/'.")
    except Exception as e:
        print(f"Erreur lors de l'extraction : {e}")
        return

    # Étape 3 : Nettoyage
    try:
        os.remove(zip_path)
        print("Nettoyage : Fichier archive .zip supprimé.")
    except OSError as e:
        print(f"Erreur lors de la suppression de l'archive : {e}")

if __name__ == "__main__":
    download_and_extract_emnist()