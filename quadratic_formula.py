def solve_quadratic(a,b,c):
    discriminant = b**2 - 4*ac
    root1 = (-b + discriminant) / 2*a
    root2 = (-b - discriminant) / 2*a
    result = (root1, root2)
    if discriminant > 0:
        return result
    elif discriminant == 0:
        return root1
    else:
        return None
