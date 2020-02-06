import math

def calculaFP(r, i):

        num = i / r
        angle = (-1) * math.atan(num)
        fp = math.cos(angle)
        return fp


#valores de resistores do laboratório
lista_resistores = [1, 4.7, 10, 18, 22, 33, 68, 100, 150, 220, 270, 390, 470, 560, 680, 820]
#valores de indutores do laboratório
lista_indutores = [0.0001, 0.00022, 0.0046, 0.000068]
#valores de capacitores do laboratório
lista_capacitores = [0.00001, 0.000033, 0.000047, 0.00022, 0.00033, 0.00047, 0.001, 0.0033, 0.01, 0.022]
impedancia_indutores = []
impedancia_capacitores = []
lista_resultados = []
w = 2000 #frequência angular

#calculando impedância dos indutores
for xx in range(0,len(lista_indutores)):
    res = w * lista_indutores[xx]
    complexo = complex(str(res) + "j")
    impedancia_indutores.append(complexo)
#calculando impedância dos capacitores
for xx in range(0,len(lista_capacitores)):
    res = 1 / (w * lista_capacitores[xx])
    complexo = complex("-" +str(res) + "j")
    impedancia_capacitores.append(complexo)
#definindo tensão
tensao = complex(5)
corrente = complex(0)

for x in range(0,len(lista_resistores)):
    for y in range(0, len(impedancia_indutores)):
        for z in range(0, len(impedancia_capacitores)):
            corrente = tensao/(lista_resistores[x]+ impedancia_indutores[y] + impedancia_capacitores[z])

            fp = calculaFP(corrente.real, corrente.imag)
            if(fp < 0.8):
                print("Resistor = ", lista_resistores[x], "Indutor = ", impedancia_indutores[y], "Capacitor = ", impedancia_capacitores[z], "Corrente =", corrente, "Fator de Potência = ", fp)






