#Generación de data set completo
import cv2
import os
import pandas as pd
def formatNum(n):
    strn = ""
    mod = 1000
    while n%mod==n:
        strn+="0"
        mod/=10
    return strn+str(n)

cont = 0
img_melanoma = []
imagen = []
idxDF = 0
bsq_row = ""
num=0
df_ph2 = pd.read_excel("./GIT/NewPH2.xlsx")
cols = df_ph2.columns.tolist()
df_Nph2 = pd.DataFrame(columns=cols)
for img in os.listdir('./PH2P'):
    bsq_row=img[:6]
    if num==0:
        num=int(bsq_row[3:6])
    bsq_idx = df_ph2.loc[df_ph2['Image Name']==bsq_row].to_dict()
    bsq_idx[cols[0]] = "IMD"+formatNum(num)
    values = []
    for i in cols:
        if cols.index(i) == 0:
            values.append(bsq_idx[i])
        else:
            dicAux = list(bsq_idx[i].values())
            if str(dicAux[0])=="nan":
                values.append("")
            else:
                values.append((str(dicAux[0])))
    df_Nph2.loc[len(df_Nph2)] = values
    values.clear()
    num+=1
    img_melanoma.append(img[:6])
    if num==0:
        num=int(img[3:6])
    if img.endswith('.bmp'):
        
        # Lee la imagen que deseas rotar
        imagen = cv2.imread(os.path.join('./PH2P', img))
        
        
        cv2.imwrite(f"./NewDataSet3/{img[:3]+formatNum(num)}.bmp", imagen)
        # Especifica el ángulo de rotación (en grados)
        angulo_rotacion = 18.8947368  # Cambia el ángulo según tus necesidades

        while angulo_rotacion < 360:
            bsq_idx[cols[0]] = "IMD"+formatNum(num)
            for i in cols:
                if cols.index(i) == 0:
                    values.append(bsq_idx[i])
                else:
                    dicAux = list(bsq_idx[i].values())
                    if str(dicAux[0])=="nan":
                        values.append("")
                    else:
                        values.append((str(dicAux[0])))
            df_Nph2.loc[len(df_Nph2)] = values
            values.clear()
            num+=1
            # Obtiene el centro de la imagen
            altura, ancho = imagen.shape[:2]
            centro = (ancho // 2, altura // 2)

            # Calcula la matriz de transformación de rotación
            matriz_rotacion = cv2.getRotationMatrix2D(centro, angulo_rotacion, 1.0)

            # Aplica la rotación a la imagen
            imagen_rotada = cv2.warpAffine(imagen, matriz_rotacion, (ancho, altura))

            # Si deseas guardar la imagen rotada en un archivo
            cv2.imwrite(f"./NewDataSet3/{img[:3]+formatNum(num)}.bmp", imagen_rotada)
            
            
            angulo_rotacion +=19

            if angulo_rotacion >340 and angulo_rotacion< 342:
                cont +=1 
                print(f"Imagen {img} rotada completa. Total: {cont}")
df_Nph2.to_excel("./PH2_Extend.xlsx",index=False)

