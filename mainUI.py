from logic_layer.LL_api import LL_API

class Main:
    def menu():
        print("\033[91m--------------------------------------\033[0m")
        print("\033[91m---           GLADIATORS           ---\033[0m")
        print("\033[91m--------------------------------------\033[0m")
        print("\033[92m---    #Organizer                  ---\033[0m")
        print("\033[92m---    #Captain                    ---\033[0m")
        print("\033[92m---    #Puplic viewer              ---\033[0m")
        print("\033[92m---                                ---\033[0m")
        print("\033[92m---    #Please select you option   ---\033[0m")
        print("\033[92m---      (1,2,3 or b for back)     ---\033[0m")
        print("\033[96m--------------------------------------\033[0m")
        print("\033[96m---     #Pleas enter your input    ---\033[0m")
        print("\033[96m--------------------------------------\033[0m")
        print("\033[96m--- Back b)                        ---\033[0m")
        print("\033[96m--------------------------------------\033[0m")
        fyrst_input = 8 #This code will change just testing
        while fyrst_input != "1" and fyrst_input != "2" and fyrst_input != "3" and fyrst_input !="b":
            print("Please select a valid valiu")
            fyrst_input = input("")
        if fyrst_input != "1" and fyrst_input != "2" and fyrst_input != "3" and fyrst_input !="b":
            quit
        elif fyrst_input == "1" or fyrst_input == "2" or fyrst_input == "3" or fyrst_input == "b":
            print("nice")

    def orginazer(self):
        self.api =LL_API
        pass

    menu()

pink = "\033[95m"
reset = "\033[0m"
blue = "\033[94m"
neonblue = "\033[96m"
Yellow = "\033[93m"
gray = "\033[90m"
red = "\033[91m"
highlite= "\033[100m"
neongreen = "\033[92m"

print(pink,"########################")
print(pink,"## ",highlite,"--Scooby doo--",reset,pink,"##")


