import pandas as pd 
import matplotlib.pyplot as plt
import scipy.stats as sps
from scipy import optimize
import numpy as np

def gaussiana(x,media,variancia):
    g = (1/(np.sqrt(2*np.pi*variancia)))*np.exp(-(1/(2*variancia))*((x-media))**2)
    return g


def plotaHist(tabelao, nome, quantBins=7):
    plt.figure(figsize=(10,8))

    print (" ")

    print ("###########  " + nome + "  ###########")

    ruido = np.linspace(20, 45, 300)
# 4 graus de liberdade
    # Fita os dados
    (mu, sigma) = sps.norm.fit(tabelao)
    print("media: " + str(mu) + "     sigma: " + str(sigma))
    gausEsp = sps.norm.pdf(ruido, mu, sigma)

#matriz de correlaçao é identidade
    # Encontra o histograma
    n, bins,_ = plt.hist(tabelao, bins=quantBins, density=1)
    

    # Fita o histograma
    #(histmu, histsigma) = sps.norm.fit(bins)
    parametros_otimos,_ = optimize.curve_fit(gaussiana,bins[0:-1],n,[31,2.5])
    print("media: " + str(parametros_otimos[0]) + "     sigma: " + str(parametros_otimos[1]))
    histEst = sps.norm.pdf(ruido, parametros_otimos[0], parametros_otimos[1])

    plt.plot(ruido, gausEsp, 'r--', linewidth=2)
    plt.plot(ruido, histEst, 'g--', linewidth=2)
    
    plt.xlabel = 'Intervalo do Ruido'
    plt.ylabel = 'Quantidade nos Bins'
    plt.title(r'$\mathrm{Histograma\ do\ Ruido :}\ \ mu=%.3f,\ \sigma=%.3f,\ histmu=%.3f,\ histsigma=%.3f$' %(mu, sigma,parametros_otimos[0],parametros_otimos[1]))
    plt.savefig(f'./Figuras/{nome}')
    plt.close()

    print("Chi quadrado: " + str((sps.chisquare(histEst,gausEsp, 2)[0])) + "%     seila: " + str(sps.chisquare(histEst,gausEsp, 2)[1]))
    pass


## Cada tabela 
tabelao_EBA_D5 = pd.read_csv('./Pedestal (Ruido)/EBA_D5_pedestal_statistics.txt', sep=" ", usecols=[0, 1, 2, 3, 4, 5, 6, 7, 8])
tabelao_EBA_D6 = pd.read_csv('./Pedestal (Ruido)/EBA_D6_pedestal_statistics.txt', sep=" ", usecols=[0, 1, 2, 3, 4, 5, 6, 7, 8])
tabelao_EBC_D5 = pd.read_csv('./Pedestal (Ruido)/EBC_D5_pedestal_statistics.txt', sep=" ", usecols=[0, 1, 2, 3, 4, 5, 6, 7, 8])
tabelao_EBC_D6 = pd.read_csv('./Pedestal (Ruido)/EBC_D6_pedestal_statistics.txt', sep=" ", usecols=[0, 1, 2, 3, 4, 5, 6, 7, 8])

#print (tabelao_EBA_D5.head())

'''
Modulo Canal Sample1 Sample2 Sample3 Sample4 Sample5 Sample6 Sample7 
0 0 33 30 31 31 32 33 31 
0 1 38 39 41 41 40 37 36 
1 0 38 33 31 32 37 37 38 
1 1 31 32 33 36 36 35 36 
2 0 33 33 35 34 31 27 26 
'''

## Separar os canais de EBA
tabelao_EBA_D5_c0 =  tabelao_EBA_D5[(tabelao_EBA_D5['Canal'] == 0) and (tabelao_EBA_D5['Modulo'] == 0)]
tabelao_EBA_D5_c1 =  tabelao_EBA_D5[tabelao_EBA_D5['Canal'] == 1 and tabelao_EBA_D5['Modulo'] == 0]
tabelao_EBA_D6_c2 =  tabelao_EBA_D6[tabelao_EBA_D6['Canal'] == 2 and tabelao_EBA_D6['Modulo'] == 0]
tabelao_EBA_D6_c3 =  tabelao_EBA_D6[tabelao_EBA_D6['Canal'] == 3 and tabelao_EBA_D5['Modulo'] == 0]


### Separar os canais de EBC
tabelao_EBC_D5_c0 =  tabelao_EBC_D5[tabelao_EBC_D5['Canal'] == 0 and tabelao_EBC_D5['Modulo'] == 0]
tabelao_EBC_D5_c1 =  tabelao_EBC_D5[tabelao_EBC_D5['Canal'] == 1 and tabelao_EBC_D5['Modulo'] == 0]
tabelao_EBC_D6_c2 =  tabelao_EBC_D6[tabelao_EBC_D6['Canal'] == 2 and tabelao_EBC_D5['Modulo'] == 0]
tabelao_EBC_D6_c3 =  tabelao_EBC_D6[tabelao_EBC_D6['Canal'] == 3 and tabelao_EBC_D5['Modulo'] == 0]


## Plotar histograma
for aux in range (1,8):
    plotaHist(tabelao_EBA_D5_c0['Sample'+str(aux)],'Hist_EBA_D5_c0_Sample'+str(aux)+'_Modulo0-10bins')
    #plotaHist(tabelao_EBA_D5_c1['Sample'+str(aux)],'Hist_EBA_D5_c1_Sample'+str(aux)+'_Modulo0-10bins')
    #plotaHist(tabelao_EBA_D6_c2['Sample'+str(aux)],'Hist_EBA_D6_c2_Sample'+str(aux)+'_Modulo0-10bins')
    #plotaHist(tabelao_EBA_D6_c3['Sample'+str(aux)],'Hist_EBA_D6_c3_Sample'+str(aux)+'_Modulo0-10bins')

    #plotaHist(tabelao_EBC_D5_c0['Sample'+str(aux)],'Hist_EBC_D5_c0_Sample'+str(aux)+'_Modulo0-10bins')
    #plotaHist(tabelao_EBC_D5_c1['Sample'+str(aux)],'Hist_EBC_D5_c1_Sample'+str(aux)+'_Modulo0-10bins')
    #plotaHist(tabelao_EBC_D6_c2['Sample'+str(aux)],'Hist_EBC_D6_c2_Sample'+str(aux)+'_Modulo0-10bins')
    #plotaHist(tabelao_EBC_D6_c3['Sample'+str(aux)],'Hist_EBC_D6_c3_Sample'+str(aux)+'_Modulo0-10bins')


## Fitting


## Chi quadrado