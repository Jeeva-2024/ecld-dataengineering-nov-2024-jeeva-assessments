def stutter(word):
    start = word[0:2]
    count = 0
    while count < 2:
        stutter = start + "... "
        print(stutter, end="")
        count = count + 1
    print(word + "?")


stutter("incredible")