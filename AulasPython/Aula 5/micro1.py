from microbit import *

tupla1 = ("11911:"
          "44044:"
          "70707:"
          "99099:"
          "00900")

# Escreva a tupla2 conforme o padrao da tupla1 (com números de 0 a 9 que representam o brilho do LED) para fazer uma nova imagem
tupla2 = ("94049:"
          "11111:"
          "05050:"
          "13731:"
          "22022")

while True:
    display.show(Image(tupla1))
    sleep(1000)
    display.show(Image(tupla2))
    sleep(1000)