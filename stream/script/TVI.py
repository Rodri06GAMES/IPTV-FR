import requests
import re

M3U_FILE = "stream/TVI.m3u8"
TOKEN_URL = "https://services.iol.pt/matrix?userId="  # Completa com o userId se necessário

def update_wms_auth_sign():
    try:
        token_response = requests.get(TOKEN_URL, timeout=10)
        token_response.raise_for_status()
        new_token = token_response.text.strip()

        # Validar que o token não está vazio e parece válido
        if not new_token or "<" in new_token:
            print("❌ Token inválido ou resposta inesperada.")
            return False

        with open(M3U_FILE, "r", encoding="utf-8") as f:
            content = f.read()

        # Usar re.escape para evitar problemas com caracteres especiais no token
        updated_content = re.sub(
            r"wmsAuthSign=[^&\s]*",
            f"wmsAuthSign={re.escape(new_token)}",
            content
        )

        # Verificar se houve alteração
        if content == updated_content:
            print("ℹ️ Nenhuma alteração detectada.")
            return True

        with open(M3U_FILE, "w", encoding="utf-8") as f:
            f.write(updated_content)

        print("✅ Ficheiro atualizado com sucesso.")
        return True

    except requests.exceptions.Timeout:
        print("❌ Erro: Timeout ao contactar o servidor.")
        return False
    except requests.exceptions.RequestException as e:
        print(f"❌ Erro de rede: {e}")
        return False
    except FileNotFoundError:
        print(f"❌ Erro: Ficheiro '{M3U_FILE}' não encontrado.")
        return False
    except Exception as e:
        print(f"❌ Erro inesperado: {e}")
        return False


if __name__ == "__main__":
    update_wms_auth_sign()
