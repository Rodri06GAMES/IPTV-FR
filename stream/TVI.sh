#!/bin/sh

TOKEN=$(wget -qO- "https://services.iol.pt/matrix?userId=" 2>/dev/null)

if [ -z "$TOKEN" ]; then
    echo "❌ Token inválido."
    exit 1
fi

echo "🔑 Token: $TOKEN"

printf "#EXTM3U\nhttps://video-auth6.iol.pt/live_tvi/live_tvi/playlist.m3u8?wmsAuthSign=%s\n" "$TOKEN" > TVI.m3u8

echo "✅ TVI.m3u8 criado com sucesso."
cat TVI.m3u8
