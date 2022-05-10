# rumus
# zi = (a * zi - 1)

a = 7
m = 13
z0 = 5

z1 = (a * z0) % m

for i in range(1,6):
    z1 = (a * z1) % m
    ui = z1 / m

    print(f"{z1} \t\t {ui}")