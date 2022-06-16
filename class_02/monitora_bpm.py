'''Monitorar batimentos cardíacos por minuto.O usuário irá inserir informações e após comprações, 
sistema irá imprimir para usuário se ele está de acordo com o ideal.''' 
print("MONITORA SAÚDE - BATIMENTOS CARDÍACOS - BPM") 
#solicitando dados do usuário 
bpm = int(input("Por favor informe a quantidade de batimentos por minuto: ")) 
idade = int(input("Por favor informe sua idade em anos completos: "))
#iniciando os teste lógicos
if 0<=idade<=2 and 120<= bpm<=140 or 8<=idade<=17 and 80<= bpm<=100 or 18<=idade<=25 and 56<=bpm<=61 or 26<=idade<=35 and 55<=bpm<=61 or 36<=idade<=45 and 57<=bpm<=62 or 46<=idade<=55 and 57<=bpm<=61 or 56<=idade<=65 and 57<=bpm<=61 or 65<idade and 56<=bpm<=61:
        print("O ritmo dos seus batimentos está Excelente para idade fornecida, isso é exemplar, muito fantástico!  " )  
elif 18<=idade<=35 and 62<=bpm<=69 or 36<=idade<=45 and 63<=bpm<=70 or 46<=idade<=55 and 64<=bpm<=70 or 56<=idade<=65 and 62<=bpm<=71 or 65<idade and 62<=bpm<=69:
       print("O ritmo dos seus batimentos está Boa para idade fornecida, continue assim gostei de ver! " )        
elif 18<=idade<=25 and 70<=bpm<=73 or 26<=idade<=35 and 71<=bpm<=74 or 36<=idade<=45 and 71<=bpm<=75 or 46<=idade<=55 and 72<=bpm<=76 or 56<=idade<=65 and 72<=bpm<=75 or 65<idade and 70<=bpm<=73:
         print("O ritmo dos seus batimentos está normal para idade fornecida! " )              
elif 18<=idade<=25 and 74<=bpm<=81 or 26<=idade<=35 and 75<=bpm<=81 or 36<=idade<=45 and 76<=bpm<=82 or 46<=idade<=55 and 77<=bpm<=83 or 56<=idade<=65 and 76<=bpm<=81 or 65<idade and 74<=bpm<=79:
         print("O ritmo dos seus batimentos não está normal para a idade fornecida, atenção! " )              
elif 18<=idade<=35 and 82<bpm or 56<=idade<=65 and 82<bpm or 36<=idade<=45 and 83<bpm or 46<=idade<=55 and 84<bpm or 65<idade and 80<bpm:
         print("O ritmo dos seus batimentos está ruim para idade fornecida, favor consultar o médico! " )             
elif 18<=idade<=25 and 56>bpm or 26<=idade<=35 and 55>bpm or 56<=idade<=65 and 57>bpm or 36<=idade<=45 and 57>bpm or 46<=idade<=55 and 58>bpm or 65<idade and 56>bpm:
            print("O ritmo dos batimentos está baixo atenção! ")
else: 
   print("Insira os dados corretamente!")
   
