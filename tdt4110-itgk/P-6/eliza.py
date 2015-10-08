# Øving 6 - Oppgave 5
# Håkon Ødegård Løvdal
# Mini-Eliza
# Fil hentet fra øvingssiden, lagt til kode der det mangler

import random # Importerer modulen random (generere tilfeldige tall)
import os

# Funksjon:     pick_sentence
# Beskrivelse:  Plukker ut en tilfeldig tekststreng fra en liste av tekstsetninger
# Input:        En liste av tekststrenger
# Ouput:        En tekststreng
def pick_sentence(sentences):
  return sentences[random.randint(0, len(sentences)-1)]

# Funksjon:     print_sentence
# Beskrivelse:  Skriver ut tre tekststrenger på ei linje til konsoll.
#               Det skal være mellomrom (space) mellom tekststreng en og to.
#               Det skal ikke være mellomrom (space) mellom tekststreng to og tre.
# Input:        Tre tekststrenger
# Output:       Ingen
def print_sentence(text1, text2, text3):
	print(text1, ' ', text2, text3, sep = '')


# Funksjon:     intro_text
# Beskrivelse:  Skriver en velkomsttekst til konsoll som skal inneholde:
#               20 linjeskift
#               Setningen: "Hei, jeg heter Eliza og vil gjerne snakke med deg."
#               Setningen: "Ikke start svar med stor bokstav og bruk hele setninger."
#               Setningen: "Skriv 'hade' hvis du vil avslutte samtalen"
#               Setningen: "**************************************************"
#               1 linjeskift
# Input:        Ingen
# Output:       Ingen
def intro_text():
	os.system("clear")
	print("Hei, jeg heter Eliza og vil gjerne snakke med deg!")
	print("Ikke start svar med stor bokstav og bruk hele setninger.")
	print("Skriv 'hade' hvis du vil avslutte samtalen")
	print("**************************************************")
	print()


# Funksjon:     main
# Beskrivelse:  Hovedfunksjonen i programmet
# Input:        Ingen
# Output:       Ingen
def main():
  # Initialisering av variabler
  answer = "ikke hade" # Sørger for at while-løkka kjører første gang

  # En liste av spørsmål
  questions = ['Hva gjør du', 'Hvordan går det', 'Hvorfor heter du',
              'Liker du å hete', 'Føler du deg bra', 'Hva har du gjort idag',
              'Hva tenker du om framtida', 'Hva gjør deg glad', 'Hva gjør deg trist']

  # En liste av oppfølgningsspørsmål
  follow_ups = ['Hvorfor sier du', 'Hva mener du med', 'Hvor lenge har du sagt',
               'Hvilke tanker har du om', 'Kan du si litt mer om',
               'Når tenkte du første gang på']

  # En liste av responser
  responses = ['Fint du sier det', 'Det skjønner jeg godt', 'Så dumt da', 'Føler meg også sånn',
              'Blir trist av det du sier', 'Så bra', 'Du er jammen frekk']

  # Skriv velkomsttekst til konsoll vha funksjonen intro_text
  intro_text()

  # Spør brukeren om navnet og lagre svaret i en variabel
  navn = input('Hva heter du? ')
  if navn == 'hade':
  	answer = 'hade'

  # Programmet kjører i løkke helt til brukeren svarer "hade"
  while answer != "hade":
    pass

    # NB: All kode her må skrives med to innrykk!!!

    # Plukk ut et tilfeldig spørsmål fra lista questions 
    # ved hjelp av funksjonen pick_sentence
    question = pick_sentence(questions)

    # Skriv spørsmålet etterfulgt av navnet til brukeren
    # og et spørsmålstegn ved hjelp av funksjonen print_sentence
    print_sentence(question, navn, '?')

    # Spør brukeren om et svar med teksten "Svar: " og lagre
    # resultatet i en variabel
    answer = input('Svar: ')

    # Plukk ut et tilfeldig oppfølgingsspørsmål fra lista follow_ups 
    # ved hjelp av funksjonen pick_sentence
    followUp = pick_sentence(follow_ups)

    # Skriv oppfølgningsspørsmålet sammen med svaret fra brukeren
    # og et spørsmålstegn ved hjelp av funksjonen print_sentence
    print_sentence(followUp, answer, '?')

    # Spør brukeren om et svar med teksten "Svar: " uten å lagre
    # resultatet til variabel
    input('Svar: ')

    # Plukk ut en tilfeldig respons fra lista responses 
    # ved hjelp av funksjonen pick_sentence
    respons = pick_sentence(responses)

    # Skriv reponsen sammen med navnet til brukeren
    # og et punktum (".") ved hjelp av funksjonen print_sentence
    print_sentence(respons, navn, '.')
    print()

    # SLik jeg forstår eksempelet skal det kun avgjøres i første spørsmål om det skal avsluttes, 
    # men kjøres ferdig.. Synes det er merkelig, og ville selv hatt et continue statement i en if-setning
    # etter begge svarene. 

main()
