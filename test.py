#import string
name = 'dgiush23479823'
name = 'sdg98953dfgh'
def if_name_correct(name) -> bool:
    for i in range(len(name)-1):
        if not 'A' <= name[i] <= 'z':
            if '0' <= name[i] <= '9':
                for j in range(i, len(name)-1):
                    if not '0' <= name[j] <= '9':
                        raise ValueError('Error')
                return 1
    raise ValueError('Error')


a = 'AUjzo346'
b = '897uyg39dfjs'

print(if_name_correct(a))
print(if_name_correct(b))
