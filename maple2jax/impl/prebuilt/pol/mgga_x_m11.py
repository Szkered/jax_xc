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
t29 = 9 ** (0.1e1 / 0.3e1)
t30 = t29 ** 2
t32 = (0.1e1 / math.pi) ** (0.1e1 / 0.3e1)
t33 = t32 ** 2
t35 = t30 * t33 * p_a_cam_omega
t37 = t2 / t28
t39 = 0.1e1 + t17 <= p_a_zeta_threshold
t41 = 0.1e1 - t17 <= p_a_zeta_threshold
t42 = jnp.where(t41, t15, t17)
t43 = jnp.where(t39, t11, t42)
t44 = 0.1e1 + t43
t46 = t44 ** (0.1e1 / 0.3e1)
t47 = jnp.where(t44 <= p_a_zeta_threshold, t22, t46)
t51 = t35 * t37 / t47 / 0.18e2
t53 = 0.135e1 < t51
t54 = jnp.where(t53, t51, 0.135e1)
t55 = t54 ** 2
t58 = t55 ** 2
t61 = t58 * t55
t64 = t58 ** 2
t76 = t64 ** 2
t80 = jnp.where(t53, 0.135e1, t51)
t81 = math.sqrt(math.pi)
t84 = math.erf(0.1e1 / t80 / 0.2e1)
t86 = t80 ** 2
t89 = math.exp(-0.1e1 / t86 / 0.4e1)
t100 = jnp.where(0.135e1 <= t51, 0.1e1 / t55 / 0.36e2 - 0.1e1 / t58 / 0.960e3 + 0.1e1 / t61 / 0.26880e5 - 0.1e1 / t64 / 0.829440e6 + 0.1e1 / t64 / t55 / 0.28385280e8 - 0.1e1 / t64 / t58 / 0.1073479680e10 + 0.1e1 / t64 / t61 / 0.44590694400e11 - 0.1e1 / t76 / 0.2021444812800e13, 0.1e1 - 0.8e1 / 0.3e1 * t80 * (t81 * t84 + 0.2e1 * t80 * (t89 - 0.3e1 / 0.2e1 - 0.2e1 * t86 * (t89 - 0.1e1))))
t102 = 6 ** (0.1e1 / 0.3e1)
t103 = math.pi ** 2
t104 = t103 ** (0.1e1 / 0.3e1)
t105 = t104 ** 2
t107 = t102 / t105
t108 = r0 ** 2
t109 = r0 ** (0.1e1 / 0.3e1)
t110 = t109 ** 2
t114 = t107 * s0 / t110 / t108
t120 = params_a_a[0]
t121 = params_a_a[1]
t122 = t102 ** 2
t124 = 0.3e1 / 0.10e2 * t122 * t105
t127 = tau0 / t110 / r0
t128 = t124 - t127
t130 = t124 + t127
t131 = 0.1e1 / t130
t133 = params_a_a[2]
t134 = t128 ** 2
t136 = t130 ** 2
t137 = 0.1e1 / t136
t139 = params_a_a[3]
t140 = t134 * t128
t142 = t136 * t130
t143 = 0.1e1 / t142
t145 = params_a_a[4]
t146 = t134 ** 2
t148 = t136 ** 2
t149 = 0.1e1 / t148
t151 = params_a_a[5]
t152 = t146 * t128
t155 = 0.1e1 / t148 / t130
t157 = params_a_a[6]
t158 = t146 * t134
t161 = 0.1e1 / t148 / t136
t163 = params_a_a[7]
t164 = t146 * t140
t167 = 0.1e1 / t148 / t142
t169 = params_a_a[8]
t170 = t146 ** 2
t172 = t148 ** 2
t173 = 0.1e1 / t172
t175 = params_a_a[9]
t176 = t170 * t128
t179 = 0.1e1 / t172 / t130
t181 = params_a_a[10]
t182 = t170 * t134
t185 = 0.1e1 / t172 / t136
t187 = params_a_a[11]
t188 = t170 * t140
t191 = 0.1e1 / t172 / t142
t193 = t120 + t121 * t128 * t131 + t133 * t134 * t137 + t139 * t140 * t143 + t145 * t146 * t149 + t151 * t152 * t155 + t157 * t158 * t161 + t163 * t164 * t167 + t169 * t170 * t173 + t175 * t176 * t179 + t181 * t182 * t185 + t187 * t188 * t191
t196 = math.exp(-0.93189002206715572255e-2 * t114)
t199 = params_a_b[0]
t200 = params_a_b[1]
t203 = params_a_b[2]
t206 = params_a_b[3]
t209 = params_a_b[4]
t212 = params_a_b[5]
t215 = params_a_b[6]
t218 = params_a_b[7]
t221 = params_a_b[8]
t224 = params_a_b[9]
t227 = params_a_b[10]
t230 = params_a_b[11]
t233 = t199 + t200 * t128 * t131 + t203 * t134 * t137 + t206 * t140 * t143 + t209 * t146 * t149 + t212 * t152 * t155 + t215 * t158 * t161 + t218 * t164 * t167 + t221 * t170 * t173 + t224 * t176 * t179 + t227 * t182 * t185 + t230 * t188 * t191
t239 = jnp.where(r0 <= p_a_dens_threshold, 0, -0.3e1 / 0.8e1 * t5 * t26 * t28 * t100 * ((0.18040e1 - 0.64641600e0 / (0.8040e0 + 0.91462500000000000000e-2 * t114)) * t193 + (0.1552e1 - 0.552e0 * t196) * t233))
t241 = jnp.where(t10, t15, -t17)
t242 = jnp.where(t14, t11, t241)
t243 = 0.1e1 + t242
t245 = t243 ** (0.1e1 / 0.3e1)
t247 = jnp.where(t243 <= p_a_zeta_threshold, t23, t245 * t243)
t249 = jnp.where(t39, t15, -t17)
t250 = jnp.where(t41, t11, t249)
t251 = 0.1e1 + t250
t253 = t251 ** (0.1e1 / 0.3e1)
t254 = jnp.where(t251 <= p_a_zeta_threshold, t22, t253)
t258 = t35 * t37 / t254 / 0.18e2
t260 = 0.135e1 < t258
t261 = jnp.where(t260, t258, 0.135e1)
t262 = t261 ** 2
t265 = t262 ** 2
t268 = t265 * t262
t271 = t265 ** 2
t283 = t271 ** 2
t287 = jnp.where(t260, 0.135e1, t258)
t290 = math.erf(0.1e1 / t287 / 0.2e1)
t292 = t287 ** 2
t295 = math.exp(-0.1e1 / t292 / 0.4e1)
t306 = jnp.where(0.135e1 <= t258, 0.1e1 / t262 / 0.36e2 - 0.1e1 / t265 / 0.960e3 + 0.1e1 / t268 / 0.26880e5 - 0.1e1 / t271 / 0.829440e6 + 0.1e1 / t271 / t262 / 0.28385280e8 - 0.1e1 / t271 / t265 / 0.1073479680e10 + 0.1e1 / t271 / t268 / 0.44590694400e11 - 0.1e1 / t283 / 0.2021444812800e13, 0.1e1 - 0.8e1 / 0.3e1 * t287 * (t81 * t290 + 0.2e1 * t287 * (t295 - 0.3e1 / 0.2e1 - 0.2e1 * t292 * (t295 - 0.1e1))))
t308 = r1 ** 2
t309 = r1 ** (0.1e1 / 0.3e1)
t310 = t309 ** 2
t314 = t107 * s2 / t310 / t308
t322 = tau1 / t310 / r1
t323 = t124 - t322
t325 = t124 + t322
t326 = 0.1e1 / t325
t328 = t323 ** 2
t330 = t325 ** 2
t331 = 0.1e1 / t330
t333 = t328 * t323
t335 = t330 * t325
t336 = 0.1e1 / t335
t338 = t328 ** 2
t340 = t330 ** 2
t341 = 0.1e1 / t340
t343 = t338 * t323
t346 = 0.1e1 / t340 / t325
t348 = t338 * t328
t351 = 0.1e1 / t340 / t330
t353 = t338 * t333
t356 = 0.1e1 / t340 / t335
t358 = t338 ** 2
t360 = t340 ** 2
t361 = 0.1e1 / t360
t363 = t358 * t323
t366 = 0.1e1 / t360 / t325
t368 = t358 * t328
t371 = 0.1e1 / t360 / t330
t373 = t358 * t333
t376 = 0.1e1 / t360 / t335
t378 = t120 + t121 * t323 * t326 + t133 * t328 * t331 + t139 * t333 * t336 + t145 * t338 * t341 + t151 * t343 * t346 + t157 * t348 * t351 + t163 * t353 * t356 + t169 * t358 * t361 + t175 * t363 * t366 + t181 * t368 * t371 + t187 * t373 * t376
t381 = math.exp(-0.93189002206715572255e-2 * t314)
t406 = t199 + t200 * t323 * t326 + t203 * t328 * t331 + t206 * t333 * t336 + t209 * t338 * t341 + t212 * t343 * t346 + t215 * t348 * t351 + t218 * t353 * t356 + t221 * t358 * t361 + t224 * t363 * t366 + t227 * t368 * t371 + t230 * t373 * t376
t412 = jnp.where(r1 <= p_a_dens_threshold, 0, -0.3e1 / 0.8e1 * t5 * t247 * t28 * t306 * ((0.18040e1 - 0.64641600e0 / (0.8040e0 + 0.91462500000000000000e-2 * t314)) * t378 + (0.1552e1 - 0.552e0 * t381) * t406))
res = t239 + t412
