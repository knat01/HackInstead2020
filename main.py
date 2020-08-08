#Brython things...
from browser import document
from browser.html import P


#The dictionaries
averages = {}
facts = {}


def parseAvgs(): #Populates averages dictionary from avgs.txt
    with open('avgs.txt','r') as f:
        for line in f:
            lst = line.split()
            averages[lst[0]] = float(lst[1]) #First word in line is key, next is value

def parseFacts(): #Populates facts dictionary from facts.txt
    global facts
    isKey = True
    with open('facts.txt','r') as f:
        stripped = [line.strip() for line in f.readlines()] #removes newline character
        for line in stripped:
            if isKey: #For alternating between lines being the key and being the value
                key = line
                isKey = False
            else:
                fact = line
                isKey = True
                facts[key] = fact #First line is key, then the fact string, repeats

def percentComparison(key, value): #Returns a string detailing the percent difference between the average value and inputted value
    global averages
    avg = averages[key]
    
    percentDiff = (abs(value-avg)/((avg+value)/2)) * 100
    if (value > avg):
        return ("Your " + key + " is " + str(percentDiff) + "% greater than average")
    elif (avg > value):
        return ("Your " + key + " is " + str(percentDiff) + "% less than average")
    else:
        return ("Your " + key + " is average!")



parseAvgs()
parseFacts()
print(facts)
print(averages)

        
#This is for running in commandline. to do so, comment out brython code and uncomment this.
##for key in averages.keys(): #Iterate through keys
##    print("What is your " + key)
##    print(percentComparison(key,float(input(" ")))) #user input & function call
##    print(facts[key]) #Print fact about this stat

mode = "numerical"
#The options being "numerical", "non"
currentKey = "salary(CAD)"
#Current key for numerical stats

#Brython code
def submitClicked(event): #Handles the submit button being clicked
    userIn = (document["userTextBox"].value)

    if mode == "numerical":
        try:
            document["zone"] <= P(percentComparison(currentKey,float(userIn)))
        except ValueError:
            document["zone"] <= P("Please double check your input")

#Link our python method to the submit button...
document["submitButton"].bind("click",submitClicked)
