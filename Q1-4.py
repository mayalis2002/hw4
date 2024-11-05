# START Q1.1

pizza_slices: int = int(input('enter pizza slices:'))
friends: int = pizza_slices // 4
print(f'youve got: {friends} slices ;)')
if pizza_slices % 4 != 0:
    print(f'lefovers in the fridge:{pizza_slices % 4}')

# END Q1.1


# START Q1.2
friend: int = int(input('how many friends?'))
pizza_slices: int = int(input('how many pizza slices:'))
friend_s: int = pizza_slices // friend
print(f'youve got: {friend_s} slices ;)')
if pizza_slices % 4 != 0:
    print(f'lefovers in the fridge:{pizza_slices % friend}')

# END Q1.2

# START Q2.1

a = 1
b = 1
if a == b:
    print(f"was True for {a} {b}")
else:
    print(f"was False for {a} {b}")

a = 1
b = 1
c = 1
d = 1
if a + b and c + d:
    print(f"was True for {a} {b} {c} {d}")
else:
    print(f"was False for {a} {b} {c} {d}")

a = 0
b = 0
c = 1
d = 0
if a >= b or c > d:
    print(f"was True for {a} {b} {c} {d}")
else:
    print(f"was False for {a} {b} {c} {d}")

a = 0
b = 0
c = 0
d = 1
if a >= b or c < d:
    print(f"was True for {a} {b} {c} {d}")
else:
    print(f"was False for {a} {b} {c} {d}")

a = 0
b = 0
c = 0
d = 0
if a == b and c <= d:
    print(f"was True for {a} {b} {c} {d}")
else:
    print(f"was False for {a} {b} {c} {d}")

a = 1
b = 1
c = 1
d = 1
if True and a + b + c + d:
    print(f"was True for {a} {b} {c} {d}")
else:
    print(f"was False for {a} {b} {c} {d}")

a = 0
b = 1
if a != b:
    print(f"was True for {a} {b}")
else:
    print(f"was False for {a} {b}")

a = 1
b = 2
c = 3
if a != b and a <= c or a <= b or True:
    print(f"was True for {a} {b} {c}")
else:
    print(f"was False for {a} {b} {c}")

a = 1
b = 3
c = 2
if a != b and a <= c or a <= b or False:
    print(f"was True for {a} {b} {c}")
else:
    print(f"was False for {a} {b} {c}")

a = 1
b = 0
c = 1
d = 1
if a % b == 0 and c % d == 1:
    print(f"was True for {a} {b} {c} {d}")
else:
    print(f"was False for {a} {b} {c} {d}")

# END Q2.1

#START Q2.2

# MAKE ALL OF THIS CONDITION FALSE

a = 1
b = 0
if a == b:
    print(f"was True for {a} {b}")
else:
    print(f"was False for {a} {b}")

a = 0
b = 0
c = 0
d = 0
if a + b and c + d:
    print(f"was True for {a} {b} {c} {d}")
else:
    print(f"was False for {a} {b} {c} {d}")

a = 4
b = 3
c = 2
d = 1
if a >= b or c > d:
    print(f"was True for {a} {b} {c} {d}")
else:
    print(f"was False for {a} {b} {c} {d}")

a = 1
b = 2
c = 4
d = 3
if a >= b or c < d:
    print(f"was True for {a} {b} {c} {d}")
else:
    print(f"was False for {a} {b} {c} {d}")

a = 1
b = 2
c = 4
d = 3
if a == b and c <= d:
    print(f"was True for {a} {b} {c} {d}")
else:
    print(f"was False for {a} {b} {c} {d}")

a = 0
b = 0
c = 0
d = 0
if True and a + b + c + d:
    print(f"was True for {a} {b} {c} {d}")
else:
    print(f"was False for {a} {b} {c} {d}")

a = 1
b = 1
if a != b:
    print(f"was True for {a} {b}")
else:
    print(f"was False for {a} {b}")

a = 1
b = 1.5
c = 0.5
if a != b and a <= c or a <= b or True:
    print(f"was True for {a} {b} {c}")
else:
    print(f"was False for {a} {b} {c}") #not possible because condisions: a!=b or a<=b or true

a = 2
b = 1
c = 1
if a != b and a <= c or a <= b or False:
    print(f"was True for {a} {b} {c}")
else:
    print(f"was False for {a} {b} {c}")

a = 1
b = 1
c = 2
d = 3
if a % b == 0 and c % d == 1:
    print(f"was True for {a} {b} {c} {d}")
else:
    print(f"was False for {a} {b} {c} {d}")
#END Q2.2

# START Q4.1
x: int = 10
while 10 <= x <= 20:
    print(x)
    x += 1
#end Q4.1

# Q4.2
x: int = 10
while 10 <= x <= 20 :
    print(x)
    x += 2
# END4.2

# START Q4.3
x = 10
y: int = int(input('gap:'))
while 10 <= x <= 20:
    print(x)
    x += y
#END 4.3