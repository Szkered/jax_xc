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
t15 = 0.1e1 / (t11 + 0.18637200000000000000e1 * t12 + 0.129352e2)
t19 = math.log(t4 * t9 * t15 / 0.4e1)
t20 = 0.310907e-1 * t19
t24 = math.atan(0.61519908197590802322e1 / (t12 + 0.372744e1))
t25 = 0.38783294878113014393e-1 * t24
t26 = t12 / 0.2e1
t28 = (t26 + 0.10498e0) ** 2
t30 = math.log(t28 * t15)
t31 = 0.96902277115443742139e-3 * t30
t34 = 0.1e1 / (t11 + 0.35302100000000000000e1 * t12 + 0.180578e2)
t38 = math.log(t4 * t9 * t34 / 0.4e1)
t43 = math.atan(0.47309269095601128300e1 / (t12 + 0.706042e1))
t46 = (t26 + 0.32500e0) ** 2
t48 = math.log(t46 * t34)
t53 = 0.1e1 / (t11 + 0.10061550000000000000e2 * t12 + 0.101578e3)
t57 = math.log(t4 * t9 * t53 / 0.4e1)
t62 = math.atan(0.11716852777089929792e1 / (t12 + 0.201231e2))
t65 = (t26 + 0.743294e0) ** 2
t67 = math.log(t65 * t53)
t71 = 0.1e1 / (t11 + 0.65360000000000000000e1 * t12 + 0.427198e2)
t75 = math.log(t4 * t9 * t71 / 0.4e1)
t80 = math.atan(0.44899888641287296627e-1 / (t12 + 0.130720e2))
t83 = (t26 + 0.409286e0) ** 2
t85 = math.log(t83 * t71)
t90 = math.pi ** 2
t95 = 0.1e1 / (t11 + 0.53417500000000000000e0 * t12 + 0.114813e2)
t99 = math.log(t4 * t9 * t95 / 0.4e1)
t103 = math.atan(0.66920720466459414830e1 / (t12 + 0.106835e1))
t106 = (t26 + 0.228344e0) ** 2
t108 = math.log(t106 * t95)
t112 = p_a_zeta_threshold ** (0.1e1 / 0.3e1)
t114 = jnp.where(0.1e1 <= p_a_zeta_threshold, t112 * p_a_zeta_threshold, 1)
t118 = 2 ** (0.1e1 / 0.3e1)
t119 = t118 - 0.1e1
res = t20 + t25 + t31 - 0.3e1 / 0.16e2 * (0.1554535e-1 * t38 + 0.52491393169780936218e-1 * t43 + 0.22478670955426118383e-2 * t48 - t20 - t25 - t31) / (0.1554535e-1 * t57 + 0.61881802979060631482e0 * t62 + 0.26673100072733151594e-2 * t67 - 0.310907e-1 * t75 - 0.20521972937837502661e2 * t80 - 0.44313737677495382697e-2 * t85) / t90 * (t99 + 0.32323836906055067299e0 * t103 + 0.21608710360898267022e-1 * t108) * (0.2e1 * t114 - 0.2e1)
