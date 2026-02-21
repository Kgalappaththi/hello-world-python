def main():
    name = input("Enter your name: ")
    if not name.strip():
        print("Name cannot be empty!")
    else:
        print(f"Hello, {name}! Welcome to my first GitHub research project.")
    print("Git allows tracking all changes.")

if __name__ == "__main__":
    main()
