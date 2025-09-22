# Basiese sakrekenaar program.
# Hierdie program hardloop op CMD.
# Funksies: plus, minus, maal, deel.
# Elke berekening is in sy eie funksie.
# Die program gebruik 'n while loop met 'n sentinel variable om die program te hardloop totdat die gebruiker kies om af te sluit.
# Die verwyder opsie verwyder die uitset.

# Funksie vir plus
def plus(a, b):
    return a + b

# Funksie vir minus
def minus(a, b):
    return a - b

# Funksie vir maal
def multiply(a, b):
    return a * b

# # Funksie vir deel (met nul-toets)
def divide(a, b):
    if b == 0:
        return "Error: Kan nie deur nul deel nie."
    return a / b

# Hoof program loop
def calculator():
    result = None  # Stoor die laaste resultaat
    running = True  # Sentinel variable om die loop te beheer

     # Terwyl die sentinel variable 'running' waar is, hou die program aan hardloop
    while running:
        # Wys die hoof titel en huidige resultaat
        print("\n")
        print("--- Basiese Sakrekenaar ---")
        print("\n")
        print("Huidige resultaat:", result)
        print("\n")
        # Wys die lys van beskikbare funksies
        print("Funksies:")
        print("1. Plus (+)")
        print("2. Minus (-)")
        print("3. Maal (*)")
        print("4. Deel (/)")
        print("5. Verwyder resultaat")
        print("6. Afsluit")
        print("\n")

        # Kry die gebruiker se keuse
        choice = input("Kies 'n opsie (1-6): ")

        # As die gebruiker 'n geldige bewerking kies
        if choice in ["1", "2", "3", "4"]:
            try:
                # Vra die gebruiker vir twee getalle
                num1 = float(input("Eerste getal: "))
                num2 = float(input("Tweede getal: "))
            except ValueError:
                # Foutboodskap as gebruiker nie getalle invoer nie
                print("Ongeldige invoer. Voer asseblief net getalle in.")
                continue
            
            # Doen die berekening volgens die keuse
            if choice == "1":
                result = plus(num1, num2)
            elif choice == "2":
                result = minus(num1, num2)
            elif choice == "3":
                result = multiply(num1, num2)
            elif choice == "4":
                result = divide(num1, num2)

             # Wys die nuwe resultaat
            print("Resultaat:", result)

        # As gebruiker die resultaat wil verwyder
        elif choice == "5":
             # Stel die resultaat terug na 'None'
            result = None
            print("Resultaat verwyder.")

         # As gebruiker wil afsluit
        elif choice == "6":
            # Verander sentinel veranderlike na False om die loop te stop
            running = False
            print("Sakrekenaar sluit af...")

          # As gebruiker 'n ongeldige opsie kies
        else:
            print("Ongeldige keuse. Kies asb 'n geldige opsie.")

# Hardloop die sakrekenaar
calculator()