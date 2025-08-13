def main() -> None:
    name: str = input("What's your name? ")
    print(hello(name))
    print(goodbye(name))

def hello(name: str="world") -> str:
    return f"hello, {name}"

def goodbye(name: str="world") -> str:
    return f"goodbye, {name}"

if __name__ == "__main__":
    main()