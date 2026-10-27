#Poeng karakterer

poeng = int(input("Skriv inn antallpoeng: "))

#Forventet: 95 gir A, 85 gir B, 75 gir C, 55 gir D, 45 gir E, 35 gir F
if poeng >= 90:
    print ("A")
elif poeng >= 80:
    print ("B")
elif poeng >= 60:
    print ("C")
elif poeng >= 50:
    print ("D")
elif poeng >= 40:
    print ("E")
else:
    print ("F")

# Jeg tror 95 gir E, fordi den første betingelsen er sann.
if poeng >= 40:
    print("E")
elif poeng >= 50:
    print("D")
elif poeng >= 60:
    print("C")
elif poeng >= 80:
    print("B")
elif poeng >= 90:
    print("A")
else:
    print("F")


# Når jeg byttet ut elif med if, så ble det slik at alle betingelsene ble sjekket uavhengig av om en tidligere betingelse var sann eller ikke.
# Derfor fikk jeg flere utskrifter for samme poengsum. For eksempel, hvis poeng var 95, så ble både A og E skrevet ut, fordi begge betingelsene var sanne.
if poeng >= 90:
    print ("A")
if poeng >= 80:
    print ("B")
if poeng >= 60:
    print ("C")
if poeng >= 50:
    print ("D")
if poeng >= 40:
    print ("E")
else:
    print ("F")

#Utvidelse: Hva skjer hvis du skriver inn 150 eller -10? Legg til sjekker som gir en feilmelding i stedet for en karakter. Tenk over hvor i kjeden de må stå.
if poeng > 100 or poeng < 0:
    print("Feil: Poengsummen må være mellom 0 og 100.")

#Reflekter og noter:

# Hva skjedde i steg 4? Hvorfor fikk 95 poeng den karakteren den fikk? 
# I steg 4 snudde vi rekkefølgen på betingelsene. Derfor fikk 95 poeng karakteren E, fordi den første betingelsen som ble sjekket var poeng >= 40, som er sann for 95.

## Hva skjedde i steg 5? Hva er forskjellen på flere if etter hverandre og en if/elif-kjede?
# Det som skjedde i steg 5 var at jeg byttet ut elif med if. Dette gjorde at alle betingelsene ble sjekket uavhengig av om en tidligere betingelse var sann eller ikke. 
# Derfor fikk jeg flere utskrifter for samme poengsum. For eksempel, hvis poeng var 95, så ble både A og E skrevet ut, fordi begge betingelsene var sanne.

# For B skriver vi bare poeng >= 80. Hvorfor trenger vi ikke også sjekke at poengene er under 90?
# Vi trenger ikke sjekke at poengene er under 90, fordi vi allerede har sjekket det i den første betingelsen. Hvis poeng var 90 eller høyere, ville den første betingelsen vært sann, og vi ville ikke kommet til den andre betingelsen.

# Når kjører else-delen?
# Else-delen kjører når ingen av de andre betingelsene er sanne. Det vil si at poeng er mindre enn 40.

