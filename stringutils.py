import xerox
import sys
def main(argv):
    s=xerox.paste()   
    print(s)
    s = s.splitlines()
    s = ''.join(s)
    print(s)
    xerox.copy(s)
    return s    

    
if __name__ == "__main__":
   main(sys.argv[1:])
