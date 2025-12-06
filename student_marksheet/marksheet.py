from typing import Dict, Union, Any

class Marksheet:
    """
    A class to represent a student's academic marksheet.
    
    This class handles the storage of subject marks, calculation of 
    totals, percentages, and grades, and provides methods to export 
    the data in different formats (JSON-compatible dict or formatted text).
    """

    def __init__(self, student_name: str, roll_no: Union[str, int]):
        """
        Initialize the Marksheet object.

        Args:
            student_name (str): The name of the student.
            roll_no (str or int): The unique roll number or ID of the student.
        """
        self.student_name = student_name
        self.roll_no = roll_no
        # Initialize an empty dictionary to store subject-wise marks
        self.marks: Dict[str, Union[int, float]] = {}

    def add_mark(self, subject: str, score: Union[int, float]) -> None:
        """
        Add or update a mark for a specific subject.

        Args:
            subject (str): The name of the subject (e.g., "Math").
            score (int or float): The score obtained (must be between 0 and 100).

        Raises:
            ValueError: If the score is not a number or is outside the 0-100 range.
        """
        # Validate that the score is a numeric type
        if not isinstance(score, (int, float)):
            raise ValueError(f"Score for '{subject}' must be a number.")

        # Validate that the score is within a realistic range
        if score < 0 or score > 100:
            raise ValueError(f"Score for '{subject}' must be between 0 and 100.")

        self.marks[subject] = score

    def total(self) -> Union[int, float]:
        """
        Calculate the sum of all marks.

        Returns:
            int or float: The total sum of marks added so far.
        """
        return sum(self.marks.values())

    def percentage(self) -> float:
        """
        Calculate the percentage based on the marks added.
        
        Assumes every subject is out of 100.

        Returns:
            float: The calculated percentage. Returns 0 if no marks exist 
            to avoid DivisionByZero errors.
        """
        # Prevent division by zero if the marksheet is empty
        if len(self.marks) == 0:
            return 0.0
        return self.total() / len(self.marks)

    def grade(self) -> str:
        """
        Determine the letter grade based on the calculated percentage.

        Grading Scale:
            A+: >= 90
            A : >= 75
            B : >= 60
            C : >= 45
            D : < 45

        Returns:
            str: The letter grade.
        """
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

    def export_json(self) -> Dict[str, Any]:
        """
        Generate a dictionary representation of the marksheet.
        
        Useful for API responses or saving to a database.

        Returns:
            dict: A dictionary containing student details, marks, and calculated stats.
        """
        return {
            "student_name": self.student_name,
            "roll_no": self.roll_no,
            "marks": self.marks,
            "total": self.total(),
            "percentage": self.percentage(),
            "grade": self.grade()
        }

    def export_text(self) -> str:
        """
        Generate a human-readable string representation of the marksheet.
        
        Useful for printing to console or saving to a text file.

        Returns:
            str: A formatted string suitable for display.
        """
        # Start constructing the formatted string
        text = f"Marksheet for {self.student_name} (Roll {self.roll_no})\n"
        text += "-" * 50 + "\n"
        
        # Iterate through marks and append to string
        for subject, score in self.marks.items():
            text += f"{subject}: {score}\n"
            
        text += "-" * 50 + "\n"
        text += f"Total: {self.total()}\n"
        text += f"Percentage: {self.percentage():.2f}%\n"
        text += f"Grade: {self.grade()}\n"
        
        return text