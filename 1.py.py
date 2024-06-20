import random

def ask_question(question):
    return input(question + '\nОтвет: ')

def random_answer(answers):
    return random.choice(answers)

def catch_ball(chance):
    return random.random() < chance

def game():
    questions = ["Ваше имя?", "Где вы живете?", "Какой ваш любимый цвет?", "Какое ваше любимое животное?", "Какое ваше хобби?"]
    computer_answers = ["На Марсе", "Голубой", "Кот", "Чтение", "Путешествия"]
    history = []
    player_name = ask_question("Введите ваше имя")
    
    for i in range(10):
        print(f"Ход {i+1}")
        if catch_ball(0.7):
            answer = ask_question("Компьютер бросает мяч:\nБросок, вы поймали мяч.\nВопрос: " + questions[i % len(questions)])
            history.append((f"Игрок ({player_name})", questions[i % len(questions)], answer))
        else:
            answer = random_answer(computer_answers)
            print(f"Компьютер бросает мяч:\nБросок, вы не поймали мяч.\nВопрос: {questions[i % len(questions)]}\nОтвет: {answer}")
            history.append(("Компьютер", questions[i % len(questions)], answer))
        
        if catch_ball(0.7):
            answer = random_answer(computer_answers)
            print(f"Вы бросаете мяч:\nБросок, компьютер поймал мяч.\nВопрос: {questions[i % len(questions)]}\nОтвет: {answer}")
            history.append(("Компьютер", questions[i % len(questions)], answer))
        else:
            answer = ask_question("Вы бросаете мяч:\nБросок, компьютер не поймал мяч.\nВопрос: " + questions[i % len(questions)])
            history.append((f"Игрок ({player_name})", questions[i % len(questions)], answer))
    
    print("\nИтог игры:")
    for entry in history:
        print(f"{entry[0]} -> {entry[1]}: {entry[2]}")

game()
