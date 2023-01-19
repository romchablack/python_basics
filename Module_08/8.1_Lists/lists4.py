N = 5
gas_cost = []

for i in range(N):
    gas_arrears = float(input("Введіть заборгованість: "))
    gas_cost.append(round(gas_arrears, 2))

print(gas_cost)
