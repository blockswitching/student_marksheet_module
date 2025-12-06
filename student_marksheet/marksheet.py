class Marksheet:
    def __init__(self, student_name, roll_no):
        self.student_name = student_name
        self.roll_no = roll_no
        self.marks = {}

    def add_mark(self, subject, score):
        if not isinstance(score, (int, float)):
            raise ValueError("Score must be a number.")
        if score < 0 or score > 100:
            raise ValueError("Score must be between 0 and 100.")
        self.marks[subject] = score

    def total(self):
        return sum(self.marks.values())

    def percentage(self):
        if len(self.marks) == 0:
            return 0
        return self.total() / len(self.marks)

    def grade(self):
        p = self.percentage()
        if p >= 90:
            return "A+"
        elif p >= 75:
            return "A"
        elif p >= 60:
            return "B"
        elif p >= 45:
            return "C"
        else:
            return "D"

    def export_json(self):
        return {
            "student_name": self.student_name,
            "roll_no": self.roll_no,
            "marks": self.marks,
            "total": self.total(),
            "percentage": self.percentage(),
            "grade": self.grade()
        }

    def export_text(self):
        text = f"Marksheet for {self.student_name} (Roll {self.roll_no})\n"
        text += "--------------------------------------------------\n"
        for subject, score in self.marks.items():
            text += f"{subject}: {score}\n"
        text += "--------------------------------------------------\n"
        text += f"Total: {self.total()}\n"
        text += f"Percentage: {self.percentage():.2f}%\n"
        text += f"Grade: {self.grade()}\n"
        return text
