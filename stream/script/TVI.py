import requests
import re
import os

M3U8_OUTPUT = "stream/TVI.m3u8"
TOKEN_URL = "https://services.iol.pt/matrix?userId="

SOURCE_URL_BASE = "https://video-auth6.iol.pt/live_tvi/live_tvi/playlist.m3u8?wmsAuthSign="

def update_tvi_m3u8():
    try:
        # 1️⃣ Obter o token
        token_response = requests.get(TOKEN_URL, timeout=10)
        token_response.raise_for_status()
        new_token = token_response.text.strip()

        if not new_token or "<" in new_token:
            print("❌ Token inválido ou resposta inesperada.")
            return False

        print(f"🔑 Token obtido: {new_token}")

        # 2️⃣ Construir a URL com o token
        source_url = f"{SOURCE_URL_BASE}{new_token}"
        print(f"🌐 URL fonte: {source_url}")

        # 3️⃣ Obter o conteúdo do ficheiro m3u8
        m3u8_response = requests.get(source_url, timeout=10)
        m3u8_response.raise_for_status()
        m3u8_content = m3u8_response.text

        if not m3u8_content.strip().startswith("#EXTM3U"):
            print("❌ Conteúdo m3u8 inválido.")
            return False

        print(f"📄 Conteúdo m3u8 obtido ({len(m3u8_content)} caracteres).")

        # 4️⃣ Guardar no ficheiro TVI.m3u8
        with open(M3U8_OUTPUT, "w", encoding="utf-8") as f:
            f.write(m3u8_content)

        print(f"✅ Ficheiro {M3U8_OUTPUT} atualizado com sucesso.")
        return True

    except requests.exceptions.RequestException as e:
        print(f"❌ Erro de rede: {e}")
        return False
    except Exception as e:
        print(f"❌ Erro inesperado: {e}")
        return False


if __name__ == "__main__":
    success = update_tvi_m3u8()
    exit(0 if success else 1)
