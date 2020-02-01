
f = open("image.ppm", "w")

f.write("P3\n500 500\n255\n")

for y in range(500):
    for x in range(500):
        num = str(x%255)
        f.write(num + " " + num + " " + num + " ")
    f.write("\n")

f.close()
