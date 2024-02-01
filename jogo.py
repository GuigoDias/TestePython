import divination

print("Do you want to play the divination game?")
testIfPlay = int(input("(1) Yes (2) No\n"))

if(testIfPlay == 1):
    divination.play_Divination()