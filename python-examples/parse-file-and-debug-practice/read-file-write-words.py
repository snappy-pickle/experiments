# Sample Python program that reads a file token by token, where  
# file token by token
from concurrent.futures import process
import os

linecount = 0
tokencount = 0

def processFile(targetFile: str, delimiter: str = None):
    # where am i?
    print("Current working directory:", os.getcwd())

    print("Processing target file:", targetFile)

    # opening the text file
    with open(targetFile,'r') as file:
    
        # reading each line    
        for line in file:
            
            # count the lines
            linecount += 1

            # reading each token        
            for token in line.split(delimiter):
    
                # displaying the tokens           
                print(token) 

                # count the tokens
                tokencount += 1

    print("token count = ", tokencount)
    print("Line count = ", linecount)

##################################

processFile('GFG.txt')
processFile('people-list.csv',',')