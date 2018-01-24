#menghitung jumlah huruf yang sering muncul jika dia perempuan
def perempuan(p):
    for i in range(0,len(p)):
        r=0
        if (p[i] == "i"):
            r = r+1
        elif (p[i] == "a"):
            r = r+1
        elif (p[i] == "u"):
            r = r+1
        elif (p[i] == "e"):
            r = r+1
        elif (p[i] == "t"):
            r = r+1
        elif (p[i] == "l"):
            r = r+1
    return r

#menghitung jumlah huruf yang sering muncul jika dia laki-laki
def laki(z):
    n=0
    for i in range(0,len(z)):
        if (z[i] == "b"):
            n = n+1
        elif (z[i] == "d"):
            n = n+1
        elif (z[i] == "o"):
            n = n+1
    return n

#menginputkan nama

x = input('masukkan nama :')
genlaki=laki(x)
genperempuan=perempuan(x)

#membandingkan jumlah huruf yang muncul

if genlaki>genperempuan:
    print("lelaki")
elif genperempuan>genlaki:
    print("perempuan")
else: print("tidak diketahui")
print("genlaki= ",genlaki,"genperempuan= ",genperempuan)


#kesimpulan = dari percobaan nama yang telah dicoba nama yang paling banyak muncul adalah perempuan
