import os

for book_dir in os.listdir('./books/'):
    print "##############################################################################################"
    print book_dir
    os.system("python main.py " + book_dir)
    print "##############################################################################################"
