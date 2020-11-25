import os
import re
import numpy as np
import copy

def promjeniPrefix(_dokument, _noviPrefix):
    """
    Mjenja string unutar apostrofa 
    """
    for i in range(len(_dokument)):
        if "prefix" in _dokument[i]:
            _dokument[i] = re.sub(r'\'[^()]*\'', "'{}'".format(_noviPrefix), _dokument[i])
            return _dokument

def promjeniNat(_dokument, _noviNat):
    """
    Mjenja nat u _dokument
    """
    for i in range(len(_dokument)):
        if "nat" in _dokument[i]:
            _dokument[i] = re.sub(r'=[^()]*\,', "= {},".format(_noviNat), _dokument[i])
            return _dokument


"""
Skripta otvara input folder savršene superčelije u inputFileDirektorij-u sa nazivom inputFileIme
Stvara novi folder s nazivom postavljenim u outputFolderNaziv
Numerira nove input fileove u kojima postavlja nat (number of atoms) na 199
Prefix postavlja na redni broj oduzetog atoma + outputFilePrefix
default: 
001AlSupercell10x10
002AlSupercell10x10
003AlSupercell10x10
...

Oduzima po jedan atom i stvara input fileove s nazivom 
default:
001al_planar_10x10.vcr.in
002al_planar_10x10.vcr.in
003al_planar_10x10.vcr.in
...
"""

#ako je input file u istom direktoriju kao i skripta ostaviti nepromjenjeno
inputFileDirektorij = os.getcwd() #inače zamjeniti os.getcwd() sa "direktorij/do/inputfile-a"
inputFileIme = "al_planar_10x10.vcr.in"

outputFolderNaziv = "GeneratedInputFiles"
outputFilePrefix = "AlSupercell10x10"

try:
    os.mkdir(outputFolderNaziv)
except FileExistsError:
    print("Output folder, već postoji. Ne stvaram novi")

with open(inputFileDirektorij + os.sep + inputFileIme,'r') as reader:
    cijeliDokument = reader.readlines()
    cijeliDokument = promjeniNat(cijeliDokument, 199)   #promjeni broj atoma

    indexOdAtomicPositions = 0
    while (not ("ATOMIC_POSITIONS" in cijeliDokument[indexOdAtomicPositions])):
        indexOdAtomicPositions += 1

    for i in np.arange(1,201):                          
        noviPrefix = "{}".format(i) + outputFilePrefix # 001AlSupercell10x10 , 002Al...
        noviDokument = promjeniPrefix(copy.deepcopy(cijeliDokument),noviPrefix)
        noviDokument.pop(indexOdAtomicPositions + i)
        noviFile = open(os.path.join(".",outputFolderNaziv,"{}".format(i)+inputFileIme),"w")
        noviFile.writelines(noviDokument)
        noviFile.close()

    print("Generiranje uspješno izvršeno")

    

