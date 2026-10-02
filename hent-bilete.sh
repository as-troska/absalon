#!/bin/sh
# Køyr i same mappe som index.html. Hentar bileta frå Wikimedia Commons til bilete/
set -u
mkdir -p bilete
UA="AbsalonBergen/1.0 (skuleprosjekt; https://absalon.sneaas.no)"
hent() {
  if curl -fsSL -A "$UA" -o "bilete/$2" "https://commons.wikimedia.org/wiki/Special:FilePath/$1?width=1600"; then
    echo "OK    $2"
  else
    echo "FEIL  $2  ($1)"
  fi
}
hent "Scoleus.jpg"                 scholeus.jpg
hent "Scoleus_Martinskirken.jpg"   martinskirken.jpg
hent "Scoleus_Mariakirken.jpg"     mariakirken.jpg
hent "Scoleus_(cropped)_Bryggen.jpg" bryggen.jpg
file bilete/*
