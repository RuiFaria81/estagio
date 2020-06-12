from Question import Question

question_prompt = [
    "De que cor são as maças?\n(a) Verde\n(b) Azul\n(c) Castanho\n\n",
    "De que cor são as bananas\n(a) Branco\n(b) Verde \n(c) Amarelo\n\n",
    "De que cor são os morangos?\n(a) Preto\n(b) Vermelho\n(c) Rosa\n\n",
    "De que cor são os limões?\n(a) Preto\n(b) Amarelo\n(c) Rosa\n\n",
]

questions = [
    Question(question_prompt [0], "a"),
    Question(question_prompt [1], "c"),
    Question(question_prompt [2], "b"),
    Question(question_prompt [3], "b"),
]






def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1

    if score == len(questions):
        print("Parabéns acertaste todas as perguntas")
    else:
        print("Tu acertaste " + str(score) + "/" + str(len(questions)) + " perguntas")


run_test(questions)