class Course():

    def __init__(self,id,nombre,profesor):
        self.id_curso=id
        self.nombre_curso=nombre
        self.profesor_curso=profesor
        self.enrolled_students=[]
        self.parciales=[]
    
    def remove_student(self,student):
        if student.nombre in self.enrolled_students:
            self.enrolled_students.remove(student.nombre)
            student.entolled_course.remove(self.nombre_curso)
            print(f"{student.nombre} Ha sido removido del curso exitosamente {self.nombre_curso}")

        else:
            print(f"{student.nombre} no se encuentra matriculado en el curso {self.nombre_curso}")
    
    def get_student_list(self):
        if self.enrolled_students:
            print(f"los estudiantes son",self.enrolled_students)
        else: 
            print(f"el curso {self.enrolled_students} no tiene estudiantes ")    

class Parcial():

    def __init__(self,curso,nombre,porcentaje,preguntas):
        self.nombre=nombre
        self.porcentaje=porcentaje
        self.preguntas=preguntas
        curso.parciales.append([self.nombre,self.porcentaje,self.preguntas])

apoo=Course("1","apoo","jonatan")

class Profesor(Parcial):

    def __init__(self,id,nombre,edad):
        
        self.id=id
        self.edad=edad
        self.cargo="profesor"
        self.materias=[]
        self.parciales=[]

jonatan=Profesor("1a","jonatan alberto de jesus",25)
jonatan.Create(apoo,"examen final",25,"1) si nado me mojo? 2)si salto me elevo? 3) si bajo voy hacia arriba? ")
print(apoo.parciales)

class Student():

    def __init__(self,id,nombre,edad):
        self.id=id
        self.nombre=nombre.lower()
        self.edad=edad
        self.cargo="estudiante"
        self.enrolled_course=[]
    
    def EnrolledCourse(self,course):
        self.enrolled_course.append(course)
        course.enrolled_students.append(self.nombre)

alveiro=Student("2b","aleveiro zapato sepulveda de nazaret",85)

alveiro.EnrolledCourse(apoo)
apoo.get_student_list()
