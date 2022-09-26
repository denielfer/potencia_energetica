from osgeo import gdal
import numpy as np

def filtra_terra(imagem_com_corres,valor_agua = 9,show = False,save_img=False,retorno=None,save_name=None):
    imarray = gdal.Open(imagem_com_corres).ReadAsArray().astype(np.uint16)
    f = (np.add(np.add(imarray[0],imarray[1]),imarray[2])/3).astype(np.uint8)>valor_agua
    if(show + save_img):
        try:
            from PIL import Image
            img = Image.fromarray(f.astype(int) *255)
            if(show):
                img.show()
            if(save_img):
                img.save(save_name if save_name is not None else imagem_com_corres.split('.')[0].join('_filtrado') )
        except Exception as e:
            print(f"Não foi possivel mostrar imagem. {e}")
    return f.sum() if retorno == 's' else f