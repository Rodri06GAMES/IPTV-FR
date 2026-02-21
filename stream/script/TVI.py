import requests
import re

M3U_FILE = "stream/TVI.m3u8"
TOKEN_URL = "https://services.iol.pt/matrix?userId"

def update_wms_auth_sign():
    try:
        token_response = requests.get(TOKEN_URL, timeout=10)
        token_response.raise_for_status()
        new_token = token_response.text.strip()

        with open(M3U_FILE, "r", encoding="utf-8") as f:
            content = f.read()

        updated_content = re.sub(
            r"wmsAuthSign=[^&]*",
            f"wmsAuthSign={new_token}",
            content
        )

        # ✅ Vérifier si changement
        if content == updated_content:
            print("ℹ Aucun changement détecté.")
            return True

        with open(M3U_FILE, "w", encoding="utf-8") as f:
            f.write(updated_content)

        print("✅ Fichier mis à jour.")
        return True

    except Exception as e:
        print(f"❌ Erreur: {e}")
        return False


if __name__ == "__main__":
    update_wms_auth_sign()
