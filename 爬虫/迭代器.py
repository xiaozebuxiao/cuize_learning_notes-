class Iterator(object):

    def __init__(self):
        self.var = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.var += 1
        if self.var == 3:
            raise StopIteration()
        return self.var


# 创建实例，并且打印结果
iterator = Iterator()
for it in iterator:
    print(it)
