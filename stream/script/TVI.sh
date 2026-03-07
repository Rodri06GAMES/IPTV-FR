sed -i "s#wmsAuthSign=[^&]*#wmsAuthSign=$(wget -qO- https://services.iol.pt/matrix?userId -o /dev/null)#g" "TVI.m3u"
