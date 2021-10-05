f = open('text.txt', 'w', encoding='utf-8')

f.write('hello')
f.write('\n')
f.write('월드')

f.close()

print('with')
with open('text.txt', 'w', encoding='utf-8') as f:  #들여쓰기가 끝나는(with가 끝나는) 동시에 close가 자동으로 된다.
    f.write('hello')
    f.write('\n')
    f.write('월드')