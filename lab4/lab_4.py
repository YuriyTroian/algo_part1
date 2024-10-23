from cmd import PROMPT


class Student():
    def __init__(self, name = "", rating = 0, growth = 0, course_num = 0, specialty = ""):
        self.__name = name
        self.__rating = rating
        self.__growth = growth
        self.course_num = course_num
        self.specialty = specialty


    def get_name(self):
        return self.__name
    def get_rating(self):
        return self.__rating
    def get_growth(self):
        return self.__growth

    def set_name(self, name):
        self.__name = name
    def set_rating(self, rating):
        if 0 < rating < 10:
            self.__rating = rating
        else:
            print("Рейтинг відємний")
    def set_growth(self, growth):
        self.__growth = growth


    def __str__(self):
        return f"Student named {self.__name}, has a rating of {self.__rating}, growth {self.__growth}"
    def __repr__(self):
        return f"Student named {self.__name}, has a rating of {self.__rating}, growth {self.__growth}"

    def __del__(self):
        print(f"Student {self.__name} was deleted")

def create_student(name, rating, growth, course_num, specialty):
    if rating > 50:
        print(f"Рейтинг {rating} завеликий. Відрахувати студента {name}.")
        return None

    return Student(name, rating, growth, course_num, specialty)

def main():
    student_Arr = [
        create_student("Yurii Troian", 14, 172, 1, "IoT"),
        create_student("John Joy", 30, 180, 2, "KI"),
        create_student("Julie Juli", 56, 165, 3, "SA")
    ]

    print(student_Arr)

    #student1 = create_student("Yurii Troian", 14, 172, 1, "IoT")
    #student2 = create_student("John Joy", 30, 180, 2, "KI")
    #student3 = create_student("Julie Juli", 56, 165, 3, "SA")

main()

