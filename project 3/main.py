class Names() :
    def __init__(self,*letter):
        self.letter = letter
        self.names = []

    def add(self):
        while True :
            choice = int(input("\nEnter '1' for add name\n'2' for add list of names\n'any number' for exit :"))
            if choice == 1 :
                name = input("Enter name :")
                self.names.append(name)
            elif choice == 2 :
                name_list = []
                no_of_name = int(input("Enter how many name you want in list : "))
                while  no_of_name>0 :
                    no_of_name -= 1
                    name = input("Enter name : ")
                    name_list.append(name)
                self.names.append(name_list)

            elif choice != 1 and 2 :
                break
            else :
                print("Check your input")
        print(self.names)

    def find(self):
        find = input("Enter name : ")
        for name in self.names :
            if find in name :
                print(name)
            for n in name :
                if find in n :
                    print(n)



gf = Names()
gf.add()
gf.find()
