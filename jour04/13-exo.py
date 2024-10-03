def convertCelsusFarenheit(tempCelsus : float) -> None :
    """
    fonction qui convertit une température Celsus en température Farenheit
    """
    tempFarenheit = tempCelsus / 5 * 9 + 32
    """ return tempFarenheit """
    print(tempFarenheit)

convertCelsusFarenheit(0)
convertCelsusFarenheit(40)
convertCelsusFarenheit(60)

""" print(help(convertCelsusFarenheit))
if(__name__ == "__main__"):
    assert convertCelsusFarenheit(0) == 32 """
