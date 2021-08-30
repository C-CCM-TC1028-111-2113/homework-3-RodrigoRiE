
def main():
    #escribe tu código abajo de esta línea
    def tarjetas(pliego, plumon) :

        tpli= pliego*12
        tplum= plumon*35

        if tpli < tplum :
            print("El número máximo de tarjetas que se pueden hacer es:",tpli)
        elif tpli > tplum :
            print("El número máximo de tarjetas que se pueden hacer es:",tplum)
        elif tpli == tplum:
            print("El número máximo de tarjetas que se pueden hacer es:",tplum) 


    pliego=int(input("Dame la cantidad de pliegos de papel albanene: "))
    plumon=int(input("Dame la cantidad de plumones: "))
    tarjetas(pliego, plumon)
    pass

if __name__=='__main__':
    main()
