class DoppelDict(dict):
    def __setitem__(self,key,value):
        super().__setitem__(key,[value]*2) #覆盖了超类（list）的setitem方法


if __name__ == "__main__":
    dd = DoppelDict(one='1')
    #上面使用的是dict的init方法，该方法替换覆盖了Doppler的setitem方法，所以是正常显示
    print(dd) # >>> {'one':1}

    dd['two'] = 2
    print(dd) #这里使用了自己覆盖的setitem方法，所以2的值加倍了

    dd.update(three=3)
    print(dd) # 同样update没有使用setitem


