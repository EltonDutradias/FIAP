
#Este programa analisa se o aluno atende aos requisitos para fazer parte de um time de esportes da FIAP .
 
rm = input("Insira seu RM: ") 
idade = input("Insira sua idade: ") 
#Estrutura IF condicional simples.  
if int(idade)>=18: 
    print("Sua participação foi autorizada, aluno de RM {}!".format(rm)) 
    print("Mais informações serão enviadas para seu e-mail cadastrado!") 
 #Estrutura IF condicional Composto.        
else: 
  #  print("Sua participação não foi autorizada por causa da sua idade! ")  
#Estrutura IF condicional encadeado  
  autorizado = input("Você possui autorização dos responsáveis? S-SIM ou N-NÃO: ") 
  if autorizado == "S": 
      print("Sua participação foi autorizada, aluno de RM {}!" .format(rm))
      print("Mais informações serão enviadas para o email dos responsáveis!") 
  else: 
      print("Sua participação não foi autorizada por causa da sua idade!")

 'Muito importante ter cuidado na indentação do código para que o programa rode conforme necessário e sem problemas .'
      