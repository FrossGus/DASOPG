flag1 = True
flag2 = False
print ("La variable flag1 es de tipo:",type(flag1))
print("La variable flag2 es de tipo:",type(flag2))


if flag1 and flag2:

    print ("Las variables son ambas verdaderas !!")
elif not flag1 and not flag2:
    print ("Las variables son ambas falsas !!")
else:
    print ("Las variables son distintas !!")