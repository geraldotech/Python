
def pode_executar(allow=None):
    if allow is None:
        return 'parametro nao informado'
    
    if not isinstance(allow, bool):        
        return 'params deve ter booleano'    
    
    if not allow: # meads value is value and not empty
        return 'vc informou um valor negativo'
    return 'execucao permitida'    

print(pode_executar(True))
print(pode_executar(False))