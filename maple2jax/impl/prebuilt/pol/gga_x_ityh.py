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
t28 = t6 ** (0.1e1 / 0.3e1)
t29 = t2 ** 2
t30 = math.pi * t29
t32 = (0.1e1 / math.pi) ** (0.1e1 / 0.3e1)
t33 = 0.1e1 / t32
t34 = 4 ** (0.1e1 / 0.3e1)
t35 = t33 * t34
t37 = t29 * t33 * t34
t38 = r0 ** 2
t39 = r0 ** (0.1e1 / 0.3e1)
t40 = t39 ** 2
t44 = math.sqrt(s0)
t47 = t44 / t39 / r0
t48 = math.asinh(t47)
t56 = 0.1e1 + 0.93333333333333333332e-3 * t37 * s0 / t40 / t38 / (0.1e1 + 0.2520e-1 * t47 * t48)
t60 = math.sqrt(t30 * t35 / t56)
t63 = 2 ** (0.1e1 / 0.3e1)
t65 = (t20 * t6) ** (0.1e1 / 0.3e1)
t69 = p_a_cam_omega / t60 * t63 / t65 / 0.2e1
t71 = 0.135e1 < t69
t72 = jnp.where(t71, t69, 0.135e1)
t73 = t72 ** 2
t76 = t73 ** 2
t79 = t76 * t73
t82 = t76 ** 2
t94 = t82 ** 2
t98 = jnp.where(t71, 0.135e1, t69)
t99 = math.sqrt(math.pi)
t102 = math.erf(0.1e1 / t98 / 0.2e1)
t104 = t98 ** 2
t107 = math.exp(-0.1e1 / t104 / 0.4e1)
t118 = jnp.where(0.135e1 <= t69, 0.1e1 / t73 / 0.36e2 - 0.1e1 / t76 / 0.960e3 + 0.1e1 / t79 / 0.26880e5 - 0.1e1 / t82 / 0.829440e6 + 0.1e1 / t82 / t73 / 0.28385280e8 - 0.1e1 / t82 / t76 / 0.1073479680e10 + 0.1e1 / t82 / t79 / 0.44590694400e11 - 0.1e1 / t94 / 0.2021444812800e13, 0.1e1 - 0.8e1 / 0.3e1 * t98 * (t99 * t102 + 0.2e1 * t98 * (t107 - 0.3e1 / 0.2e1 - 0.2e1 * t104 * (t107 - 0.1e1))))
t123 = jnp.where(r0 <= p_a_dens_threshold, 0, -0.3e1 / 0.8e1 * t5 * t26 * t28 * t118 * t56)
t125 = jnp.where(t10, t15, -t17)
t126 = jnp.where(t14, t11, t125)
t127 = 0.1e1 + t126
t129 = t127 ** (0.1e1 / 0.3e1)
t131 = jnp.where(t127 <= p_a_zeta_threshold, t23, t129 * t127)
t133 = r1 ** 2
t134 = r1 ** (0.1e1 / 0.3e1)
t135 = t134 ** 2
t139 = math.sqrt(s2)
t142 = t139 / t134 / r1
t143 = math.asinh(t142)
t151 = 0.1e1 + 0.93333333333333333332e-3 * t37 * s2 / t135 / t133 / (0.1e1 + 0.2520e-1 * t142 * t143)
t155 = math.sqrt(t30 * t35 / t151)
t159 = (t127 * t6) ** (0.1e1 / 0.3e1)
t163 = p_a_cam_omega / t155 * t63 / t159 / 0.2e1
t165 = 0.135e1 < t163
t166 = jnp.where(t165, t163, 0.135e1)
t167 = t166 ** 2
t170 = t167 ** 2
t173 = t170 * t167
t176 = t170 ** 2
t188 = t176 ** 2
t192 = jnp.where(t165, 0.135e1, t163)
t195 = math.erf(0.1e1 / t192 / 0.2e1)
t197 = t192 ** 2
t200 = math.exp(-0.1e1 / t197 / 0.4e1)
t211 = jnp.where(0.135e1 <= t163, 0.1e1 / t167 / 0.36e2 - 0.1e1 / t170 / 0.960e3 + 0.1e1 / t173 / 0.26880e5 - 0.1e1 / t176 / 0.829440e6 + 0.1e1 / t176 / t167 / 0.28385280e8 - 0.1e1 / t176 / t170 / 0.1073479680e10 + 0.1e1 / t176 / t173 / 0.44590694400e11 - 0.1e1 / t188 / 0.2021444812800e13, 0.1e1 - 0.8e1 / 0.3e1 * t192 * (t99 * t195 + 0.2e1 * t192 * (t200 - 0.3e1 / 0.2e1 - 0.2e1 * t197 * (t200 - 0.1e1))))
t216 = jnp.where(r1 <= p_a_dens_threshold, 0, -0.3e1 / 0.8e1 * t5 * t131 * t28 * t211 * t151)
res = t123 + t216
