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
        self.__rating = rating
    def set_growth(self, growth):
        self.__growth = growth


    def __str__(self):
        return f"Student named {self.__name}, has a rating of {self.__rating}, growth {self.__growth}"
    def __repr__(self):
        return f"Student named {self.__name}, has a rating of {self.__rating}, growth {self.__growth}"

    def __del__(self):
        print(f"Student {self.__name} was deleted")

def main():
    student1 = Student("Yurii Troian", 14, 172, 1, "IoT")
    student2 = Student("John Joy", 30, 180, 2, "KI")
    student3 = Student("Julie Juli", 56, 165, 3, "SA")

    print(student1)
    print(student2)
    print(student3)

main()


