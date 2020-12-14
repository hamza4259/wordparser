import time
from callinganotherfunction import perform_computation

start_time = time.time()


#filename = input()#'C:/Users/hamza/OneDrive/Desktop/wordcount.docx'




#file_stopwords = input() #'C:/Users/hamza/OneDrive/Desktop/stopwords.txt'



#outputfile = input() #'itworked4.csv'


if __name__ == "__main__":
    print('Which file do you want to perform the wordscraping for?')
    print('It should look like C:/Users/hamza/OneDrive/Desktop/wordcount.docx')
    filename = input()
    print('Which file do you want the stopwords for?')
    print('It should look like C:/Users/hamza/OneDrive/Desktop/stopwords.txt')
    file_stopwords = input()
    print(file_stopwords)
    print('Which output file do you want?')
    print('It can be anyname.csv')
    outputfile = input()
    perform_computation(filename, file_stopwords, outputfile)


