t3 = 3 ** (0.1e1 / 0.3e1)
t4 = math.pi ** (0.1e1 / 0.3e1)
t7 = 0.1e1 <= p_a_zeta_threshold
t8 = p_a_zeta_threshold - 0.1e1
t10 = jnp.where(t7, -t8, 0)
t11 = jnp.where(t7, t8, t10)
t12 = 0.1e1 + t11
t14 = p_a_zeta_threshold ** (0.1e1 / 0.3e1)
t16 = t12 ** (0.1e1 / 0.3e1)
t18 = jnp.where(t12 <= p_a_zeta_threshold, t14 * p_a_zeta_threshold, t16 * t12)
t20 = r0 ** (0.1e1 / 0.3e1)
t21 = 6 ** (0.1e1 / 0.3e1)
t23 = math.pi ** 2
t24 = t23 ** (0.1e1 / 0.3e1)
t25 = t24 ** 2
t26 = 0.1e1 / t25
t28 = 2 ** (0.1e1 / 0.3e1)
t29 = t28 ** 2
t31 = r0 ** 2
t32 = t20 ** 2
t35 = s0 * t29 / t32 / t31
t38 = t21 ** 2
t41 = 0.1e1 / t24 / t23
t43 = s0 ** 2
t45 = t31 ** 2
t49 = t43 * t28 / t20 / t45 / r0
t52 = t23 ** 2
t53 = 0.1e1 / t52
t56 = t45 ** 2
t58 = t43 * s0 / t56
t79 = jnp.where(r0 / 0.2e1 <= p_a_dens_threshold, 0, -0.3e1 / 0.8e1 * t3 / t4 * t18 * t20 * (0.1e1 + params_a_a1 * t21 * t26 * t35 / 0.24e2 + params_a_a2 * t38 * t41 * t49 / 0.288e3 + params_a_a3 * t53 * t58 / 0.576e3) / (0.1e1 + params_a_b1 * t21 * t26 * t35 / 0.24e2 + params_a_b2 * t38 * t41 * t49 / 0.288e3 + params_a_b3 * t53 * t58 / 0.576e3))
res = 0.2e1 * t79
