def prod_floats(x0: float, x1: float, x2: float) -> float:
    x1 *= x0
    x2 *= x1
    return x2


def prod_list(xs: list[float]) -> float:
    i: int = 1
    while i < len(xs):
        xs[i] = xs[i] * xs[i - 1]
        i += 1
    return xs[len(xs) - 1]


nums: list[float] = [4.0, 3.0, 2.0]
prod: int = 0

prod = prod_floats(nums[0], nums[1], nums[2])
print(prod)

prod = prod_list(nums)
print(prod)

prod = prod_list(nums)
print(prod)
prod = prod_list(nums)
print(prod)