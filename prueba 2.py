
permu=list("453")
def caracteresPermutando(permu):
    k0 = None
    for i in range(len(permu)-1):
        if permu[i]<permu[i+1]:
            k0=i
    if k0 == None:
        return None

    l0 = k0+1
    for i in range(k0+1, len(permu)):
        if permu[k0] < permu[i]:
            l0 = i

    permu[k0], permu[l0] = permu[l0], permu[k0]
    permu[k0+1:] = reversed(permu[k0+1:])
    return permu

while permu:
    print (permu)
    permu = caracteresPermutando(permu)






        
        
        
        






