spelactief = True
while spelactief:
    print("Welkom bij Italiaanse Boter, Kaas en Eieren")
    naamSpeler1 = input("Wat is de naam van speler 1?")
    naamSpeler2 = input("Wat is de naam van speler 2?")
    plaats = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    plaatsen = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    print(plaats[0], plaats[1], plaats[2])
    print(plaats[3], plaats[4], plaats[5])
    print(plaats[6], plaats[7], plaats[8])
    for turn in range(3):
        while True:
            plaatsSpeler = input(f"Waar wil {naamSpeler1} een steen plaatsen?")
            if plaatsSpeler not in plaatsen:
                print("Antwoord met een plaats tussen de 1 en 9")
            elif plaatsSpeler in plaats:
                plaats[int(plaatsSpeler) - 1] = "X"
                print(plaats[0], plaats[1], plaats[2])
                print(plaats[3], plaats[4], plaats[5])
                print(plaats[6], plaats[7], plaats[8])
                break
            else:
                print("Deze plaats is bezet")
            print(plaats[0], plaats[1], plaats[2])
            print(plaats[3], plaats[4], plaats[5])
            print(plaats[6], plaats[7], plaats[8])
        while True:
            if (plaats[0] == "X" and plaats[1] == "X" and plaats[2] == "X") or (
                    plaats[3] == "X" and plaats[4] == "X" and plaats[5] == "X") or (
                    plaats[6] == "X" and plaats[7] == "X" and plaats[8] == "X") or (
                    plaats[0] == "X" and plaats[3] == "X" and plaats[6] == "X") or (
                    plaats[1] == "X" and plaats[4] == "X" and plaats[7] == "X") or (
                    plaats[2] == "X" and plaats[5] == "X" and plaats[8] == "X") or (
                    plaats[0] == "X" and plaats[4] == "X" and plaats[8] == "X") or (
                    plaats[2] == "X" and plaats[4] == "X" and plaats[6] == "X"):
                break
            else:
                plaatsSpeler = input(f"Waar wil {naamSpeler2} een steen plaatsen?")
                if plaatsSpeler not in plaatsen:
                    print("Antwoord met een plaats tussen de 1 en 9")
                elif plaatsSpeler in plaats:
                    plaats[int(plaatsSpeler) - 1] = "O"
                    print(plaats[0], plaats[1], plaats[2])
                    print(plaats[3], plaats[4], plaats[5])
                    print(plaats[6], plaats[7], plaats[8])
                    break
                else:
                    print("Deze plaats is bezet")
                print(plaats[0], plaats[1], plaats[2])
                print(plaats[3], plaats[4], plaats[5])
                print(plaats[6], plaats[7], plaats[8])
    geenDrieOpEenRij = True
    while geenDrieOpEenRij:
        if (plaats[0] == "X" and plaats[1] == "X" and plaats[2] == "X") or (
                plaats[3] == "X" and plaats[4] == "X" and plaats[5] == "X") or (
                plaats[6] == "X" and plaats[7] == "X" and plaats[8] == "X") or (
                plaats[0] == "X" and plaats[3] == "X" and plaats[6] == "X") or (
                plaats[1] == "X" and plaats[4] == "X" and plaats[7] == "X") or (
                plaats[2] == "X" and plaats[5] == "X" and plaats[8] == "X") or (
                plaats[0] == "X" and plaats[4] == "X" and plaats[8] == "X") or (
                plaats[2] == "X" and plaats[4] == "X" and plaats[6] == "X"):
            print(f"{naamSpeler1} heeft gewonnen")
            break
        if (plaats[0] == "O" and plaats[1] == "O" and plaats[2] == "O") or (
                plaats[3] == "O" and plaats[4] == "O" and plaats[5] == "O") or (
                plaats[6] == "O" and plaats[7] == "O" and plaats[8] == "O") or (
                plaats[0] == "O" and plaats[3] == "O" and plaats[6] == "O") or (
                plaats[1] == "O" and plaats[4] == "O" and plaats[7] == "O") or (
                plaats[2] == "O" and plaats[5] == "O" and plaats[8] == "O") or (
                plaats[0] == "O" and plaats[4] == "O" and plaats[8] == "O") or (
                plaats[2] == "O" and plaats[4] == "O" and plaats[6] == "O"):
            print(f"{naamSpeler2} heeft gewonnen")
            break
        else:
            verplaatsjuist = False
            while not verplaatsjuist:
                verplaats = input(f"Welke steen wil {naamSpeler1} verplaatsen")
                if verplaats not in plaatsen:
                    print("Antwoord met een plaats tussen de 1 en 9")
                    print(plaats[0], plaats[1], plaats[2])
                    print(plaats[3], plaats[4], plaats[5])
                    print(plaats[6], plaats[7], plaats[8])
                elif plaats[int(verplaats) - 1] != "X":
                    print("Hier staat geen steen van jou")
                    print(plaats[0], plaats[1], plaats[2])
                    print(plaats[3], plaats[4], plaats[5])
                    print(plaats[6], plaats[7], plaats[8])
                else:
                    print(plaats[0], plaats[1], plaats[2])
                    print(plaats[3], plaats[4], plaats[5])
                    print(plaats[6], plaats[7], plaats[8])
                    while True:
                        plaatsSpeler = input("Waar wil je deze steen plaatsen?")
                        if plaatsSpeler not in plaatsen:
                            print("Antwoord met een plaats tussen de 1 en 9")
                        elif plaatsSpeler in plaats:
                            plaats[int(verplaats) - 1] = verplaats
                            plaats[int(plaatsSpeler) - 1] = "X"
                            verplaatsjuist = True
                            print(plaats[0], plaats[1], plaats[2])
                            print(plaats[3], plaats[4], plaats[5])
                            print(plaats[6], plaats[7], plaats[8])
                            break
                        else:
                            print("Deze plaats is bezet")
                        print(plaats[0], plaats[1], plaats[2])
                        print(plaats[3], plaats[4], plaats[5])
                        print(plaats[6], plaats[7], plaats[8])
            if (plaats[0] == "X" and plaats[1] == "X" and plaats[2] == "X") or (
                    plaats[3] == "X" and plaats[4] == "X" and plaats[5] == "X") or (
                    plaats[6] == "X" and plaats[7] == "X" and plaats[8] == "X") or (
                    plaats[0] == "X" and plaats[3] == "X" and plaats[6] == "X") or (
                    plaats[1] == "X" and plaats[4] == "X" and plaats[7] == "X") or (
                    plaats[2] == "X" and plaats[5] == "X" and plaats[8] == "X") or (
                    plaats[0] == "X" and plaats[4] == "X" and plaats[8] == "X") or (
                    plaats[2] == "X" and plaats[4] == "X" and plaats[6] == "X"):
                print(f"{naamSpeler1} heeft gewonnen")
                break
            else:
                verplaatsjuist = False
                while not verplaatsjuist:
                    verplaats = input(f"Welke steen wil {naamSpeler2} verplaatsen")
                    if verplaats not in plaatsen:
                        print("Antwoord met een plaats tussen de 1 en 9")
                        print(plaats[0], plaats[1], plaats[2])
                        print(plaats[3], plaats[4], plaats[5])
                        print(plaats[6], plaats[7], plaats[8])
                    elif plaats[int(verplaats) - 1] != "O":
                        print("Hier staat geen steen van jou")
                        print(plaats[0], plaats[1], plaats[2])
                        print(plaats[3], plaats[4], plaats[5])
                        print(plaats[6], plaats[7], plaats[8])
                    else:
                        print(plaats[0], plaats[1], plaats[2])
                        print(plaats[3], plaats[4], plaats[5])
                        print(plaats[6], plaats[7], plaats[8])
                        while True:
                            plaatsSpeler = input("Waar wil je deze steen plaatsen?")
                            if plaatsSpeler not in plaatsen:
                                print("Antwoord met een plaats tussen de 1 en 9")
                            elif plaatsSpeler in plaats:
                                plaats[int(verplaats) - 1] = verplaats
                                plaats[int(plaatsSpeler) - 1] = "O"
                                verplaatsjuist = True
                                print(plaats[0], plaats[1], plaats[2])
                                print(plaats[3], plaats[4], plaats[5])
                                print(plaats[6], plaats[7], plaats[8])
                                break
                            else:
                                print("Deze plaats is bezet")
                            print(plaats[0], plaats[1], plaats[2])
                            print(plaats[3], plaats[4], plaats[5])
                            print(plaats[6], plaats[7], plaats[8])
    antwoordjuist = False
    while not antwoordjuist:
        antwoord = input("Wil je nog een keer spelen?")
        if antwoord.lower() == "ja":
            antwoordjuist = True
        elif antwoord.lower() == "nee":
            antwoordjuist = True
            print("Dankjewel voor het spelen van Italiaanse Boter, Kaas en Eieren")
            spelactief = False
