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
t39 = 0.1e1 / t38
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
t89 = t36 * t39 * t60 * (-0.3109070e-1 * (0.1e1 + 0.51370000000000000000e-1 * t11) * t71 + t33 - 0.19751673498613801407e-1 * t85)
t91 = 0.19751673498613801407e-1 * t60 * t85
t92 = t45 ** 2
t93 = t47 ** 2
t94 = jnp.where(t44, t92, t93)
t95 = t52 ** 2
t96 = jnp.where(t51, t92, t95)
t98 = t94 / 0.2e1 + t96 / 0.2e1
t100 = s0 + 0.2e1 * s1 + s2
t101 = math.sqrt(t100)
t104 = t98 ** 2
t105 = t104 * t98
t106 = 0.1e1 / t105
t112 = t98 ** (0.50000000000000000000e-1 * t101 * t100 * t39 * t106 / t14 / t11)
t113 = math.log(0.2e1)
t114 = 0.1e1 - t113
t116 = math.pi ** 2
t117 = 0.1e1 / t116
t123 = t56 ** 2
t129 = math.exp(-t25 / 0.4e1)
t134 = 0.786e0 * t117 + 0.17500000000000000000e-1 * t101 / t8 / t7 * t123 / t98 / t14 * (0.1e1 - t129)
t146 = 0.1e1 / t114
t147 = t134 * t146
t152 = math.exp(-(-t33 + t89 + t91) * t146 * t116 * t106)
t155 = t116 / (t152 - 0.1e1)
t156 = t100 ** 2
t162 = t104 ** 2
t171 = t100 / t8 / t37 * t56 / t104 * t19 / t3 * t5 / 0.96e2 + t147 * t155 * t156 / t22 / t38 * t123 / t162 * t1 / t20 * t6 / 0.3072e4
t181 = math.log(0.1e1 + t134 * t171 * t146 * t116 / (t147 * t155 * t171 + 0.1e1))
res = t112 * t114 * t117 * t105 * t181 - t33 + t89 + t91
