class SparklingWater:
    def __init__(self, color, taste, mixin=set()):
        self.color = color
        self.taste = taste
        self.mixin = mixin

    def add_mixin(self, addition):
        self.mixin.add(addition)
        return self.mixin
    
    def check_mixin(self, addition):
        return addition in self.mixin
