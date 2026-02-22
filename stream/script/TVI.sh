#!/bin/sh

TOKEN=$(wget -qO- "https://services.iol.pt/matrix?userId=")

if [ -z "$TOKEN" ]; then
    echo "❌ Token inválido."
    exit 1
fi

echo "🔑 Token obtido: $TOKEN"

sed -i "/live_tvi\/live_tvi/ c https://video-auth6.iol.pt/live_tvi/live_tvi/playlist.m3u8?wmsAuthSign=$TOKEN" stream/TVI.m3u8

echo "✅ TVI.m3u8 atualizado com sucesso."
