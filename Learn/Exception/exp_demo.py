def fetcher(obj,index):
    return obj[index]
msg = 'god'
def after():
    try:
        fetcher(msg,10)
    except Exception:
        print(Exception.__name__)
    else:
        print('Hello result')


if __name__=='__main__':
    after()