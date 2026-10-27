riktig_svar = "Oslo"

svar = input("Hva er hovedstaden i Norge? ")

if svar.lower() == riktig_svar.lower():
    print("Riktig!")
else:
    print("Feil! Riktig svar er:", riktig_svar)

alder = int(input("Hvor gammel er du? "))

if alder >= 18:
    print("Du er akkurat myndig!")
else:
    print("Du er ikke 18.")



# Når du skriver inn 18, vil programmet likevel skrive «Du er ikke 18.»
# Det skjer fordi input() gir deg tekst, mens sammenligningen bruker heltallet 18.
# Rett dette ved å gjøre svaret om til et heltall med int():
# Dette kalles en logisk feil: Programmet kjører uten feilmelding, men gir feil resultat.

#Reflekter og noter:

#Hva var feilene? Beskriv dem kort med egne ord.
#Feilen var at når brukeren skrev inn alderen sin, ble den lagret som en tekststreng (string) i stedet for et heltall (int). Derfor ble sammenligningen med tallet 18 ikke korrekt, og programmet ga feil resultat.
# I tillegg så kunne man skrive Oslo med stor O, men ikke oslo med liten o. Dette er en logisk feil fordi programmet kjører uten feilmelding, men gir feil resultat.

#Den siste feilen ga ingen feilmelding. Hvordan oppdaget du den? Hvorfor tror du Python ikke klager?
#Nei den ga ingen feilmelding fordi programmet kjører, men gir feil resultat. Jeg oppdaget den ved å teste med verdien 18 og se at utskriften ikke var som forventet.

#Hva er forskjellen på en syntaksfeil og en logisk feil? Hvilken av dem tror du er farligst i et ekte program?
#Forskjellen på en syntaksfeil og en logisk feil er at en syntaksfeil oppstår når koden ikke følger språkets regler, og programmet vil ikke kjøre før feilen er rettet. 
# En logisk feil oppstår når koden kjører, men gir et uventet eller feil resultat. 
# Logiske feil kan være farligere i et ekte program fordi de kan gå ubemerket hen og føre til feilaktige resultater eller handlinger.

#Hvilke verdier er lurt å teste med for å finne logiske feil i et program som dette?
#Verdier som er på grensen av betingelsene, som 17, 18 og 19, er lurt å teste med for å finne logiske feil i et program som dette. 
# Dette hjelper med å sikre at programmet håndterer alle relevante tilfeller korrekt.
