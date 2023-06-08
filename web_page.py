'''a simple program to create an html file from a given
string, and call the default web browser to display
the file.'''
contents = '''<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transistional//EN">
<html>
<head>
    <meta content="text/html; charset=ISO-8859-1"
   http-equiv="content-type">
    <title>Hello </title>
</head>
<body>
hello, world!
</body>
</html>
'''

def main():
    browseLocal(contents, 'helloPython.html')


def strToFile(text, filename):
    '''write a file with the given name and the given text'''
    output = open(filename, "w")
    output.write(text)
    output.close()

def browseLocal(webpageText, filename):
    """start your webbrowser on a local file containing the text"""
    strToFile(webpageText, filename)
    import webbrowser
    webbrowser.open(filename)

main()