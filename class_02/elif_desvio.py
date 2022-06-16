#O ELIF tem o poder de eliminar a necessidade de utilização de vários IFs e ELSEs,  
# possibilitando um códgio com menos linhas e maior segurança para indentação correta.  
'''pontuacao = input("Insira a pontuação do cliente: ")  
pontuacao = int(pontuacao) 
if pontuacao >= 1000: 
    print("O cliente tem direito a receber mais 3gb na sua franquia de internet!") 
else: 
    if pontuacao >=500: 
        print("O cliente tem direito a receber mais 1,5gb na sua franquia de internte!")     
    else: 
        if pontuacao >=200: 
            print("O cliente tem direito a receber mais 500mb na sua franquia de internte!")         
        else: 
            print("O cliente não receberá bônus.")  '''  
#O códgio acima utilizamos IF e ELSE para mostrarmos que é possível executar utilizar com eles. 
#No código abaixo realizaremos a mesma tarefa, porém utilizaremos o ELIF no código. 

pontuacao = input("Insira a pontuação do cliente: ")  
pontuacao = int(pontuacao) 
if pontuacao >= 1000: 
    print("O cliente tem direito a receber mais 3gb na sua franquia de internet!")   
elif pontuacao >= 500: 
    print("O cliente tem direito a receber mais 1,5gb na sua franquia de internet!")       
elif pontuacao >= 200: 
    print("O cliente tem direito a receber mais 500mb na sua franquia de internet!")     
else: 
    print("O cliente não receberá bônus.")    
    '''Como é possível observar tivemos fácil gestão da indentação do código e eliminamos 2 linhas de código,  
    obtvemos o mesmo sucesso do código anterior que foi utilizado somente IF e ELSE.'''