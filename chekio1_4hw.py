def checkio(first, second):
    first = first.split(',')
    second = second.split(',')
    common_words = []
    for element in first:
        if element in second:
            common_words.append(element)
    common_words.sort()
    result = '"' + ",".join(common_words) + '"'
    return result


print(checkio("hello,world", "hello,earth"))
