import cv2
import os
cont = 0
img_melanoma = []
imagen = []
for img in os.listdir('./PH2'):
    img_melanoma.append(img[:6])
    if img.endswith('.bmp'):
        # Lee la imagen que deseas rotar
        imagen = cv2.imread(os.path.join('./PH2', img))
        # Especifica el ángulo de rotación (en grados)
        angulo_rotacion = 18.8947368  # Cambia el ángulo según tus necesidades

        while angulo_rotacion < 360:
            # Obtiene el centro de la imagen
            altura, ancho = imagen.shape[:2]
            centro = (ancho // 2, altura // 2)

            # Calcula la matriz de transformación de rotación
            matriz_rotacion = cv2.getRotationMatrix2D(centro, angulo_rotacion, 1.0)

            # Aplica la rotación a la imagen
            imagen_rotada = cv2.warpAffine(imagen, matriz_rotacion, (ancho, altura))

            # Si deseas guardar la imagen rotada en un archivo
            cv2.imwrite(f"./NewDataSet3/{img[:6]}_{angulo_rotacion:.2f}.bmp", imagen_rotada)

            angulo_rotacion +=19

            if angulo_rotacion >340 and angulo_rotacion< 342:
                cont +=1 
                print(f"Imagen {img} rotada completa. Total: {cont}")
                