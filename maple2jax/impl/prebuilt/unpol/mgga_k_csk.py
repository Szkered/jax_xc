t3 = 3 ** (0.1e1 / 0.3e1)
t4 = t3 ** 2
t5 = math.pi ** (0.1e1 / 0.3e1)
t8 = 0.1e1 <= p_a_zeta_threshold
t9 = p_a_zeta_threshold - 0.1e1
t11 = jnp.where(t8, -t9, 0)
t12 = jnp.where(t8, t9, t11)
t13 = 0.1e1 + t12
t15 = p_a_zeta_threshold ** (0.1e1 / 0.3e1)
t16 = t15 ** 2
t18 = t13 ** (0.1e1 / 0.3e1)
t19 = t18 ** 2
t21 = jnp.where(t13 <= p_a_zeta_threshold, t16 * p_a_zeta_threshold, t19 * t13)
t22 = r0 ** (0.1e1 / 0.3e1)
t23 = t22 ** 2
t25 = 6 ** (0.1e1 / 0.3e1)
t26 = math.pi ** 2
t27 = t26 ** (0.1e1 / 0.3e1)
t28 = t27 ** 2
t30 = t25 / t28
t31 = 2 ** (0.1e1 / 0.3e1)
t32 = t31 ** 2
t34 = r0 ** 2
t38 = t30 * s0 * t32 / t23 / t34
t47 = 0.5e1 / 0.54e2 * t30 * l0 * t32 / t23 / r0 - 0.5e1 / 0.81e2 * t38
t49 = math.log(0.1e1 - DBL_EPSILON)
t50 = 0.1e1 / params_a_csk_a
t51 = (-t49) ** (-t50)
t53 = math.log(DBL_EPSILON)
t54 = (-t53) ** (-t50)
t55 = -t54 < t47
t56 = jnp.where(t55, -t54, t47)
t58 = jnp.where(-t51 < t56, t56, -t51)
t59 = abs(t58)
t60 = t59 ** params_a_csk_a
t62 = math.exp(-0.1e1 / t60)
t64 = (0.1e1 - t62) ** t50
t65 = jnp.where(t55, 1, t64)
t66 = jnp.where(t47 < -t51, 0, t65)
t72 = jnp.where(r0 / 0.2e1 <= p_a_dens_threshold, 0, 0.3e1 / 0.20e2 * t4 * t5 * math.pi * t21 * t23 * (0.1e1 + 0.5e1 / 0.72e2 * t38 + t47 * t66))
res = 0.2e1 * t72
