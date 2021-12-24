import random
import time

print('Dobar Dan!')
time.sleep(1)
print('Napiši mi komandu!(.help za listu komanda)')
while True:
    a=input()
    if a=='.help':
        print('.help - Komande, .69 - Zezancija, .temperatura - Lažna temperatura za školu, .copypasta - Nova copypasta svake nove verzije, .glazba - Preporuka albuma od autora programa(mijenja se svake verzije), .motivacija - Motivacijski citat(mijenja se svake verzije)')
    if a=='.69':
        randMeme=random.randint(1,5)
        if randMeme==1:
            print('LMAO LMAO LMAO SUTRA')
        elif randMeme==2:
            print('Ti si zezancija.')
        elif randMeme==3:
            print('LMAAOOOOOOOAOAOAOOOO')
        elif randMeme==4:
            print('Ej, BABA DROGA!')
        elif randMeme==5:
            print('NISMO NUBOVI MI SMO PROOVI')
        elif randMeme==6:
            print('tata dođi natrag s mlijekom već jednom doslovno te čekam 12 godina')
    if a=='.temperatura':
        temperatura=random.randint(1,3)
        if temperatura==1:
            print('35,8')
        elif temperatura==2:
            print('36,6')
        elif temperatura==3:
            print('36,3')
    if a=='.copypasta':
        print('ona mene pali kurve su mi tu al mi ljubav fali ona rola vu kada mi se vari vrti mi se manta u klubu smo glavni pušite mi kurac')
    if a=='.glazba':
        glazba=random.randint(1, 3)
        if glazba==1:
            print('Pop Food - Jack Stauber')
        if glazba==2:
            print('Turn on the Bright Lights - Interpol')
        if glazba==3:
            print('Carrie & Lowell - Sufjan Stevens')
    if a=='.motivacija':
        print('"Ajde, popuš mi kurac!" - Bega, 2006')
