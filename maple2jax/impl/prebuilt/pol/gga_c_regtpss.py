t1 = 3 ** (0.1e1 / 0.3e1)
t3 = (0.1e1 / math.pi) ** (0.1e1 / 0.3e1)
t5 = 4 ** (0.1e1 / 0.3e1)
t6 = t5 ** 2
t7 = r0 + r1
t8 = t7 ** (0.1e1 / 0.3e1)
t11 = t1 * t3 * t6 / t8
t14 = math.sqrt(t11)
t17 = t11 ** 0.15e1
t19 = t1 ** 2
t20 = t3 ** 2
t22 = t8 ** 2
t25 = t19 * t20 * t5 / t22
t31 = math.log(0.1e1 + 0.16081979498692535067e2 / (0.37978500000000000000e1 * t14 + 0.89690000000000000000e0 * t11 + 0.20477500000000000000e0 * t17 + 0.12323500000000000000e0 * t25))
t33 = 0.621814e-1 * (0.1e1 + 0.53425000000000000000e-1 * t11) * t31
t34 = r0 - r1
t35 = t34 ** 2
t36 = t35 ** 2
t37 = t7 ** 2
t38 = t37 ** 2
t42 = t34 / t7
t43 = 0.1e1 + t42
t44 = t43 <= p_a_zeta_threshold
t45 = p_a_zeta_threshold ** (0.1e1 / 0.3e1)
t46 = t45 * p_a_zeta_threshold
t47 = t43 ** (0.1e1 / 0.3e1)
t49 = jnp.where(t44, t46, t47 * t43)
t50 = 0.1e1 - t42
t51 = t50 <= p_a_zeta_threshold
t52 = t50 ** (0.1e1 / 0.3e1)
t54 = jnp.where(t51, t46, t52 * t50)
t56 = 2 ** (0.1e1 / 0.3e1)
t60 = (t49 + t54 - 0.2e1) / (0.2e1 * t56 - 0.2e1)
t71 = math.log(0.1e1 + 0.32163958997385070134e2 / (0.70594500000000000000e1 * t14 + 0.15494250000000000000e1 * t11 + 0.42077500000000000000e0 * t17 + 0.15629250000000000000e0 * t25))
t84 = math.log(0.1e1 + 0.29608749977793437516e2 / (0.51785000000000000000e1 * t14 + 0.90577500000000000000e0 * t11 + 0.11003250000000000000e0 * t17 + 0.12417750000000000000e0 * t25))
t85 = (0.1e1 + 0.27812500000000000000e-1 * t11) * t84
t89 = t36 / t38 * t60 * (-0.3109070e-1 * (0.1e1 + 0.51370000000000000000e-1 * t11) * t71 + t33 - 0.19751673498613801407e-1 * t85)
t91 = 0.19751673498613801407e-1 * t60 * t85
t92 = math.log(0.2e1)
t93 = 0.1e1 - t92
t94 = math.pi ** 2
t97 = t45 ** 2
t98 = t47 ** 2
t99 = jnp.where(t44, t97, t98)
t100 = t52 ** 2
t101 = jnp.where(t51, t97, t100)
t103 = t99 / 0.2e1 + t101 / 0.2e1
t104 = t103 ** 2
t105 = t104 * t103
t111 = (0.1e1 + 0.25000000000000000000e-1 * t11) / (0.1e1 + 0.44450000000000000000e-1 * t11)
t113 = s0 + 0.2e1 * s1 + s2
t125 = 0.1e1 / t93
t126 = t111 * t125
t132 = math.exp(-(-t33 + t89 + t91) * t125 * t94 / t105)
t135 = t94 / (t132 - 0.1e1)
t136 = t113 ** 2
t141 = t56 ** 2
t143 = t104 ** 2
t152 = t113 / t8 / t37 * t56 / t104 * t19 / t3 * t5 / 0.96e2 + 0.21720231316129303386e-4 * t126 * t135 * t136 / t22 / t38 * t141 / t143 * t1 / t20 * t6
t164 = math.log(0.1e1 + 0.66724550603149220e-1 * t111 * t152 * t125 * t94 / (0.1e1 + 0.66724550603149220e-1 * t126 * t135 * t152))
res = -t33 + t89 + t91 + t93 / t94 * t105 * t164
