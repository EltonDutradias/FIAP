#solicitando os dados do alunos
email_aluno = input("Informe o e-mail do aluno: ") 
nota_semestral = input("Informe a nota semestral do aluno: ") 
#convertendo a nota para  formato float (decimal) 
nota_semestral = float(nota_semestral) 
#realizando o teste lógico 
if nota_semestral > 8.5: 
    print("ENVIANDO E-MAIL PARA {}".format(email_aluno)) 
