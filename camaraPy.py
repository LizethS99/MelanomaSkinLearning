import cv2
name=input("Ingrese el nombre del paciente: ")
captura = cv2.VideoCapture(0)
img_counter=0
while (captura.isOpened):
    ret, video= captura.read()
    if(ret):
        cv2.imshow('Frame', video)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            img_name=name+"_{}.jpg".format(img_counter)
            cv2.imwrite(img_name,video)
            print("¡{} guardada!".format(img_name))
            img_counter+=1
        """if cv2.waitKey(1) & 0x6C == ord('l'):
            break"""
captura.release()
cv2.destroyAllWindows()
"""Esto es una prueba"""

"""import cv2
name=input("Ingrese el nombre del paciente: ")
captura = cv2.VideoCapture(0)
img_counter=0
while (captura.isOpened):
    ret, video= captura.read()
    if(ret):
        cv2.imshow('Frame', video)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        if 0x6C == ord('l'):#l de Liz-to ya tienes tu foto
            img_name=name+"_{}".format(img_counter)
            cv2.imwrite(img_name,video)
            print("¡{} guardada!".format(img_name))
            img_counter+=1
captura.release()
cv2.destroyAllWindows()"""