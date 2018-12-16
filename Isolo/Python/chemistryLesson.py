#OLADEJI ABDULLAH
#07083837048
#oladejiabdullah17@gmail.com
#A test run on the running of a school chemistry lesson plan for specific Grade 1 to Grade 3 students
#CodeLagos Batch5

while True:
    print("OLADEJI ABDULLAH\n07083837048\noladejiabdullah17@gmail.com\nA test run on the running of a school chemistry lesson plan for Grade 1 to Grade 3 students.\nCodeLagos Batch5")
    print("  ")
    print("Instruction: this program only runs for specific Grade 1 to 3 student whose name has been registered to access this program, otherwise you won't gain access")
    print("Chemistry lesson plan for Grades 1-3")
    Grade1=["oladeji abdullah","king george","elijah ebule","clinton"]
    Grade2=["david","zuriel","sammywellz","omoba","oriz ayebo"]
    Grade3=["opara francis","abdulwasiu balogun","mustapha","Abdurroqeeb Jakkari"]
    print("Note:Enter your name below with the appropriate spelling to enable you take the class")
    name=input("Enter your name: ")
    if(name in Grade1):
        print("You're welcome", name, "to grade 1 chemistry, lesson 01")
        print("MATTER\nIntroduction\nChemistry is a branch of science that deals with the study of the nature and the composition of various forms of matter and the way they undergo changes under different external conditions.\n    MATTER is a substance that has mass and occupies space. Matter can exist either in solid, liquid or gaseous state. Various forms of matter abound naturally in the universe as mixtures. They could be mixtures of elements or that of compounds.")
        print("By this definition of matter, it follows that the enviroment we live in is made up of matter. The water we drink, drink, the air we breathe in, the plants andanimals are all forms of matter. It is a common knowledge that students often confuse mass from weight. The two terms are used interchangeably because of the practical units used for the two of them which is gramme or kilogramme. We shall now look at difference between the two terms.")
        print("Experiments have proved that matter is made of particles and the particles of matter could be atoms, molecules or ions.\n     Mass is therefore defined as the total amount of particles a substance contains.\n     Weight is the force acting on a substance due to gravitatonal pull on it.")
        print("from the above definitions, we can see that mass is a countable enity whereas weightis not as it is a pull on a substance.")
        print("Matter can exist in three different physical states. The three different states of matter are:\n{1} Solid state.\n{2} Liquid state.\n{3} Gaseous state.")
        input("Type yes to access your understanding\n ")
        print("Answer the following questions before proceeding to the next lesson")
        print("choose from option a-d")
        ans1=input("Matter is defined to be anything that has____and occupies space.\na. weight \nb. size \nc. mass \nd. all of the above.\nAnswer: ")
        score=0
        if(ans1=="c"):
            score=score+5
        else:
            score=score
            print("Note that matter has mass and not weight")
        ans2=input("Weight is different from the mass of an object due to i) gravitational pull ii) human force.\na. ii only \nb. i only\nc. i and ii\nd. None of the above\nAnswer: ")
        if(ans2=="b"):
            score=score+5
        else:
            score =score
            print("Remember: that weight of an object is due to the mass + gravitational pull to the earth")
        print("You scored", score,"from 10")
        print("Please leave your question if you seem not to understand any part of the lesson")
        input("Question: ")
        print("okay", name,"your question has been noted")
        print("Goodbye", name,"until the next lesson")
        break
    elif(name in Grade2):
        print("You're welcome", name, "to grade 2 chemistry, lesson 01")
        print("ACID\nIntroduction\nAn acid can be defined on the basis of the taste given  by a substance. If a substance has a sour taste, it is    classified as an acid. But recent investigations show that the ability of a substance to taste sour may not be  enough evidence to classify the substance as an acid.")
        print("Thus, acid is now defined on the basis of its behaviour when in solution. From the activities,  we saw that  an   acid.")
        print("    i)	Dissolves and\nii)	Ionises in water")
        print("Applying this, we now define an acid:")
        print("An acid is any substance which will dissolve and readily ionise to produce hydrogen ion,in form of hydroxonium (or oxonium) ion H3O+, when in aqueous solution.")
        print("Acid + Water -----> hydrogen(in form of oxonium ion) + acid radical(anion)")
        print("For acid, we have:\nHA + H2O(l) ---> HA(aq) <----> H2O+(aq) + A-(aq)(oxonium ion)")
        input("Type yes to access your understanding\n ")
        print("Answer the following questions before proceeding to the next lesson")
        print("choose from option a-d")
        ans1=input("What does acid produce when ionised?\na. Oxygen gas\nb. Oxygen ion\nc. Hydrgen ion\nd. Water\nAnswer: ")
        score=0
        if(ans1=="c"):
            score=score+5
        else:
            score=score
            print("Remember: that acid will dissolve and readily ionise to produce hydrogen ion...")
        print("You scored", score,"from 5")
        print("Goodbye", name,"until the next lesson")
        break
    elif(name in Grade3):
        print("You're welcome", name, "to grade 2 chemistry")
        print("Hydrocarbons\nThe simplest form of organic compounds are those containing carbon and hydrogen atoms only. These compounds are called hydrocarbons.")
        print("Classification of hydrocarbons\nHydrocarbons may be classified as:")
        print("i)	Alkanes\nii)	Alkenes\niii)	Alkynes\niv)	Benzenes")
        print("   Alkanes are straight or branched chain hydrocarbons in which all the adjacent carbon atoms in the molecules of the alkanes are joined by single bonds.")
        print("Examples\nStraight chain Alkane H-C-C-C-C-C-H ")
        input("Type yes to access your understanding\n ")
        print("Answer the following questions before proceeding to the next lesson")
        print("choose from option a-d")
        ans1=input("what classification of hydrocarbon  are joined by single bond?\na. Alkenes\nb. Benzenes\nc. Alkynes\nd, Alkanes\nAnswer: ")
        score=0
        if(ans1=="d"):
            score=score+5
        else:
            score=score
            print("Remember: ...carbon atoms in the molecules of Alkanes  are joined by single bond.")
        print("You scored", score,"from 5")
        print("Goodbye", name,"until the next lesson")
        break
    else:
        print("You're not eligible to run this program.")
        break
