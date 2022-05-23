class gen_N:
    def __init__(self, N):
        self.n = N

    def __iter__(self):
        return gen_N_iterator(self.n)

class gen_N_iterator:
    def __init__(self, K):
        self.k = K
        self.c = -1

    def __next__(self):
        if self.c < self.k:
            self.c += 1
            return self.c
        else:
            raise StopIteration


k = gen_N(10)
print([i for i in k])