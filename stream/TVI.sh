#!/bin/sh

CONTENT=$(wget -qO- "https://video-auth6.iol.pt/live_tvi/live_tvi/playlist.m3u8?wmsAuthSign=$(wget -qO- https://services.iol.pt/matrix?userId= 2>/dev/null)" 2>/dev/null \
| sed "s#edge_servers#https://video-auth6.iol.pt/edge_servers#g")

if [ -z "$CONTENT" ]; then
    echo "❌ Conteúdo m3u8 inválido."
    exit 1
fi

echo "$CONTENT" > stream/TVI.m3u8

echo "✅ stream/TVI.m3u8 criado com sucesso."
cat stream/TVI.m3u8
