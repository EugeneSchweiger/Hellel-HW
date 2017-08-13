import Godzilla
import Human

def main():
    while True:
        try:
            print ()
            print ("This is Godzilla")
            print ("2-Feed godzilla")
            print ("3-Godzilla stats ")
            print ("4-Human stats")
            print ("-----------------------------")
            print ("0 - Exit")

            user_input = input("Enter you choice: ")
            choice = int(user_input)

            if choice == 2:
                godzilla.eat(human)
            elif choice == 3:
                godzilla.print_god_stats()
            elif choice == 4:
                human.print_hum_stats()
            elif choice == 0:
                print ("Bye!")
                break
            else:
                print ("Chose one of them!")
        except ValueError:
                print("Something went wrong. Try again...")



if __name__ == "__main__":
    godzilla=Godzilla.Godzilla(1000)
    human=Human.Human(100)
    main()


