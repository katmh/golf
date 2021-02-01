i="Fizz"
u="Buzz"
for n in range(1,101):f,b=(n%3==0,n%5==0);print(i+u if f&b else i if f else u if b else n)
