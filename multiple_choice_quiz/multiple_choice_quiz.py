from questions import Question


question_prompts = [
    "De qué color son las manzanas?\n(a) Rojo/Verde\n(b) Violeta\n(c) Naranja\n\n",
    "De qué color son las bananas?\n(a) Amarillo\n(b) Magenta\n(c) Naranja\n\n",
    "De qué color son las frutillas?\n(a) Verde\n(b) Rojo\n(c) Azul\n\n",
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "a"),
    Question(question_prompts[2], "b"),
]


def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("Obtuviste " + str(score) + "/" + str(len(questions)) + " correctas")


run_test(questions)
