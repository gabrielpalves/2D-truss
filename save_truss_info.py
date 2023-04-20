import pandas as pd
import numpy as np

def save_truss_info(data, secoes, material, group, conec, x, y, GDL_rest, forcas, no_critico, pp, gravidade, gama_d, n):
    filename = 'output_' + str(n) + '.xlsx'
    with pd.ExcelWriter(filename) as writer:
        data.to_excel(writer, sheet_name="analysis")

        # Salva os materiais e seção na database
        df_sec = pd.DataFrame(secoes, index=list(range(1, secoes.shape[0]+1)), columns = ["A", "b", "t", "Ix", "Iy", "rx", "ry", "rz_min", "wdt", "J", "W", "x", "s4g"])
        df_sec.to_excel(writer, sheet_name="sections")

        df_mat = pd.DataFrame(material, index=list(range(1, material.shape[0]+1)), columns = ["E", "fy_k", "density"])
        df_mat.to_excel(writer, sheet_name="materials")

        # Salva os grupos
        df_gru = pd.DataFrame(group, index=list(range(1, group.shape[0]+1)), columns=np.zeros((group.shape[1])))
        df_gru.to_excel(writer, sheet_name="groups")
        
        # Salva as coordenadas e conectividades
        coord = np.array([x,y])
        df_coo = pd.DataFrame(coord, index=['x', 'y'], columns=list(range(1, x.shape[0]+1)))
        df_coo.to_excel(writer, sheet_name="coord")
        
        df_con = pd.DataFrame(conec[:,-2:], index=list(range(1, conec.shape[0]+1)), columns=['node 1', 'node 2'])
        df_con.to_excel(writer, sheet_name="elements")
        
        # Salva os GDL restringidos
        df_res = pd.DataFrame(GDL_rest, index=list(range(1, GDL_rest.shape[0]+1)), columns=['node', 'rest x', 'rest y'])
        df_res.to_excel(writer, sheet_name="GDL_rest")
        
        # Salva as forças
        df_for = pd.DataFrame(forcas, index=list(range(1, forcas.shape[0]+1)), columns=['node', 'Fx', 'Fy'])
        df_for.to_excel(writer, sheet_name="ext forces")
        
        # Salva informações
        df_inf = pd.DataFrame([pp, gravidade, gama_d, no_critico], index=['self weight coef', 'gravity', 'fy_k reduction', 'observed node'])
        df_inf.to_excel(writer, sheet_name="info")