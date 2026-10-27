alder = 31
aldersgrense = 18
navn = "Hedda"
antall_studenter = 30

# Jeg tror resultatet blir : True
print (alder > aldersgrense)

# Jeg tror resultatet blir : True
print (alder == 31)

# Jeg tror resultatet blir : True
print (alder != aldersgrense)

# Jeg tror resultatet blir : False
print (alder <= aldersgrense)

# Jeg tror resultatet blir : True
print (navn == "Hedda")

# Jeg tror resultatet blir : False
print (navn == "hedda")

# Jeg tror resultatet blir : True
print (antall_studenter >= 30)

# Jeg tror resultatet blir : True
print (alder + 5 > antall_studenter)

##Reflekter og noter:

#Uttrykk 5 og 6 ser nesten like ut, men gir ulikt svar. Hvorfor?
# Uttrykk 5 og 6 ser nesten like ut, men gir ulikt svar fordi uttrykk 5 sammenligner navnet "Hedda" med en streng som har stor H, mens uttrykk 6 sammenligner navnet "Hedda" med en streng som har liten h. 
# Strenger er case-sensitive, så de to uttrykkene gir forskjellige resultater.

# Hva er forskjellen på = og ==? Forklar med egne ord.
# Forskjellen på = og == er at = brukes for å tildele en verdi til en variabel, mens == brukes for å sammenligne to verdier.

# Uttrykk 8 inneholder både en aritmetisk og en sammenligningsoperator. Hvilken rekkefølge tror du Python gjør dem i?
# Python gjør først den aritmetiske operasjonen, og deretter sammenligningen. Dette er fordi aritmetiske operatorer har høyere prioritet enn sammenligningsoperatorer.

# Alle svarene her er True eller False. Hvor tror du slike verdier er nyttige i et program?
# True og False verdier er nyttige i et program fordi de kan brukes til å kontrollere flyten i programmet. For eksempel, man kan bruke dem i if-setninger for å bestemme hvilke deler av koden som skal kjøres basert på visse betingelser.

