from microbit import *

foto1 = ("11911:"
         "44044:"
         "70707:"
         "99099:"
         "00900")
foto2 = ("94049:"
         "11111:"
         "05050:"
         "13731:"
         "22022")
foto3 = ("15151:"
         "46264:"
         "55555:"
         "22222:"
         "98742")

album = {"foto1": Image(foto1), "foto2": Image(foto2), "foto3": Image(foto3)}

fotos = ("foto1", "foto2", "foto3")

indice = 0

while True:
    if button_a.was_pressed():
        indice = indice + 1
    if button_b.was_pressed():
        indice = indice - 1
    if indice < 0:
        indice = len(fotos) - 1
    if indice >= len(fotos):
        indice = 0
    display.show(album[fotos[indice]])