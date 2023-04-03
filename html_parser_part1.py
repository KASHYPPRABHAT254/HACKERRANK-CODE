from html.parser import HTMLParser
# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start :", tag)
        for ele in attrs:
            print('->',ele[0],'>',ele[1])
        # if(tag == '{}'.format(tag_name)):
        #     for attr, value in attrs:
        #         if(attr == Attribute1 and value == Attribute_value1):
        #             if(all(attr == Attribute2[i] and value == Attribute_value2[i])for i in range(len(Attribute2))):
        #                 print(tag)
    def handle_endtag(self, tag):
        print("End   :", tag)
    def handle_startendtag(self, tag, attrs):
        print("Empty :", tag)
        for ele in attrs:
            print('->',ele[0],'>',ele[1])
    
# instantiate the parser and fed it some HTML
html_doc = ''
n = int(input())
for i in range(n):
    html_doc += input().rstrip() + '\n'

parser = MyHTMLParser()
parser.feed(html_doc)





