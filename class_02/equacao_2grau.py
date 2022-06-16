'Usando desvio condicional encadeado'

    #solicitando os valores de A, B e C 
import math


a = float(input("informe o valor de A: ")) 
b = float(input("informe o valor de B: ")) 
c = float(input("informe o valor de C: ")) 
#cálculo de delta 
delta = b*b - 4*a*c 
#verificando as condições com IF encadeado
if delta > 0.0: 
    #cálculo de 2 valores para X  
    x1 = (-b + math.sqrt(delta)) / (2*a) 
    x2 = (-b - math.sqrt(delta)) / (2*a) 
    print("Para a equação {}x² + {}x + {} = 0, obtivemos os seguintes valores : x1 = {} e x2 = {} .".format(a, b, c, x1, x2))
else: 
    if delta == 0.0: 
        #cálculo de 1 valor para X  
        x = (-b + math.sqrt(delta)) / (2*a) 
        print("Para a equação {}x² + {}x + {} = 0, obtivemos o seguinte valor: x {} .".format(a, b, c, x))
    else: 
        #exibição da mensagem 
        print("Para a equação {}x² + {}x + {} = 0, não existem valores reais para x" .format(a, b, c))