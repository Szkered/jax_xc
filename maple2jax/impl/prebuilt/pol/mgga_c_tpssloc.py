t1 = r0 - r1
t2 = r0 + r1
t4 = t1 / t2
t6 = jnp.where(0.0e0 < t4, t4, -t4)
t8 = t1 ** 2
t9 = t2 ** 2
t13 = t8 ** 2
t14 = t9 ** 2
t16 = t13 / t14
t24 = 0.1e1 + t4
t25 = t24 <= p_a_zeta_threshold
t26 = p_a_zeta_threshold - 0.1e1
t27 = 0.1e1 - t4
t28 = t27 <= p_a_zeta_threshold
t30 = jnp.where(t28, -t26, t4)
t31 = jnp.where(t25, t26, t30)
t32 = t31 ** 2
t34 = r0 ** 2
t35 = r0 ** (0.1e1 / 0.3e1)
t36 = t35 ** 2
t39 = s0 / t36 / t34
t40 = 0.1e1 + t31
t41 = t40 / 0.2e1
t42 = t41 ** (0.1e1 / 0.3e1)
t43 = t42 ** 2
t46 = r1 ** 2
t47 = r1 ** (0.1e1 / 0.3e1)
t48 = t47 ** 2
t51 = s2 / t48 / t46
t52 = 0.1e1 - t31
t53 = t52 / 0.2e1
t54 = t53 ** (0.1e1 / 0.3e1)
t55 = t54 ** 2
t59 = s0 + 0.2e1 * s1 + s2
t60 = t2 ** (0.1e1 / 0.3e1)
t61 = t60 ** 2
t64 = t59 / t61 / t9
t67 = 3 ** (0.1e1 / 0.3e1)
t68 = math.pi ** 2
t69 = t68 ** (0.1e1 / 0.3e1)
t70 = t69 ** 2
t73 = t40 ** (0.1e1 / 0.3e1)
t74 = t73 * t40
t76 = t52 ** (0.1e1 / 0.3e1)
t77 = t76 * t52
t84 = (0.1e1 + (0.1e1 - t32) * (t39 * t43 * t41 + t51 * t55 * t53 - t64) * t67 / t70 * (0.1e1 / t74 + 0.1e1 / t77) / 0.24e2) ** 2
t85 = t84 ** 2
t88 = jnp.where(-t6 <= -0.999999999999e0, 0.398e1, (0.35e0 + 0.87e0 * t8 / t9 + 0.50e0 * t16 + 0.226e1 * t13 * t8 / t14 / t9) / t85)
t93 = t24 / 0.2e1
t94 = t93 ** (0.1e1 / 0.3e1)
t95 = t94 ** 2
t101 = t27 / 0.2e1
t102 = t101 ** (0.1e1 / 0.3e1)
t103 = t102 ** 2
t109 = t64 / (tau0 / t36 / r0 * t95 * t93 + tau1 / t48 / r1 * t103 * t101) / 0.8e1
t111 = jnp.where(0.1e1 < t109, 1, t109)
t112 = t111 ** 2
t115 = jnp.logical_or(r0 <= p_a_dens_threshold, t25)
t117 = (0.1e1 / math.pi) ** (0.1e1 / 0.3e1)
t118 = t67 * t117
t119 = 4 ** (0.1e1 / 0.3e1)
t120 = t119 ** 2
t121 = 0.1e1 / t60
t123 = t118 * t120 * t121
t126 = math.sqrt(t123)
t129 = t123 ** 0.15e1
t131 = t67 ** 2
t132 = t117 ** 2
t133 = t131 * t132
t134 = 0.1e1 / t61
t136 = t133 * t119 * t134
t142 = math.log(0.1e1 + 0.16081979498692535067e2 / (0.37978500000000000000e1 * t126 + 0.89690000000000000000e0 * t123 + 0.20477500000000000000e0 * t129 + 0.12323500000000000000e0 * t136))
t144 = 0.621814e-1 * (0.1e1 + 0.53425000000000000000e-1 * t123) * t142
t145 = t32 ** 2
t146 = t40 <= p_a_zeta_threshold
t147 = p_a_zeta_threshold ** (0.1e1 / 0.3e1)
t148 = t147 * p_a_zeta_threshold
t149 = jnp.where(t146, t148, t74)
t150 = t52 <= p_a_zeta_threshold
t151 = jnp.where(t150, t148, t77)
t152 = t149 + t151 - 0.2e1
t154 = 2 ** (0.1e1 / 0.3e1)
t157 = 0.1e1 / (0.2e1 * t154 - 0.2e1)
t168 = math.log(0.1e1 + 0.32163958997385070134e2 / (0.70594500000000000000e1 * t126 + 0.15494250000000000000e1 * t123 + 0.42077500000000000000e0 * t129 + 0.15629250000000000000e0 * t136))
t181 = math.log(0.1e1 + 0.29608749977793437516e2 / (0.51785000000000000000e1 * t126 + 0.90577500000000000000e0 * t123 + 0.11003250000000000000e0 * t129 + 0.12417750000000000000e0 * t136))
t182 = (0.1e1 + 0.27812500000000000000e-1 * t123) * t181
t184 = -0.3109070e-1 * (0.1e1 + 0.51370000000000000000e-1 * t123) * t168 + t144 - 0.19751673498613801407e-1 * t182
t186 = t145 * t152 * t157 * t184
t189 = 0.19751673498613801407e-1 * t152 * t157 * t182
t190 = math.log(0.2e1)
t191 = 0.1e1 - t190
t193 = t191 / t68
t194 = t147 ** 2
t195 = t73 ** 2
t196 = jnp.where(t146, t194, t195)
t197 = t76 ** 2
t198 = jnp.where(t150, t194, t197)
t200 = t196 / 0.2e1 + t198 / 0.2e1
t201 = t200 ** 2
t202 = t201 * t200
t205 = t59 / t60 / t9
t206 = 0.1e1 / t201
t209 = 0.1e1 / t117
t212 = math.exp(-t136 / 0.4e1)
t215 = t131 * t209 * t119 * (0.1e1 - t212)
t218 = 0.375e-1 + 0.83333333333333333332e-3 * t205 * t154 * t206 * t215
t219 = t205 * t154
t221 = t209 * t119
t225 = 0.1e1 / t191
t226 = t218 * t225
t232 = math.exp(-(-t144 + t186 + t189) * t225 * t68 / t202)
t235 = t68 / (t232 - 0.1e1)
t236 = t59 ** 2
t241 = t154 ** 2
t242 = 0.1e1 / t61 / t14 * t241
t243 = t201 ** 2
t246 = 0.1e1 / t132
t248 = t67 * t246 * t120
t252 = t219 * t206 * t131 * t221 / 0.96e2 + t226 * t235 * t236 * t242 / t243 * t248 / 0.3072e4
t254 = t225 * t68
t262 = math.log(0.1e1 + t218 * t252 * t254 / (t226 * t235 * t252 + 0.1e1))
t265 = t193 * t202 * t262 - t144 + t186 + t189
t268 = t118 * t120
t269 = t121 * t154
t271 = (0.1e1 / t40) ** (0.1e1 / 0.3e1)
t273 = t268 * t269 * t271
t276 = math.sqrt(t273)
t279 = t273 ** 0.15e1
t281 = t133 * t119
t282 = t134 * t241
t283 = t271 ** 2
t285 = t281 * t282 * t283
t291 = math.log(0.1e1 + 0.16081979498692535067e2 / (0.37978500000000000000e1 * t276 + 0.89690000000000000000e0 * t273 + 0.20477500000000000000e0 * t279 + 0.12323500000000000000e0 * t285))
t293 = 0.621814e-1 * (0.1e1 + 0.53425000000000000000e-1 * t273) * t291
t294 = 0.2e1 <= p_a_zeta_threshold
t296 = jnp.where(t294, t148, 0.2e1 * t154)
t297 = 0.0e0 <= p_a_zeta_threshold
t298 = jnp.where(t297, t148, 0)
t300 = (t296 + t298 - 0.2e1) * t157
t311 = math.log(0.1e1 + 0.32163958997385070134e2 / (0.70594500000000000000e1 * t276 + 0.15494250000000000000e1 * t273 + 0.42077500000000000000e0 * t279 + 0.15629250000000000000e0 * t285))
t324 = math.log(0.1e1 + 0.29608749977793437516e2 / (0.51785000000000000000e1 * t276 + 0.90577500000000000000e0 * t273 + 0.11003250000000000000e0 * t279 + 0.12417750000000000000e0 * t285))
t325 = (0.1e1 + 0.27812500000000000000e-1 * t273) * t324
t328 = t300 * (-0.3109070e-1 * (0.1e1 + 0.51370000000000000000e-1 * t273) * t311 + t293 - 0.19751673498613801407e-1 * t325)
t330 = 0.19751673498613801407e-1 * t300 * t325
t331 = jnp.where(t294, t194, t241)
t332 = jnp.where(t297, t194, 0)
t334 = t331 / 0.2e1 + t332 / 0.2e1
t335 = t334 ** 2
t336 = t335 * t334
t338 = 0.1e1 / t335 * t131
t339 = t39 * t338
t341 = t60 / t271
t343 = math.exp(-t285 / 0.4e1)
t349 = 0.375e-1 + 0.83333333333333333332e-3 * t339 * t221 * t341 * (0.1e1 - t343)
t353 = t349 * t225
t358 = t68 / t336
t360 = math.exp(-(-t293 + t328 + t330) * t225 * t358)
t362 = 0.1e1 / (t360 - 0.1e1)
t363 = s0 ** 2
t365 = t34 ** 2
t371 = t335 ** 2
t374 = 0.1e1 / t371 * t67 * t246
t375 = t120 * t61
t381 = t339 * t221 * t341 / 0.96e2 + t353 * t68 * t362 * t363 / t35 / t365 / r0 * t374 * t375 / t283 / 0.3072e4
t391 = math.log(0.1e1 + t349 * t381 * t254 / (t353 * t68 * t362 * t381 + 0.1e1))
t394 = t193 * t336 * t391 - t293 + t328 + t330
t396 = jnp.where(t265 < t394, t394, t265)
t399 = jnp.where(t115, t265 * t24 / 0.2e1, t396 * t40 / 0.2e1)
t401 = jnp.logical_or(r1 <= p_a_dens_threshold, t28)
t405 = (0.1e1 / t52) ** (0.1e1 / 0.3e1)
t407 = t268 * t269 * t405
t410 = math.sqrt(t407)
t413 = t407 ** 0.15e1
t415 = t405 ** 2
t417 = t281 * t282 * t415
t423 = math.log(0.1e1 + 0.16081979498692535067e2 / (0.37978500000000000000e1 * t410 + 0.89690000000000000000e0 * t407 + 0.20477500000000000000e0 * t413 + 0.12323500000000000000e0 * t417))
t425 = 0.621814e-1 * (0.1e1 + 0.53425000000000000000e-1 * t407) * t423
t436 = math.log(0.1e1 + 0.32163958997385070134e2 / (0.70594500000000000000e1 * t410 + 0.15494250000000000000e1 * t407 + 0.42077500000000000000e0 * t413 + 0.15629250000000000000e0 * t417))
t449 = math.log(0.1e1 + 0.29608749977793437516e2 / (0.51785000000000000000e1 * t410 + 0.90577500000000000000e0 * t407 + 0.11003250000000000000e0 * t413 + 0.12417750000000000000e0 * t417))
t450 = (0.1e1 + 0.27812500000000000000e-1 * t407) * t449
t453 = t300 * (-0.3109070e-1 * (0.1e1 + 0.51370000000000000000e-1 * t407) * t436 + t425 - 0.19751673498613801407e-1 * t450)
t455 = 0.19751673498613801407e-1 * t300 * t450
t456 = t51 * t338
t458 = t60 / t405
t460 = math.exp(-t417 / 0.4e1)
t466 = 0.375e-1 + 0.83333333333333333332e-3 * t456 * t221 * t458 * (0.1e1 - t460)
t470 = t466 * t225
t475 = math.exp(-(-t425 + t453 + t455) * t225 * t358)
t477 = 0.1e1 / (t475 - 0.1e1)
t478 = s2 ** 2
t480 = t46 ** 2
t491 = t456 * t221 * t458 / 0.96e2 + t470 * t68 * t477 * t478 / t47 / t480 / r1 * t374 * t375 / t415 / 0.3072e4
t501 = math.log(0.1e1 + t466 * t491 * t254 / (t470 * t68 * t477 * t491 + 0.1e1))
t504 = t193 * t336 * t501 - t425 + t453 + t455
t506 = jnp.where(t265 < t504, t504, t265)
t509 = jnp.where(t401, t265 * t27 / 0.2e1, t506 * t52 / 0.2e1)
t514 = t24 ** (0.1e1 / 0.3e1)
t516 = jnp.where(t25, t148, t514 * t24)
t517 = t27 ** (0.1e1 / 0.3e1)
t519 = jnp.where(t28, t148, t517 * t27)
t521 = (t516 + t519 - 0.2e1) * t157
t523 = t16 * t521 * t184
t525 = 0.19751673498613801407e-1 * t521 * t182
t526 = t514 ** 2
t527 = jnp.where(t25, t194, t526)
t528 = t517 ** 2
t529 = jnp.where(t28, t194, t528)
t531 = t527 / 0.2e1 + t529 / 0.2e1
t532 = t531 ** 2
t533 = t532 * t531
t534 = 0.1e1 / t532
t539 = 0.375e-1 + 0.83333333333333333332e-3 * t205 * t154 * t534 * t215
t544 = t539 * t225
t550 = math.exp(-(-t144 + t523 + t525) * t225 * t68 / t533)
t553 = t68 / (t550 - 0.1e1)
t556 = t532 ** 2
t562 = t219 * t534 * t131 * t221 / 0.96e2 + t544 * t553 * t236 * t242 / t556 * t248 / 0.3072e4
t571 = math.log(0.1e1 + t539 * t562 * t254 / (t544 * t553 * t562 + 0.1e1))
t576 = -(0.1e1 + t88) * t112 * (t399 + t509) + (t88 * t112 + 0.1e1) * (t193 * t533 * t571 - t144 + t523 + t525)
res = t576 * (0.1e1 + 0.45e1 * t576 * t112 * t111)
