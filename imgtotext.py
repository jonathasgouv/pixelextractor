from colorsys import hsv_to_rgb
from PIL import Image, ImageDraw

# Pede o endereço da imagem
caminho = str(input("Digite o caminho da imagem:  "))


imagem = Image.open(caminho, "r")
pix_val = list(imagem.getdata())
pix_val_flat = [x for sets in pix_val for x in sets]

size = imagem.size
altura = str(size[0])
largura = str(size[1])
pix_val_flat.append(int(altura))
pix_val_flat.append(int(largura))

caminhoc = str(input("Digite onde deseja salvar a imagem convertida/como texto:  "))

with open(caminhoc + ".jntsg", "a+") as myfile:
    myfile.write(",".join(map(str, pix_val_flat)))