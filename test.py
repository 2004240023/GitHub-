from ast import If


def main():
    print('Hello Python')

if __name__=='__main__':
    main()

def a(b):
    return  b

num = int(input('整数を入力してね＞'))
if num % 2 == 0:
     print('偶数')
else:
     print('奇数')

for num in range(1, 10):
    print(num)