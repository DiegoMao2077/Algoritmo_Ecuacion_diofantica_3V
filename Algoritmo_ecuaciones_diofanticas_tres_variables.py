from sys import stdin
l1=[]
l3=[]
def euclides(num1,num2,iteracciones=1):
    l2=[]
    # Si el num1 es inferior al num2, los invertimos
    if num1<num2:
        num1,num2=num2,num1
     
    # obtenemos el residuo de la division
    resto=num1%num2
    cociente=num1//num2
    print("------------------------------")
    print(str(num1)+" "+"|_"+str(num2))
    print("r:",resto,"c:",cociente)
    print("------------------------------")
    l2.append(num1)
    l2.append(num2)
    l2.append(resto)
    l2.append(cociente)
    l1.append(l2)
    if resto==0:
        return (num2,iteracciones)
 
    # llamamos nuevamente a la función pasando como primer parametro el
    # segundo numero y el resto de la division
    return euclides(num2,resto,iteracciones+1) # -> Ecuación de recurrencia
def euclides2(num1,num2,iteracciones=1):
    l2=[]
    # Si el num1 es inferior al num2, los invertimos
    if num1<num2:
        num1,num2=num2,num1
     
    # obtenemos el residuo de la division
    resto=num1%num2
    cociente=num1//num2
    print("------------------------------")
    print(str(num1)+" "+"|_"+str(num2))
    print("r:",resto,"c:",cociente)
    print("------------------------------")
    l2.append(num1)
    l2.append(num2)
    l2.append(resto)
    l2.append(cociente)
    l3.append(l2)
    if resto==0:
        return (num2,iteracciones)
 
    # llamamos nuevamente a la función pasando como primer parametro el
    # segundo numero y el resto de la division
    return euclides2(num2,resto,iteracciones+1) # -> Ecuación de recurrencia
    

print("numero a: ",end="") 
num1=int(stdin.readline())
print("numero b: ",end="") 
num2=int(stdin.readline())
print("numero c: ",end="") 
num3=int(stdin.readline())
print("numero n: ",end="") 
final=int(stdin.readline())
 
comunDivisor,iteracciones=euclides(num1,num2)
 
print("El comun divisor de {} y {} es {}".format(num1,num2,comunDivisor))
print("Se ha encontrado en {} iteracciones".format(iteracciones))
#
print("(1) "+str(num1)+"x + "+str(num2)+"y"+" = "+str(comunDivisor)+"r") #-> EC1
print("(2) "+str(final)+" - "+str(num3)+"z"+" = "+str(comunDivisor)+"r") #-> EC2
#
for x in l1:
    print(str(x[0])+" = "+str(x[1])+"("+str(x[3])+") + "+str(x[2])+"(1)")
print("")
print(str(comunDivisor)+" = "+str(num1)+"(ß)"+" + "+str(num2)+"(æ)")
print(num1,"* (Introduccir beta) : ",end="")
b1=int(stdin.readline())
print(num2,"* (Introduccir alfa) : ",end="")
a1=int(stdin.readline())
res=((num1)*(b1))+((num2)*(a1))

