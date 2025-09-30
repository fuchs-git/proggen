with open("test.txt", "r") as f:
    wav = f.readlines()

count = 0
for item in wav:
    try:

        if item.split()[8] == "ff7f":
            print("1", end="")
        else:
            print("0", end="")
        count += 1
        if count == 4:
            print(" ", end="")
            count = 0
    except ValueError:
        continue