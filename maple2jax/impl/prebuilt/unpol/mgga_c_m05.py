t3 = 0.1e1 <= p_a_zeta_threshold
t4 = jnp.logical_or(r0 / 0.2e1 <= p_a_dens_threshold, t3)
t5 = jnp.where(t3, p_a_zeta_threshold, 1)
t6 = 3 ** (0.1e1 / 0.3e1)
t8 = (0.1e1 / math.pi) ** (0.1e1 / 0.3e1)
t9 = t6 * t8
t10 = 4 ** (0.1e1 / 0.3e1)
t11 = t10 ** 2
t13 = r0 ** (0.1e1 / 0.3e1)
t14 = 0.1e1 / t13
t15 = 2 ** (0.1e1 / 0.3e1)
t17 = p_a_zeta_threshold ** (0.1e1 / 0.3e1)
t19 = jnp.where(t3, 0.1e1 / t17, 1)
t21 = t9 * t11 * t14 * t15 * t19
t24 = math.sqrt(t21)
t27 = t21 ** 0.15e1
t29 = t6 ** 2
t30 = t8 ** 2
t31 = t29 * t30
t33 = t13 ** 2
t34 = 0.1e1 / t33
t35 = t15 ** 2
t37 = t19 ** 2
t39 = t31 * t10 * t34 * t35 * t37
t45 = math.log(0.1e1 + 0.16081979498692535067e2 / (0.37978500000000000000e1 * t24 + 0.89690000000000000000e0 * t21 + 0.20477500000000000000e0 * t27 + 0.12323500000000000000e0 * t39))
t47 = 0.621814e-1 * (0.1e1 + 0.53425000000000000000e-1 * t21) * t45
t49 = t17 * p_a_zeta_threshold
t51 = jnp.where(0.2e1 <= p_a_zeta_threshold, t49, 0.2e1 * t15)
t53 = jnp.where(0.0e0 <= p_a_zeta_threshold, t49, 0)
t57 = 0.1e1 / (0.2e1 * t15 - 0.2e1)
t58 = (t51 + t53 - 0.2e1) * t57
t69 = math.log(0.1e1 + 0.32163958997385070134e2 / (0.70594500000000000000e1 * t24 + 0.15494250000000000000e1 * t21 + 0.42077500000000000000e0 * t27 + 0.15629250000000000000e0 * t39))
t82 = math.log(0.1e1 + 0.29608749977793437516e2 / (0.51785000000000000000e1 * t24 + 0.90577500000000000000e0 * t21 + 0.11003250000000000000e0 * t27 + 0.12417750000000000000e0 * t39))
t83 = (0.1e1 + 0.27812500000000000000e-1 * t21) * t82
t92 = jnp.where(t4, 0, t5 * (-t47 + t58 * (-0.3109070e-1 * (0.1e1 + 0.51370000000000000000e-1 * t21) * t69 + t47 - 0.19751673498613801407e-1 * t83) + 0.19751673498613801407e-1 * t58 * t83) / 0.2e1)
t97 = r0 ** 2
t100 = t35 / t33 / t97
t103 = params_a_gamma_ss * s0 * t100 + 0.1e1
t108 = params_a_gamma_ss ** 2
t110 = s0 ** 2
t112 = t97 ** 2
t116 = t15 / t13 / t112 / r0
t117 = t103 ** 2
t126 = t112 ** 2
t128 = t110 * s0 / t126
t135 = t108 ** 2
t137 = t110 ** 2
t142 = t35 / t33 / t126 / t97
t143 = t117 ** 2
t156 = tau0 ** 2
t161 = params_a_Fermi_D_cnst ** 2
t166 = math.exp(-0.8e1 * t156 * t15 / t13 / t97 / r0 / t161)
t172 = t9 * t11 * t14
t175 = math.sqrt(t172)
t178 = t172 ** 0.15e1
t181 = t31 * t10 * t34
t187 = math.log(0.1e1 + 0.16081979498692535067e2 / (0.37978500000000000000e1 * t175 + 0.89690000000000000000e0 * t172 + 0.20477500000000000000e0 * t178 + 0.12323500000000000000e0 * t181))
t190 = jnp.where(t3, t49, 1)
t204 = math.log(0.1e1 + 0.29608749977793437516e2 / (0.51785000000000000000e1 * t175 + 0.90577500000000000000e0 * t172 + 0.11003250000000000000e0 * t178 + 0.12417750000000000000e0 * t181))
t217 = 0.2e1 * params_a_gamma_ab * s0 * t100 + 0.1e1
t223 = params_a_gamma_ab ** 2
t226 = t217 ** 2
t240 = t223 ** 2
t243 = t226 ** 2
res = 0.2e1 * t92 * (params_a_css[0] + params_a_css[1] * params_a_gamma_ss * s0 * t100 / t103 + 0.2e1 * params_a_css[2] * t108 * t110 * t116 / t117 + 0.4e1 * params_a_css[3] * t108 * params_a_gamma_ss * t128 / t117 / t103 + 0.4e1 * params_a_css[4] * t135 * t137 * t142 / t143) * (0.1e1 - s0 / r0 / tau0 / 0.8e1) * (0.1e1 - t166) + (-0.621814e-1 * (0.1e1 + 0.53425000000000000000e-1 * t172) * t187 + 0.19751673498613801407e-1 * (0.2e1 * t190 - 0.2e1) * t57 * (0.1e1 + 0.27812500000000000000e-1 * t172) * t204 - 0.2e1 * t92) * (params_a_cab[0] + 0.2e1 * params_a_cab[1] * params_a_gamma_ab * s0 * t100 / t217 + 0.8e1 * params_a_cab[2] * t223 * t110 * t116 / t226 + 0.32e2 * params_a_cab[3] * t223 * params_a_gamma_ab * t128 / t226 / t217 + 0.64e2 * params_a_cab[4] * t240 * t137 * t142 / t243)
