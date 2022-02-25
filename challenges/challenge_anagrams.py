def is_anagram(first_string, second_string):
    """ Faça o código aqui"""

    # Não passou devido a complexidade

    # while first_string != '':
    #     # strings com comprimentos diferentes não podem ser Anagramas Então retorna False
    #     if len(first_string) != len(second_string):
    #         return False
    #     # Capturando primeiro item da string
    #     tmp = first_string[0]
    #     first_string = first_string.replace(tmp, '')

    #     try:
    #         second_string = second_string.replace(tmp, '')
    #     except:
    #         return False

    # if second_string != '':
    #     return False
    # else:
    #     return True

    if len(first_string)!=len(second_string): 
        return False
    
    # criando dois hashmaps para contagem de palavras
    FS,SS = {},{}
    
    for i in range(len(first_string)): # iterando através de qualquer string
        # A função get ajudará a lidar com o erro de chave passando o valor padrão como 0
        FS[first_string[i]] = 1 + FS.get(first_string[i],0) 
        SS[second_string[i]] = 1 + SS.get(second_string[i],0)
            
    for c in FS: 
        #a contagem de ambas as strings não é igual então retorna false
        if FS[c] !=SS.get(c,0):
            return False
        
    return True # Sendo igual, retorn True