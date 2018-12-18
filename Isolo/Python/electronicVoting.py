print("OJIKUTU PAUL TEMIDAYO")
print("dayo.ojikutu@gmail.com")
print("08030561715")
print("This program will be used for Electronic Voting \nUser have to be 18 years and above to participate")
print("Voting can be stopped at anytime by typing 'end' to view the results")
print("Batch 5 CodeLagos\n\n")


voteADP=0
voteAPC=0
votePDP=0
voteSDP=0
rej=0
while True:
    name=input("Enter your name ").lower()
    if(name=="end"):
        break
    print("Welcome " + name)
    dob=input("Enter your year of birth ").lower()
    if(dob=="end"):
        break
    dob=int(dob)
    age=2018 - dob
    if(age >= 18):
        print(name + " you are " + str(age) + " years old and eligible to vote\n")
        print("1. ADP \n2. APC \n3. PDP \n4. SDP")
        party=input("From the options 1 to 4, choose the party you wish to vote for ").upper()
        if(party=="END"):
            break
        elif(party=="1"):
            print("You have voted for ADP \nVote Accepted!\n")
            voteADP=voteADP+1
        elif(party=="2"):
            print("You have voted for APC \nVote Accepted!\n")
            voteAPC=voteAPC+1
        elif(party=="3"):
            print("You have voted for PDP \nVote Accepted!\n")
            votePDP=votePDP+1
        elif(party=="4"):
            print("You have voted for SDP \nVote Accepted!\n")
            voteSDP=voteSDP+1
        elif(party==" "):
            print("Vote unaccepted! \nPlease try again!\n")
            voteADP=voteADP
            voteAPC=voteAPC
            votePDP=votePDP
            voteSDP=voteSDP
        else:
            print("Vote Rejected!\n")
            rej=rej+1
    else:
        print(name + " you are " + str(age) + " years old and not eligible to vote\n")

print("Total votes are; ")
print("ADP " + str(voteADP) + " votes")
print("APC " + str(voteAPC) + " votes")
print("PDP " + str(votePDP) + " votes")
print("SDP " + str(voteSDP) + " votes")
print("Rejected " + str(rej) + " votes")
