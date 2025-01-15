# CIPHER.PY -MODUULIN YKSIKKÖTESTIT
# =================================

import pytest # Järjestelmätason virheiden testaus
import cipher # Testattavan moduulin lataus

plainText = b'Selkokieliteksti'
key = b'-SsqnFWfgh2pX_nnnOjiCXDH3LN9lmyhSd9SUt6S2HM='
cipherEngine = cipher.createChipher(key)
cryptoText = cipher.encrypt(cipherEngine, plainText)

def test_decrypt():
    assert cipher.decrypt(cipherEngine, cryptoText, True) == plainText

# TODO: Tee tähän testi decryptString-funktiosta
# Luodaan salateksti käyttämällä encryptString-funktiota
cryptoText2 = cipher.encryptString('Selkokieliteksti')

# Tehdään testi, joka käyttää decryptString-funktiota
def test_decryptString():
    assert cipher.decryptString(cryptoText2) == 'Selkokieliteksti'