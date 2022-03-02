class Grandfather() :
    def __init__(self,*letter):
        self.letter = letter
        self.names = []

    def add(self):
        while True :
            choice = int(input("Enter '1' if you wanna add name otherwise enter 'any number'"))
            if choice == 1 :
                name = input("Enter name :")
                self.names.append(name)
            elif choice != 1 :
                break
            else :
                print("Check your input")
        print(self.names)

    def find(self):
        find = input("Enter name : ")
        for name in self.names :
            if find in name :
                print(name)


gf = Grandfather()
gf.add()
gf.find()
