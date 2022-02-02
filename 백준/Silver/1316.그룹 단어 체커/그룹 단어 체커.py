def checkGroupWord(word):
  wordDict = {word[0]: 1}
  
  for i in range(1, len(word)):
    if (word[i] != word[i-1]):
      if (word[i] in wordDict):
        return False
      wordDict[word[i]] = 1
  return True

n = int(input())
result = 0

for i in range(n):
  inputWord = input()
  if checkGroupWord(inputWord):
    result += 1
print(result)