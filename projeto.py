import matplotlib.pyplot as plt
import numpy as np
from scipy import fft, ifft,signal


def main2():
    bar="/"
    fLabel = open("C:/Users/ruipm/Desktop/Projeto ATD/RawData/labels.txt",'r')
    lstFinal=[[],[],[],[],[],[],[],[],[],[],[],[]]
    lst=fLabel.read().split('\n')
    for i in range(len(lst)-1):
        aux=lst[i].split(' ')
        exp=int(aux[0])
        action=int(aux[2])-1
        user=int(aux[1])
        if(exp>=34 and exp<=41):
            nomeFile="C:/Users/ruipm/Desktop/Projeto ATD/RawData"+bar+"acc_exp"+intForm(exp)+"_user"+intForm(user)+".txt"
            fTimes=open(nomeFile,'r')
            lstTimes=fTimes.read().split('\n')
            lstAux=[[],[],[]]
            for k in range(3):
                for j in range(int(aux[3]),int(aux[4])):
                    lstAux[k].append(float(lstTimes[j].split(' ')[k]))
            lstFinal[action].append(lstAux)
            
            fTimes.close()
    #plots(lstFinal[0][0][0])
    #ex3_2(lstFinal)
    #ex3_1(lstFinal[0][0][0])
    #createStepsTable(lstFinal)
    #createStepsTable(lstFinal)
    funcao(lstFinal[11])
   # print(stepsPerMinute(abs(np.fft.fftshift(fft(signal.detrend(lstFinal[0][0][0]))))))
   # stft(lstFinal[0][0][0])  
    
    
   
    fLabel.close()
def funcao(lst):
    media1Pico=0
    mediaNrPicos=0
    mediaMagnitudes=0
    somaA0=0
    somaA1=0
    somaA2=0
    somaB0=0
    somaB1=0
    somaB2=0
    somaC0=0
    somaC1=0
    somaC2=0
    
    
    for i in range(len(lst)):
        for j in range(3):
            y = abs(np.fft.fftshift(fft(signal.detrend(lst[int(i)][int(j)]))))
            peaksw,dictio=signal.find_peaks(y,0)
            values=list(dictio.get('peak_heights'))
            soma=0
            soma2=0
            flag=False
            aux=0
            n=0
            for w in values:
                
                if w>0.4*max(values):
                    soma+=1
                    soma2+=w
                    if flag==False:
                        aux=n
                        flag=True
                n=n+1
                        
            media=soma2/soma 
            media1Pico+=aux
            mediaNrPicos+=soma
            mediaMagnitudes+=soma2
            media1Pico=media1Pico/len(lst)
            mediaNrPicos=mediaNrPicos/len(lst)
            mediaMagnitudes=mediaMagnitudes/len(lst)
            if (j == 0):
                somaA0 += media1Pico
                somaA1 += mediaNrPicos
                somaA2 += mediaMagnitudes
            elif  (j == 1):
                somaB0 += media1Pico
                somaB1 += mediaNrPicos
                somaB2 += mediaMagnitudes
            elif  (j == 2):
                somaC0 += media1Pico
                somaC1 += mediaNrPicos
                somaC2 += mediaMagnitudes
                
    tam = len(lst)
    mfinalA0 = somaA0 / tam
    mfinalA1 = somaA1 / tam
    mfinalA2 = somaA2 / tam
    mfinalB0 = somaB0 / tam
    mfinalB1 = somaB1 / tam
    mfinalB2 = somaB2 / tam
    mfinalC0 = somaC0 / tam
    mfinalC1 = somaC1 / tam
    mfinalC2 = somaC2 / tam
    
    print(str(mfinalA0) + "    " + str(mfinalA1) + "     " + str(mfinalA2) + "     " + "X\n" + str(mfinalB0) + "    " + str(mfinalB1) + "     " + str(mfinalB2) + "     " + "Y\n" + str(mfinalC0) + "    " + str(mfinalC1) + "     " + str(mfinalC2) + "     " + "Z\n" )
            
            
            
            #print(str(media1Pico)+ "      " +str(mediaNrPicos)+ "        " +str(mediaMagnitudes) + "    "+str(j )+"\n")
    
    
    
