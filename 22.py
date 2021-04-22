def gen(pair):
    n = pair * 2
    dict = {'0':1}
    length = 1
    while length < n:
        dict , length , n = update(dict, length, n)
    ans = []
    for elem in dict:
        string = ''
        for item in elem:
            if item == '0':
                string += '('
            else:
                string += ')'
        ans.append(string)
    print(ans)

def update(dict, length, n):
    newdict = {}
    for elem in dict:
        diff = dict[elem]
        if elem.count('0') == n // 2:
            newdict[elem + '1'] = diff - 1
        elif diff > 0 and diff < n // 2:
            newdict[elem + '0'] = diff + 1
            newdict[elem + '1'] = diff - 1
        elif diff >= n // 2:
            newdict[elem + '1'] = diff - 1
        else:
            newdict[elem + '0'] = diff + 1

    return newdict, length+1, n

gen(1)
gen(2)
gen(3)
