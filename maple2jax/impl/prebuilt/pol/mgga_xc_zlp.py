t1 = 3 ** (0.1e1 / 0.3e1)
t3 = (0.1e1 / math.pi) ** (0.1e1 / 0.3e1)
t4 = t1 * t3
t5 = 4 ** (0.1e1 / 0.3e1)
t6 = t5 ** 2
t11 = r0 + r1
t12 = t11 ** 2
t13 = t11 ** (0.1e1 / 0.3e1)
t14 = t13 ** 2
t18 = r0 ** (0.1e1 / 0.3e1)
t19 = t18 ** 2
t25 = (r0 - r1) / t11
t27 = 0.1e1 / 0.2e1 + t25 / 0.2e1
t28 = t27 ** (0.1e1 / 0.3e1)
t29 = t28 ** 2
t32 = r1 ** (0.1e1 / 0.3e1)
t33 = t32 ** 2
t38 = 0.1e1 / 0.2e1 - t25 / 0.2e1
t39 = t38 ** (0.1e1 / 0.3e1)
t40 = t39 ** 2
t52 = math.log(0.1e1 + 0.48849425066691677572e3 / t13)
t57 = t1 ** 2
res = -(0.20710800000000000000e0 * t4 * t6 + 0.53877250000000000000e-2 * t4 * t6 * ((s0 + 0.2e1 * s1 + s2) / t14 / t12 / 0.8e1 - l0 / t19 / r0 * t29 * t27 / 0.8e1 - l1 / t33 / r1 * t40 * t38 / 0.8e1)) * (0.1e1 - 0.20471070000000000000e-2 * t52 * t13) * t57 / t3 * t5 * t13 / 0.3e1
