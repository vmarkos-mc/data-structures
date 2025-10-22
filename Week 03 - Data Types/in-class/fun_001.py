# in-class/fun_001.py

x = 1.0 # 1 is an integer, 1.0 is a float
i = 0
while x > 0.0:
    if x / 2 == 0.0:
        print(x)
    x = x / 2
    i = i + 1
print(i)