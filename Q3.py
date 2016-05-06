from Stack import Stack

def htmlChecker(htmlString):
    s = Stack()
    balanced = True
    index = 0
    opens = ['<html>', '<title>', '<body>', '<head>', '<h1>']  # html open tags
    closers = ['</html>', '</title>', '</body>', '</head>', '</h1>']  # html close tags
    while index < len(htmlString) and balanced:
        html = htmlString[index]
        if html in opens:
            s.push(html)
        elif html in closers:
            if s.isEmpty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top,html):
                       balanced = False
        index = index + 1
    if balanced and s.isEmpty():
        return True
    else:
        return False

def matches(open,close):
    opens = ['<html>', '<title>', '<body>', '<head>', '<h1>']
    closers = ['</html>', '</title>', '</body>', '</head>', '</h1>']
    return opens.index(open) == closers.index(close)

htmlCheck = ['<html>','<head>','<title>','</title>','</head>','<body>','<h1>','</h1>','</body>','</html>']
htmlChecktest = ['<html>','<head>','<title>','</title>','</head>','<body>','<h1>','</h1>','</body>']
htmlChecktest1 = ['<html>', '<head>', '</head>', '<body>']
print (htmlChecker(htmlCheck))
print (htmlChecker(htmlChecktest))
print (htmlChecker(htmlChecktest1))
