import csv


class Exams:
    exams = {}
    fieldnames = [
        "Exam Name",
        "Number of Candidates",
        "Number of Passed Exams",
        "Number of Failed Exams",
        "Best Score",
        "Worst Score",
    ]

    def __init__(self, name):
        self.name = name
        self.results = []
        self.candidates = []
        self.scores = []
        self.grades = []

    @classmethod
    def get_results_for_exam(cls, name):
        for row in cls.exams[name].results:
            print(", ".join(row))

    @classmethod
    def load_results(cls, results):
        with open(results) as csvfile:
            reader = csv.reader(csvfile)
            fieldnames = next(reader)  # To omit first row with fieldnames.
            for row in reader:
                if row[0] not in cls.exams.keys():
                    cls.exams[row[0]] = cls(row[0])
                    cls.exams[row[0]].results.append(fieldnames)
                cls.exams[row[0]].results.append(row)
                if row[1] not in cls.exams[row[0]].candidates:
                    cls.exams[row[0]].candidates.append(row[1])
                cls.exams[row[0]].scores.append(row[2])
                cls.exams[row[0]].grades.append(row[3])

    @classmethod
    def make_report(cls):
        for exam in cls.exams.values():
            exam.results = [
                exam.name,
                len(exam.candidates),
                exam.grades.count("Pass"),
                exam.grades.count("Fail"),
                max(exam.scores),
                min(exam.scores),
            ]

    @classmethod
    def generate_report(cls):
        print(",".join(cls.fieldnames))
        for exam in cls.exams.values():
            print(", ".join(map(lambda x: str(x), exam.results)))


Exams.load_results("data/exam_results.csv")
Exams.get_results_for_exam("Maths")
Exams.get_results_for_exam("Physics")
Exams.get_results_for_exam("Biology")
Exams.make_report()
Exams.generate_report()