def stft(arr): 
    fs=50
    ts=1/fs
    tam=len(arr)
    t=tam*ts
    tF=0.005*t
    tOl=tF/2
    Nf=round(tF*fs)
    h=np.hamming(Nf)
    nOvL=round(tOl*fs)
    spectre=[]
    nframes=0
    f=np.linspace(-fs/2,fs/2,Nf)
    x = np.where(f >= 0)
    
    for i in range(1,Nf-nOvL,tam-Nf):
        x_f=arr[i:i+Nf-1]
        m_x_frame =abs(np.fft.fftshift(fft(x_f)))
        spectre=np.hstack(spectre,m_x_frame[x])
       # nframes=nframes+1
    plt.figure()
    
    signal.spectrogram(len(x),Nf,nOvL,[],fs)
    
    #plt.imshow(20*np.log10(spectre))
    #plt.set(gca,'YDir','normal')
        
    
    
    
    
    
    
    
    
def stftBef(arr):
    step=50
    freq=20
    tam=len(arr)
    i=0
    
    while (i<tam):
        aux=[]
        for j in range(i,i+step):
            aux.append(arr[j])
        dft=abs(np.fft.fftshift(fft(signal.detrend(aux)))) 
        plt.figure()
        plt.plot(np.linspace(-freq,+freq,len(dft)))
        
        i=i+step;
    print(arr)
    
    
    
    
    
    
def ex3_1(arr):
    plt.figure()
    tam=len(arr)
    dft=abs(np.fft.fftshift(fft(signal.detrend(arr))))
    hamm=np.hamming(tam)
    hann=np.hanning(tam)
    blackm=np.blackman(tam)
    
    nHamm=[]
    nHann=[]
    nBlackm=[]
    for i in range(tam):
        nHamm.append(arr[i]*hamm[i])
    for i in range(tam):
        nHann.append(arr[i]*hann[i])
    for i in range(tam):
        nBlackm.append(arr[i]*blackm[i])
    plt.subplot(311)
    plt.plot(np.arange(tam),nHamm)
    plt.xlabel("Tempo")
    plt.ylabel("Valor")
    plt.title("Sinal com a janela de Hamming")
    plt.subplot(312)
    plt.plot(np.arange(tam),nHann)
    plt.xlabel("Tempo")
    plt.ylabel("Valor")
    plt.title("Sinal com a janela de Hanning")
    plt.subplot(313)
    plt.plot(np.arange(tam),nBlackm)
    plt.xlabel("Tempo")
    plt.ylabel("Valor")
    plt.title("Sinal com a janela de Blackman")
    plt.tight_layout()
    
    
    
    
    
    
    
    
def ex3_2(arr):
    for i in range(len(arr)):
       
        for j in range(len(arr[i])):
            
            plots(arr[i][j][0])
            
            plots(arr[i][j][1])
            
            plots(arr[i][j][2])
    
    
    
    
    
def plots(arr):
    ls=[]
    for i in range(len(arr)):
        ls.append(i)
    #print(ls)
    plt.figure()
    arr=tratamentoDeDados(arr)
    plt.subplot(311)
    plt.plot(ls,arr,color='black')
    plt.xlabel("Tempo")
    plt.ylabel("Valor")
    plt.title("Sinal Original")
    
    frq=50
    
    freqs=np.linspace(-frq/2,frq/2,len(arr))
    xx=abs(np.fft.fftshift(fft(arr)))
    plt.subplot(312)
    plt.plot(freqs,xx,color='black')
    plt.xlabel("Frequencia [Hz]")
    plt.ylabel("Magnitude")
    plt.title("DFT do sinal com tendência")
    
    
    
    y = abs(np.fft.fftshift(fft(signal.detrend(arr))))
    
    plt.subplot(313)
    plt.plot(freqs,y,color='black')
    plt.xlabel("Frequencia [Hz]")
    plt.ylabel("Magnitude")
    plt.title("DFT do sinal sem tendência")
    plt.tight_layout()
    plt.show()
    
    
    
    
    


