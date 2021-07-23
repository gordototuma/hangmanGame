import os
import random

wo_un=[]


def process(input_word,word_is):    
    global wo_un
    for i,char in enumerate(word_is):
        if input_word == char:
            wo_un[i] = input_word


def underscore(word_is):
    global wo_un
    wo_un = ["_" for x in range(len(word_is))]


def word():
    a = random.randint(0,171)
    with open("./data.txt", "r", encoding="utf-8") as words:
        return words.readlines()[a].replace("\n","")


def main():
    word_is = word()
    input_word=""
    underscore(word_is) 
    while "".join(wo_un) != word_is and input_word != word_is:
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")
        
        if input_word.isnumeric():
                print("Ingresa solo caracteres\n")
        
        print("¡Adivina la palabra!")
        print("No olvides las tildes\n")
        print(" ".join(wo_un).upper())              
        input_word = input("\nIngresa una letra: ")
        process(input_word,word_is)
        
    os.system("cls")
    print(f"¡Ganaste! La palabra es: {word_is.upper()}")

if __name__ == "__main__":
    main()
