def find_min_number(x):

    digits = list(x)
    
    digits.sort()
    
    # 先頭に0が来ないようにするため、最初に0以外の数字を見つける
    if digits[0] == '0':
        for i in range(1, len(digits)):
            if digits[i] != '0':
                # 最初に0以外の数字を先頭に持ってくる
                digits[0], digits[i] = digits[i], '0'
                break

    min_value = ''.join(digits)
    return min_value

if __name__ == "__main__":
    x = input().strip()
    print(find_min_number(x))
