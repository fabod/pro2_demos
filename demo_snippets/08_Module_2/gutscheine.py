def rabatt(preis, gutschein):
    preis = float(preis)
    gutschein = int(gutschein)
    preis = preis - ((preis/100) * gutschein)
    return preis