from edu.hillel.homework.Task36.plane import Plane
from edu.hillel.homework.Task36.train import Train
import sys
def main():
    plane1 = Plane(100, 1000, 12000)
    train1 = Train(50, 120, 2000)
    while True:
        try:
            print ()
            print ("~ Welcome to Train and Plane simulator ~")
            print ("We have Plane and Train")
            print ("Chose what to do:")
            print ("-"*50)
            print ("  1 - Start Train engine")
            print ("  2 - Stop Train engine")
            print ("  3 - Start Plane turbine")
            print ("  4 - Stop Plane turbine")
            print ("  5 - Refuel Train")
            print ("  6 - Refuel Plane")
            print ("  7 - Ride with train")
            print ("  8 - Fly with plane")
            print ("  9 - Print Train info")
            print ("  10 - Print Plane info")
            print ("-"*50)
            print ("     0 - Exit")

            user_input = input("Enter you choice: ")
            choice = int(user_input)

            if choice == 1:
                train1.start_engine()
            elif choice == 2:
                train1.stop_engine()
            elif choice == 3:
                plane1.start_turbine()
            elif choice==4:
                plane1.stop_turbine()
            elif choice == 5:
                fuel=int(input("enter amount of fuel to refuel Train(liters)"))
                train1.refuel(fuel)
            elif choice == 6:
                fuel = int(input("enter amount of fuel to refuel Plane(liters)"))
                plane1.refuel(fuel)
            elif choice == 7:
                dist=int(input("Enter distance for Train travel(km)"))
                train1.drive(dist)
            elif choice == 8:
                dist = int(input("Enter distance for Plane travel(km)"))
                plane1.fly(dist)
            elif choice == 9:
                train1.print_info()
            elif choice == 10:
                plane1.print_info()
            elif choice == 0:
                print ("Bye!")
                break
            else:
                print ("Chose one of them!")
        except ValueError:
                print("Something went wrong. Try again...")



if __name__ == "__main__":
    main()
    print(sys.path)