t1 = math.sqrt(math.pi)
t2 = math.sqrt(r0)
t3 = t1 * t2
t6 = 0.39274e1 * t2 + t1 / 0.2e1
t8 = t2 / t6
t10 = 0.39274e1 * t8 - 0.1e1
t11 = 0.2e1 + params_a_c
t12 = math.sqrt(t11)
t21 = t6 ** 2
t23 = t11 ** (-0.15e1)
t27 = 0.1e1 + params_a_c
t28 = math.sqrt(t27)
res = 0.32416023070084253575e-1 * (0.19637000000000000000e1 * t3 * t10 / t12 + 0.39274e1 * t8 * t10 / t11 + 0.98185000000000000000e0 * t3 / t21 * t23 + 0.39274e1 * t3 * t10 / t28 + 0.39274e1 * t8 / t27) * math.pi
