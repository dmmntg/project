meme_dict = {
    "CRINGE": "Algo excepcionalmente raro o embarazoso",
    "LOL": "Una respuesta común a algo gracioso",
    "ROFL": "Una respuesta a una broma",
    "SHEESH": "Ligera desaprobación",
    "CREEPY": "Aterrador, siniestro",
    "AGGRO": "Ponerse agresivo o enojado"
}

print("¡Bienvenido al diccionario de memes!")
print("Escribe una palabra que no entiendas (¡en mayúsculas!) y te diremos su significado.")
print("Puedes buscar hasta 5 palabras en una sola ejecucion.\n")

for i in range(5):
    word = input("(" + str(i + 1) + "/5) Escribe una palabra que no entiendas: ")
    
    if word in meme_dict:
        print(word + ": " + meme_dict[word] + "\n")
    else:
        print("Lo siento, esa palabra no esta en nuestro diccionario.\n")
