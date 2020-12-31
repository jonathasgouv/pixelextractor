from colorsys import hsv_to_rgb
from PIL import Image, ImageDraw
from numpy import loadtxt

pix_val_flat = []
pix_val_flat2 = []

# Importa lista de pixels
caminho = str(input("Digite o caminho do arquivo que deseja transformar em imagem: "))
f = open(caminho, 'r')
pix_val_flat = f.read().split(",")
f.close()

pix_val_flat = list(map(int, pix_val_flat))

a = len(pix_val_flat)
l = len(pix_val_flat) - 1

altura = pix_val_flat[a-1]
largura = pix_val_flat[l-1]

size = [altura, largura]

del(pix_val_flat[a-1])
del(pix_val_flat[l-1])

pix_val_flat2 = pix_val_flat

# Converte lista de pixels em bytes
pix_val_flat2 = bytes(pix_val_flat2)
novaimagem = Image.frombytes('RGB', (size), pix_val_flat2)


# Pede o endereço e salva nova imagem
caminhof = str(input("Digite o caminho de onde deseja salvar a imagem: "))
novaimagem.save(caminhof+'.jpg')
novaimagem.show()