print("")
#Confirmación
if res==comunDivisor:
    #Ampliación de R | Ecuación 1 (EC1)
    print(str(comunDivisor)+"r"+" = "+str(num1)+"("+str(b1)+"r"+")"+" + "+str(num2)+"("+str(a1)+"r"+")")
    #X y Y prima
    print("")
    print("x´= "+"("+str(b1)+"r"+")"" + "+str((num2/comunDivisor))+"t")
    print("y´= "+"("+str(a1)+"r"+")"" - "+str((num1/comunDivisor))+"t")
    print("")
    #Ecuación 2 (EC2)
    print(str(comunDivisor)+"r"+" + "+str(num3)+"z"+" = "+str(final)) #-> EC2 DESPEJADA
    comunDivisor2,iteracciones=euclides2(comunDivisor,num3)
    print("El comun divisor de {} y {} es {}".format(comunDivisor,num3,comunDivisor2))
    print("Se ha encontrado en {} iteracciones".format(iteracciones))
    for y in l3:
        print(str(y[0])+" = "+str(y[1])+"("+str(y[3])+") + "+str(y[2])+"(1)")
    print("")
    print(str(comunDivisor2)+" = "+str(comunDivisor)+"(ß)"+" + "+str(num3)+"(æ)")
    
    print(comunDivisor,"* (Introduccir beta) : ",end="")
    beta=int(stdin.readline())
    print(num3,"* (Introduccir alfa) : ",end="")
    alfa=int(stdin.readline())
    res2=((comunDivisor)*(beta))+((num3)*(alfa))
    print(str(comunDivisor2*(final/comunDivisor2))+" = "+str(comunDivisor)+"("+str(beta*final)+")"+" + "+str(num3)+"("+str(alfa*final)+")")
    print("")
    if res2==comunDivisor2:
        r1=beta*(final/comunDivisor2)
        r2=alfa*(final/comunDivisor2)
        print("r´= "+str(r1)+" + "+str((num3/comunDivisor2))+"u")
        print("z´= "+str(r2)+" - "+str((comunDivisor/comunDivisor2))+"u")
        print("")
        t1=(-1*r1)/(num3/comunDivisor2)
        t2=r2/(comunDivisor/comunDivisor2)
        print("u >",((-1*r1)/(num3/comunDivisor2)))
        print("u >",(r2/(comunDivisor/comunDivisor2)))
        print("")
        #num2 -> num3
        #num1 -> comunDivisor
        #comunDivisor -> comunDivisor2
        if (t2 > t1):
            u=int(t2+1)
            print("u=",u)
            #Reemplazar p1
            vr=r1+((num3/comunDivisor2)*u)
            vz=r2-((comunDivisor/comunDivisor2)*u)
            print("r= ",vr)
            print("z= ",vz)
            print("")
            #Reemplazar p2
            print("r´= "+str(vr)+" + "+str((num3/comunDivisor2))+"u")
            print("z´= "+str(vz)+" - "+str((comunDivisor/comunDivisor2))+"u")
            print("")
            print("#-----------------------")
            print("|","x´= "+"("+str(b1)+"("+str(vr)+" + "+str((num3/comunDivisor2))+"u"+")"+")"" + "+str((num2/comunDivisor))+"t")
            print("|","y´= "+"("+str(a1)+"("+str(vr)+" + "+str((num3/comunDivisor2))+"u"+")"+")"" - "+str((num1/comunDivisor))+"t")
            print("|","z´= "+str(vz)+" - "+str((comunDivisor/comunDivisor2))+"u")
            print("#-----------------------")
            print("")
            #
            print("Sustituir con u=0 y t=0")
            xa=b1*(vr+((num3/comunDivisor2)*0))+((num2/comunDivisor)*0)
            ya=a1*(vr+((num3/comunDivisor2)*0))-((num1/comunDivisor)*0)
            za=vz-((comunDivisor/comunDivisor2)*0)
            print("#-----------------------")
            print("x=",xa)
            print("y=",ya)
            print("z=",za)
            print("#-----------------------")
            print(str(num1)+"("+str(xa)+") +"+str(num2)+"("+str(ya)+") + "+str(num3)+"("+str(za)+") = "+str(final))
            print("("+str(num1*xa)+") +"+"("+str(num2*ya)+") + "+"("+str(num3*za)+") = "+str(final))
            rfinal=(num1*xa)+(num2*ya)+(num3*za)
            print(str(rfinal)+" = "+str(final))
            print(rfinal)
        elif (t1 > t2):
            u=int(t1+1)
            print("u=",u)
            #Reemplazar p1
            vr=r1+((num3/comunDivisor2)*u)
            vz=r2-((comunDivisor/comunDivisor2)*u)
            print("r=",vr)
            print("z=",vz)
            print("")
            #Reemplazar p2
            print("r´= "+str(vr)+" + "+str((num3/comunDivisor2))+"u")
            print("z´= "+str(vz)+" - "+str((comunDivisor/comunDivisor2))+"u")
            print("")
            print("#-----------------------")
            print("|","x´= "+"("+str(b1)+"("+str(vr)+" + "+str((num3/comunDivisor2))+"u"+")"+")"" + "+str((num2/comunDivisor))+"t")
            print("|","y´= "+"("+str(a1)+"("+str(vr)+" + "+str((num3/comunDivisor2))+"u"+")"+")"" - "+str((num1/comunDivisor))+"t")
            print("|","z´= "+str(vz)+" - "+str((comunDivisor/comunDivisor2))+"u")
            print("#-----------------------")
            print("")
            print("Sustituir con u=0 y t=0")
            xa=b1*(vr+((num3/comunDivisor2)*0))+((num2/comunDivisor)*0)
            ya=a1*(vr+((num3/comunDivisor2)*0))-((num1/comunDivisor)*0)
            za=vz-((comunDivisor/comunDivisor2)*0)
            print("#-----------------------")
            print("x=",xa)
            print("y=",ya)
            print("z=",za)
            print("#-----------------------")
            print(str(num1)+"("+str(xa)+") +"+str(num2)+"("+str(ya)+") + "+str(num3)+"("+str(za)+") = "+str(final))
            print("("+str(num1*xa)+") +"+"("+str(num2*ya)+") + "+"("+str(num3*za)+") = "+str(final))
            rfinal=(num1*xa)+(num2*ya)+(num3*za)
            print(str(rfinal)+" = "+str(final))
            print(rfinal)
    else:
        print("Alfa o beta no coinciden con el máximo común divisor de r y c")
else:
    print("Alfa o beta no coinciden con el máximo común divisor de a y b")

    

