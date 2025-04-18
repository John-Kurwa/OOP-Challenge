from pet import Pet

if __name__ == "__main__":
    print("🐾 Welcome to the Virtual Pet Simulator!")
    name = input("What would you like to name your pet? 🐶: ")
    pet = Pet(name)

    # The loop for the methods.
    while True:
        print("\nWhat would you like to do?")
        print("1. Feed 🍗")
        print("2. Let it sleep 😴")
        print("3. Play 🎾")
        print("4. Train a new trick 🎓")
        print("5. Show tricks 🧠")
        print("6. Show pet status 📋")
        print("7. Exit ❌")

        choice = input("Enter choice (1–7): ")

        # Methods/ actions, user can perform.
        if choice == "1":
            pet.eat()
        elif choice == "2":
            pet.sleep()
        elif choice == "3":
            pet.play()
        elif choice == "4":
            trick = input("Enter a trick to teach your pet: ")
            pet.train(trick)
        elif choice == "5":
            pet.show_tricks()
        elif choice == "6":
            pet.get_status()
        elif choice == "7":
            print(f"Goodbye! 👋 {pet.name} will miss you!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 7.")
