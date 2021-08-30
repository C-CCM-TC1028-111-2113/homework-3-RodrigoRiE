
def main():
    #escribe tu código abajo de esta línea
    año = int(input("Inserte un año: ")) 

    if año % 4 != 0: 
        print("No es bisiesto")
    elif año % 4 == 0 and año % 100 != 0: 
        print("Es bisiesto")
    elif año % 4 == 0 and año % 100 == 0 and año % 400 != 0:
        print("No es bisiesto")
    elif año % 4 == 0 and año % 100 == 0 and año % 400 == 0: 
        print("Es bisiesto")
    pass

if __name__=='__main__':
    main()
