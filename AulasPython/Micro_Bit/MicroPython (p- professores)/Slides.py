Image() # Cria uma imagem 5x5 em branco.
Image(matriz) # Cria uma imagem baseado numa matriz de strings com valores de brilho para cada LED.
# Ex:
display.show(Image("90009\n"
                   "09090\n"
                   "00900\n"
                   "09090\n"
                   "90009"))
Image(width, height) # Cria uma imagem em branco no tamanho dado.
Image(width, height, buffer) # Cria uma imagem a partir do buffer dado.
# Ex:
display.show(Image(2, 2, bytearray([9,9,9,9])))

# Imagem - Métodos

# Retorna o número de colunas na imagem.
width()

# Retorna o número de linhas na imagem.
height()

# Muda o brilho do pixel na coluna x e linha y para o valor, que deve ser entre 0 e 9. Esse método irá lançar uma exceção quando for chamado em alguma imagem built-in read-only, como Image.HEART.
set_pixel(x, y, valor)

# Retorna o brilho do pixel na coluna x e na linha y como um inteiro entre 0 e 9.
get_pixel(x, y)

# Ex:
from microbit import *

imagem = Image("090\n"
               "909\n"
               "090\n")
while True:
    display.show(imagem)
    sleep(500)
    imagem.set_pixel(0,0,4)
    display.show(imagem)
    sleep(500)
    brilho = imagem.get_pixel(1,0)
    display.show(brilho)
    sleep(500)
    display.clear()

# Retorna uma nova imagem criado ao deslocar a original para a esquerda por n colunas.
shift_left(n)

# Igual a image.shift_left(-n)
shift_right(n)

# Retorna uma nova imagem criado ao deslocar a original para a cima por n linhas.
shift_up(n)

# Igual a image.shift_up(-n)
shift_down(n)

# Retorna uma nova imagem ao cortar a original para a largura w e a altura h, começando a partir do pixel na coluna x e linha y.
crop(x, y, w, h)

# Ex:
from microbit import *

imagem = Image("0440\n"
               "4994\n"
               "0440\n")

while True:
    display.show(imagem)
    sleep(500)
    imagem = imagem.shift_right(1)
    display.show(imagem)
    sleep(500)
    imagem = imagem.shift_down(1)
    display.show(imagem)
    sleep(500)
    imagem = imagem.shift_left(1)
    display.show(imagem)
    sleep(500)
    imagem = imagem.shift_up(1)
    display.show(imagem)
    sleep(500)
    imagem = imagem.crop(1, 1, 3, 3)
    display.show(imagem)
    sleep(500)
    imagem = Image("0440\n"
                   "4994\n"
                   "0440\n")

# Retorna uma cópia exata da imagem.
copy()

# Retorna uma nova imagem ao inverter o brilho dos pixels da imagem original.
invert()

# Muda o brilho de todos os pixels da imagem para o valor, que deve estar entre 0 (escuro) e 9 (brilhante). Esse método lançará uma exceção quando chamado em alguma imagem built-in read-only, como Image.HEART.
fill(value)

# Copia o retângulo definido por x, y, w, h da imagem original para esta imagem em xdest e ydest. Áreas no retângulo original, mas fora da imagem original são tratadas como tendo valor 0.
blit(src, x, y, w, h, xdest=0, ydest=0)

# Ex:
from microbit import *

while True:
    imagem = Image("0440\n"
                   "4994\n"
                   "0440\n")
    display.show(imagem)
    sleep(500)
    copia = imagem.copy()
    display.show(copia)
    sleep(500)
    invertido = imagem.invert()
    display.show(invertido)
    sleep(500)
    copia.fill(2)
    display.show(copia)
    sleep(500)
    imagem.blit(imagem, 0, 0, 3, 3, 1, 0)
    display.show(imagem)
    sleep(500)
    imagem.blit(imagem, 1, 0, 3, 2, 1, 1)
    display.show(imagem)
    sleep(500)
    imagem.blit(imagem, 1, 1, 3, 2, 0, 1)
    display.show(imagem)
    sleep(500)
    imagem.blit(imagem, 0, 1, 3, 2, 0, 0)
    display.show(imagem)
    sleep(500)
    imagem.blit(imagem, 1, 1, 3, 3, 1, 1)
    display.show(imagem)
    sleep(500)

# Imagem - Operações

# Cria uma string compacta representando a imagem.
repr(image)

