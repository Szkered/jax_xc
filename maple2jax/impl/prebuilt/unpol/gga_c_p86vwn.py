t1 = 3 ** (0.1e1 / 0.3e1)
t2 = 0.1e1 / math.pi
t3 = t2 ** (0.1e1 / 0.3e1)
t4 = t1 * t3
t5 = 4 ** (0.1e1 / 0.3e1)
t6 = t5 ** 2
t7 = r0 ** (0.1e1 / 0.3e1)
t8 = 0.1e1 / t7
t9 = t6 * t8
t10 = t4 * t9
t11 = t10 / 0.4e1
t12 = math.sqrt(t10)
t15 = 0.1e1 / (t11 + 0.18637200000000000000e1 * t12 + 0.129352e2)
t19 = math.log(t4 * t9 * t15 / 0.4e1)
t24 = math.atan(0.61519908197590802322e1 / (t12 + 0.372744e1))
t26 = t12 / 0.2e1
t28 = (t26 + 0.10498e0) ** 2
t30 = math.log(t28 * t15)
t32 = math.pi ** 2
t36 = 0.1e1 / (t11 + 0.56553500000000000000e0 * t12 + 0.130045e2)
t40 = math.log(t4 * t9 * t36 / 0.4e1)
t44 = math.atan(0.71231089178181179908e1 / (t12 + 0.113107e1))
t47 = (t26 + 0.47584e-2) ** 2
t49 = math.log(t47 * t36)
t53 = 0.1e1 <= p_a_zeta_threshold
t54 = p_a_zeta_threshold ** (0.1e1 / 0.3e1)
t56 = jnp.where(t53, t54 * p_a_zeta_threshold, 1)
t59 = 2 ** (0.1e1 / 0.3e1)
t60 = t59 - 0.1e1
t68 = r0 ** 2
t76 = t3 * t6 * t8
t79 = t1 ** 2
t81 = t3 ** 2
t83 = t7 ** 2
t85 = t81 * t5 / t83
t102 = params_a_aa + (params_a_bb + params_a_malpha * t1 * t76 / 0.4e1 + params_a_mbeta * t79 * t85 / 0.4e1) / (0.1e1 + params_a_mgamma * t1 * t76 / 0.4e1 + params_a_mdelta * t79 * t85 / 0.4e1 + 0.75000000000000000000e4 * params_a_mbeta * t2 / r0)
t104 = math.sqrt(s0)
t106 = r0 ** (0.1e1 / 0.6e1)
t111 = math.exp(-params_a_ftilde * (params_a_aa + params_a_bb) / t102 * t104 / t106 / r0)
t113 = t54 ** 2
t115 = jnp.where(t53, t113 * p_a_zeta_threshold, 1)
t116 = math.sqrt(t115)
res = 0.310907e-1 * t19 + 0.38783294878113014393e-1 * t24 + 0.96902277115443742139e-3 * t30 - 0.1e1 / t32 * (t40 + 0.31770800474394146400e0 * t44 + 0.41403379428206274608e-3 * t49) * (0.9e1 * t56 - 0.9e1) / 0.24e2 + s0 / t7 / t68 * t111 * t102 / t116
