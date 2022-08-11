# Python program to read 
# file word by word
from concurrent.futures import process
import os

linecount = 0
wordcount = 0

def processFile(targetFile, delimiter):
    # where am i?
    print("Current working directory:", os.getcwd())

    print("Processing target file:", targetFile)

    # opening the text file
    with open(targetFile,'r') as file:
    
        # reading each line    
        for line in file:
            
            # count the lines
            linecount += 1

            # reading each word        
            for word in line.split(delimiter):
    
                # displaying the words           
                print(word) 

                # count the words
                wordcount += 1

    print("Word count = ", wordcount)
    print("Line count = ", linecount)

processFile('GFG.txt')
processFile('people-list.csv',',')