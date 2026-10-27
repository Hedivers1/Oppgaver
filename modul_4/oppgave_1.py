
navn = input("Hva heter du? ")

print("Hei,", navn)

print(f"Hei, {navn}!")

alder = input("Hvor gammel er du? ")
alder = int(alder)
print(type(alder))

print(f"Neste år blir du {alder + 1} år gammel")

høyde = input("Hvor høy er du i meter? ")
høyde = float(høyde)

print(type(høyde))
print(f"Du er {høyde} meter høy")


#Reflekter og noter:

# Hva svarte type() på alderen før du brukte int()? Hvorfor tror du input() gir deg akkurat denne datatypen?
#Type() svarte på alderen som en string før jeg brukte int(). Dette er fordi input() alltid returnerer en streng, uansett hva brukeren skriver inn.

# Hva klaget Python på i steg 5? Beskriv feilmeldingen med egne ord.
# Python klaget på at man ikke kan legge sammen en streng og et heltall.


# Sammenlign print("Hei,", navn) og f-strengen. Hvilken synes du er lettest å lese? Hva skjer med mellomrommene i de to variantene?
# Jeg synes f-strengen er lettest å lese. I f-strengen kan man skrive variabelen direkte inn i strengen, mens i den andre varianten må man bruke komma for å legge til variabelen. 
# Mellomrommene blir håndtert automatisk i f-strengen, mens i den andre varianten må man passe på å legge til mellomrom selv.

# Hva tror du skjer hvis brukeren skriver tretti i stedet for 30? Prøv.
# Hvis brukeren skriver "tretti" i stedet for "30", vil Python kaste en ValueError når den prøver å konvertere strengen til et heltall med int(). 
# Dette er fordi "tretti" ikke kan tolkes som et tall.
