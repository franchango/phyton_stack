class MathDojo:
    def __init__(self):
    	self.result = 0
    def add(self, num, *nums):
        result = num
        for num in nums:
            result = result + num
        return result

    def subtract(self, num, *nums):
        result = num
        for num in nums:
            result = result - num
        return result
md = MathDojo()
x =md.add(15,10)
print(x)
x =md.add(70,4,2)
print(x)
x =md.add(10,60)
print(x)

x =md.subtract(20,10)
print(x)
x =md.add(12,13)
print(x)
x =md.add(15,16)
print(x)
