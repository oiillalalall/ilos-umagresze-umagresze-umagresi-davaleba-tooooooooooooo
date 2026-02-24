class Student:
    def __init__(self, სახელი, გვარი, ასაკი):
        self.სახელი = სახელი
        self.გვარი = გვარი
        self.ასაკი = ასაკი

    def get_info(self):
        print(f"სტუდენტის სახელი: {self.სახელი}\nსტუდენტის გვარი: {self.გვარი}")
        #aq tqven rom oopl.py chaagdet amiti mivyevi lol onlinze kartofils vwvavdi da kargat ver gavige amitom oopl.py-s mivyvebi
        #ai es @staticmethod da @classmethod ver movuwvi raari googlshi uew vnaxav
class School:
    def __init__(self, სკოლის_სახელი, სკოლის_მისამართი):
        self.სკოლის_სახელი = სკოლის_სახელი
        self.სკოლის_მისამართი = სკოლის_მისამართი
        self.სტუდენტები = []

    def add_student(self, სტუდენტი):
        self.სტუდენტები.append(სტუდენტი)

    def remove_student(self, ინდექსი):
        if 0 <= ინდექსი < len(self.სტუდენტები):
            self.სტუდენტები.pop(ინდექსი)
        else:
            print("არასწორი ინდექსი ბრაააააატ")

    def show_students(self):
        if not self.სტუდენტები:
            print("სია ცარიელიაააა")
        for სტუდენტი in self.სტუდენტები:
            სტუდენტი.get_info()

school_obi = School("186-საჯარო სკოლა", "იოანე პეტრიწის რაღაცა ნომერი")
student_obi = Student("ილია", "ზაბახიძე", "15")
student_obi1 = Student("ბადრი", "შუბლაძე", "50")
student_obi2 = Student("გრიშა", "ონიანი", "54")

school_obi.add_student(student_obi) #esec oop.py dan mivxvdi rogor unda meqna
school_obi.add_student(student_obi1)
school_obi.add_student(student_obi2)

#vaaaa ar yofila zalian zneli magram rom ar vusmendi cota gamiwirda
#vcdilob rom ai gamoyeneba shevamciro da marto ertxel gamoviyene
# remove_studentis gaketeba ar vicodi vecade metviton mefiqra magramm ar vicodi rogor meqnna
#amitom am ertxel gamovikene ai
#danarcheni marto powerpointis slide shouebit da oopl.py ro chaagzavnet magas gavyevi
#es kargiaa kargiaa kargiaaaaa

