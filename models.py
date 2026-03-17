from datetime import datetime


class Question:
    def __init__(self, question_id, text, options, correct_answer, topic):
        self.question_id = question_id
        self.text = text
        self.options = options  # dict: {"A": "...", "B": "...", "C": "...", "D": "..."}
        self.correct_answer = correct_answer  # "A", "B", "C", or "D"
        self.topic = topic

    def check_answer(self, user_answer):
        """Returns True if user_answer matches correct_answer."""
        return user_answer.upper() == self.correct_answer.upper()

    def to_dict(self):
        return {
            "question_id": self.question_id,
            "text": self.text,
            "options": self.options,
            "correct_answer": self.correct_answer,
            "topic": self.topic,
        }


class TestResult:
    def __init__(self, student_name, answers, questions):
        self.student_name = student_name
        self.answers = answers  # dict: {question_id: user_answer}
        self.questions = questions
        self.timestamp = datetime.now()
        self.score, self.total, self.details = self._calculate_score()

    def _calculate_score(self):
        """Calculate score and return (score, total, details list)."""
        score = 0
        total = len(self.questions)
        details = []
        for q in self.questions:
            user_ans = self.answers.get(str(q.question_id), "")
            correct = q.check_answer(user_ans)
            if correct:
                score += 1
            details.append({
                "question": q.text,
                "topic": q.topic,
                "user_answer": user_ans,
                "correct_answer": q.correct_answer,
                "options": q.options,
                "is_correct": correct,
            })
        return score, total, details

    def get_percentage(self):
        if self.total == 0:
            return 0
        return round((self.score / self.total) * 100, 1)

    def get_grade(self):
        pct = self.get_percentage()
        if pct >= 90:
            return "A"
        elif pct >= 80:
            return "B"
        elif pct >= 70:
            return "C"
        elif pct >= 60:
            return "D"
        else:
            return "F"

    def get_formatted_timestamp(self):
        return self.timestamp.strftime("%B %d, %Y at %I:%M %p")

