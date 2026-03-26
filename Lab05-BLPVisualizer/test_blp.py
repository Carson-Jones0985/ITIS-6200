from blp import BLPModel

def setup():
    model = BLPModel()
    model.add_subject("Alice", "S", "U")
    model.add_subject("Bob", "C", "C")
    model.add_subject("Eve", "U", "U")

    model.add_object("pub.txt", "U")
    model.add_object("emails.txt", "C")
    model.add_object("username.txt", "S")
    model.add_object("password.txt", "TS")

    return model

while True:
    print("\nSelect a test to run: ")
    print("\nOptions")
    print("\n    [1-18] Run a specific test case (1 to 18)")
    print("\n    [A] Run all test cases sequentially")
    print("\n    [Q] Quit")

    choice = input("\nEnter choice: ")

    if (choice == "1"):
        model = setup()
        print("--------Testing case 1--------")
        print(f"Alice starting level: {model.subjects["Alice"].current_level}")

        model.read("Alice", "emails.txt")
    elif (choice == "2"):
        model = setup()
        print("--------Testing case 2--------")
        print(f"Alice starting level: {model.subjects["Alice"].current_level}")

        model.read("Alice", "password.txt")
    elif (choice == "3"):
        model = setup()
        print("--------Testing case 3--------")
        print(f"Eve starting level: {model.subjects["Eve"].current_level}")

        model.read("Eve", "pub.txt")
    elif choice == "4":
        model = setup()
        print("--------Testing case 4--------")
        print(f"Eve starting level: {model.subjects["Eve"].current_level}")

        model.read("Eve", "emails.txt")
    elif (choice == "5"):
        model = setup()
        print("--------Testing case 5--------")
        print(f"Bob starting level: {model.subjects["Bob"].current_level}")

        model.read("Bob", "password.txt")
    elif (choice == "6"):
        model = setup()
        print("--------Testing case 6--------")
        print(f"Alice starting level: {model.subjects["Alice"].current_level}")

        model.read("Alice", "emails.txt")
        model.write("Alice", "pub.txt")
    elif (choice == "7"):
        model = setup()
        print("--------Testing case 7--------")
        print(f"Alice starting level: {model.subjects["Alice"].current_level}")

        model.read("Alice", "emails.txt")
        model.write("Alice", "password.txt")
    elif (choice == "8"):
        model = setup()
        print("--------Testing case 8--------")
        print(f"Alice starting level: {model.subjects["Alice"].current_level}")

        model.read("Alice", "emails.txt")
        model.write("Alice", "emails.txt")
        model.read("Alice", "username.txt")
        model.write("Alice", "emails.txt")
    elif (choice == "9"):
        model = setup()
        print("--------Testing case 9--------")
        print(f"Alice starting level: {model.subjects["Alice"].current_level}")

        model.read("Alice", "username.txt")
        model.write("Alice", "emails.txt")
        model.read("Alice", "password.txt")
        model.write("Alice", "password.txt")
    elif (choice == "10"):
        model = setup()
        print("--------Testing case 10--------")
        print(f"Alice starting level: {model.subjects["Alice"].current_level}")
        print(f"Bob starting level: {model.subjects["Bob"].current_level}")

        model.read("Alice", "pub.txt")
        model.write("Alice", "emails.txt")
        model.read("Bob", "emails.txt")
    elif (choice == "11"):
        model = setup()
        print("--------Testing case 11--------")
        print(f"Alice starting level: {model.subjects["Alice"].current_level}")
        print(f"Bob starting level: {model.subjects["Bob"].current_level}")

        model.read("Alice", "pub.txt")
        model.write("Alice", "username.txt")
        model.read("Bob", "username.txt")
    elif (choice == "12"):
        model = setup()
        print("--------Testing case 12--------")
        print(f"Alice starting level: {model.subjects["Alice"].current_level}")
        print(f"Bob starting level: {model.subjects["Bob"].current_level}")

        model.read("Alice", "pub.txt")
        model.write("Alice", "password.txt")
        model.read("Bob", "password.txt")
    elif (choice == "13"):
        model = setup()
        print("--------Testing case 13--------")
        print(f"Alice starting level: {model.subjects["Alice"].current_level}")
        print(f"Eve starting level: {model.subjects["Eve"].current_level}")

        model.read("Alice", "pub.txt")
        model.write("Alice", "emails.txt")
        model.read("Eve", "emails.txt")
    elif (choice == "14"):
        model = setup()
        print("--------Testing case 14--------")
        print(f"Alice starting level: {model.subjects["Alice"].current_level}")
        print(f"Eve starting level: {model.subjects["Eve"].current_level}")

        model.read("Alice", "emails.txt")
        model.write("Alice", "pub.txt")
        model.read("Eve", "pub.txt")
    elif (choice == "15"):
        model = setup()
        print("--------Testing case 15--------")
        print(f"Alice starting level: {model.subjects["Alice"].current_level}")

        model.set_level("Alice", "S")
        model.read("Alice", "username.txt")
    elif (choice == "16"):
        model = setup()
        print("--------Testing case 16--------")
        print(f"Alice starting level: {model.subjects["Alice"].current_level}")
        print(f"Eve starting level: {model.subjects["Eve"].current_level}")

        model.read("Alice", "emails.txt")
        model.set_level("Alice", "U")
        model.write("Alice", "pub.txt")
        model.read("Eve", "pub.txt")
    elif (choice == "17"):
        model = setup()
        print("--------Testing case 17--------")
        print(f"Alice starting level: {model.subjects["Alice"].current_level}")
        print(f"Eve starting level: {model.subjects["Eve"].current_level}")

        model.read("Alice", "username.txt")
        model.set_level("Alice", "C")
        model.write("Alice", "emails.txt")
        model.read("Eve", "emails.txt")
    elif (choice == "18"):
        model = setup()
        print("--------Testing case 18--------")
        print(f"Eve starting level: {model.subjects["Eve"].current_level}")

        model.read("Eve", "pub.txt")
        model.read("Eve", "emails.txt")
    elif choice == "A":

        model = setup()
        print("\n--------Testing case 1--------")
        print(f"Alice starting level: {model.subjects["Alice"].current_level}")

        model.read("Alice", "emails.txt")

        model = setup()
        print("\n--------Testing case 2--------")
        print(f"Alice starting level: {model.subjects["Alice"].current_level}")

        model.read("Alice", "password.txt")

        model = setup()
        print("\n--------Testing case 3--------")
        print(f"Eve starting level: {model.subjects["Eve"].current_level}")

        model.read("Eve", "pub.txt")

        model = setup()
        print("\n--------Testing case 4--------")
        print(f"Eve starting level: {model.subjects["Eve"].current_level}")

        model.read("Eve", "emails.txt")

        model = setup()
        print("\n--------Testing case 5--------")
        print(f"Bob starting level: {model.subjects["Bob"].current_level}")

        model.read("Bob", "password.txt")

        model = setup()
        print("\n--------Testing case 6--------")
        print(f"Alice starting level: {model.subjects["Alice"].current_level}")

        model.read("Alice", "emails.txt")
        model.write("Alice", "pub.txt")

        model = setup()
        print("\n--------Testing case 7--------")
        print(f"Alice starting level: {model.subjects["Alice"].current_level}")

        model.read("Alice", "emails.txt")
        model.write("Alice", "password.txt")

        model = setup()
        print("\n--------Testing case 8--------")
        print(f"Alice starting level: {model.subjects["Alice"].current_level}")

        model.read("Alice", "emails.txt")
        model.write("Alice", "emails.txt")
        model.read("Alice", "username.txt")
        model.write("Alice", "emails.txt")

        model = setup()
        print("\n--------Testing case 9--------")
        print(f"Alice starting level: {model.subjects["Alice"].current_level}")

        model.read("Alice", "username.txt")
        model.write("Alice", "emails.txt")
        model.read("Alice", "password.txt")
        model.write("Alice", "password.txt")

        model = setup()
        print("\n--------Testing case 10--------")
        print(f"Alice starting level: {model.subjects["Alice"].current_level}")
        print(f"Bob starting level: {model.subjects["Bob"].current_level}")

        model.read("Alice", "pub.txt")
        model.write("Alice", "emails.txt")
        model.read("Bob", "emails.txt")

        model = setup()
        print("\n--------Testing case 11--------")
        print(f"Alice starting level: {model.subjects["Alice"].current_level}")
        print(f"Bob starting level: {model.subjects["Bob"].current_level}")

        model.read("Alice", "pub.txt")
        model.write("Alice", "username.txt")
        model.read("Bob", "username.txt")

        model = setup()
        print("\n--------Testing case 12--------")
        print(f"Alice starting level: {model.subjects["Alice"].current_level}")
        print(f"Bob starting level: {model.subjects["Bob"].current_level}")

        model.read("Alice", "pub.txt")
        model.write("Alice", "password.txt")
        model.read("Bob", "password.txt")

        model = setup()
        print("\n--------Testing case 13--------")
        print(f"Alice starting level: {model.subjects["Alice"].current_level}")
        print(f"Eve starting level: {model.subjects["Eve"].current_level}")

        model.read("Alice", "pub.txt")
        model.write("Alice", "emails.txt")
        model.read("Eve", "emails.txt")

        model = setup()
        print("\n--------Testing case 14--------")
        print(f"Alice starting level: {model.subjects["Alice"].current_level}")
        print(f"Eve starting level: {model.subjects["Eve"].current_level}")

        model.read("Alice", "emails.txt")
        model.write("Alice", "pub.txt")
        model.read("Eve", "pub.txt")

        model = setup()
        print("\n--------Testing case 15--------")
        print(f"Alice starting level: {model.subjects["Alice"].current_level}")

        model.set_level("Alice", "S")
        model.read("Alice", "username.txt")

        model = setup()
        print("\n--------Testing case 16--------")
        print(f"Alice starting level: {model.subjects["Alice"].current_level}")
        print(f"Eve starting level: {model.subjects["Eve"].current_level}")

        model.read("Alice", "emails.txt")
        model.set_level("Alice", "U")
        model.write("Alice", "pub.txt")
        model.read("Eve", "pub.txt")

        model = setup()
        print("\n--------Testing case 17--------")
        print(f"Alice starting level: {model.subjects["Alice"].current_level}")
        print(f"Eve starting level: {model.subjects["Eve"].current_level}")

        model.read("Alice", "username.txt")
        model.set_level("Alice", "C")
        model.write("Alice", "emails.txt")
        model.read("Eve", "emails.txt")

        model = setup()
        print("\n--------Testing case 18--------")
        print(f"Eve starting level: {model.subjects["Eve"].current_level}")

        model.read("Eve", "pub.txt")
        model.read("Eve", "emails.txt")
    elif choice == 'Q':
        break

