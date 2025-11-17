myMixedTypeList = [45, 290578, 1.02, True, "My dog is on the bed.", "45"]
print(type(myMixedTypeList))
print(type(myMixedTypeList[0])) #45
print(type(myMixedTypeList[1])) #290578
print(type(myMixedTypeList[2])) #1.02
print(type(myMixedTypeList[3])) #True
print(type(myMixedTypeList[4])) #"My dog is on the bed."
print(type(myMixedTypeList[5])) #"45"

print("=======")
print(type(myMixedTypeList))
for item in myMixedTypeList:
    print(type(item))