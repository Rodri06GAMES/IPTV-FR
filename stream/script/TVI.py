import requests
import re
import os

M3U_FILE = "stream/TVI.m3u8"
TOKEN_URL = "https://services.iol.pt/matrix?userId="  # ← adiciona o userId aqui ou via variável de ambiente

def update_wms_auth_sign():
    try:
        # 1️⃣ Récupérer le nouveau token
        token_response = requests.get(TOKEN_URL, timeout=10)
        token_response.raise_for_status()
        new_token = token_response.text.strip()

        if not new_token or "<" in new_token:
            print("❌ Token inválido ou resposta inesperada.")
            return False

        print(f"🔑 Novo token obtido: {new_token}")

        # 2️⃣ Lire le fichier M3U
        with open(M3U_FILE, "r", encoding="utf-8") as f:
            content = f.read()

        # 3️⃣ Remplacer wmsAuthSign=...
        updated_content = re.sub(
            r"wmsAuthSign=[^&\s]*",
            f"wmsAuthSign={re.escape(new_token)}",  # ← re.escape() importante
            content
        )

        if content == updated_content:
            print("ℹ️ Nenhuma alteração necessária.")
            return True

        # 4️⃣ Écrire le fichier modifié
        with open(M3U_FILE, "w", encoding="utf-8") as f:
            f.write(updated_content)

        print("✅ Ficheiro TVI.m3u atualizado com sucesso.")
        return True

    except requests.exceptions.RequestException as e:
        print(f"❌ Erro de rede: {e}")
        return False
    except FileNotFoundError:
        print(f"❌ Ficheiro '{M3U_FILE}' não encontrado.")
        return False
    except Exception as e:
        print(f"❌ Erro inesperado: {e}")
        return False


if __name__ == "__main__":
    success = update_wms_auth_sign()
    exit(0 if success else 1)  # ← importante para a GitHub Action detectar falhas
