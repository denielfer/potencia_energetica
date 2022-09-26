from osgeo import gdal
from PIL import Image
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
        if(tipo == 'v'):
            search_vect = vect
        elif(tipo == 'h'):
            search_vect = vect[0]
        topo = target*(a+1)*(1+tolerancia)
        chao = target*(a+1)*(1-tolerancia)
        while True:
            point = int(len(search_vect)/2)
            if(tipo == 'v'):
                soma = vect[:inicio+point].sum()
            elif(tipo == 'h'):
                soma = vect[:,:inicio+point].sum()
            left = soma<topo
            right = chao<soma
                # print(inicio+point, soma,target)
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

def get_img_separado(img_n,faixas,tolerancia=0.01,tipo='v',show=True):
    faixas = faixas_iguais(img_n,20,tolerancia=tolerancia,tipo=tipo)
    img = gdal.Open(img_n).ReadAsArray()[0]
    # print(faixas)
    for a in faixas:
        img[a] +=255
    # print(img.shape)
    if(show):
        Image.fromarray(img).show()
    return img

if __name__ == '__main__':
    img_n = 'BlackMarble_2012_3km_gray_geo.tif'
    #linha horizontal
    faixas = faixas_iguais(img_n,4,tolerancia=0.01)
    img = gdal.Open(img_n).ReadAsArray()
    print(faixas)
    for a in faixas:
        img[0][a] +=255
    print(img.shape)
    Image.fromarray(img[0]).show()

    #linha vertical
    faixas = faixas_iguais(img_n,2,tipo = 'h',tolerancia=0.01)
    img = gdal.Open(img_n).ReadAsArray()
    print(faixas)
    print(img.shape)
    for a in faixas:
        img[0][:,a] +=255
    Image.fromarray(img[0]).show()