#!/bin/bash

# Obtener el título de la canción actual
song_title=$(playerctl metadata title)

# Obtener el nombre del artista
artist=$(playerctl metadata artist)

# Imprimir la información de la canción actual
echo "$artist - $song_title"
