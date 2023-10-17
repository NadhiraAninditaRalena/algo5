print('@@@ @  @@@ @@@@   @   @ @ @@@@@@     @@@')
print('@ @ @ @  @ @   @  @   @ @ @     @   @   @')
print("@ @ @ @@@@ @  @   @@@@@ @ @@@@@@    @@@@@")
print("@ @@@ @  @ @@     @   @ @ @    @    @   @")

jumlah = int(input("Masukkan jumlah bilangan: "))
bil1 = int(input("Masukkan angka pertama: "))
bil2 = int(input("Masukkan angka kedua: "))

deretfibonacci=[bil1, bil2]
for i in range(2,jumlah):
  nextfibonacci=deretfibonacci[i-1]+deretfibonacci[i-2]
  deretfibonacci.append(nextfibonacci)
for y in deretfibonacci: 
  print(f'berikut urutannya {y}')
  
  