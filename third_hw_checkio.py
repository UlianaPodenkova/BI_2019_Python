def checkio(data: list) -> list:
    # Your code here
    # It's main function. Don't remove this function
    # It's used for auto-testing and must return a result for check.
    bunch_1 = []
    for elmnt in data:
        if data.count(elmnt) == 1:
            bunch_1.append(elmnt)
    for x in bunch_1:
        data.remove(x)
    # replace this for solution
    return data
