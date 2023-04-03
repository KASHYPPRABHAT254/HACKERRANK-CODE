# Enter your code here. Read input from STDIN. Print output to STDOUT
from html.parser import HTMLParser
# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        for ele in attrs:
            print('->',ele[0],'>',ele[1])
    # def handle_endtag(self, tag):
    #     print("End   :", tag)
    def handle_startendtag(self, tag, attrs):
        print(tag)
        for ele in attrs:
            print('->',ele[0],'>',ele[1])
    # def handle_comment(self, data):
    #     lst = data.split("\n")
    #     if(len(lst)==1):
    #         print(">>> Single-line Comment")
    #         print(lst[0])
    #     else:
    #         print(">>> Multi-line Comment")
    #         print(*lst,sep='\n')
            
    # def handle_data(self, data):
    #     if(data!="\n"):
    #         print(">>> Data")
    #         print(data)
    
# instantiate the parser and fed it some HTML
html_doc = ''
n = int(input())
for i in range(n):
    html_doc += input().rstrip() + '\n'

parser = MyHTMLParser()
parser.feed(html_doc)





