def lin():
    print('-='*20)


def titulo(txt):
    lin()
    print(txt.upper())
    lin()


def menu(list):
    for m in range(0,len(list)):
        print(f'\033[34mOpção {m+1} - {list[m]}\033[m')
    lin()