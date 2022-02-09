class ComplexNumbers:
    def __init__(self,real,imag):
        self.real = real
        self.imag = imag
        
    def plus(self,cn):
        self.real += cn.real
        self.imag += cn.imag
        
    def multiply(self,cn):
        a = self.real*cn.real
        b = self.real*cn.imag
        c = self.imag.cn.real
        d = self.imag*cn.imag
        self.real = a - d
        self.imag = b + c
        self.imag*=cn.imag
        
    def print_c(self):
        print(f"{self.real} + i{self.imag}")
        
    
#Driver's code goes here.
    

    
    
    
    
    
    
    
    
    
    
