x=int(input("Enter the divident:"))
y=int(input("Enter the divisor:"))

q = 0
while x >= y:
  x -= y
  q += 1

print(f'Product: {q} & remainder {x}')