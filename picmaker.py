import math


f = open("image.ppm", "w")

f.write("P3\n500 500\n255\n")

for y in range(500):
    for x in range(500):
#        num = str(x%100)
#        num2 = str(y%255)
        num = str(int(math.fabs(math.ldexp(x,y)*255)))
        num2 = str(int(math.fabs(math.sin(x*y))*255))
        num3 = str(int(math.fabs(math.cos(x/(y+1)))*255))
        #print(num, num2)
        if(y<83):
            f.write(num2 + " " + num3 + " " + num + " ")
        elif(y<167):
            f.write(num2 + " " + num + " " + num3 + " ")
        elif(y<250):
            f.write(num + " " + num2 + " " + num3 + " ")
        elif(y<333):
            f.write(num + " " + num3 + " " + num2 + " ")
        elif(y<417):
            f.write(num3 + " " + num + " " + num2 + " ")
        else:
            f.write(num3 + " " + num2 + " " + num + " ")
    f.write("\n")

f.close()
