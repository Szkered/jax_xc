t1 = 0.1e1 / math.pi
t3 = t1 / r0
t6 = 3 ** (0.1e1 / 0.3e1)
t7 = t6 ** 2
t8 = t1 ** (0.1e1 / 0.3e1)
t11 = 4 ** (0.1e1 / 0.3e1)
t12 = r0 ** (0.1e1 / 0.3e1)
t14 = t7 / t8 * t11 * t12
t17 = math.log(0.1e1 + 0.10e2 * t14)
t19 = 0.252e-1 * (0.1e1 + t3 / 0.36000e5) * t17
t20 = t8 ** 2
t22 = t12 ** 2
t25 = t7 * t20 * t11 / t22
t28 = t11 ** 2
t31 = t6 * t8 * t28 / t12
t33 = 0.1e1 <= p_a_zeta_threshold
t34 = p_a_zeta_threshold ** (0.1e1 / 0.3e1)
t36 = jnp.where(t33, t34 * p_a_zeta_threshold, 1)
t39 = 2 ** (0.1e1 / 0.3e1)
t48 = math.log(0.1e1 + 0.25000000000000000000e2 * t14)
t56 = math.pi ** 2
t57 = t56 ** (0.1e1 / 0.3e1)
t60 = r0 ** 2
t63 = s0 / t22 / t60
t66 = t34 ** 2
t68 = jnp.where(t33, t66 * p_a_zeta_threshold, 1)
t69 = math.sqrt(t68)
t72 = t1 ** (0.1e1 / 0.6e1)
t74 = math.sqrt(s0)
t76 = r0 ** (0.1e1 / 0.6e1)
t81 = math.exp(-t6 * params_a_lm_f / t72 * t74 / t76 / r0)
res = -t19 + 0.70000000000000000000e-5 * t25 - 0.10500000000000000000e-3 * t31 + 0.84000000000000000000e-2 + (0.2e1 * t36 - 0.2e1) / (0.2e1 * t39 - 0.2e1) * (-0.127e-1 * (0.1e1 + 0.17777777777777777778e-5 * t3) * t48 - 0.64355555555555555556e-5 * t25 + 0.83833333333333333334e-4 * t31 - 0.41666666666666666667e-2 + t19) + math.pi * t7 / t57 / t56 * (-0.7e1 / 0.9e1 * t63 * t36 + 0.2e1 / t69 * t81 * t63) * t12 / 0.144e3
