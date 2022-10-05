import sys

cat = 1

while(cat < len(sys.argv)):
    file = open(sys.argv[cat] , "r")
    sys.stdout.write(file.read())
    file.close ()
    cat += 1
