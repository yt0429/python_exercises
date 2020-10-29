namelist = ("Bill", "Anne", "Angy", "Cony", "Daniel", "Occhan")

def main(x):
    for i, x in enumerate(x):
        if i == 2:
            print("{}.My name is {}.".format(i+1,"Andy"))
        else:
            print("{}.{} is my classmate".format(i+1,x))

if __name__ == "__main__":
    main(namelist)

