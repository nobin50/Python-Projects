
from urllib.request import urlopen

def read_text():

    file_quote = open(r"C:\Users\MD. Nobin\Downloads\movie_quotes.txt")
    file_content = file_quote.read()
    print(file_content)
    file_content = file_content.replace(" ", "")
    file_content = file_content.replace("\n", "")
    file_quote.close()
    check_curse(file_content)

def check_curse(text_check):
    with urlopen("http://www.wdylike.appspot.com/?q="+ text_check) as fc:
        output = fc.read().decode('utf-8')
        print('\n\n')
        print('Here goes the result:.....')
        if output:
            if "true" in output:
                print('The text file contains profane or curse words.')
            else:
                print('The text file does not contain any profanity.')


read_text()
