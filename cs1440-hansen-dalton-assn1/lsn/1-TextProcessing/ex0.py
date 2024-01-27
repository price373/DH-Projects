def findWords(sentence):
    sentence.split()
    wordsToReturn = []
    wordList = sentence.split()
    print(wordList)
    for word in range(len(wordList)):
        wordlength = list((wordList[word]))
        if len(wordlength) > 5:
            continue
        else:
            wordsToReturn.append(wordList[word])


    return wordsToReturn
    # TODO: Return the words in `sentence` that are five characters or less
    # for word in sentence...
        # *Hint Hint* The `split` method on strings may be useful...
        # `help(str.split)`


if __name__ == '__main__':
    provided = [
        "Craftsman Keep Reveal personal it harmful engine short friendly killer honest season and camera strange hiccup horseshoe sphere charismatic ceiling sweet formation substitute daughter perfect",
        "Keep reject",
        "Do or do not, there is no try.",
        "TechnicallyI'mOneWordOnly",
        "One two skip a few, 99 100!"
    ]

    resultList = []
    for string in provided:
        resultList.append(findWords(string))

    for result in resultList:
        print(result)

    # Should Output:
        # ['Keep', 'it', 'short', 'and', 'sweet']
        # ['Keep']
        # ['Do', 'or', 'do', 'not,', 'there', 'is', 'no', 'try.']
        # []
        # ['One', 'two', 'skip', 'a', 'few,', '99', '100!']
