# 1) Faça funções em Python em células do Jupyter Notebook para calcular a média: 
# a. Aritmética:
def media_aritmetica(x): 
      return sum(x) / len(x)
# b. Geométrica:
def media_geometrica(x):
    product = 1
    for value in x:
            product *= value
    return product ** (1 / len(x)) 
# c. Harmônica:
def media_harmonica(x):
    inv_sum = sum(1 / value for value in x)
    return len(x) / inv_sum 
# d. Verifique que: 𝑥ҧ𝑎𝑟𝑖𝑡𝑚é𝑡𝑖𝑐𝑎 > 𝑥𝑔𝑒𝑜𝑚é𝑡𝑟𝑖𝑐𝑎 ҧ > 𝑥ҧℎ𝑎𝑟𝑚ô𝑛𝑖𝑐𝑎 
# Use como entrada 
x = [39, 38, 27, 22, 20, 17, 10, 10, 10, 10, 7, 7, 7, 7, 6]
media_aritmetica_result = media_aritmetica(x)
media_geometrica_result = media_geometrica(x)
media_harmonica_result = media_harmonica(x)
media_aritmetica_result > media_geometrica_result and media_geometrica_result > media_harmonica_result

# Exercício 2: Função para calcular média ponderada:
def media_ponderada(x, w):
    weighted_sum = sum(xi * wi for xi, wi in zip(x, w))
    total_weight = sum(w)
    return weighted_sum / total_weight

w = [113, 88, 58, 65, 71, 46, 36, 33, 37, 40, 24, 21, 20, 15, 20]
media_ponderada_result = media_ponderada(x, w)


# Exercício 3: Funções para calcular moda e mediana:

def calcula_moda(x):
    counts = {value: x.count(value) for value in x}
    max_count = max(counts.values())
    modas = [value for value, count in counts.items() if count == max_count]
    return modas

def calcula_mediana(x):
    sorted_x = sorted(x)
    n = len(x)
    if n % 2 == 1:
        return sorted_x[n // 2]
    else:
        middle_values = sorted_x[(n // 2) - 1 : (n // 2) + 1]
        return sum(middle_values) / 2

x = [39, 38, 27, 22, 20, 17, 10, 10, 10, 10, 7, 7, 7, 7, 6]
moda_result = calcula_moda(x)
mediana_result = calcula_mediana(x)

# Exercício 4: Funções para calcular variâncias e desvios padrão:
def variancia_amostral(x):
    n = len(x)
    media = media_aritmetica(x)
    return sum((xi - media) ** 2 for xi in x) / (n - 1)

def variancia_populacional(x):
    n = len(x)
    media = media_aritmetica(x)
    return sum((xi - media) ** 2 for xi in x) / n

def desvio_padrao_amostral(x):
    return variancia_amostral(x) ** 0.5

def desvio_padrao_populacional(x):
    return variancia_populacional(x) ** 0.5

def incerteza_media(x):
    return desvio_padrao_amostral(x) / (len(x) ** 0.5)

variancia_amostral_result = variancia_amostral(x)
variancia_populacional_result = variancia_populacional(x)
desvio_padrao_amostral_result = desvio_padrao_amostral(x)
desvio_padrao_populacional_result = desvio_padrao_populacional(x)
incerteza_media_result = incerteza_media(x)
