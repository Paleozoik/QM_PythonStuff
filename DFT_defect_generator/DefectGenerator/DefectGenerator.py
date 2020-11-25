import os
import copy
import obradaInputa as oi

inputFileDirektorij = os.getcwd()
inputFileIme = oi.unosInputFileImena()

while (not os.path.exists(inputFileIme)):
    print("Unešeni file ne postoji")
    inputFileIme = oi.unosInputFileImena()

outputFolderNaziv = oi.unosOutFolderNaziv()

try:
    os.mkdir(outputFolderNaziv)
except FileExistsError:
    print("Output folder, već postoji. Ne stvaram novi")

with open(inputFileDirektorij + os.sep + inputFileIme,'r') as reader:
    cijeliDokument = reader.readlines()

    indexOdAtomicPositions = oi.odrediIndexOdAtomicPositions(cijeliDokument)
    brojAtoma = oi.prebrojAtome(cijeliDokument, indexOdAtomicPositions, "Al")

    cijeliDokument = oi.promjeniNat(cijeliDokument, brojAtoma-1) 


    for i in range(1,brojAtoma+1):                          
        prefixAppend = "{}".format(i)
        noviDokument = oi.promjeniPrefix(copy.deepcopy(cijeliDokument),prefixAppend)
        noviDokument.pop(indexOdAtomicPositions + i)
        noviFile = open(os.path.join(".",outputFolderNaziv,"{}".format(i)+inputFileIme),"w")
        noviFile.writelines(noviDokument)
        noviFile.close()

    print("Generiranje uspješno izvršeno")