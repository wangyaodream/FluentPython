from collections import namedtuple

Result = namedtuple('Result','count average')

#子生成器

def averager():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield
        if term is None:
            break
        total += term
        count += 1
        average = total/count
    return Result(count,average)


#委派生成器

def grouper(results,key):
    while True:
        results[key] = yield from averager()

#client code

def main(data):
    results = {}
    for key,values in data.items():
        group = grouper(results,key)
        next(group) #预激活
        for value in values:
            group.send(value)
        group.send(None)
    report(results)

#报告函数

def report(results):
    for key,result in sorted(results.items()):
        group,unit = key.split(';')
        print('{:2}{:3} averaging {:.2f}{}'.format(result.count,group,result.average,unit))


#构造数据
data = {
    'girls;kg':
        [41.6, 46.5, 41.3, 50.0, 38.8, 46.6, 46.7, 47.2, 38.6, 44.6],
    'girls;m':
        [1.47, 1.43, 1.59, 1.47, 1.36, 1.5, 1.48, 1.57, 1.54, 1.37],
    'boys;kg':
        [41.3, 48.1, 52.9, 51.8, 44.1, 51.7, 51.8, 50.2, 45.9, 40.9],
    'boys;m':
        [1.65, 1.53, 1.67, 1.68, 1.63, 1.53, 1.61, 1.63, 1.66, 1.58]
}


if __name__ == '__main__':
    main(data)