def tratamentoDeDados(arr):
    media=median(arr)
    desvio=np.std(arr)
    arrFinal=[]
    for i in range(len(arr)):
        if ( not arr[i]>media+3*desvio and  not arr[i]>media+3*desvio):
            arrFinal.append(arr[i])
        else:
            if (arr[i]>media+3*desvio):
                arrFinal.append(media+(2.5*desvio))
            if (arr[i]<media-3*desvio):
                arrFinal.append(media-(2.5*desvio))
    return arrFinal
        
    
def median(arr):
    tam=len(arr)
    soma=0
    for i in range(tam):
        soma=soma+arr[i]
    
    return soma/tam

    
    
    
def createStepsTable(arr):
    Walk_x=[]
    Walk_y=[]
    Walk_z=[]
    Walk_U_x=[]
    Walk_U_y=[]
    Walk_U_z=[]
    Walk_D_x=[]
    Walk_D_y=[]
    Walk_D_z=[]
    for i in range(len(arr[0])):
        Walk_x.append(stepsPerMinute(abs(np.fft.fftshift(fft(signal.detrend(arr[0][i][0]))))))
        Walk_y.append(stepsPerMinute(abs(np.fft.fftshift(fft(signal.detrend(arr[0][i][1]))))))
        Walk_z.append(stepsPerMinute(abs(np.fft.fftshift(fft(signal.detrend(arr[0][i][2]))))))
    for i in range(len(arr[1])):
        Walk_U_x.append(stepsPerMinute(abs(np.fft.fftshift(fft(signal.detrend(arr[1][i][0]))))))
        Walk_U_y.append(stepsPerMinute(abs(np.fft.fftshift(fft(signal.detrend(arr[1][i][1]))))))
        Walk_U_z.append(stepsPerMinute(abs(np.fft.fftshift(fft(signal.detrend(arr[1][i][2]))))))
    for i in range(len(arr[2])):
        Walk_D_x.append(stepsPerMinute(abs(np.fft.fftshift(fft(signal.detrend(arr[2][i][0]))))))
        Walk_D_y.append(stepsPerMinute(abs(np.fft.fftshift(fft(signal.detrend(arr[2][i][1]))))))
        Walk_D_z.append(stepsPerMinute(abs(np.fft.fftshift(fft(signal.detrend(arr[2][i][2]))))))
    print(median(Walk_D_z))
    print(np.std(Walk_D_z))
    print(Walk_D_z)
         
    
def stepsPerMinute(dft):
    
    maxi=max(dft)
    treshH=0.4*maxi
    freq=50
    peaksw,dictio=signal.find_peaks(dft,0)
    values=list(dictio.get('peak_heights'))
    arrAux=np.linspace(-freq/2,freq/2,len(dft))
    
    
    for i in range(len(peaksw)):
        peak=dft[peaksw[i]]
        if peak>treshH:
            return 60*abs(arrAux[peaksw[i]])
    
    
    
    
    
def main():
    lstFinal=[[],[],[],[],[],[],[],[]]
    for i in range(34,42):
        lstAux=[[],[],[]]
        nomeFile="C:/Users/ruipm/Desktop/Projeto ATD/RawData/acc_exp"+intForm(i)+"_user"+intForm(int(i/2))+".txt"
        fTimes=open(nomeFile,'r')
        lstTimes=fTimes.read().split('\n')
        for j in range(len(lstTimes)-1):
            for k in range(3):
                lstAux[k].append(float(lstTimes[j].split(' ')[k]))   
        lstFinal[i-34]=lstAux
    fTimes.close()
    #print(lstFinal)
    ls=[]
    for i in range(len(lstFinal[2][0])):
        ls.append(i)
    #print(lstFinal[0])
    showData(lstFinal,37)
    #print(ls)
    
    
def intForm(n):
    if n<10:
        return '0'+str(n)
    else:
        return str(n)



