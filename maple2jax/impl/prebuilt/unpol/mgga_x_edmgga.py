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
t19 = r0 ** (0.1e1 / 0.3e1)
t21 = 4 ** (0.1e1 / 0.3e1)
t22 = t3 ** 2
t24 = math.pi ** 2
t25 = t24 ** (0.1e1 / 0.3e1)
t27 = t21 * t22 * t25 / 0.9e1
t28 = 0.1e1 - t27
t29 = 2 ** (0.1e1 / 0.3e1)
t30 = t29 ** 2
t32 = t19 ** 2
t34 = 0.1e1 / t32 / r0
t37 = r0 ** 2
t46 = 6 ** (0.1e1 / 0.3e1)
t48 = t25 ** 2
t50 = (tau0 * t30 * t34 - s0 * t30 / t32 / t37 / 0.8e1 - l0 * t30 * t34 / 0.4e1) * t46 / t48
t51 = 0.5e1 / 0.9e1 * t50
t53 = 0.39111111111111111111e0 * t50
t57 = jnp.where(0.0e0 < 0.70414204545454545455e0 - t53, -0.14204545454545454545e-3, 0.704e0 - t53)
t60 = t57 ** 2
t66 = (0.1e1 - t51) ** 2
t69 = math.sqrt(0.1e1 + 0.495616e0 * t66)
t71 = jnp.where(-t51 < -0.14205545454545454545e5, -0.1e1 / t57 / 0.2e1 + 0.1e1 / t60 / t57 / 0.8e1, 0.704e0 - t53 + t69)
t75 = math.sqrt(0.30e2)
t76 = math.sqrt(t71)
t78 = t28 ** 2
t92 = math.asinh(0.12611295594149683617e-1 / t78 / t28 * t24 * math.pi * t75 * (0.59400000000000000006e1 * t78 / t24 - 0.206514e-1) * (t71 - 0.1e1))
t103 = jnp.where(r0 / 0.2e1 <= p_a_dens_threshold, 0, -0.3e1 / 0.8e1 * t3 / t4 * t18 * t19 * (t27 + t28 * t71 / (0.1e1 + 0.44497190922573977694e0 * t28 / math.pi * t75 * t76 * t92)))
res = 0.2e1 * t103
