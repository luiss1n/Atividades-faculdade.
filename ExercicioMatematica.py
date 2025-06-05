import numpy as np
import statistics as st
#importando as bibliotecas necessárias para realizar a atividade#

numeros = [1.2, 1.0, 1.4, 1.1, 1.3, 1.0, 1.2, 1.3, 1.0, 1.5, 1.1, 1.2]
#criando a lista de números para realizar as operações#

media = st.mean(numeros)
mediana = st.median(numeros)
moda = st.multimode(numeros)
#realizando as operações para encontrar a média, mediana e moda#

print("Média:", media)
print("Mediana:", mediana)
print("Moda:", moda)

#LETRA A RESOLVIDA ACIMA#

amplitude = max(numeros) - min(numeros)
print("Amplitude:", amplitude)

variancia = np.var(numeros)
print("Variância:", variancia)

desvio_padrao = np.std(numeros)
print("Desvio Padrão : ", desvio_padrao)

#LETRA B RESOLVIDA ACIMA#

print("O site apresenta bom desempenho e estabilidade, sendo carregado rapidamente e sem falhas, sendo um bom site pro usuário que está acessando.")

#LETRA C RESOLVIDA ACIMA#