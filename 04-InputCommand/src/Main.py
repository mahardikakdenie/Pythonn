#Episode input Users

# data yang di masukan pasti string

# data = input("Masukan Data : ")
# print("data : ",data,"tipe : ",type(data))

# Jika inggin mengambil int ,maka -> bisa float / int

# data_int = float(input("Masukan Angka : "))
# print("data : ",data_int,"tipe : ",type(data_int))

# Bagaimana dengan boolean : 
# data_bool = bool(int(input("masukan nilai boolean : ")))
# print("Nilai : ",data_bool,",tipe : ",type(data_bool))




# Opeasi Aritmatika !! 



me = int(input("Masukan Nilai Inputan : "))
you = int(input("Masukan Nilai Inputan : ")) 


# Operasi Penjumlahan ( + ):
hasil_Penjumlahan = me + you
print("a =",me ,"b =", you ,"Operator : ( + ) :")
print(me , "+",you," = ",hasil_Penjumlahan)

# Operasi Pengurangan ( + ):
hasil_Pengurangan = me - you
print("a =",me ,"b =", you ,"Operator : ( - ) :")
print(me,"-",you, " = ",hasil_Pengurangan)

# Operasi Perkalian  ( * ):
hasil_perkalian = me * you
print("a =",me ,"b =", you ,"Operator : ( * ) :")
print(me,"*",you, " = ",hasil_perkalian)

# Operasi Pembagian ( / ):
hasil_Pembagian = me / you 
print("a =",me ,"b =", you ,"Operator : ( / ) :")
print(me,"/",you, " = ",hasil_Pembagian)
# Operator Pangkat ( ** )
hasil_Pangkat = me ** you
print("a =",me ,"b =", you ,"Operator : ( ^ ) :")
print(me,"^",you, " = ",hasil_Pangkat)

# Operator Sisa (Mod)
hasil_Mod = me % you 
print("a =",me ,"b =", you ,"Operator : ( MOD ) :")
print(me,"MOD",you, " = ",hasil_Mod)

# Operasi floor division //
hasil_floo = me // you 
print("a =",me ,"b =", you ,"Operator : ( // ) :")
print(me,"//",you, " = ",hasil_floo)

# prioritas Operasi 

hasil_Operasi = me ** you * me + you / me - you % me // you
print("a =",me ,"b =", you ,"Operator : ( ^ ) :")
print("----------------------")
print(me, "**" ,you ,"*" ,me," +" ,you, "/", me," - ",you, "%", me ,"//",you)
print("Hasilnya ", " = ",hasil_Pangkat)


