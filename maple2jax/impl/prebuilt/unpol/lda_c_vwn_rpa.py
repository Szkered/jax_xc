t1 = 3 ** (0.1e1 / 0.3e1)
t3 = (0.1e1 / math.pi) ** (0.1e1 / 0.3e1)
t4 = t1 * t3
t5 = 4 ** (0.1e1 / 0.3e1)
t6 = t5 ** 2
t7 = r0 ** (0.1e1 / 0.3e1)
t9 = t6 / t7
t10 = t4 * t9
t11 = t10 / 0.4e1
t12 = math.sqrt(t10)
t15 = 0.1e1 / (t11 + 0.65360000000000000000e1 * t12 + 0.427198e2)
t19 = math.log(t4 * t9 * t15 / 0.4e1)
t24 = math.atan(0.44899888641287296627e-1 / (t12 + 0.130720e2))
t26 = t12 / 0.2e1
t28 = (t26 + 0.409286e0) ** 2
t30 = math.log(t28 * t15)
t34 = p_a_zeta_threshold ** (0.1e1 / 0.3e1)
t36 = jnp.where(0.1e1 <= p_a_zeta_threshold, t34 * p_a_zeta_threshold, 1)
t38 = 0.2e1 * t36 - 0.2e1
t39 = 2 ** (0.1e1 / 0.3e1)
t42 = 0.1e1 / (0.2e1 * t39 - 0.2e1)
t48 = 0.1e1 / (t11 + 0.10061550000000000000e2 * t12 + 0.101578e3)
t52 = math.log(t4 * t9 * t48 / 0.4e1)
t57 = math.atan(0.11716852777089929792e1 / (t12 + 0.201231e2))
t60 = (t26 + 0.743294e0) ** 2
t62 = math.log(t60 * t48)
res = (0.310907e-1 * t19 + 0.20521972937837502661e2 * t24 + 0.44313737677495382697e-2 * t30) * (-t38 * t42 + 0.1e1) + (0.1554535e-1 * t52 + 0.61881802979060631482e0 * t57 + 0.26673100072733151594e-2 * t62) * t38 * t42
