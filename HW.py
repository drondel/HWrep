import os, glob, re

search_key = input('Введите нужное слово: ')
trk = input('Введите путь до файла: ')

if not trk.endswith('.log'):
    os.chdir(trk)
    for filename in glob.glob('*.log'):
        f = open(filename, 'r')
        for line in f.readlines():
            if search_key in line:
                print(line + ' ' + 'Найдено совпадение')
                with open('parsing.log', 'a') as pars:
                    pars.write(line)

else:
    os.chdir(os.path.join(trk, '..'))
    f = open(trk, 'r')
    print(os.getcwd())
    for line in f.readlines():
        if search_key in line:
            print(line + ' ' + 'Найдено совпадение')
            with open(os.path.join(os.getcwd(), 'justone.log'), 'a') as one:
                one.write(line)
