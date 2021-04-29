veryfication_code = "058"


def veryfication():
    print("Ověřovací kód: " + veryfication_code)

def bomb_id():
    serial_no = input("Vložte sériové číslo")
    nokontrolkas = int(input("Vložte počet pojmenovaných indikátorů"))
    kontrolkas = []
    for i in range(0, nokontrolkas):
        kontrolkas.append(input("Vložte kontrolku č. " + str(i + 1) + ": "))
    batteries = int(input("Vložte počet baterií: "))
    ports = []
    noports = int(input("Vložte počet portů: "))
    for i in range(0, noports):
        ports.append(input("Vložte port č. " + str(i + 1) + " bez překlepů: (dvid, paralel, ps2, rj45, seriove, stereo): "))
    vystup = [serial_no, kontrolkas, batteries, ports]
    return vystup

def help():
    print("Nápověda k programu")
    print("Zadejte 'verif' pro zjištění ověřovacího kódu. Pokud kód není validní, dejte mi vědět.")
    print("Před zneškodňováním bomby, zadejte 'id' pro zapsání sériového čísla, kontrolek, baterií a portů.")
    print("Zadejte zkrácený název modulu pro jeho odjištění. názvy pro zadání: dráty, tlačítko, klávesnice, kuba, první(kdo je první, používejte pouze první), pamět(bez háčku nad t), morse, komplikované, posloupnost, bludiště, hesla, plyn(Upouštění plynu, použivejte plyn), kondenzátor, knoflíky")

def kabels():
    dratno = int(input("Zadej počet drátů (3 - 6): "))
    if dratno == 3:
        cerveny = str(input("Je některý drát červený?(a/n)"))
        if cerveny == "n":
            print("Přeříznout 1. drát")
        elif :
