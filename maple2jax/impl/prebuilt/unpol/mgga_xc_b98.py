t1 = 3 ** (0.1e1 / 0.3e1)
t2 = math.pi ** (0.1e1 / 0.3e1)
t5 = 0.1e1 <= p_a_zeta_threshold
t6 = p_a_zeta_threshold ** (0.1e1 / 0.3e1)
t7 = t6 * p_a_zeta_threshold
t8 = jnp.where(t5, t7, 1)
t9 = r0 ** (0.1e1 / 0.3e1)
t11 = 2 ** (0.1e1 / 0.3e1)
t12 = t11 ** 2
t14 = t9 ** 2
t16 = 0.1e1 / t14 / r0
t19 = r0 ** 2
t28 = 6 ** (0.1e1 / 0.3e1)
t30 = math.pi ** 2
t31 = t30 ** (0.1e1 / 0.3e1)
t32 = t31 ** 2
t36 = 0.1e1 - 0.5e1 / 0.9e1 * (tau0 * t12 * t16 - s0 * t12 / t14 / t19 / 0.8e1 - l0 * t12 * t16 / 0.4e1) * t28 / t32
t37 = t36 ** 2
t39 = 0.1e1 + 0.121e-1 * t37
t40 = math.sqrt(t39)
t53 = jnp.logical_or(r0 / 0.2e1 <= p_a_dens_threshold, t5)
t54 = jnp.where(t5, p_a_zeta_threshold, 1)
t56 = (0.1e1 / math.pi) ** (0.1e1 / 0.3e1)
t57 = t1 * t56
t58 = 4 ** (0.1e1 / 0.3e1)
t59 = t58 ** 2
t61 = 0.1e1 / t9
t64 = jnp.where(t5, 0.1e1 / t6, 1)
t66 = t57 * t59 * t61 * t11 * t64
t69 = math.sqrt(t66)
t72 = t66 ** 0.15e1
t74 = t1 ** 2
t75 = t56 ** 2
t76 = t74 * t75
t78 = 0.1e1 / t14
t80 = t64 ** 2
t82 = t76 * t58 * t78 * t12 * t80
t88 = math.log(0.1e1 + 0.16081824322151104822e2 / (0.37978500000000000000e1 * t69 + 0.89690000000000000000e0 * t66 + 0.20477500000000000000e0 * t72 + 0.12323500000000000000e0 * t82))
t90 = 0.62182e-1 * (0.1e1 + 0.53425000000000000000e-1 * t66) * t88
t93 = jnp.where(0.2e1 <= p_a_zeta_threshold, t7, 0.2e1 * t11)
t95 = jnp.where(0.0e0 <= p_a_zeta_threshold, t7, 0)
t99 = 0.1e1 / (0.2e1 * t11 - 0.2e1)
t100 = (t93 + t95 - 0.2e1) * t99
t111 = math.log(0.1e1 + 0.32164683177870697974e2 / (0.70594500000000000000e1 * t69 + 0.15494250000000000000e1 * t66 + 0.42077500000000000000e0 * t72 + 0.15629250000000000000e0 * t82))
t124 = math.log(0.1e1 + 0.29608574643216675549e2 / (0.51785000000000000000e1 * t69 + 0.90577500000000000000e0 * t66 + 0.11003250000000000000e0 * t72 + 0.12417750000000000000e0 * t82))
t125 = (0.1e1 + 0.27812500000000000000e-1 * t66) * t124
t134 = jnp.where(t53, 0, t54 * (-t90 + t100 * (-0.31090e-1 * (0.1e1 + 0.51370000000000000000e-1 * t66) * t111 + t90 - 0.19751789702565206229e-1 * t125) + 0.19751789702565206229e-1 * t100 * t125) / 0.2e1)
t136 = 0.1e1 + 0.256e1 * t37
t137 = math.sqrt(t136)
t155 = t57 * t59 * t61
t158 = math.sqrt(t155)
t161 = t155 ** 0.15e1
t164 = t76 * t58 * t78
t170 = math.log(0.1e1 + 0.16081824322151104822e2 / (0.37978500000000000000e1 * t158 + 0.89690000000000000000e0 * t155 + 0.20477500000000000000e0 * t161 + 0.12323500000000000000e0 * t164))
t186 = math.log(0.1e1 + 0.29608574643216675549e2 / (0.51785000000000000000e1 * t158 + 0.90577500000000000000e0 * t155 + 0.11003250000000000000e0 * t161 + 0.12417750000000000000e0 * t164))
t193 = 0.1e1 + 0.196e-1 * t37
t194 = math.sqrt(t193)
res = -0.3e1 / 0.4e1 * t1 / t2 * t8 * t9 * (0.8085e0 + 0.73502e-1 * t36 / t40 + 0.171820e-2 * t37 / t39) + 0.2e1 * t134 * (0.2606e0 - 0.153728e1 * t36 / t137 + 0.2309888e1 * t37 / t136) * (0.1e1 - s0 / r0 / tau0 / 0.8e1) + (-0.62182e-1 * (0.1e1 + 0.53425000000000000000e-1 * t155) * t170 + 0.19751789702565206229e-1 * (0.2e1 * t8 - 0.2e1) * t99 * (0.1e1 + 0.27812500000000000000e-1 * t155) * t186 - 0.2e1 * t134) * (0.12033e1 - 0.318038e0 * t36 / t194 + 0.1880816e-1 * t37 / t193)
