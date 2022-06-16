#Cupom de desconto realiza a comparação do cupom para verificar se o cumpom é valido ou não 
#solicitando dados do cliente. 
valor_compra = input("Informe o valor da compra realizada: ") 
cupom = input("Digite o cumpo de desconto: ")  
#realizando o teste lógico com o cupom em  maiúscula
if cupom.upper() == "NIVER10": 
    #cálculo de 10% de desconto. 
    valor_final = float(valor_compra)*0.9 
else: 
    valor_final = float(valor_compra)     
    print("CUPOM INVÁLIDO!") 
#exibindo o valor final da compra 
print("O valor final da compra é {}".format(valor_final))    