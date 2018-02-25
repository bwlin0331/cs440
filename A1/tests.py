from mg2 import *

def main():
    #running aStar tests on all 50 testcases
    for i in range(50):
        #normal
        test(str(i+1))
        #highg
        test(str(i+1), "highg")
        #lowg
        test(str(i+1), "lowg")
        #back
        test(str(i+1), "back")
        #adaptive
        test(str(i+1), "adaptive")

def combine():
    return


if __name__ == "__main__":
    main()
