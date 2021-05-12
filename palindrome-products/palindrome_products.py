def smallest(max_factor, min_factor):
    return palindrome(min_factor, max_factor)


def largest(max_factor, min_factor):
    return palindrome(min_factor, max_factor, smallest=False)


def palindrome(mn, mx, smallest=True):
    if mn > mx:
        raise ValueError(' ')

    palin = None
    palin_factors = []
    args = (mn**2, mx**2+1) if smallest else (mx**2, mn**2-1, -1)

    for r in range(*args):
        s = str(r)
        if s == s[::-1]:
            if any(mn <= r//j <= mx for j in range(mn, mx+1) if r % j == 0):
                palin = r
                break

    if palin: 
        for i in range(mn, mx+1):
            if palin % i == 0:
                factors = i, palin//i
                if mn <= factors[0] <= mx and mn <= factors[1] <= mx:
                    palin_factors.append(factors)
        
    return palin, palin_factors

