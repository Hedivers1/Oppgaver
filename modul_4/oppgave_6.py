riktig_brukernavn = "Hedda"
riktig_passord = "python123"

brukernavn = input("Skriv inn brukernavn:")
passord = input("Skriv inn passord: ")
alder = int(input("Skriv inn alderen din: "))

if brukernavn == riktig_brukernavn and passord == riktig_passord:
    if alder < 13:
        print ("Du er for ung til å logge inn")
    print(f"Velkommen, {brukernavn}!")
elif brukernavn == riktig_brukernavn:
    print("Feil passord!")
else:
    print("Ukjent bruker.")

#Test

#1 riktig brukernavn, riktig passord
#Jeg tror den svarer Velkommen, Hedda! fordi både brukernavn og passord er riktige.
#Den gir riktig svar: Velkommen, Hedda!

#2 riktig brukernavn, feil passord
#Jeg tror den svarer Feil passord! fordi brukernavnet er riktig, men passordet er feil.
#Den gir svaret: Feil passord.

#3 feil brukernavn, riktig passord
#Jeg tror den svarer både feilpassord og ukjent bruker.
#Den svarte kun ukjent bruker.

#4 feil brukernavn, feil passord
#Jeg tror den kommer til å svare ukjent bruker. 
#Den svarte ukjent bruker

#Refleksjon og Notater:

#Hvordan løste du oppgaven? Brukte du and, eller noe annet? Finnes det flere måter å løse den på?
#Jeg brukte and for å sjekke at både brukernavn og passord var riktige. Jeg kunne også brukt flere if-setninger inni hverandre.

#I hvilken rekkefølge måtte sjekkene stå? Hva skjedde hvis du endret den?
#Sjekken av både brukernavn og passord måtte komme først. Hvis bare brukernavnet ble sjekket først, kunne programmet skrevet «Feil passord!» selv om passordet var riktig.

#Mange ekte nettsider skriver bare «Feil brukernavn eller passord», uten å si hvilken av dem som var feil. Hvorfor tror du det?
#Meldingen «Feil brukernavn eller passord» gjør det vanskeligere for uvedkommende å finne ut hvilke brukernavn som finnes.

#Hvorfor er det lurt å teste alle fire kombinasjonene, og ikke bare den der alt er riktig?
#Alle fire kombinasjonene bør testes for å sjekke at programmet gir riktig melding også når noe er feil.
