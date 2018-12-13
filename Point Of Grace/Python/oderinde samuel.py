#name: oderinde samuel oladimeji
#occupation: student/programmer/entrepreneur
#contact details
#twitter: @zheph_walker
#instagram: @zheph_walker
#whatsapp: 09091357470



#program to run a test of knowledge

print("enter yes or no")

def get_questions():
      return [["python is a general purpose language? ", "yes"],
             ["it easy to learn ? ", "yes"],
             ["it has its own idle? ", "yes"],
             ["is the code lagos programme free? ", "yes"],
             ["python is trash? ", "no"]]

def check_question(question_and_answer):
    question = question_and_answer[0]
    answer = question_and_answer[1]

    given_answer = input(question)

    if answer == given_answer:
        print("correct")
        return True
    else:
        print("incorrect, correct was: ", answer)
        return False

def run_test(question):
    if len(question) == 0:
        print("no questions were given. ")
        return
    index = 0
    right = 0
    while index < len(question):
        if check_question(question[index]):
            right = right + 1
        index = index + 1

    i = right * 100 / len(question)


    print("you got", round(i, 2) ,
          " % right out of", len(question))

run_test(get_questions())

