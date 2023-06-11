'''improvements and new lines of code are commented "#new" '''
pageTemplate = '''
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<head>
  <meta content="text/html; charset=ISO-8859-1"
 http-equiv="content-type">
</head>
<body>
hello, {person}!
</body>
</html>''' #NEW note '{person}' two lines up

def main():
    person = input('enter your name: ') #new
    contents = pageTemplate.format(**locals())
    browseLocal(contents, 'helloPython2.html') #new filename

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