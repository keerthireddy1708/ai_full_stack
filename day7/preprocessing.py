with open("sample.txt","r") as file:
    text=file.read()
print(text)
print("No of characters: ",len(text))
print("no of words: ",len(text.split()))
print("no of lines: ",len(text.splitlines()))
