t2 = jnp.where(0 < 0, 0, 0)
t4 = 0.1e1 <= p_a_zeta_threshold
t5 = p_a_zeta_threshold - 0.1e1
t7 = jnp.where(t4, -t5, 0)
t8 = jnp.where(t4, t5, t7)
t9 = t8 ** 2
t11 = 2 ** (0.1e1 / 0.3e1)
t12 = t11 ** 2
t13 = s0 * t12
t14 = r0 ** 2
t15 = r0 ** (0.1e1 / 0.3e1)
t16 = t15 ** 2
t18 = 0.1e1 / t16 / t14
t19 = 0.1e1 + t8
t20 = t19 / 0.2e1
t21 = t20 ** (0.1e1 / 0.3e1)
t22 = t21 ** 2
t26 = 0.1e1 - t8
t27 = t26 / 0.2e1
t28 = t27 ** (0.1e1 / 0.3e1)
t29 = t28 ** 2
t36 = 3 ** (0.1e1 / 0.3e1)
t37 = math.pi ** 2
t38 = t37 ** (0.1e1 / 0.3e1)
t39 = t38 ** 2
t42 = t19 ** (0.1e1 / 0.3e1)
t43 = t42 * t19
t45 = t26 ** (0.1e1 / 0.3e1)
t46 = t45 * t26
t53 = (0.1e1 + (0.1e1 - t9) * (t13 * t18 * t22 * t20 + t13 * t18 * t29 * t27 - s0 * t18) * t36 / t39 * (0.1e1 / t43 + 0.1e1 / t46) / 0.24e2) ** 2
t54 = t53 ** 2
t57 = jnp.where(-t2 <= -0.999999999999e0, 0.398e1, 0.35e0 / t54)
t63 = s0 / r0 / tau0 / 0.8e1
t65 = jnp.where(0.1e1 < t63, 1, t63)
t66 = t65 ** 2
t70 = jnp.logical_or(r0 / 0.2e1 <= p_a_dens_threshold, t4)
t72 = (0.1e1 / math.pi) ** (0.1e1 / 0.3e1)
t73 = t36 * t72
t74 = 4 ** (0.1e1 / 0.3e1)
t75 = t74 ** 2
t76 = 0.1e1 / t15
t78 = t73 * t75 * t76
t81 = math.sqrt(t78)
t84 = t78 ** 0.15e1
t86 = t36 ** 2
t87 = t72 ** 2
t88 = t86 * t87
t89 = 0.1e1 / t16
t91 = t88 * t74 * t89
t97 = math.log(0.1e1 + 0.16081979498692535067e2 / (0.37978500000000000000e1 * t81 + 0.89690000000000000000e0 * t78 + 0.20477500000000000000e0 * t84 + 0.12323500000000000000e0 * t91))
t98 = (0.1e1 + 0.53425000000000000000e-1 * t78) * t97
t100 = t9 ** 2
t101 = t19 <= p_a_zeta_threshold
t102 = p_a_zeta_threshold ** (0.1e1 / 0.3e1)
t103 = t102 * p_a_zeta_threshold
t104 = jnp.where(t101, t103, t43)
t105 = t26 <= p_a_zeta_threshold
t106 = jnp.where(t105, t103, t46)
t107 = t104 + t106 - 0.2e1
t111 = 0.1e1 / (0.2e1 * t11 - 0.2e1)
t122 = math.log(0.1e1 + 0.32163958997385070134e2 / (0.70594500000000000000e1 * t81 + 0.15494250000000000000e1 * t78 + 0.42077500000000000000e0 * t84 + 0.15629250000000000000e0 * t91))
t125 = 0.621814e-1 * t98
t136 = math.log(0.1e1 + 0.29608749977793437516e2 / (0.51785000000000000000e1 * t81 + 0.90577500000000000000e0 * t78 + 0.11003250000000000000e0 * t84 + 0.12417750000000000000e0 * t91))
t137 = (0.1e1 + 0.27812500000000000000e-1 * t78) * t136
t141 = t100 * t107 * t111 * (-0.3109070e-1 * (0.1e1 + 0.51370000000000000000e-1 * t78) * t122 + t125 - 0.19751673498613801407e-1 * t137)
t144 = t107 * t111 * t137
t146 = math.log(0.2e1)
t147 = 0.1e1 - t146
t149 = t147 / t37
t150 = t102 ** 2
t151 = t42 ** 2
t152 = jnp.where(t101, t150, t151)
t153 = t45 ** 2
t154 = jnp.where(t105, t150, t153)
t156 = t152 / 0.2e1 + t154 / 0.2e1
t157 = t156 ** 2
t158 = t157 * t156
t161 = s0 / t15 / t14
t162 = 0.1e1 / t157
t165 = 0.1e1 / t72
t168 = math.exp(-t91 / 0.4e1)
t171 = t86 * t165 * t74 * (0.1e1 - t168)
t174 = 0.375e-1 + 0.83333333333333333332e-3 * t161 * t11 * t162 * t171
t175 = t161 * t11
t177 = t165 * t74
t181 = 0.1e1 / t147
t182 = t174 * t181
t183 = 0.19751673498613801407e-1 * t144
t189 = math.exp(-(-t125 + t141 + t183) * t181 * t37 / t158)
t192 = t37 / (t189 - 0.1e1)
t193 = s0 ** 2
t196 = t14 ** 2
t198 = 0.1e1 / t16 / t196
t199 = t198 * t12
t200 = t157 ** 2
t203 = 0.1e1 / t87
t205 = t36 * t203 * t75
t209 = t175 * t162 * t86 * t177 / 0.96e2 + t182 * t192 * t193 * t199 / t200 * t205 / 0.3072e4
t211 = t181 * t37
t219 = math.log(0.1e1 + t174 * t209 * t211 / (t182 * t192 * t209 + 0.1e1))
t221 = t149 * t158 * t219
t223 = -0.31090700000000000000e-1 * t98 + t141 / 0.2e1 + 0.98758367493069007035e-2 * t144 + t221 / 0.2e1
t224 = -t125 + t141 + t183 + t221
t225 = t73 * t75
t226 = t76 * t11
t228 = (0.1e1 / t19) ** (0.1e1 / 0.3e1)
t230 = t225 * t226 * t228
t233 = math.sqrt(t230)
t236 = t230 ** 0.15e1
t238 = t88 * t74
t239 = t89 * t12
t240 = t228 ** 2
t242 = t238 * t239 * t240
t248 = math.log(0.1e1 + 0.16081979498692535067e2 / (0.37978500000000000000e1 * t233 + 0.89690000000000000000e0 * t230 + 0.20477500000000000000e0 * t236 + 0.12323500000000000000e0 * t242))
t250 = 0.621814e-1 * (0.1e1 + 0.53425000000000000000e-1 * t230) * t248
t251 = 0.2e1 <= p_a_zeta_threshold
t253 = jnp.where(t251, t103, 0.2e1 * t11)
t254 = 0.0e0 <= p_a_zeta_threshold
t255 = jnp.where(t254, t103, 0)
t257 = (t253 + t255 - 0.2e1) * t111
t268 = math.log(0.1e1 + 0.32163958997385070134e2 / (0.70594500000000000000e1 * t233 + 0.15494250000000000000e1 * t230 + 0.42077500000000000000e0 * t236 + 0.15629250000000000000e0 * t242))
t281 = math.log(0.1e1 + 0.29608749977793437516e2 / (0.51785000000000000000e1 * t233 + 0.90577500000000000000e0 * t230 + 0.11003250000000000000e0 * t236 + 0.12417750000000000000e0 * t242))
t282 = (0.1e1 + 0.27812500000000000000e-1 * t230) * t281
t285 = t257 * (-0.3109070e-1 * (0.1e1 + 0.51370000000000000000e-1 * t230) * t268 + t250 - 0.19751673498613801407e-1 * t282)
t287 = 0.19751673498613801407e-1 * t257 * t282
t288 = jnp.where(t251, t150, t12)
t289 = jnp.where(t254, t150, 0)
t291 = t288 / 0.2e1 + t289 / 0.2e1
t292 = t291 ** 2
t293 = t292 * t291
t296 = t161 / t292 * t86
t298 = t12 / t228
t300 = math.exp(-t242 / 0.4e1)
t306 = 0.375e-1 + 0.83333333333333333335e-3 * t296 * t177 * t298 * (0.1e1 - t300)
t310 = t306 * t181
t315 = t37 / t293
t317 = math.exp(-(-t250 + t285 + t287) * t181 * t315)
t319 = 0.1e1 / (t317 - 0.1e1)
t323 = t292 ** 2
t326 = 0.1e1 / t323 * t36 * t203
t327 = t75 * t11
t333 = t296 * t177 * t298 / 0.96e2 + t310 * t37 * t319 * t193 * t198 * t326 * t327 / t240 / 0.1536e4
t343 = math.log(0.1e1 + t306 * t333 * t211 / (t310 * t37 * t319 * t333 + 0.1e1))
t346 = t149 * t293 * t343 - t250 + t285 + t287
t348 = jnp.where(t224 < t346, t346, t224)
t351 = jnp.where(t70, t223, t348 * t19 / 0.2e1)
t353 = (0.1e1 / t26) ** (0.1e1 / 0.3e1)
t355 = t225 * t226 * t353
t358 = math.sqrt(t355)
t361 = t355 ** 0.15e1
t363 = t353 ** 2
t365 = t238 * t239 * t363
t371 = math.log(0.1e1 + 0.16081979498692535067e2 / (0.37978500000000000000e1 * t358 + 0.89690000000000000000e0 * t355 + 0.20477500000000000000e0 * t361 + 0.12323500000000000000e0 * t365))
t373 = 0.621814e-1 * (0.1e1 + 0.53425000000000000000e-1 * t355) * t371
t384 = math.log(0.1e1 + 0.32163958997385070134e2 / (0.70594500000000000000e1 * t358 + 0.15494250000000000000e1 * t355 + 0.42077500000000000000e0 * t361 + 0.15629250000000000000e0 * t365))
t397 = math.log(0.1e1 + 0.29608749977793437516e2 / (0.51785000000000000000e1 * t358 + 0.90577500000000000000e0 * t355 + 0.11003250000000000000e0 * t361 + 0.12417750000000000000e0 * t365))
t398 = (0.1e1 + 0.27812500000000000000e-1 * t355) * t397
t401 = t257 * (-0.3109070e-1 * (0.1e1 + 0.51370000000000000000e-1 * t355) * t384 + t373 - 0.19751673498613801407e-1 * t398)
t403 = 0.19751673498613801407e-1 * t257 * t398
t405 = t12 / t353
t407 = math.exp(-t365 / 0.4e1)
t413 = 0.375e-1 + 0.83333333333333333335e-3 * t296 * t177 * t405 * (0.1e1 - t407)
t417 = t413 * t181
t422 = math.exp(-(-t373 + t401 + t403) * t181 * t315)
t424 = 0.1e1 / (t422 - 0.1e1)
t433 = t296 * t177 * t405 / 0.96e2 + t417 * t37 * t424 * t193 * t198 * t326 * t327 / t363 / 0.1536e4
t443 = math.log(0.1e1 + t413 * t433 * t211 / (t417 * t37 * t424 * t433 + 0.1e1))
t446 = t149 * t293 * t443 - t373 + t401 + t403
t448 = jnp.where(t224 < t446, t446, t224)
t451 = jnp.where(t70, t223, t448 * t26 / 0.2e1)
t456 = jnp.where(t4, t103, 1)
t461 = 0.19751673498613801407e-1 * (0.2e1 * t456 - 0.2e1) * t111 * t137
t462 = jnp.where(t4, t150, 1)
t463 = t462 ** 2
t464 = t463 * t462
t465 = 0.1e1 / t463
t470 = 0.375e-1 + 0.83333333333333333332e-3 * t161 * t11 * t465 * t171
t475 = t470 * t181
t481 = math.exp(-(-t125 + t461) * t181 * t37 / t464)
t484 = t37 / (t481 - 0.1e1)
t487 = t463 ** 2
t493 = t175 * t465 * t86 * t177 / 0.96e2 + t475 * t484 * t193 * t199 / t487 * t205 / 0.3072e4
t502 = math.log(0.1e1 + t470 * t493 * t211 / (t475 * t484 * t493 + 0.1e1))
t507 = -(0.1e1 + t57) * t66 * (t351 + t451) + (t57 * t66 + 0.1e1) * (t149 * t464 * t502 - t125 + t461)
res = t507 * (0.1e1 + 0.45e1 * t507 * t66 * t65)
