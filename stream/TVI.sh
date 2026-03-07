#!/bin/sh

TOKEN=$(wget -qO- "https://services.iol.pt/matrix?userId=" 2>/dev/null)

if [ -z "$TOKEN" ]; then
    echo "❌ Token inválido."
    exit 1
fi

echo "🔑 Token obtido: $TOKEN"

sed -i "s#wmsAuthSign=[^&]*#wmsAuthSign=$TOKEN#g" stream/TVI.m3u8

echo "✅ m3u8/TVI.m3u8 atualizado com sucesso."
