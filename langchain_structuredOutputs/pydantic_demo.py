from pydantic import BaseModel

class Student(BaseModel):
    name: str


new_student = {"name": "Akshat"}
student = Student(**new_student)
print(student.name)