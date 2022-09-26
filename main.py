import util
import filtro_de_terra
import valor_medio_img
gray = util.get_all_files_from_directory('seções')
colored = util.get_all_files_from_directory('seções cor')

vec = []
for n,a in enumerate(gray):
    print("Processando: ",a)
    selected = colored[n] if(a.split('_')[2] in colored[n]) else None
    if(selected is None):
        t = a.split('_')[2]
        for b in colored:
            if t in b:
                selected = b
    value = valor_medio_img.valor_medio(a)
    map = filtro_de_terra.filtra_terra(selected,retorno='s')
    vec.append((a,value/map))
vec.sort(key=lambda x: x[1],reverse=True)
print(vec)