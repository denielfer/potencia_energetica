import os

files = []
diretorio_lista_arquivos = "seções"
for p, d, arquivo in os.walk(diretorio_lista_arquivos):
    for a in arquivo: #concatena path com file name
        files.append(p+"/"+a)

from osgeo import gdal
import numpy as np
arr = []
for a in files:
    ds = gdal.Open(a)
    imarray = ds.ReadAsArray()
    print(a)
    n = a
    print(imarray.shape)
    # print(len(imarray[0][0]))
    im = imarray
    soma = 0
    a = im[0]
    l = 0
    for b in a:
        s = 0
        for c in b:
            s += c
            l+=c
        soma+= c/len(b)
        s += l/len(a)
        # print(s)
    print(s)
    arr.append((n,s))
print()
print(arr)
print()
print(sorted(arr,key=lambda x:x[1]))
# im.show()
    # s = np.zeros_like(imarray[0],dtype=np.float64)
    # b = np.zeros_like([ 0 for a in range(imarray.shape[0])])
    # for n,a in enumerate(imarray):
    #     b[n] = sum(a/len(a))
    #     for m,c in enumerate(a):
    #         s[m] += c
    #     # print(sum(a/len(a)))
    # print(len(imarray))
    # c = 0
    # p = 0
    # for n,a in enumerate(b):
    #     if(a>c):
    #         c = a
    #         p = n
    # print('maior ativação',c,' linha: ',p)
    # print('maior ativação',max(b),' linha: ',b[22])

    # for m,c in enumerate(s):
    #     s[m] = c/len(imarray)
    # print(max(s))
# #soma para pixel em linha
# for a in imarray: 
#     corres = np.array([0,0,0,0])
#     for b in a:
#         corres+= b
#     print(corres/len(a))
# print("_____________________________")
# #soma para cada pixel em uma coluna
# corres = [np.array([0,0,0,0]) for a in range(len(imarray[0]))]
# for n,a in enumerate(imarray): 
#     for b in a:
#         corres[n]+=b
# corres = np.array(corres)
# print(corres/len(imarray[0]))
