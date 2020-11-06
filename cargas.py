'''
Fisica para Ciencias de la computacion DDB/C
Carlos Ferroa 
Joaquin Aguirre
Renzo Damian 
Renzo Mondragón
'''
from math import *
import matplotlib.pyplot as plt

#Constante
K = 9*10**9 # NM²/c²

#Densidad lineal de carga (DLC)# Min 20 Max 80
densidadLinealCarga = 20 # λ(nC/m)
Lambda = densidadLinealCarga * pow(10,-9)

# Distancia entre la carga y el punto P # Min 2 Max Inf.
distanciaX = 2 # metros                               

def getDeltaQ(distanciaX, r):
	# Δy = Δq / λ
	# (Δy)² = r² - x²
	# Δy = √(r² - x²)
	# Δq / λ = √(r² - x²)
	# Δq = λ √(r² - x²)
	return Lambda * sqrt( pow(r,2) - pow(distanciaX,2) ) 

def getRadio(distanciaX, i, q):
	# ri = √(x²+(iΔy)²)
	# Δy = Δq / λ
	# ri = √(x²+(iΔq/λ)²)
	return sqrt( pow(distanciaX,2) + pow(i*q/Lambda, 2) )
    
def getError(x0,x1):
	aux = abs((x0-x1)*100/x1)
	return aux 

def getETeorico(distanciaX):
	eo = 8.85*pow(10,-12)
	return Lambda/(2*pi*eo*distanciaX)


def getE(distanciaX):
	# E = Σ(2kΔq/ri² * cos(θ))
	# cos(θ) = x/ri # Cateto Adyacente / Hipotenusa
	# Et = Eo + Σ(2kΔq/ri² * x/ri)
	# Et = Eo + Σ(2kΔqx/ri³)
	E = 0
	ri = distanciaX + 0.0001 # r
	Q = getDeltaQ(distanciaX, ri)

	contador = 1
	
	# Que corra el while hasta que la diferencia de E sea muy pequeña
	while(1):
		# Se guarda el valor E antes de hacerle una modificacion
		Eaux = E

		# Se calcula el nuevo valor de la sumatoria
		ri = getRadio(distanciaX, contador, Q) 
		E += 1 / pow(ri,3)

		# Se compara el valor E con el anterior valor E para notar la diferencia
		if E - Eaux < 0.000001:
			break
		
		contador += 1
		
	E *= 2*K*Q*distanciaX
	E += K*Q/pow(distanciaX,2) # Sumando Eo
	return E

## A) Calcular el campo electrico a una distancia mayor a 2,00 m. En este caso X es 4,00 m
distanciaX = 6
print("Valor X:", distanciaX)

campoElectrico = getE(distanciaX)
print("E calculado: ", campoElectrico)

campoElectricoTeorico = getETeorico(distanciaX)
print("E teorico: ", campoElectricoTeorico)

errorCalculado = round(getError(campoElectrico,campoElectricoTeorico),4)
print("Error: ", errorCalculado, "%", sep = "")


## B) Realizar un grafico Gráfico E vs X para x >= 2,00m
graficoEvX = []
for i in range(2, 100):
	graficoEvX.append(getE(i))

plt.plot(range(2,100), graficoEvX, label="Curva E v X")
plt.title("Grafica E v X")
plt.xlabel("X (metros)")
plt.ylabel("E (N/C)")
plt.legend()
plt.show()