t1 = 2 ** (0.1e1 / 0.12e2)
t2 = t1 ** 2
t3 = t2 * t1
t4 = t2 ** 2
t5 = t4 ** 2
t7 = r0 ** (0.1e1 / 0.12e2)
t11 = 2 ** (0.1e1 / 0.6e1)
t12 = t11 ** 2
t13 = t12 ** 2
t15 = r0 ** (0.1e1 / 0.6e1)
t19 = 2 ** (0.1e1 / 0.3e1)
t20 = t19 ** 2
t21 = r0 ** (0.1e1 / 0.3e1)
t25 = math.sqrt(0.2e1)
t26 = math.sqrt(r0)
t30 = t21 ** 2
t32 = t19 * t30 * r0
t36 = math.sqrt(s0)
t38 = p_a_zeta_threshold ** (0.1e1 / 0.3e1)
t40 = jnp.where(0.1e1 <= p_a_zeta_threshold, t38 * p_a_zeta_threshold, 1)
t41 = t36 * t40
t53 = 0.1e1 / r0
t55 = t40 ** 2
t56 = s0 * t55
t59 = t15 ** 2
t60 = t59 ** 2
t61 = t60 * t15
t70 = r0 ** 2
t73 = s0 / t30 / t70
t75 = t73 * t55 - t73
t84 = 0.33941550000000000000e0 * t5 * t3 * t7 * r0 - 0.87910500000000000000e0 * t13 * t11 * t15 * r0 + 0.63838000000000000000e0 * t20 * t21 * r0 - 0.80394500000000000000e0 * t25 * t26 * r0 + 0.18280500000000000000e0 * t32 - 0.45331750000000000000e-1 * t4 * t3 * t7 * t41 + 0.36743250000000000000e-1 * t25 * t15 * t41 + 0.36785250000000000000e-1 * t19 * t21 * t41 - 0.17922925000000000000e-1 * t11 * t26 * t41 - 0.50895875000000000000e-2 * t19 * t53 * t56 + 0.26828125000000000000e-2 * t11 / t61 * t56 - 0.96019500000000000000e-4 / t30 * s0 * t55 + 0.15518850000000000000e-1 * t32 * t75 - 0.36016300000000000000e-1 * t11 * t61 * r0 * t75 + 0.22328100000000000000e-1 * t70 * t75
res = t84 * t53
