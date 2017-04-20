import re

fileOP=open('madlibs.txt', 'r')

madLibsRegex=re.compile("(ADJECTIVE|NOUN|ADVERB|VERB)") # regex for the keywords
rawText=fileOP.read()

fileOP.close()

moMadLibs=madLibsRegex.findall(rawText)

wordList = []
inputWord = ""

for i in range (len(moMadLibs)): # prompts n user inputs, being n the amount of keywords found on the text file
    if(moMadLibs[i].lower()=='adjective'): # if/else only exists for the sake of differentiating 'a' from 'an'
        inputWord = input("Enter an adjective: ")
    else:
        inputWord = input("Enter a %s: " % moMadLibs[i].lower())
    
    wordList.append(inputWord) # saves each input into a list

finalText=rawText

for i in range(len(wordList)):
    # syntax: re.sub(regex, substitution, dst_string, number_of_subs)
    finalText=re.sub("(ADJECTIVE|NOUN|ADVERB|VERB)", wordList[i], finalText, 1)
    # ^^^ searches for one of the keywords, substitute it for the respective user input, save to 'finalText', repeat
    
print("New text: \n\n" + finalText + "\n")
    
fileOP=open('madlibsfinal.txt', 'w')

fileOP.write(finalText)

print("File created.")

fileOP.close()

