import pandas as pd
import cv2
import os
import openpyxl

df = pd.read_excel("NewPH2.xlsx",usecols=['Image Name','Common Nevus','Atypical Nevus','Melanoma'])
img_contEx = df['Image Name'].tolist()
img_data = []
img_names = []
listFormat = []
classes=["Common Nevus","Atypical Nevus","Melanoma"]
for idx,row in df.iterrows():
    listFormat.append(row['Image Name']+".bmp")  #image: 'IMD920.bmp', class: 'Melanoma'
    val_Comm = row['Common Nevus']
    val_Atyp = row['Atypical Nevus']
    val_Mela = row['Melanoma']
    classif=0
    if val_Comm == "X":
        classif=1
    elif val_Atyp=="X":
        classif=2
    elif val_Mela=="X":
        classif=3
    listFormat.append(classes[classif-1])
    print(listFormat)
    listFormat.clear()

    


for filename in os.listdir('./PH2'):
    img_names.append(filename[:6])
    if filename.endswith('.bmp'):
        img = cv2.imread(os.path.join('./PH2',filename))
        img_data.append(img)

