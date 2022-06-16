''' Uma empresa agência de viagens lhe procura para desenvolvimento de um programa no qual recebe o VALOR BRUTO do pacote de viagem,  
a CATEGORIA DOS ASSENTOS no voo e a QUANTIDADE DE VIAJANTES que moram na mesma casa e calcule os descontos de acordo com as categorias: 
 Tabela de descontos
Econômica: 2 == Viajantes == 3%, 3 == Viajantes == 4%, 4 <=Viajantes == 5%
Executiva: 2 == Viajantes == 5%, 3 == Viajantes == 7%, 4 <=Viajantes == 8%
Primeira Classe: 2==Viajantes==10%, 3==Viajantes==15%, 4<=Viajantes == 20% 
O Programa deverá exibir o valor BRUTO DA VIAGEM (o mesmo que foi digitado), o VALOR DOS DESCONTO, o 
 VALOR LÍQUIDO DA VIAGEM(valor bruto menos os descontos) e o VALOR MÉDIO POR VIAJANTE
''' 
################### Inicio #####################
print("Olá, Bem-vindo(a)  ao Partiu Viagens!")
valor_bruto = float(input("Por favor informe o valor bruto do seu pacote de viagem: "))
viajantes = int(input("Por favor informe a quantidade de viajantes:  "))  
categoria = (input("Por favor informe a categoria dos assentos Econômica, Executiva ou Primeira-Classe:  "))   
valor_liquido = 0 
valor_desconto = 0 
valor_medio = 0

if categoria.upper() == "ECONÔMICA" or "ECONOMICA": #or "EXECUTIVA" or "PRIMEIRA-CLASSE":'''
       if viajantes == 2: 
           valor_desconto = valor_bruto * 0.03 
           valor_liquido = valor_bruto - valor_desconto 
           valor_medio = valor_liquido / viajantes
           
       elif viajantes == 3: 
           valor_desconto = valor_bruto * 0.04 
           valor_liquido = valor_bruto - valor_desconto 
           valor_medio = valor_liquido / viajantes
         
       elif viajantes >= 4: 
           valor_desconto = valor_bruto * 0.05 
           valor_liquido = valor_bruto - valor_desconto 
           valor_medio = valor_liquido / viajantes
           print("O valor bruto do pacote ficou em : ${}.".format(valor_bruto),'\n'"O valor do desconto ficou em : ${}".format(valor_desconto),'\n' "O valor final a ser pago  ficou em : ${}".format(valor_liquido),'\n' "A categoria dos assentos são: {}.".format(categoria),'\n' "O valor médio por passageiro ficou em: ${}".format(valor_medio))