# Cria uma string legível representando a imagem.
str(image)

# Cria uma nova imagem ao adicionar o valor de brilho das duas imagens para cada pixel.
image1 + image2

# Cria uma nova imagem ao multiplicar o brilho de cada pixel por n
image * n

# Display - Funções

# Rola value horizontalmente na display. Se value é um inteiro ou um float, ele é primeiro convertido para string. O delay define quão rápido o texto rola.
display.scroll(value, delay=150, *, wait=True, loop=False, monospace=False)

# Use on() para ligar o display.
display.on()

# Use off() para desligar o display (permitindo assim a reutilização dos pinos GPIO associados com o display para outros propósitos).
display.off()

# Retorna True se o display estiver ligada, caso contrário retorna False.
display.is_on()

# Usa os LEDs do display em modo viés-reverso para medir a quantidade de luz incidindo sobre o display. Retorna um inteiro entre 0 e 255 representando o nivel de luminosidade, com maior significando mais luz.
display.read_light_level()

# Ex:
from microbit import *

while True:
    brilho = display.read_light_level()
    if brilho < 10:
        display.show(brilho)
    else:
        display.scroll(brilho)

# UART - Funções

# Inicializa a comunicação serial com os parâmetros especificados nos pinos tx e rx especificados. Note que para uma comunicação correta, os parâmetro devem ser os mesmos em ambos dispositivos comunicando. O baudrate define a velocidade de comunicação. Valores de baud rate comuns são: 9600, 14400, 19200, 28800, 38400, 57600 e 115200. O bits define o tamanho dos bytes sendo transmitidos, a placa só suporta 8. O parity define como a paridade é checada, e pode ser None, uart.ODD ou uart.EVEN. O stop indica o número de bits de parada, e só pode ser 1 para essa placa.
uart.init(baudrate=9600, bits=8, parity=None, stop=1, *, tx=None, rx=None)

# Retorna True se algum dado está em espera, caso contrário retorna False.
uart.any()

# Lê bytes. Se nbyters for especificado, então no máximo essa quantidade de bytes, caso contrário lê quantos bytes for possível.
# Retorna um objeto bytes ou None em caso de timeout. Como caracteres em ASCII cabem em um único byte, o objeto bytes é geralmente usado para representar textos simples.
uart.read([nbytes])

# Ex:
from microbit import *

uart.init(baudrate=9600)
esperandoMensagem = [Image("00000\n"
                           "00000\n"
                           "90000\n"
                           "00000\n"
                           "00000\n"),
                     Image("00000\n"
                           "00000\n"
                           "90900\n"
                           "00000\n"
                           "00000\n"),
                     Image("00000\n"
                           "00000\n"
                           "90909\n"
                           "00000\n"
                           "00000\n")]
while True:
    if uart.any():
        display.clear()
        mensagem = str(uart.read(), 'UTF-8')
        display.scroll(mensagem)
    else:
        display.show(esperandoMensagem, delay=200, loop=True)

# Lê bytes para o buf. Se nbytes for specificado, então lê no máximo essa quantidade de bytes, senâo lê até len(buf) bytes.
# Retorna o número de bytes lidos e armazenados em buf ou None em caso de timeout.
uart.readinto(buf[, nbytes])

# Lê uma linha, terminando em um caractere de linha nova.
# Retorna a linha lida ou None em caso de timeout. O caractere de linha nova é incluido no bytes retornado.
uart.readline()

# Escreve o buf para o bus, pode ser um objeto bytes ou uma string.
# Retorna o numeros de bytes escritos ou None em caso de timeout.
uart.write(buf)

# Ex:
from microbit import *

uart.init(baudrate=9600)
display.show(1)
uart.write('hello world')
sleep(500)
display.show(2)
uart.write(b'hello world')
sleep(500)
display.show(3)
uart.write(bytes([1, 2, 3]))
A
# SPI - Funções

# Inicializa a comunicação SPI com os parâmetros especificados nos pinos escolhidos. O 'baudrate' define a velocidade de comunicação. O 'bits' define o tamanho dos bytes sendo transmitidos (atualmento só é suportado bits=8). O 'mode' determina a combinação entre polaridade e fase de clock. Os argumentos 'slck','mosi' e 'miso' specificam os pinos usados para cada tipo de sinal.
spi.init(baudrate=1000000, bits=8, mode=0, sclk=pin13, mosi=pin15, miso=pin14)

