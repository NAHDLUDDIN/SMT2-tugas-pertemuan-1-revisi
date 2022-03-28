#pengecekan bilangan prima pada range tertentu dan hasilnya dimasukkan ke dalam stack
angka=int(input("masukkan angka: "))
stack = []
if angka > 1:
#karena index dimulai dari angka 0 maka angka harus ditambahkan 1 pada rangenya
    for i in range (2, angka +1):
        for j in range (2, i):
            if i % j == 0:
                break
        else:
#memasukkan hasil i (bilPrima) ke dalam stack 
            stack.append(i)
#stack  pada kondisi awal            
print (stack)
#(LIFO) mengeluarkan item pada posisi paling atas yang terakhir masuk
stack.pop()
print (stack)
#mengeluarkan item pada index tertentu contoh pop index ke 2, maka angka 5 pada bilangan prima 
#akan di keluarkan dengan asumsi banyaknya indek adalah 2 atau lebih
stack.pop(2)
print (stack)

            
            
            
            
           
           
            
          
          
            