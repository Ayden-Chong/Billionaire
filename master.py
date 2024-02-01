from questions_classes import Question_class
from typing import List
from photo import winning_image, starting_image, losing_image
import random


class Master:
    def __init__(self, q_list: List[Question_class]):
        self.q_list = q_list
        self.number = 1
        self.score = 0

    def display_next_question(self):
        current_question = self.q_list[random.randint(0, len(self.q_list)-1)]

        prompt = f"Q {self.number} - {current_question.questions} (True or False): "
        answer = input(prompt).strip().title()
        print(f"Ans: {answer}")

        while answer != 'True'and answer != 'False':
            print("Invalid response")
            answer = input(current_question.questions).strip().title()

        if str(current_question.ans) == answer:
            print("You are correct!")
            self.score += 1
        else:
            print("You were wrong")
        self.number += 1

    def start_quiz(self):
        print(starting_image)
        while self.number <= 10:
            self.display_next_question()

        print(f"Quiz is over, you scored {self.score}")
        if self.score < 5:
            print(losing_image)
        else:
            print(winning_image)