def showData1(lista, exp):
    fLabel = open("C:/Users/ruipm/Desktop/Rui/Eng Informatica UC/ATD/DATA/RawData/labels.txt",'r')
    lst=fLabel.read().split('\n')
    tempo = 0
    colors = ["red","blue","yellow","white","pink","olive","blueviolet","fushia","gold","aquamarine","orange","peru"]
    plt.figure(exp)
    for i in range(len(lst)-1):
        labelsDivided = lst[i].split(' ')
        expAtual = int(labelsDivided[0])
        user = int(labelsDivided[1])
        if expAtual == exp:
            action = int(labelsDivided[2])-1
            tempoI = int(labelsDivided[3])
            tempoF = int(labelsDivided[4])
            X = []
            Yx = []
            Yy = []
            Yz = []
            for k in range(tempo,tempoI):
                X.append(k)
                Yx.append(lista[0][k])
                Yy.append(lista[1][k])
                Yz.append(lista[2][k])
            plt.subplot(311)
            plt.plot(X,Yx,color="black")
            plt.subplot(312)
            plt.plot(X,Yy,color="black")
            plt.subplot(313)
            plt.plot(X,Yz,color="black")
            tempo=tempoF

def showData(lista, exp):
    fLabel = open("C:/Users/ruipm/Desktop/Projeto ATD/RawData/labels.txt",'r')
    lst=fLabel.read().split('\n')
    tempo = 0
    colors = ["red","blue","yellow","white","pink","olive","blueviolet","darkcyan","gold","aquamarine","orange","peru"]
    plt.figure(exp)
    for i in range(len(lst)-1):
        labelsDivided = lst[i].split(' ')
        expAtual = int(labelsDivided[0])
        user = int(labelsDivided[1])
        if expAtual == exp:
            action = int(labelsDivided[2])-1
            tempoI = int(labelsDivided[3])
            tempoF = int(labelsDivided[4])
            X = []
            Yx = []
            Yy = []
            Yz = []
            for k in range(tempo,tempoI+1):
                X.append(k)
                Yx.append(lista[exp-34][0][k])
                Yy.append(lista[exp-34][1][k])
                Yz.append(lista[exp-34][2][k])
            plt.subplot(311)
            plt.plot(X,Yx,color="black")
            plt.subplot(312)
            plt.plot(X,Yy,color="black")
            plt.subplot(313)
            plt.plot(X,Yz,color="black")
            X = []
            Yx = []
            Yy = []
            Yz = []
            for k in range(tempoI,tempoF+1):
                X.append(k)
                Yx.append(lista[exp-34][0][k])
                Yy.append(lista[exp-34][1][k])
                Yz.append(lista[exp-34][2][k])
            plt.subplot(311)
            plt.plot(X,Yx,color=colors[action])
            plt.xlabel("Tempo")
            plt.ylabel("Valor")
            plt.title("Experiencia "+ str(exp) + " AccX")
            
            plt.subplot(312)
            plt.plot(X,Yy,color=colors[action])
            plt.xlabel("Tempo")
            plt.ylabel("Valor")
            plt.title("Experiencia "+ str(exp) + " AccY")
            
            plt.subplot(313)
            plt.plot(X,Yz,color=colors[action])
            plt.xlabel("Tempo")
            plt.ylabel("Valor")
            plt.title("Experiencia "+ str(exp) + " AccZ")
 
            tempo=tempoF
    maxi = len(lista[exp-34][0])
    X = []
    Yx = []
    Yy = []
    Yz = []
    for k in range(tempo,maxi):
        X.append(k)
        Yx.append(lista[exp-34][0][k])
        Yy.append(lista[exp-34][1][k])
        Yz.append(lista[exp-34][2][k])
    plt.subplot(311)
    plt.plot(X,Yx,color="black")
    plt.subplot(312)
    plt.plot(X,Yy,color="black")
    plt.subplot(313)
    plt.plot(X,Yz,color="black")
    plt.tight_layout()
    plt.show()       
                
def main3():
    x = [1, 2, 3, 4,5]
    plt.subplot(211)
    plt.plot([1,2,3,4,5],x,color='black')
    
    y = fft(x)
    plt.subplot(212)
    plt.plot([1,2,3,4,5],y,color='black')
    #print(y)         
                
                
                
             
main2()              
                
                