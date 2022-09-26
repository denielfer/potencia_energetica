from osgeo import gdal
import numpy as np
def faixas_iguais(filename,qtd_faixas,tipo='v',tolerancia=.01) -> int:
    if(qtd_faixas <= 0):
        return None
    vect = gdal.Open(filename).ReadAsArray()[0]
    if(qtd_faixas == 1):
        return vect
    maximo = vect.sum()
    target = maximo/qtd_faixas
    print(maximo)
    # if(tipo == 'v'):
    points = []
    for a in range(qtd_faixas-1):
        inicio = 0
        search_vect = vect
        topo = target*(a+1)*(1+tolerancia)
        chao = target*(a+1)*(1-tolerancia)
        while True:
            point = int(len(search_vect)/2)
            if(tipo == 'v'):
                soma = vect[:inicio+point].sum()
                # print(inicio+point, soma,target)
                left = soma<topo
                right = chao<soma
                if(left and right):
                    points.append(inicio+point)
                    print(f'alvo: {target*(a+1):15.3f}\t,obtido: {soma:15.3f}\t,erro: {(soma-target*(a+1))/(target*(a+1))*100:5.3f}%')
                    # print(inicio+point)
                    break
                else:
                    # print(left, right)
                    if(left):
                        inicio+=point
                        search_vect = search_vect[point:]
                    else:
                        search_vect = search_vect[:point]
    return points
if __name__ == '__main__':
    img = 'BlackMarble_2012_3km_gray_geo.tif'
    faixas = faixas_iguais(img,20,tolerancia=0.01)
    from PIL import Image
    img = gdal.Open(img).ReadAsArray()
    print(faixas)
    for a in faixas:
        img[0][a] +=255
    # c = 0
    # for a in faixas:
    #     img[c][a] +=255
    #     c+=1
    #     if(c>len(img)):
    #         c=0
    print(img.shape)
    Image.fromarray(img[0]).show()
    # Image.fromarray(img, mode="RGB").show()