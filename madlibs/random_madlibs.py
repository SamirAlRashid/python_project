from sample_madlibs import hp, code, zombie, hungergames
import random

if __name__ == "__main__":
    m = random.choice([hp, code, zombie, hungergames])
    m.madlib()
    #if __name__=="__main__" allows you to specify some code that:
    #Only executes when the file is run as script
    #Doesn't execute when the file is imported as a module
    