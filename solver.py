import csv
import numpy as np

def lerArquivo (nome_arq):

    with open (nome_arq) as csv_file:

        arquivo_csv = csv_file.readlines()
        array_arquivo = csv.reader (arquivo_csv, delimiter=' ', skipinitialspace=True)
        
        aux = list (array_arquivo)

        for linha in aux:
            del linha[9]

        np_arquivo = np.array (aux).astype("int")

    return np_arquivo


FILE_EBA_D5 = "/home/lucas/Documents/UFRJ/ITM/Trabalho/database/EBA_D5_pedestal_statistics.txt"

EBA_D5 = lerArquivo(FILE_EBA_D5)
print (EBA_D5)