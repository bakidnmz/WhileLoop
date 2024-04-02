i = 0
while i < 5:  # koşul gerçekleşene kadar döngü devam eder
    i += 1  # komut öncesi parametre davranışı değiştirilebilir
    print(i)  # 1 ile 5 aralığını yazdırır

print("*"*40)

j = 0
while j < 5:
    print(j)
    j += 1  # 0 ile 4 aralığını yazdırır komut sonrası parametre davranışı

print("*"*40)

# 1'den 100'e kadar sayılar içinden 10 ile tam bölünen ve 3 ile tam bölünemeyen sayıları yazdıralım
m = 1
while m < 100:
    if m % 10 == 0 and m % 3 != 0:
        print(m)
    m += 1

print("*"*40)

ad = input("Adınız : ")
while True:
    x = int(input("Kaç Kere Yazalım? "))
    if x >= 10:  # sayı 10 ve üzeri girilirse komut çalıştırılmayıp yeni sayı istenecek
        continue  # bu ifade ile if ile belirtilen şart sağlandığı sürece komut pas geçilir dikkate alınmaz
    elif x == 0:
        print(f"See you later ___{ad}___")
        break
    else:
        print(f"*{ad}* " * x)

print("*"*40)

# iç içe döngü ile çarptm tablosu yapalım
k = 0
while k < 10:
    k += 1
    for p in range(1, 11):
        print(f"{k} * {p} =", k*p)
    print("\n")
