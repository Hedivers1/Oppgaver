aldersgrense = 18

alder = int(input("Hvor gammel er du? "))

if alder > aldersgrense:
    print(f"Du er {alder} år , og gammel nok.")
else:
    print(f"Du er {alder} år , og ikke gammel nok.")

print("Takk for at du sjekket!")


    #Test 17 år
    #Jeg tror dette blir ikke gammel nok, fordi 17 er mindre enn 18.

    #Test 18 år
    #Jeg tror dette blir gammel nok, fordi 18 er lik aldersgrensen.

    #Test 19 år
    #Jeg tror dette blir gammel nok, fordi 19 er større enn 18.

#Bytte ut >= med > gjorde at 18 år ikke lenger er gammel nok, fordi 18 ikke er større enn 18.

#Reflekter og noter:

#Hva skjedde i steg 5 og 6? Hva forteller innrykket og kolonet Python?

#Linjen fra steg 7 ble skrevet ut uansett hvilken alder du skrev inn. Hvorfor?

#Uttrykket alder >= aldersgrense kjenner du fra forrige modul. Hva slags verdi gir det? Hvordan bruker if den verdien?

#I utvidelsen: hvilken av > og >= er riktig for en aldersgrense på 18? Hvorfor er dette en lett feil å gjøre?
