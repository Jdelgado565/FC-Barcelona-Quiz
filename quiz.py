print("Hello and welcome to the FC Barcelona quiz!")
answerq1=input("Who is the leads the team in goals scored all time? \n a) Lionel Messi \n b) Ronaldinho \n c) Maradona \n d) Ronaldo Nazario")
score= 0

if answerq1 == "a": 
    score = score + 1

print("The answere is a (Lionel Messi)!")

answerq2=int(input("How many Champions League trophies has Barcelona won?"))

if answerq2 == 5:
    score= score + 1

print("The answere is 5!")

answerq3 = input("Neymar joined Barcelona in 2013 after leaving Santos FC in Brazil, true or false? ")
converted_answerq3 = bool(answerq3 == "true")

if converted_answerq3:
    score += 1

print("The answere is True!")

if score == 0:
    print("you scored is 0, you are not a real fan!")

if score == 1:
    print("You scored a 1, you should brush up on your FC Barceliona knowledge!")

if score == 2:
    print("you scored a 2, not bad!")

if score == 3:
    print("Wow you scored a 3! You sure are a Culer!")