from hashlib import md5

input = 'cxdnnyjw'
code = ['' for _ in range(8)]
chars = 0
count = 0

while chars < 8:
    h = md5()
    h.update(bytes(f'{input}{count}', encoding='ascii'))
    digest = h.hexdigest()
    if digest.startswith('00000'):
        if digest[5].isdigit() and int(digest[5]) < 8 and code[int(digest[5])] == '':
            code[int(digest[5])] = digest[6]
            chars += 1

    count += 1

print(''.join(code))

