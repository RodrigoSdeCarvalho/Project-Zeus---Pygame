class Difficulty(object):
    mode = 1
    
    @classmethod
    def increase(cls):
        cls.mode += 1
    
    @classmethod
    def reset(cls):
        cls.mode = 1