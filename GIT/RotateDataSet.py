import cv2

# Lee la imagen que deseas rotar
imagen = cv2.imread('nombre_de_tu_imagen.jpg')

# Especifica el ángulo de rotación (en grados)
angulo_rotacion = 45  # Cambia el ángulo según tus necesidades

# Obtiene el centro de la imagen
altura, ancho = imagen.shape[:2]
centro = (ancho // 2, altura // 2)

# Calcula la matriz de transformación de rotación
matriz_rotacion = cv2.getRotationMatrix2D(centro, angulo_rotacion, 1.0)

# Aplica la rotación a la imagen
imagen_rotada = cv2.warpAffine(imagen, matriz_rotacion, (ancho, altura))

# Muestra la imagen rotada (puedes omitir esto si no deseas mostrarla)
cv2.imshow('Imagen Rotada', imagen_rotada)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Si deseas guardar la imagen rotada en un archivo
cv2.imwrite('nombre_de_la_imagen_rotada.jpg', imagen_rotada)
