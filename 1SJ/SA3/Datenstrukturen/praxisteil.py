import time



start = time.time()
for buch in 'Rotkäppchen Götz Memoiren_einer_Sozialistin Bibel'.split():
    print(buch)
    with open(f'{buch}.txt', 'r') as f:
        f.readline()
        inhalt = f.read().lower()

    buchstaben = 'qwertzuiopüasdfghjklöäyxcvbnmß'
    worte = ''.join([zeichen if zeichen in buchstaben else ' ' for zeichen in inhalt])
    # print(worte)
    print(len(worte.split()))
    print(len(set(worte.split())))
print(time.time()-start, "sek")

print(hash(1887739074256335311))

