t3 = 0.1e1 <= p_a_zeta_threshold
t4 = jnp.logical_or(r0 / 0.2e1 <= p_a_dens_threshold, t3)
t5 = jnp.where(t3, p_a_zeta_threshold, 1)
t6 = 3 ** (0.1e1 / 0.3e1)
t8 = (0.1e1 / math.pi) ** (0.1e1 / 0.3e1)
t9 = t6 * t8
t10 = 4 ** (0.1e1 / 0.3e1)
t11 = t10 ** 2
t12 = t9 * t11
t13 = r0 ** (0.1e1 / 0.3e1)
t14 = 0.1e1 / t13
t15 = 2 ** (0.1e1 / 0.3e1)
t16 = t14 * t15
t17 = p_a_zeta_threshold ** (0.1e1 / 0.3e1)
t19 = jnp.where(t3, 0.1e1 / t17, 1)
t21 = t12 * t16 * t19
t22 = t21 / 0.4e1
t23 = math.sqrt(t21)
t26 = 0.1e1 / (t22 + 0.18637200000000000000e1 * t23 + 0.129352e2)
t31 = math.log(t12 * t16 * t19 * t26 / 0.4e1)
t32 = 0.310907e-1 * t31
t36 = math.atan(0.61519908197590802322e1 / (t23 + 0.372744e1))
t37 = 0.38783294878113014393e-1 * t36
t38 = t23 / 0.2e1
t40 = (t38 + 0.10498e0) ** 2
t42 = math.log(t40 * t26)
t43 = 0.96902277115443742139e-3 * t42
t46 = 0.1e1 / (t22 + 0.35302100000000000000e1 * t23 + 0.180578e2)
t51 = math.log(t12 * t16 * t19 * t46 / 0.4e1)
t56 = math.atan(0.47309269095601128300e1 / (t23 + 0.706042e1))
t59 = (t38 + 0.32500e0) ** 2
t61 = math.log(t59 * t46)
t65 = t17 * p_a_zeta_threshold
t67 = jnp.where(0.2e1 <= p_a_zeta_threshold, t65, 0.2e1 * t15)
t69 = jnp.where(0.0e0 <= p_a_zeta_threshold, t65, 0)
t72 = t15 - 0.1e1
t74 = 0.1e1 / t72 / 0.2e1
t79 = jnp.where(t4, 0, t5 * (t32 + t37 + t43 + (0.1554535e-1 * t51 + 0.52491393169780936218e-1 * t56 + 0.22478670955426118383e-2 * t61 - t32 - t37 - t43) * (t67 + t69 - 0.2e1) * t74) / 0.2e1)
t80 = t15 ** 2
t81 = s0 * t80
t82 = r0 ** 2
t83 = t13 ** 2
t85 = 0.1e1 / t83 / t82
t86 = t81 * t85
t88 = 0.1e1 + 0.2e0 * t86
t93 = s0 ** 2
t94 = t93 * t15
t95 = t82 ** 2
t98 = 0.1e1 / t13 / t95 / r0
t99 = t88 ** 2
t105 = t95 ** 2
t107 = t93 * s0 / t105
t115 = t11 * t14
t116 = t9 * t115
t117 = t116 / 0.4e1
t118 = math.sqrt(t116)
t121 = 0.1e1 / (t117 + 0.18637200000000000000e1 * t118 + 0.129352e2)
t125 = math.log(t9 * t115 * t121 / 0.4e1)
t130 = math.atan(0.61519908197590802322e1 / (t118 + 0.372744e1))
t132 = t118 / 0.2e1
t134 = (t132 + 0.10498e0) ** 2
t136 = math.log(t134 * t121)
t138 = math.pi ** 2
t142 = 0.1e1 / (t117 + 0.56553500000000000000e0 * t118 + 0.130045e2)
t146 = math.log(t9 * t115 * t142 / 0.4e1)
t150 = math.atan(0.71231089178181179908e1 / (t118 + 0.113107e1))
t153 = (t132 + 0.47584e-2) ** 2
t155 = math.log(t153 * t142)
t159 = jnp.where(t3, t65, 1)
t170 = 0.1e1 + 0.6e-2 * t86
t175 = t170 ** 2
res = 0.2e1 * t79 * (0.136823e-1 + 0.537840e-1 * t81 * t85 / t88 - 0.4406152e-1 * t94 * t98 / t99 + 0.3326304e-1 * t107 / t99 / t88) + (0.310907e-1 * t125 + 0.38783294878113014393e-1 * t130 + 0.96902277115443742139e-3 * t136 - 0.3e1 / 0.8e1 / t138 * (t146 + 0.31770800474394146400e0 * t150 + 0.41403379428206274608e-3 * t155) * (0.2e1 * t159 - 0.2e1) * t74 * t72 - 0.2e1 * t79) * (0.836897e0 + 0.1032306e-1 * t81 * t85 / t170 - 0.20051856e-3 * t94 * t98 / t175 - 0.395283456e-5 * t107 / t175 / t170)
