from time import sleep

name = raw_input("Please enter your name: ")
print "Hello", name, "!"
sleep(1)
print "Is this your first rodeo?"
sleep(1)
print("0. No")
sleep(1)
print("1. Yes")
sleep(1)
answer = raw_input("Which one is it?")
if(answer == "1"):
    print "Would you like help with a story?"
    sleep(1)
    print "Of course you would, you've executed my program!"
    sleep(2)
    print "Broadly borrowing from Joseph Campbell, Dan Harmon describes stories as having the fundamental form of: "
    sleep(1)
    print "1) A character is in a zone of comfort, "
    sleep(1)
    print "2) But they want/need something."
    sleep(1)
    print "3) They enter an unfamiliar situation, "
    sleep(1)
    print "4) Face trials, "
    sleep(1)
    print "5) Learn\Get what they wanted, "
    sleep(1)
    print "6) Which allows them to confront something, "
    sleep(1)
    print "7) Then return to their familiar situation, "
    sleep(1)
    print "8) Having Changed."
    sleep(5)
    print "Take Campbell or Harmon however you want, but I think it can be a helpful tool."
    sleep(2)
    print "I think the concepts of 'Intention' and 'Obstacle' in screenplay are similarly useful"
    sleep(2)
    print "That's even simpler than this. It just basically asks what does a character want/need/must and what's in the way of it?"
    sleep(1)
    print "Anyway, back to the point."
    sleep(2)
    print "We'll use the short hand of: "
    sleep(1)
    print "1) YOU: A character is in a zone of comfort, "
    sleep(1)
    print "2) NEED: But they want/need something."
    sleep(1)
    print "3) GO: They enter an unfamiliar situation, "
    sleep(1)
    print "4) SEARCH: Face trials, "
    sleep(1)
    print "5) FIND: Learn\Get what they wanted, "
    sleep(1)
    print "6) TAKE: Which allows them to confront something, "
    sleep(1)
    print "7) RETURN: Then return to their familiar situation, "
    sleep(1)
    print "8) CHANGE: Having changed."
    sleep(5)
    print "Does that make sense?"
    sleep(2)
    print "Hope so!"
    sleep(2)
    print "I'm going to prompt you for each of those steps in your burgeoning story!"
    sleep(.1)
    print "Okay, then let's skip to the good part!"
    sleep(1)
    you = raw_input("Who?")
    sleep(.1)
    need = raw_input("Need, must or want to?")
    sleep(.1)
    because = raw_input("because...")
    sleep(.1)
    go = raw_input("So they go to _____")
    sleep(.1)
    search = raw_input("To face the trials of...")
    sleep(.1)
    find = raw_input("Finding?")
    sleep(.1)
    take = raw_input("Which allows them to confront?")
    sleep(.1)
    retrn = raw_input("So they can return to _____?")
    sleep(.1)
    change = raw_input("But not exactly, because now _____?")
    sleep(.1)
    print "Okay, so it's a story about", you, "who needs to", need, "because", because, ".So, they go to", go, "making it through", search, "all while finding", find, "which allows them to confront", take, ". They return to", retrn, "but not exactly because now ", change, "?"
    sleep(5)
    print "Hmmm, does that make sense?"
    sleep(2)
    print "."
    sleep(1)
    print ".."
    sleep(1)
    print "..."
    sleep(1)
    print "To be honest, I'm not programmed to make sense of that! I'm not even programmed beyond the next two lines, sorry."
    sleep(.5)
    print "Good luck", name, "!"
elif(answer == "0"):
    print "Okay, then let's skip to the good part!"
    sleep(1)
    you = raw_input("Who?")
    sleep(.1)
    need = raw_input("Need, must or want to?")
    sleep(.1)
    because = raw_input("because...")
    sleep(.1)
    go = raw_input("So they go to _____")
    sleep(.1)
    search = raw_input("Making it through...")
    sleep(.1)
    find = raw_input("Finding?")
    sleep(.1)
    take = raw_input("Which allows them to confront?")
    sleep(.1)
    retrn = raw_input("So they can return to _____?")
    sleep(.1)
    change = raw_input("But not exactly, because now _____?")
    sleep(.1)
    print "Okay, it's a story about", you, "who needs to", need, "because", because, ".So, they go to", go, "making it through", search, "all while finding", find, "which allows them to confront", take, ". They return to", retrn, "but not exactly because now ", change, ". Is that right?"
    sleep(5)
    print "Hmmm, does that make sense?"
    sleep(2)
    print "."
    sleep(1)
    print ".."
    sleep(1)
    print "..."
    sleep(1)
    print "To be honest, I'm not programmed to make sense of that! I'm not even programmed beyond the next two lines, sorry."
    sleep(.5)
    print "Good luck", name, "!"
