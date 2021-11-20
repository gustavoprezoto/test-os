import os
import shutil
from pathlib import Path

def renomearArquivo(arquivo):
    if '.wmlsc' in arquivo:
        p = Path(arquivo)
        return p.rename(p.with_suffix('.wsc'))


def moverArquivo():
    arquivos = os.listdir()


    for arquivo in arquivos:
        arquivo = arquivo.lower()
        oldpath = os.path.abspath(arquivo)
        if arquivo.endswith('.wsc'):
            shutil.move(oldpath, ffolder)
            print(f'Done(Move) - {oldpath} -> {ffolder}')
        elif arquivo.endswith('.wmlsc'):
            oldpath = renomearArquivo(arquivo)
            print(oldpath)
            shutil.move(oldpath, ffolder)
            print(f'Done(Move) - {oldpath} -> {ffolder}')
        elif arquivo.endswith('.wml'):
            shutil.copy(oldpath, ifolder)
            print(f'Done(Copy) - {oldpath} -> {ifolder}')
        elif 'config.ini' in arquivo:
            shutil.copy(oldpath, ifolder)
            print(f'Done(Copy) - {oldpath} -> {ifolder}')
        else:
            print(f'{arquivo} ignored.')


    print('all possible /src/POSWEB/ files moved')


def moveDB():
    os.chdir('./db')
    files = os.listdir()
    for file in files:
        oldpath = os.path.abspath(file)
        shutil.copy(oldpath, ifolder)
    os.chdir('..')


def moveIMG():
    os.chdir("./images")
    files = os.listdir()
    for file in files:
        oldpath = os.path.abspath(file)
        shutil.copy(oldpath, ffolder)
    os.chdir('..')


def movesrcex():
    #primeiro diretório (_font)
    os.chdir('./_font')
    files = os.listdir()
    for file in files:
        if file.endswith('.pwf'):
            oldpath = os.path.abspath(file)
            shutil.copy(oldpath, ffolder)
    #segundo diretorio (_minimal)
    os.chdir('..')
    os.chdir('./_minimal')
    files = os.listdir()
    for file in files:
        oldpath = os.path.abspath(file)
        shutil.copy(oldpath, ffolder)
    #terceiro diretorio (_theme)
    os.chdir('..')
    os.chdir('./_theme')
    files = os.listdir()
    for file in files:
        oldpath = os.path.abspath(file)
        shutil.copy(oldpath, ifolder)
    os.chdir('..')
    os.chdir('..')


def writelogs():
    os.chdir('./load/POSWEB')
    print(os.getcwd())
    #Arquivos da Pasta F
    ftxt = open("flist.txt", "w+")
    os.chdir('./f')
    files = os.listdir()
    for file in files:
        ftxt.write(f'{file}\n')
    ftxt.close()
    os.chdir('..')
    itxt = open("ilist.txt", "w+")
    os.chdir('./i')
    files = os.listdir()
    for file in files:
        itxt.write(f'{file}\n')
    itxt.close()


#absolute paths pasta F e I de load
ffolder = os.path.abspath(r'buildtests\load\POSWEB\f')
ifolder = os.path.abspath(r'buildtests\load\POSWEB\i')


def mainApp():
    #1 - os.startfile() para startar a aplicação WMLSCOMP.exe
    os.chdir('buildtests/src/POSWEB')
    moverArquivo() #funçao para mover o arquivo para as pastas L ou I e renomear WMLSC
    moveDB() #funçao para mover a pasta DB
    moveIMG() #funçao para mover a pasta images
    os.chdir('..')
    movesrcex() #funçao para mover os arquivos extras da pasta src (_font, _minimal e _theme)
    writelogs() #funçao para escrever os arquivos transferidos em Ilist e Llist


mainApp()