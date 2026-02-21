import requests
import os

SOURCE_M3U = "https://raw.githubusercontent.com/LITUATUI/M3UPT/refs/heads/main/M3U/TVI.m3u"
OUTPUT_FILE = "stream/tvi.m3u8"

def download_and_copy():
    try:
        # Télécharger le fichier source
        response = requests.get(SOURCE_M3U, timeout=10)
        response.raise_for_status()

        # Créer le dossier si nécessaire
        os.makedirs("stream", exist_ok=True)

        # Copier tout le contenu tel quel dans le fichier output
        with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
            f.write(response.text)

        print(f"✅ Toutes les lignes ont été copiées dans {OUTPUT_FILE}")
        return True

    except Exception as e:
        print(f"❌ Erreur: {str(e)}")
        return False

if __name__ == "__main__":
    if not download_and_copy():
        exit(1)
