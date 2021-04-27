import this

def demo(gruss, name):
    nachricht = "{}, {}!".format(gruss, name)
    nachricht = f"{gruss}, {name}!"
    print(nachricht)


if __name__ == "__main__":
    demo("Hoi", "Fabian")
    demo("Sali", "Sarah")
    demo("Hallo", "Hans")