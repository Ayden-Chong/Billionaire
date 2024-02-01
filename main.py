from questions_classes import Question_class
from master import Master
from questions_list import answers

questions_bank = []
for qndict in answers:
    qn = qndict["question"]
    ans = qndict["answer"]
    questions_bank.append(Question_class(qn,ans))

qm = Master(questions_bank)
qm.start_quiz()
