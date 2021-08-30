
def main():
    #escribe tu código abajo de esta línea
    def area (a,b):
      area=a*b
      return area

    a=float(input("Ingrese ancho de rectangulo: "))
    b=float(input("Ingrese alto de rectangulo: "))

    print("El área del rectángulo es: ",area(a,b))

    pass

if __name__=='__main__':
    main()
