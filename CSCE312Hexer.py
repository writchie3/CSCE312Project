f = open("312T.txt", "r")
g = open("312H.txt", "w")

for x in f:
    if "irmov" in x:
        g.write("30 ")
    if "rrmov" in x:
        g.write("40 ")
    if "and" in x:
        g.write("f7 ")
    if "ld" in x:
        g.write("d1 ")
    if "add" in x:
        g.write("f3 ")
    if "st" in x:
        g.write("e1 ")
    if "jne" in x:
        g.write("75 ")
        s = open("312T.txt", "r")
        check = x.find("jne")
        string1 = x[check+4:-1]
        string1 = string1 +':'
        print(string1)
        for i in s:
            if string1 in i:
                g.write(i[2:4])
                s.close()
                break
    if "halt" in x:
        g.write("00")
        g.close()
        f.close()
        exit()
    check = x.find(",")
    string1 = x[8:check]
    string2 = x[check:-1]
    if "%rA" in string1:
        g.write("1")
    if "%rB" in string1 :
        g.write("2")
    if "%rC" in string1:
        g.write("3")
    if "%rD" in string1:
        g.write("4")
    if "%rE" in string1:
        g.write("5")
    if "%rF" in string1:
        g.write("6")
    if "%rA" in string2:
        g.write("1")
    if "%rB" in string2:
        g.write("2")
    if "%rC" in string2:
        g.write("3")
    if "%rD" in string2:
        g.write("4")
    if "%rE" in string2:
        g.write("5")
    if "%rF" in string2:
        g.write("6")
    if "$0x" in string1:
        check2 = string1.find("x")
        string3 = string1[check2+1:]
        if "-" in string3:
            toWrite = "f"
            string3 = string3[1:]
            if '1' in string3:
                string3 = string3.replace('1','f')
        else:
            toWrite = "0"
        zeroes = 4 - len(string3)
        for i in range (1,zeroes):
            g.write(toWrite)
            if i % 2 != 0:
                g.write(" ")
        g.write(string3)
    if':' not in x:
        g.write(" ")
f.close()
g.close()