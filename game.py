import os
import random

wo_un=[]


def process(input_word,word_is):    
    global wo_un
    for i,char in enumerate(word_is):
        if input_word == char:
            wo_un.insert(i,input_word)
            wo_un.pop()


def underscore(word_is):
    global wo_un
    wo_un = ["_" for x in range(1,len(word_is))]


def word():
    a = random.randint(0,171)
    with open("./data.txt", "r", encoding="utf-8") as words:
        return words.readlines()[a]


def main():
    word_is = word()
    input_word=""
    underscore(word_is) 

    while input_word != word_is or "".join(wo_un) != word_is:
        os.system("cls")
        print("¡Adivina la palabra!\n")
        print(" ".join(wo_un))        
        input_word = input("\nIngresa una letra: ")
        process(input_word,word_is)
   

if __name__ == "__main__":
    main()
