from PIL import Image
import numpy as np
import cv2


imagem = 'lena.jpg'
imagem_aberta = Image.open(imagem)
print(imagem_aberta.size)

def converter_para_cinza(imagem):
    largura, altura = imagem.size
    imagem_cinza = Image.new("L",  (largura, altura)) # Escala de cinza
    
    for y in range(altura):
        for x in range(largura):
            r, g, b = imagem.getpixel((x, y))
            valor_cinza = int(0.300 * r + 0.600 * g + 0.100 * b)
            imagem_cinza.putpixel((x, y), valor_cinza)
    return imagem_cinza

def converter_para_binario(imagem_cinza, limiar=127):
    largura, altura = imagem_cinza.size
    imagem_binaria = Image.new("1", (largura, altura)) # Binária

    for y in range(altura):
        for x in range(largura):
            valor_cinza = imagem_cinza.getpixel((x, y))
            valor_binario = 1 if valor_cinza > limiar else 0
            imagem_binaria.putpixel((x, y), valor_binario)
    return imagem_binaria

imagem_cinza = converter_para_cinza(imagem_aberta)
imagem_binaria = converter_para_binario(imagem_cinza)

imagem_cinza_np = np.array(imagem_cinza) # Transformando em array numpy
imagem_binaria_np = np.array(imagem_binaria) # Transformando em array numpy

imagem_binaria_np = imagem_binaria_np.astype(np.uint8) * 255 

cv2.imshow("Imagem Cinza", imagem_cinza_np)
cv2.imshow("Imagem Binária", imagem_binaria_np)

cv2.waitKey(0)
cv2.destroyAllWindows()