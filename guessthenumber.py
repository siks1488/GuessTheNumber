import random

def main():
    x = random.randint(1,10)
    you = int(input("Add a number: "))

    if you not in range(1,10):
        print("You must choose a number between 1 and 10")
        return

    def alt():
        print(x,you)

    if you == x :
        print("You won")
        alt()
    else:
      print("You lose")
      alt()


main()
 
