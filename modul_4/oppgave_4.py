alder = 25
er_student = True
har_medlemskort = False


#DEL 1

#Jeg tror dette blir False, fordi 25 er mindre enn 12 og er_student er True.
print(alder < 12 or alder > 67)

#Jeg tror dette blir True, fordi 25 er mindre enn 30 og er_student er True.
print(er_student and alder < 30)

#Jeg tror dette blir True, fordi har_medlemskort er False.
print(not har_medlemskort)

# Jeg tror dette blir False, fordi er_student er True og har_medlemskort er False.
print(er_student and har_medlemskort)

#Jeg tror dette blir True, fordi er_student er True.
print(er_student or har_medlemskort)

#Jeg tror dette blir True, fordi er_student er False og alder er mindre enn 30.
print(not er_student or alder < 30 )

#DEL 2

alder = int(input("Hvor gammel er du? "))
er_student = input("Er du student? (ja/nei) ").lower() == "ja"

# Gratis hvis brukeren er under 12 eller over 67
if alder < 12 or alder > 67:
    pris = 0

# Rabatt hvis brukeren er student og under 30
elif er_student and alder < 30:
    pris = 50

# Vanlig pris for alle andre
else:
    pris = 120

print(f"Biletten koser {pris} kr.")

#Hva skjer hvis brukeren skriver Ja med stor J? Hvorfor? (Tenk tilbake på oppgave 5 i forrige modul.)
# Hvis brukeren skriver "Ja" med stor J, vil programmet tolke det som "nei" fordi sammenligningen er case-sensitive. 
# Derfor vil ikke brukeren få studentrabatten, selv om de er student.

#Prøv å skrive input(...).lower() == "ja" i stedet, og test igjen. Hva tror du .lower() gjør?
# Hvis man bruker .lower(), vil det konvertere hele strengen til små bokst

#Reflekter og noter:

# Forklar forskjellen på and og or med egne ord.
#Forskjellen på and og or er at and krever at begge betingelsene er sanne for at hele uttrykket skal være sant, mens or krever at minst en av betingelsene er sann for at hele uttrykket skal være sant

# Hvilken pris fikk 35-åringen som er student? Hvorfor?
# 35-åringen som er student fikk vanlig pris på 120 kr, fordi de ikke oppfyller noen av de første to betingelsene. De er ikke under 12 eller over 67, og de er ikke under 30.

# Hva gjør not? Kunne du skrevet sjekken i steg 4 uten not? Hvordan?
# Not gjør at man kan sjekke om en betingelse ikke er sann. Man kunne skrevet sjekken i steg 4 uten not ved å bruke en annen logisk operator, for eksempel ved å bruke or i stedet for and.

# Hva om en 70-åring også er student? Hvilken regel slår inn, og spiller rekkefølgen i kjeden noen rolle her?
# Hvis en 70-åring også er student, vil den første regelen om gratis billett slå inn, fordi de er over 67. Rekkefølgen i kjeden spiller en rolle her, fordi hvis man hadde sjekket for studentrabatt først, ville de fått rabatt i stedet for gratis billett.
