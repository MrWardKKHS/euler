from sympy import primefactors

def phi_over_n(n):
    count = 0
    pf_n = primefactors(n)
    for i in range(1, n):
        pf_i = primefactors(i)
        if any([n in pf_n for n in pf_i]):
            continue
        count += 1
    return n / count

highscore = 0

for i in range(210, 10**6 + 1, 10):
    if (p_o_n := phi_over_n(i)) > highscore:
        highscore = p_o_n
        print(i, p_o_n)
    
