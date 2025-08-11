class HTMLTagMatcher:
    def __init__(self):
        self.opening = ["<html>", "<body>", "<h1>", "<p>", "<ul>", "<li>"]
        self.closing = ["</html>", "</body>", "</h1>", "</p>", "</ul>", "</li>"]

    def match_checker(self, tags):
        stack = []
        for tag in tags:
            if tag in self.opening:
                stack.append(tag)
            elif tag in self.closing:
                if len(stack) == 0:
                    return False
                if self.opening.index(stack.pop()) != self.closing.index(tag):
                    return False
        return len(stack) == 0

    def extract_tags(self, text):
        tags = []
        start = text.find("<")
        while start != -1:
            end = text.find(">", start + 1)
            if end == -1:
                break
            tag = text[start:end + 1]
            tags.append(tag)
            start = text.find("<", end + 1)
        return tags

if __name__ == "__main__":
    matcher = HTMLTagMatcher()
    text = input("Enter a HTML string: ")
    tags = matcher.extract_tags(text)
    if matcher.match_checker(tags):
        print("True")
    else:
        print("False")
    for tag in tags:
        print(tag, end=" ")