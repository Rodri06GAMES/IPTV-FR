import requests
import re

M3U_FILE = "stream/TVI.m3u8"
TOKEN_URL = "https://services.iol.pt/matrix?userId"

def update_wms_auth_sign():
    try:
        # 1️⃣ Récupérer le nouveau token (équivalent à wget -qO-)
        token_response = requests.get(TOKEN_URL, timeout=10)
        token_response.raise_for_status()
        new_token = token_response.text.strip()

        print(f"🔑 Nouveau token récupéré: {new_token}")

        # 2️⃣ Lire le fichier M3U
        with open(M3U_FILE, "r", encoding="utf-8") as f:
            content = f.read()

        # 3️⃣ Remplacer wmsAuthSign=... par le nouveau token
        updated_content = re.sub(
            r"wmsAuthSign=[^&]*",
            f"wmsAuthSign={new_token}",
            content
        )

        # 4️⃣ Écrire le fichier modifié
        with open(M3U_FILE, "w", encoding="utf-8") as f:
            f.write(updated_content)

        print("✅ Fichier TVI.m3u mis à jour avec succès.")
        return True

    except Exception as e:
        print(f"❌ Erreur: {e}")
        return False


if __name__ == "__main__":
    update_wms_auth_sign()
