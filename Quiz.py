def quiz():
    for i in range(len(questions)):
        answer = input(questions[i])
        user_answers.append(answer)

def check_answers():
    score = 0
    for i in range(len(questions)):
        if user_answers[i] == correct_answers[i]:
            score = score + 1
    percent = score / len(questions) * 100
    return percent

def report_score(percent = int):
    if percent > 80:
        print("Great job! You really know your Justice League Trivia!")
    elif percent > 0:
        print("You need to study your Justice League Trivia more!")
    else:
        print("You knew nothing? Do you live under a rock?")

def main():
    quiz()
    percent = check_answers()
    report_score(percent)

questions = ["What is Batman's secret identity?", "Who is Clark Kent's alter ego?", "What city is Aquaman the king of?", "Cyborg used to be a skilled player of which sport?", "Wonder Woman is from what warrior tribe?", "Green Lanterns ring works through which emotion?", "The Flash's powers originate from what source?"]
correct_answers = ["Bruce Wayne", "Superman", "Atlantis", "Football", "Amazons", "Willpower", "The Speed Force"]
user_answers = []


main()