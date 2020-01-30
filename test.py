def chocolateFeast(n, c, m):
    wrappers = 0
    total = 0
    # spend money first
    wrappers = n // c
    total += wrappers
    # trade wrappers until he can't anymore
    while wrappers >= m:
        current_tradein = wrappers // m
        wrappers -= current_tradein * m
        wrappers += current_tradein
        total += current_tradein
    return total

print(chocolateFeast(10, 2, 5))
print(chocolateFeast(12, 4, 4))
