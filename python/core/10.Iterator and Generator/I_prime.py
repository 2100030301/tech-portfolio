class prime:
    def __init__(self,n):
        self.c=0
        self.n=n
    def __iter__(self):
        return self
    def __next__(self):
        i=2
        while self.c<self.n:
            if prime.is_prime(i):
                self.c+=1
                print(i)
            i+=1
        else:
            raise StopIteration
    @staticmethod
    def is_prime(n):
        if n==0 or n==1:
            return False
        for i in range(2,n):
            if n % i == 0 :
                return False
        return True
p1 = prime(25)
for i in p1:
    print(i)