import Local
import Remote

class Juice(object):
    
    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2
        self.main()
        
    def main(self):
        methodname = self.arg2
        if(self.arg1 == 0):# 0 represents local query
            print("Querying Local Machine for: ", methodname)
            result = getattr(Local.Local, methodname)#method to be called
            result()
        if(self.arg1 == 1 ):
            result = getattr(Remote.Remote, methodname)
            result()
        