# Lê até 'nbytes' bytes, retorna o que foi lido.
spi.read(nbytes)

# Envia o 'buffer' de bytes para o barramento.
spi.write(buffer)

# Envia o 'out' buffer para o barramento e lê qualquer resposta para o 'in' buffer. Os buffers devem ter mesmo tamanho e podem ser o mesmo objeto.
spi.write_readinto(out, in)

# I2C - Funções

# Re-inicializa os periféricos com a frequência de clock especificada nos pinos sda e scl escolhidos.
i2c.init(freq=100000, sda=pin20, scl=pin19)

# Procura no barramento por dispositivos. Retorna uma lista de endereços de 7 bits correspondentes aos dispositivos que respondereram ao chamado.
i2c.scan()

# Lê 'n' bytes do dispositivo com o endereço de 7 bits 'addr'. Se 'repeat' for True, não será enviado um bit de parada.
i2c.read(addr, n, repeat=False)

# Escreve bytes de 'buf' no dispositivo com o endereço de 7 bits 'addr'. Se 'repeat' for True, não será enviado um bit de parada.
i2c.write(addr, buf, repeat=False)

# Acelerômetro - Funções

# Retorna a aceleração no eixo x como inteiro positivo ou negativo, dependendo da direção. As medidas retornadas são na ordem de milli-g. Por padrão, o acelerômetro é configurado para até +/- 2g, portanto esse método retornará até +/- 2000mg.
accelerometer.get_x()

# Retorna a aceleração no eixo y como inteiro positivo ou negativo, dependendo da direção. As medidas retornadas são na ordem de milli-g. Por padrão, o acelerômetro é configurado para até +/- 2g, portanto esse método retornará até +/- 2000mg.
accelerometer.get_y()

# Retorna a aceleração no eixo z como inteiro positivo ou negativo, dependendo da direção. As medidas retornadas são na ordem de milli-g. Por padrão, o acelerômetro é configurado para até +/- 2g, portanto esse método retornará até +/- 2000mg.
accelerometer.get_z()

# Retorna a aceleração em todos os eixos ao mesmo tempo, como uma tupla (lista imutável) de três elementos inteiros X, Y e Z, respectivamente. As medidas retornadas são na ordem de milli-g. Por padrão, o acelerômetro é configurado para até +/- 2g, portanto X, Y e Z terão valores até +/- 2000mg.
accelerometer.get_values()

# Retorna o nome do gesto atual.
accelerometer.current_gesture()

# Ex:
from microbit import *
while True:
    gesto = accelerometer.current_gesture()
    accelerometer.was_gesture
    if gesto == "shake":
        display.show(Image.CONFUSED)
        sleep(300)
        display.clear()
    elif gesto == "left":
        display.show(Image.ASLEEP)
        sleep(300)
        display.clear()
    elif gesto == "face down":
        display.show(Image.SAD)
        sleep(300)
        display.clear()
    elif gesto == "right":
        display.show(Image.ANGRY)
        sleep(300)
        display.clear()
    sleep(50)

# Retorna True ou False para indicar se o gesto 'name' está ativo.
microbit.accelerometer.is_gesture(name)

# Retorna True ou False para indicar se o gesto 'name' está ativo desde a última chamada.
microbit.accelerometer.was_gesture(name)

# Retorna uma tuple com o histórico de gestos. Os mais recentes são listados por último. Também limpa o histórico de gestos antes de retornar.
microbit.accelerometer.get_gestures()

# Ex:
# Autor original: Nicholas Tollervey. Fevereiro de 2016.
from microbit import *
import random

respostas = ["Isso eh certo", "Eh decididamente isso", "Sem nenhuma duvida", "Sim, definitivamente", "Pode contar com isso", "A meu ver, sim", "Provavelmente", "A previsao eh boa", "Sim", "Os sinais indicam que sim", "Resposta confusa, tente novamente", "Pergunte mais tarde", "Melhor nao te dizer agora", "Nao posso prever no momento", "Se concentre e pergunte novamente", "Nao conte com isso", "Minha resposta eh nao", "Minhas fontes dizem que nao", "A previsao nao parece tao boa", "Duvido"]

while True:
    display.show('8')
    if accelerometer.was_gesture('shake'):
        display.clear()
        sleep(1000)
        display.scroll(random.choice(respostas))
    sleep(10)
