import matplotlib.pyplot as plt
import matplotlib_venn as venn

F = {6, 4, 1, 3}
S = {9, 2, 3, 1}
M = {5, 4, 3, 2}

# A&C: INTERSECCION
# A|C: UNION
# A-C: DIFERENCIA
# A^C: DIFERENCIA SIMETRICA

# DIAGRAMA CREADOR DE VENN DE 3 CONJUNTOS
diagrama = venn.venn3([F,M,S],set_labels=('F','M','S'))

diagrama.get_label_by_id('100').set_text(F-(M|S))
diagrama.get_label_by_id('110').set_text(F&M-(F&M&S))
diagrama.get_label_by_id('101').set_text(F&S-(F&M&S))
diagrama.get_label_by_id('011').set_text(M&S-(F&M&S))
diagrama.get_label_by_id('001').set_text(S-(F|M))
diagrama.get_label_by_id('010').set_text(M-(F|S))
diagrama.get_label_by_id('111').set_text(F&M&S)
#plt.show()

print("••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••")
def menu():
    print("=====MENU=====\n")
    print("1) A. ¿Cuántos catedráticos orientarán o Física I u orientarán Sistemas Geométricos, pero no Algebra y Trigonometría?")
    print("2) B. ¿Cuántos catedráticos orientaran solamente 2 asignaturas o únicamente Física I o Sistemas geométricos?")
    print("3) C. ¿Cuántos catedráticos si orientaran Sistemas geométricos, pero no Física I entonces, no orientarán Algebra y Trigonometría?")
    print("4) Salir")
    opcion = int(input("Seleccione una opcion: "))
    return opcion

opcion = 0
while opcion != 4:
    opcion = menu()

    if opcion == 1:
        catedraicos1 = (F^S) & ((F|S)- M)
        it=iter(catedraicos1)
        suma=0
        for i in (it):
            suma=suma+i
        print(f"El conjunto resultante del punto A es {catedraicos1} y La suma de sus elemento es: {suma}")

        diagrama.get_label_by_id('101').set_color('#FF5733')
        diagrama.get_label_by_id('100').set_color('#FF5733')
        diagrama.get_label_by_id('001').set_color('#FF5733')
        plt.show()
        break

    elif opcion == 2:
        catedraicos3 = ((F&S)|(S&M)|(M&F)|(S-(M|F))|(F-(M|S)))-(F&S&M)
        it2=iter(catedraicos3)
        suma2=0
        for i in (it2):
            suma2=suma2+i
        print(f"El conjunto resultante del punto B es {catedraicos3} y La suma de sus elemento es: {suma2}")

        diagrama.get_label_by_id('101').set_color('#FF5733')
        diagrama.get_label_by_id('011').set_color('#FF5733')
        diagrama.get_label_by_id('110').set_color('#FF5733')
        diagrama.get_label_by_id('100').set_color('#FF5733')
        diagrama.get_label_by_id('001').set_color('#FF5733')
        plt.show()
        break

    elif opcion == 3:
        catedraicos3 = (((F|M)-S)|F)|((F|S)-M)
        it3=iter(catedraicos3)
        suma3=0
        for i in (it3):
            suma3=suma3+i
        print(f"El cunjunto resultante del punto C es {catedraicos3} y la suma de sus elemento es: {suma3}")

        diagrama.get_label_by_id('101').set_color('#FF5733')
        diagrama.get_label_by_id('111').set_color('#FF5733')
        diagrama.get_label_by_id('110').set_color('#FF5733')
        diagrama.get_label_by_id('100').set_color('#FF5733')
        diagrama.get_label_by_id('010').set_color('#FF5733')
        diagrama.get_label_by_id('001').set_color('#FF5733')
        plt.show()
        break

    elif opcion == 4:
        print("Hasta Luego")
        break
    else:
        print("Respuesta incorrecta")

print("\nTrabajo realizado por Juan Diego Salazar Gil")