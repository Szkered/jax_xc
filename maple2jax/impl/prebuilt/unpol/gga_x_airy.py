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
t21 = 6 ** (0.1e1 / 0.3e1)
t22 = t21 ** 2
t23 = math.pi ** 2
t24 = t23 ** (0.1e1 / 0.3e1)
t27 = math.sqrt(s0)
t28 = 2 ** (0.1e1 / 0.3e1)
t33 = t22 / t24 * t27 * t28 / t19 / r0
t34 = t33 ** 0.2626712e1
t37 = (0.1e1 + 0.13471619689594796103e-3 * t34) ** (-0.657946e0)
t40 = t33 ** 0.3217063e1
t42 = t33 ** 0.3223476e1
t45 = t33 ** 0.3473804e1
t54 = jnp.where(r0 / 0.2e1 <= p_a_dens_threshold, 0, -0.3e1 / 0.8e1 * t3 / t4 * t18 * t19 * (0.60146019220211109872e-4 * t34 * t37 + (0.1e1 - 0.45212413010769857073e-1 * t40 + 0.45402221956620378581e-1 * t42) / (0.1e1 + 0.47702180224903349918e-3 * t45)))
res = 0.2e1 * t54
