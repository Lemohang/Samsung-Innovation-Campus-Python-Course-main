def match_checker(tags):
    opening = ["<html>", "<body>", "<h1>", "<p>", "<ul>", "<li>"]
    closing = ["</html>", "</body>", "</h1>", "</p>", "</ul>", "</li>"]

    stack = []
    for tag in tags:
        if tag in opening:
            stack.append(tag)
        elif tag in closing:
            if len(stack) == 0:
                return False
            if opening.index(stack.pop()) != closing.index(tag):
                return False
    return len(stack) == 0

text = input("Enter a HTML string: ")

tags = []
start = text.find("<")
while start != -1:
    end = text.find(">", start + 1)
    if end == -1:
        break
    tag = text[start:end + 1]
    tags.append(tag)
    start = text.find("<", end + 1)

if match_checker(tags):
    print("Valid input")
else:
    print("Invalid input")

for tag in tags:
    print(tag, end=" ")




            