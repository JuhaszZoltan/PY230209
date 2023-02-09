class Bolygo:
    def __init__(self, sor:str):
        v:list[str] = sor.strip().split(';')
        self.nev:str = v[0]
        self.holdak_szama:int = int(v[1])
        self.terfogat_arany:float = float(v[2])