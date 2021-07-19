import os
import random

udscr=[]

def process(input_word):
    if input_word in udscr:
        pass



def underscore():    
    udscr=["_" for x in range(len(word()))]
    for x in udscr:
        print(x, end=" ")


def word():
    a = random.randint(0,171)
    with open("./data.txt", "r", encoding="utf-8") as words:
        return words.readlines()[a]
    


def main():
    os.system("cls")
    print("¡Adivina la palabra!")
    underscore()    
    input_word = input("\nIngresa una letra: ")
    process(input_word)
    


if __name__ == "__main__":
    main()