t3 = r0 + r1
t4 = t3 ** 2
t5 = t4 ** 2
t6 = t3 ** (0.1e1 / 0.3e1)
t7 = t6 ** 2
t11 = r0 ** (0.1e1 / 0.3e1)
t12 = t11 ** 2
t16 = r0 - r1
t18 = t16 / t3
t19 = 0.1e1 + t18
t20 = t19 / 0.2e1
t21 = t20 ** (0.1e1 / 0.3e1)
t22 = t21 ** 2
t25 = r1 ** (0.1e1 / 0.3e1)
t26 = t25 ** 2
t30 = 0.1e1 - t18
t31 = t30 / 0.2e1
t32 = t31 ** (0.1e1 / 0.3e1)
t33 = t32 ** 2
t38 = t16 ** 2
t43 = 3 ** (0.1e1 / 0.3e1)
t45 = (0.1e1 / math.pi) ** (0.1e1 / 0.3e1)
t47 = 4 ** (0.1e1 / 0.3e1)
t48 = t47 ** 2
t51 = t43 * t45 * t48 / t6
t54 = math.sqrt(t51)
t57 = t51 ** 0.15e1
t59 = t43 ** 2
t60 = t45 ** 2
t64 = t59 * t60 * t47 / t7
t70 = math.log(0.1e1 + 0.16081979498692535067e2 / (0.37978500000000000000e1 * t54 + 0.89690000000000000000e0 * t51 + 0.20477500000000000000e0 * t57 + 0.12323500000000000000e0 * t64))
t72 = 0.621814e-1 * (0.1e1 + 0.53425000000000000000e-1 * t51) * t70
t73 = t38 ** 2
t77 = p_a_zeta_threshold ** (0.1e1 / 0.3e1)
t78 = t77 * p_a_zeta_threshold
t79 = t19 ** (0.1e1 / 0.3e1)
t81 = jnp.where(t19 <= p_a_zeta_threshold, t78, t79 * t19)
t83 = t30 ** (0.1e1 / 0.3e1)
t85 = jnp.where(t30 <= p_a_zeta_threshold, t78, t83 * t30)
t87 = 2 ** (0.1e1 / 0.3e1)
t91 = (t81 + t85 - 0.2e1) / (0.2e1 * t87 - 0.2e1)
t102 = math.log(0.1e1 + 0.32163958997385070134e2 / (0.70594500000000000000e1 * t54 + 0.15494250000000000000e1 * t51 + 0.42077500000000000000e0 * t57 + 0.15629250000000000000e0 * t64))
t115 = math.log(0.1e1 + 0.29608749977793437516e2 / (0.51785000000000000000e1 * t54 + 0.90577500000000000000e0 * t51 + 0.11003250000000000000e0 * t57 + 0.12417750000000000000e0 * t64))
t116 = (0.1e1 + 0.27812500000000000000e-1 * t51) * t115
res = (0.1e1 - (s0 + 0.2e1 * s1 + s2) / t7 / t5 / (tau0 / t12 / r0 * t22 * t20 + tau1 / t26 / r1 * t33 * t31) * t38 / 0.8e1) * (-t72 + t73 / t5 * t91 * (-0.3109070e-1 * (0.1e1 + 0.51370000000000000000e-1 * t51) * t102 + t72 - 0.19751673498613801407e-1 * t116) + 0.19751673498613801407e-1 * t91 * t116)
