class student:
    def __init__(self,firstname,course,language):
        self.firstname = firstname
        self.course = course
        self.language = language

    def sleep(self):
        print(self.firstname, "is sleeping")


c = student("Caleb", "MIT","Python")
print(c.firstname)
print(c.course)
c.sleep()



student2 = student("Clarence","Web","Kotlin")

print(student2.firstname)
print(student2.course)
student2.sleep()