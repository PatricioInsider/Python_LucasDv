#Son las funciones anonimas sin nombre

'''
def palindrome(string):
    return string == string[::-1]
'''
palindrome = lambda string:string == string[::-1]#Funciones anonimas lamda(palindrome es lo que reforna labda)

mylist=[1,4,5,6,9,13,19,21]#Lamda tambien es capazde filtrar mas de un dato, extrayendo de la lista mabda a,b:a*b,mylist
odd= list(filter(lambda i : i%2 !=0,mylist))
    
if __name__=='__main__':
    print(palindrome(str(input("Ingresa el palindromo: "))))
    print(odd)
