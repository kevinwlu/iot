# IoT Textbook Chapter 6 Lab Exercises: Word count and top ten words

import sys
import string
def readFile(filename):
    fc = open(filename, 'r')
    contents= fc.read()
    fc.close()
    return contents
def wordCount(contents):
    wordCount = 0
    wordCountDict = {}
    lowerContents = contents.lower()
    listWords = lowerContents.split()
    stopWords = ['a', 'and', 'the', 'are', 'be', 'is',
                 'by', 'for', 'from', 'in', 'of', 'on',
                 'to', 'with', 'that', 'which'
                ]
    for word in listWords:
        word = word.strip(string.punctuation)
        wordCount = wordCount + 1
        if not word in stopWords:
            if wordCountDict.has_key(word):
                wordCountDict[word] = wordCountDict[word] + 1
            else:
                wordCountDict[word] = 1
    print "Word Count: %d" % (wordCount)
    return wordCountDict
def topTenWords(wordCountDict):
    topTenWords = sorted(wordCountDict.iteritems(), key=lambda x: -x[1])[:10]
    print "Top Ten Words: " + str(topTenWords)
def main():
    filename = sys.argv[1]
    contents = readFile(filename)
    wordCountDict = wordCount(contents)
    topTenWords(wordCountDict)
if __name__ == '__main__':
    main()
