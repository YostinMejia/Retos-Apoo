from dataclasses import dataclass

@dataclass
class Person:
    Name:str
    Age:int
    Hair_Color:str

    def Walk(self,Distance:int)-> str:
        return f"voy a caminar {Distance} metros"

    def Eat(self,Food:str)-> str:
        return f"coy a come {Food}"

    def Speak(self,Languge:str)-> str:
        return f"Yo hablo {Languge}"

class Student(Person):
    
    def Study(self, Subject)-> str:
        return f"estoy estudiando {Subject}"


class Teacher(Person):
    
    def Teach(self,Subject)-> str:
        return f"estoy enseñando {Subject}"


if __name__=="__main__":
    
        yostin=Student("yostin",18,"negro")
        octavio=Student("Octavio",32,"negro")

        marcelo=Teacher("marcelo",88,"azul")
        rodrigo=Teacher("rodrigo",67,"marron")

        print(yostin.Age)
        print(yostin.Walk(12))
        print(yostin.Eat("mortadela"))
        
        print(octavio.Speak("maleantoso"))
        print(octavio.Study("Modelado 3d"))

        print(marcelo.Teach("Modelado 3d"))
        
  
