import xerox
import sys
def main(argv):
    s=xerox.paste()   
    s = s.splitlines()
    s = ''.join(s)
    xerox.copy(s)
    return s    

    
if __name__ == "__main__":
   main(sys.argv[1:])
