
def palindromo (palabra): 
    for i in range(0,int (len(palabra))):
        if palabra [i] !=palabra[-i-1]: 
            return False
        return True 

