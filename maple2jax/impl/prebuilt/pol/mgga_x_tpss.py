t2 = 3 ** (0.1e1 / 0.3e1)
t3 = math.pi ** (0.1e1 / 0.3e1)
t5 = t2 / t3
t6 = r0 + r1
t7 = 0.1e1 / t6
t10 = 0.2e1 * r0 * t7 <= p_a_zeta_threshold
t11 = p_a_zeta_threshold - 0.1e1
t14 = 0.2e1 * r1 * t7 <= p_a_zeta_threshold
t15 = -t11
t17 = (r0 - r1) * t7
t18 = jnp.where(t14, t15, t17)
t19 = jnp.where(t10, t11, t18)
t20 = 0.1e1 + t19
t22 = p_a_zeta_threshold ** (0.1e1 / 0.3e1)
t23 = t22 * p_a_zeta_threshold
t24 = t20 ** (0.1e1 / 0.3e1)
t26 = jnp.where(t20 <= p_a_zeta_threshold, t23, t24 * t20)
t27 = t6 ** (0.1e1 / 0.3e1)
t29 = 0.1e1 / r0
t31 = 0.1e1 / tau0
t39 = (s0 * t29 * t31 / 0.8e1) ** (params_a_BLOC_a + params_a_BLOC_b * s0 * t29 * t31 / 0.8e1)
t41 = s0 ** 2
t42 = r0 ** 2
t43 = 0.1e1 / t42
t45 = tau0 ** 2
t46 = 0.1e1 / t45
t47 = t41 * t43 * t46
t50 = (0.1e1 + t47 / 0.64e2) ** 2
t54 = 6 ** (0.1e1 / 0.3e1)
t56 = math.pi ** 2
t57 = t56 ** (0.1e1 / 0.3e1)
t58 = t57 ** 2
t59 = 0.1e1 / t58
t61 = r0 ** (0.1e1 / 0.3e1)
t62 = t61 ** 2
t64 = 0.1e1 / t62 / t42
t65 = t59 * s0 * t64
t71 = s0 * t64
t73 = tau0 / t62 / r0 - t71 / 0.8e1
t77 = 0.5e1 / 0.9e1 * t73 * t54 * t59 - 0.1e1
t79 = t54 * t59
t84 = math.sqrt(0.5e1 * params_a_b * t73 * t79 * t77 + 0.9e1)
t90 = 0.27e2 / 0.20e2 * t77 / t84 + t79 * t71 / 0.36e2
t91 = t90 ** 2
t94 = t54 ** 2
t96 = 0.1e1 / t57 / t56
t97 = t94 * t96
t98 = t42 ** 2
t101 = 0.1e1 / t61 / t98 / r0
t106 = math.sqrt(0.50e2 * t97 * t41 * t101 + 0.162e3 * t47)
t110 = 0.1e1 / params_a_kappa * t94
t115 = math.sqrt(params_a_e)
t120 = params_a_e * params_a_mu
t121 = t56 ** 2
t122 = 0.1e1 / t121
t125 = t98 ** 2
t131 = t115 * t54
t135 = (0.1e1 + t131 * t65 / 0.24e2) ** 2
t147 = jnp.where(r0 <= p_a_dens_threshold, 0, -0.3e1 / 0.8e1 * t5 * t26 * t27 * (0.1e1 + params_a_kappa * (0.1e1 - params_a_kappa / (params_a_kappa + ((0.10e2 / 0.81e2 + params_a_c * t39 / t50) * t54 * t65 / 0.24e2 + 0.146e3 / 0.2025e4 * t91 - 0.73e2 / 0.97200e5 * t90 * t106 + 0.25e2 / 0.944784e6 * t110 * t96 * t41 * t101 + t115 * t41 * t43 * t46 / 0.720e3 + t120 * t122 * t41 * s0 / t125 / 0.2304e4) / t135))))
t149 = jnp.where(t10, t15, -t17)
t150 = jnp.where(t14, t11, t149)
t151 = 0.1e1 + t150
t153 = t151 ** (0.1e1 / 0.3e1)
t155 = jnp.where(t151 <= p_a_zeta_threshold, t23, t153 * t151)
t157 = 0.1e1 / r1
t159 = 0.1e1 / tau1
t167 = (s2 * t157 * t159 / 0.8e1) ** (params_a_BLOC_a + params_a_BLOC_b * s2 * t157 * t159 / 0.8e1)
t169 = s2 ** 2
t170 = r1 ** 2
t171 = 0.1e1 / t170
t173 = tau1 ** 2
t174 = 0.1e1 / t173
t175 = t169 * t171 * t174
t178 = (0.1e1 + t175 / 0.64e2) ** 2
t184 = r1 ** (0.1e1 / 0.3e1)
t185 = t184 ** 2
t187 = 0.1e1 / t185 / t170
t188 = t59 * s2 * t187
t194 = s2 * t187
t196 = tau1 / t185 / r1 - t194 / 0.8e1
t200 = 0.5e1 / 0.9e1 * t196 * t54 * t59 - 0.1e1
t206 = math.sqrt(0.5e1 * params_a_b * t196 * t79 * t200 + 0.9e1)
t212 = 0.27e2 / 0.20e2 * t200 / t206 + t79 * t194 / 0.36e2
t213 = t212 ** 2
t216 = t170 ** 2
t219 = 0.1e1 / t184 / t216 / r1
t224 = math.sqrt(0.50e2 * t97 * t169 * t219 + 0.162e3 * t175)
t237 = t216 ** 2
t246 = (0.1e1 + t131 * t188 / 0.24e2) ** 2
t258 = jnp.where(r1 <= p_a_dens_threshold, 0, -0.3e1 / 0.8e1 * t5 * t155 * t27 * (0.1e1 + params_a_kappa * (0.1e1 - params_a_kappa / (params_a_kappa + ((0.10e2 / 0.81e2 + params_a_c * t167 / t178) * t54 * t188 / 0.24e2 + 0.146e3 / 0.2025e4 * t213 - 0.73e2 / 0.97200e5 * t212 * t224 + 0.25e2 / 0.944784e6 * t110 * t96 * t169 * t219 + t115 * t169 * t171 * t174 / 0.720e3 + t120 * t122 * t169 * s2 / t237 / 0.2304e4) / t246))))
res = t147 + t258
