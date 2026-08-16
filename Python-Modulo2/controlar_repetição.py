'''

break, continue e pass

'''

#Break (Freio de mão)
for i in range(50):
    print(i)
    if i == 30:
        print('achei')
        break

#Pass pode ser escrito por ... ou pass
for i in range(1, 51):
    if i % 2 != 0:
        ...
    else:
        print(i)
