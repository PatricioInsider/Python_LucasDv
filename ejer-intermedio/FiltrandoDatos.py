from unicodedata import name


DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]


def run():
    #Esta lista ingresa a cada una de los dicc(worker) de la lista y busca la llave name para comparar el valor con python
    allPythonDevs = [worker["name"] for worker in DATA if worker["language"] == "python"] 
    print("Todos los trabajadores de python")
    for worker in allPythonDevs:
        print(worker)
    #Esta declaracion nos impreme todos los trabajadores de platzi
    allPlatziWorkers = [worker["name"] for worker in DATA if worker["organization"]=="Platzi"]
    print("Todos los trabajadores de Platzi")
    for worker in allPlatziWorkers:
        print(worker)
        
    #Lista de los adultos
    #Funciones lambda (lo que obtiene:la condicion: lista)
    print("Todas las personas de la lista mayores de 18----------")
    adults = list(filter(lambda worker:worker["age"]>18,DATA))
    adults = list(map(lambda worker:worker["name"], adults))
    #| sirve devolver un diccionario con una llave y una clave nueva a un diccionario
    allPeople = list(map(lambda worker:worker | {"old": worker["age"]> 70},DATA ))
    
    for worker in allPeople:
        print(worker)
    
if __name__=='__main__':
    
    #Recuerda siempre colocar esta linea para que nos acostumbremos a trabajar en paradigma modular o orientado
    run()
    #Codigo
