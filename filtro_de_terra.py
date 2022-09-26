from osgeo import gdal
import numpy as np

def filtra_terra(imagem_com_corres,valor_agua = 9,show = False,save_img=False,retorno=None,save_name=None):
    imarray = gdal.Open(imagem_com_corres).ReadAsArray().astype(np.uint16)
    f = (np.add(np.add(imarray[0],imarray[1]),imarray[2])/3).astype(np.uint8)>valor_agua
    if(show or save_img):
        try:
            from PIL import Image
            img = Image.fromarray(f.astype(int) *255)
            if(show):
                img.show()
            if(save_img):
                img.save(save_name if save_name is not None else 'terar/'+imagem_com_corres.split('/')[1].split('.')[0]+'_filtrado.png' )
        except Exception as e:
            print(f"Não foi possivel mostrar imagem. {e}")
    return f.sum() if retorno == 's' else f

if __name__ == "__main__":
            filtra_terra(f'seções cor/BlackMarble_2012_D2_geo.tif',retorno='s',show=True)