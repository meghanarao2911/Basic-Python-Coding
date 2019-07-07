def getAllLargeValue(listVal):
    getLargeValueIndex = []

    largeValue = listVal[0]

    if len(listVal) == 0:
        return "Empty List"

    for index, val in enumerate(listVal):
        if (largeValue < val):
            getLargeValueIndex.append(index)
            largeValue = val
    return getLargeValueIndex


def updateLargeValue(listValue, allLargeValue):
    count = 0
    largeValueListLength = len(allLargeValue)
    updateLargeList = []

    if (largeValueListLength == 0):
        for ind, val in enumerate(listValue):
            updateLargeList.append(-1)
        return updateLargeList

    largeIndexValue = allLargeValue[count]
    largeValue = listValue[largeIndexValue]

    for ind, val in enumerate(listValue):

        if (listValue[ind] < largeValue):
            updateLargeList.append(largeValue)
        else:
            count = count + 1

            if (count < largeValueListLength):
                largeIndexValue = allLargeValue[count]
                largeValue = listValue[largeIndexValue]
                updateLargeList.append(largeValue)
            else:
                updateLargeList.append(-1)

    updateLargeList[len(updateLargeList) - 1] = -1
    return updateLargeList


list_1 = [2, 1, 6, 5, 6, 20]

list_2 = [22, 1, 6, 5, 6, 20]

Test_case_1 = [2, 1, 5, 2, 6, 2]
Test_case_2 = [2, 1, 5, 2, 6, 20]
Test_case_3 = [22, 1, 5, 2, 6, 20]
Test_case_4 = [0, 1, 5, 2, 6, 20]
Test_case_5 = [100, 111, 115, 222, 666, 777]

val_1 = getAllLargeValue(Test_case_1)
test_case_1a = updateLargeValue(Test_case_1, val_1)
print("1) Input : ", Test_case_1, " and  Output : ", test_case_1a)

val_2 = getAllLargeValue(Test_case_2)
test_case_2b = updateLargeValue(Test_case_2, val_2)
print("2) Input : ", Test_case_2, " and  Output : ", test_case_2b)

val_3 = getAllLargeValue(Test_case_3)
test_case_3c = updateLargeValue(Test_case_3, val_3)
print("3) Input : ", Test_case_3, " and  Output : ", test_case_3c)

val_4 = getAllLargeValue(Test_case_4)
test_case_4d = updateLargeValue(Test_case_4, val_4)
print("4) Input : ", Test_case_4, " and  Output : ", test_case_4d)

val_5 = getAllLargeValue(Test_case_5)
test_case_5e = updateLargeValue(Test_case_5, val_5)
print("5) Input : ", Test_case_5, " and  Output : ", test_case_5e)