

dias=3
casas=[1,1,1,0,1,0,1,1]


if dias <0 or dias >8 :
    print("parametros equivocados")
elif dias > 0 or dias <8:
    
    for x in range(dias):
        for c in range(len(casas)):
            if casas[c]==0:
                casas [c]= 1
            elif casas[c]==1:
                casas[c]=0
                
                       

 


            
print(casas)






        
        
        
        






