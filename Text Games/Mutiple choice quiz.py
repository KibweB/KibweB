from question import question

question_prompts=[
"What year was basketball invented?\n(a)1939 \n(b)1904 \n(c)1891\n\n",
"What is Spider-Man's full name?\n(a)Peter Parker \n(b)Ben Reily \n(c)Flash Thompson\n\n",
"How many rings does Tom Brady have?\n(a)6 \n(b)5 \n(c)7\n\n",
]

questions=[
    question(question_prompts[0], "c"),
    question(question_prompts[1], "a"),
    question(question_prompts[2], "c"),  
]

def run_test(questions):
    score=0
    for question in questions:
        answer=input(question.prompt)
        if answer==question.answer:
            score +=1
    print("\nYou got "+str(score)+"/"+str(len(questions)) +" correct")

run_test(questions)