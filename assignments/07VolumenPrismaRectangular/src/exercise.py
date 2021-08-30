
def main():
    #escribe tu código abajo de esta línea
    def vol (b,a,p):
      vol = b*a*p
      return vol


    b = float(input("Dame la base: "))
    a = float(input("Dame la altura: "))
    p = float(input("Dame la profundidad: "))

    print("El volumen del prisma es: ", vol(b,a,p))
    pass

if __name__=='__main__':
    main()
