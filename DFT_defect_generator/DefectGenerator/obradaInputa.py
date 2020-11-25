import re


def unosInputFileImena():
    _inputFileIme = ""
    while (".vcr.in" not in _inputFileIme):
        _inputFileIme = input("Naziv input file-a prema kojem generiramo defekte: ")
    return _inputFileIme


def unosOutFolderNaziv():
    _outFolderNaziv = ""
    _outFolderNaziv = input("Naziv novog output foldera: ")
    if _outFolderNaziv == "":
        return "GeneratedInputFiles"
    else:
        return _outFolderNaziv


def odrediIndexOdAtomicPositions(_dokument):
    _indexOdAtomicPositions = 0
    while (not ("ATOMIC_POSITIONS" in _dokument[_indexOdAtomicPositions])):
        _indexOdAtomicPositions += 1
    return _indexOdAtomicPositions


def prebrojAtome(_dokument, _startingIndex, _atom):
    _brojAtoma = 0
    _duljinaNazivaAtoma = len(_atom)
    for i in range(len(_dokument)-_startingIndex-1):
        if _atom in _dokument[_startingIndex + i][:_duljinaNazivaAtoma]:
            _brojAtoma += 1
    return _brojAtoma


def promjeniPrefix(_dokument, _noviPrefix):
    """
    Dodaje redni broj defekta na output prefix u _dokument 
    """
    for i in range(len(_dokument)):
        if "prefix" in _dokument[i]:
            _prefix = _noviPrefix + re.findall(r"'(.*?)'",_dokument[i])[0]
            _dokument[i] = re.sub(r'\'[^()]*\'', "'{}'".format(_prefix), _dokument[i])
            return _dokument

def promjeniNat(_dokument, _noviNat):
    """
    Mjenja nat (broj atoma) u _dokument
    """
    for i in range(len(_dokument)):
        if "nat" in _dokument[i]:
            _dokument[i] = re.sub(r'=[^()]*\,', "= {},".format(_noviNat), _dokument[i])
            return _dokument
