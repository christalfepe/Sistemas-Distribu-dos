from emissor import process
from receptor import process_pi

def main():
        i=0
        numproc = 3
        
        if i <= numproc:
                r = process(numproc)
                e = process_pi()

if __name__ == '__main__':
    main()