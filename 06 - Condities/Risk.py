# invoer
a = float(input('aantal ogen dobbelsteen: '))
b = float(input('aantal ogen dobbelsteen: '))
c = float(input('aantal ogen dobbelsteen: '))

d = float(input('aantal ogen dobbelsteen: '))
e = float(input('aantal ogen dobbelsteen: '))

if a >= b and a >= c:
    if a > d and a > e:
        if (b > d and b > e) or (c > d and c > e):
            uitkomst = 'aanvaller verliest 0 legers, verdediger verliest 2 legers'
        if (b < d and b < e) or (c < d and c < e):
            uitkomst = 'aanvaller verliest 1 leger, verdediger verliest 1 leger'
        if (b == d or b == e) or (c == d or c == e):
            uitkomst = 'aanvaller verliest 1 leger, verdediger verliest 1 leger'

    if a < d and a < e:
        uitkomst = 'aanvaller verliest 2 legers, verdediger verliest 0 leger'
    if a == d:
        if b > e or c > e:
            uitkomst = 'aanvaller verliest 1 leger, verdediger verliest 1 leger'
        if b <= e or c <= e:
            uitkomst = 'aanvaller verliest 2 legers, verdediger verliest 0 leger'
    if a == e:
        if b > d or c > d:
            uitkomst= 'aanvaller verliest 1 leger, verdediger verliest 1 leger'
        if b <= d or c <= d:
            uitkomst = 'aanvaller verliest 2 legers, verdediger verliest 0 leger'

if b >= a and b >= c:
    if b > d and b > e:
        if (a > d and a > e) or (c > d and c > e):
            uitkomst = 'aanvaller verliest 0 legers, verdediger verliest 2 legers'
        if (a < d and a < e) or (c < d and c < e):
            uitkomst = 'aanvaller verliest 1 leger, verdediger verliest 1 leger'
        if (a == d or a == e) or (c == d or c == e):
                uitkomst = 'aanvaller verliest 1 leger, verdediger verliest 1 leger'
    if b < d and b < e:
        uitkomst = 'aanvaller verliest 2 legers, verdediger verliest 0 leger'
    if b == d:
        if a > e or c > e:
            uitkomst = 'aanvaller verliest 1 leger, verdediger verliest 1 leger'
        if a <= e or c <= e:
            uitkomst = 'aanvaller verliest 2 legers, verdediger verliest 0 leger'
    if b == e:
        if a > d or c > d:
            uitkomst = 'aanvaller verliest 1 leger, verdediger verliest 1 leger'
        if a <= d or c <= d:
            uitkomst = 'aanvaller verliest 2 legers, verdediger verliest 0 leger'

if c >= a and c >= b:
    if c > d and c > e:
        if (a > d and a > e) or (b > d and b > e):
            uitkomst = 'aanvaller verliest 0 legers, verdediger verliest 2 legers'
        if (a < d and a < e) or (b < d and b < e):
            uitkomst = 'aanvaller verliest 1 leger, verdediger verliest 1 leger'
        if (a == d or a == e) or (b == d or b == e):
            uitkomst = 'aanvaller verliest 1 leger, verdediger verliest 1 leger'
    if c < d and c < e:
        uitkomst = 'aanvaller verliest 2 legers, verdediger verliest 0 leger'
    if c == d:
        if a > e or b > e:
            uitkomst = 'aanvaller verliest 1 leger, verdediger verliest 1 leger'
        if a <= e or b <= e:
            uitkomst = 'aanvaller verliest 2 legers, verdediger verliest 0 leger'
    if c == e:
        if a > d or b > d:
            uitkomst = 'aanvaller verliest 1 leger, verdediger verliest 1 leger'
        if a <= d or b <= d:
            uitkomst = 'aanvaller verliest 2 legers, verdediger verliest 0 leger'

# uitvoer
print(uitkomst)