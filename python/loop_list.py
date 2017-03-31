def censor(text, word):
    result = []
    lists = text.split()

    print( lists )

    for item in lists:
        if item == word:
            string = ""
            for char in item:
                string += "*"
            result.append(string)
        else:
            result.append(item)

    result = " ".join(result)
    return result

print (censor("hey hey hey", "hey"))
