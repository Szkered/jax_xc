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
t20 = t19 + 0.1e1
t22 = p_a_zeta_threshold ** (0.1e1 / 0.3e1)
t23 = t22 * p_a_zeta_threshold
t24 = t20 ** (0.1e1 / 0.3e1)
t26 = jnp.where(t20 <= p_a_zeta_threshold, t23, t24 * t20)
t27 = t6 ** (0.1e1 / 0.3e1)
t29 = 6 ** (0.1e1 / 0.3e1)
t30 = math.pi ** 2
t31 = t30 ** (0.1e1 / 0.3e1)
t32 = t31 ** 2
t34 = t29 / t32
t35 = r0 ** 2
t36 = r0 ** (0.1e1 / 0.3e1)
t37 = t36 ** 2
t38 = t37 * t35
t42 = t34 * s0 / t38 / 0.24e2
t43 = 0.0e0 < t42
t44 = jnp.where(t43, t42, 0)
t45 = t44 ** (0.1e1 / 0.4e1)
t48 = math.exp(-params_a_task_c / t45)
t50 = jnp.where(t43, 0.1e1 - t48, 0)
t52 = params_a_task_bnu[0]
t53 = t35 ** 2
t55 = t37 * t53 * t35
t58 = t53 * r0
t60 = r0 * tau0
t63 = 0.1e1 / r0
t65 = 0.1e1 / tau0
t74 = jnp.where(0.0e0 < 0.12500000000000000000e0 * (0.79999999992000000000e1 * t60 - s0) * t63 * t65, (0.8e1 * t60 - s0) * t63 * t65 / 0.8e1, 0.1e-9)
t75 = t74 * tau0
t79 = t36 * t35 * r0
t81 = t74 ** 2
t82 = tau0 ** 2
t83 = t81 * t82
t86 = t37 * r0
t90 = t81 * t74 * t82 * tau0
t93 = t81 ** 2
t95 = t82 ** 2
t98 = params_a_task_bnu[1]
t110 = params_a_task_bnu[2]
t119 = 0.47049607861172565388e8 * t52 * t55 + 0.41291508340807648886e8 * t52 * t58 * t75 + 0.13589289623490307943e8 * t52 * t79 * t83 + 0.19876972814512516632e7 * t52 * t86 * t90 + 0.10902723556992837954e6 * t52 * t93 * t95 - 0.47049607861172565388e8 * t98 * t55 - 0.20645754170403824442e8 * t98 * t58 * t75 + 0.99384864072562583159e6 * t98 * t86 * t90 + 0.10902723556992837954e6 * t98 * t93 * t95 + 0.47049607861172565386e8 * t110 * t55 - 0.41291508340807648885e8 * t110 * t58 * t75 - 0.22648816039150513236e8 * t110 * t79 * t83
t126 = params_a_task_bnu[3]
t141 = params_a_task_bnu[4]
t156 = -0.19876972814512516631e7 * t110 * t86 * t90 + 0.10902723556992837954e6 * t110 * t93 * t95 - 0.47049607861172565384e8 * t126 * t55 + 0.14452027919282677111e9 * t126 * t58 * t75 + 0.1e-11 * t126 * t79 * t83 - 0.69569404850793808212e7 * t126 * t86 * t90 + 0.10902723556992837955e6 * t126 * t93 * t95 + 0.4704960786117256539e8 * t141 * t55 - 0.28904055838565354220e9 * t141 * t58 * t75 + 0.15854171227405359266e9 * t141 * t79 * t83 - 0.13913880970158761643e8 * t141 * t86 * t90 + 0.10902723556992837954e6 * t141 * t93 * t95
t161 = (0.82820720060468819300e2 * t86 + 0.18171205928321396589e2 * t75) ** 2
t162 = t161 ** 2
t167 = t3 ** 2
t168 = t167 * t30
t169 = t36 * t58 * t168
t170 = params_a_task_anu[0]
t173 = params_a_task_anu[1]
t176 = params_a_task_anu[2]
t179 = t38 * t29
t180 = t3 * math.pi
t181 = t180 * s0
t188 = t29 ** 2
t189 = s0 ** 2
t190 = t188 * t189
t199 = (t29 * s0 + 0.24e2 * t180 * t38) ** 2
t204 = t50 ** params_a_task_d
t210 = jnp.where(r0 <= p_a_dens_threshold, 0, -0.3e1 / 0.8e1 * t5 * t26 * t27 * (params_a_task_h0x * t50 + (0.10e1 - (t119 + t156) / t162) * ((0.48e2 * t179 * t181 * t170 - 0.144e3 * t179 * t181 * t176 + 0.576e3 * t169 * t170 - 0.576e3 * t169 * t173 + 0.576e3 * t169 * t176 + t190 * t170 + t190 * t173 + t190 * t176) / t199 - params_a_task_h0x) * t204))
t212 = jnp.where(t10, t15, -t17)
t213 = jnp.where(t14, t11, t212)
t214 = t213 + 0.1e1
t216 = t214 ** (0.1e1 / 0.3e1)
t218 = jnp.where(t214 <= p_a_zeta_threshold, t23, t216 * t214)
t220 = r1 ** 2
t221 = r1 ** (0.1e1 / 0.3e1)
t222 = t221 ** 2
t223 = t222 * t220
t227 = t34 * s2 / t223 / 0.24e2
t228 = 0.0e0 < t227
t229 = jnp.where(t228, t227, 0)
t230 = t229 ** (0.1e1 / 0.4e1)
t233 = math.exp(-params_a_task_c / t230)
t235 = jnp.where(t228, 0.1e1 - t233, 0)
t237 = t220 ** 2
t239 = t222 * t237 * t220
t242 = t237 * r1
t244 = r1 * tau1
t247 = 0.1e1 / r1
t249 = 0.1e1 / tau1
t258 = jnp.where(0.0e0 < 0.12500000000000000000e0 * (0.79999999992000000000e1 * t244 - s2) * t247 * t249, (0.8e1 * t244 - s2) * t247 * t249 / 0.8e1, 0.1e-9)
t259 = tau1 * t258
t263 = t221 * t220 * r1
t265 = tau1 ** 2
t266 = t258 ** 2
t267 = t265 * t266
t270 = t222 * r1
t274 = t265 * tau1 * t266 * t258
t277 = t265 ** 2
t279 = t266 ** 2
t301 = 0.47049607861172565388e8 * t52 * t239 + 0.41291508340807648886e8 * t52 * t242 * t259 + 0.13589289623490307943e8 * t52 * t263 * t267 + 0.19876972814512516632e7 * t52 * t270 * t274 + 0.10902723556992837954e6 * t52 * t277 * t279 - 0.47049607861172565388e8 * t98 * t239 - 0.20645754170403824442e8 * t98 * t242 * t259 + 0.99384864072562583159e6 * t98 * t270 * t274 + 0.10902723556992837954e6 * t98 * t277 * t279 + 0.47049607861172565386e8 * t110 * t239 - 0.41291508340807648885e8 * t110 * t242 * t259 - 0.22648816039150513236e8 * t110 * t263 * t267
t336 = -0.19876972814512516631e7 * t110 * t270 * t274 + 0.10902723556992837954e6 * t110 * t277 * t279 - 0.47049607861172565384e8 * t126 * t239 + 0.14452027919282677111e9 * t126 * t242 * t259 + 0.1e-11 * t126 * t263 * t267 - 0.69569404850793808212e7 * t126 * t270 * t274 + 0.10902723556992837955e6 * t126 * t277 * t279 + 0.4704960786117256539e8 * t141 * t239 - 0.28904055838565354220e9 * t141 * t242 * t259 + 0.15854171227405359266e9 * t141 * t263 * t267 - 0.13913880970158761643e8 * t141 * t270 * t274 + 0.10902723556992837954e6 * t141 * t277 * t279
t341 = (0.82820720060468819300e2 * t270 + 0.18171205928321396589e2 * t259) ** 2
t342 = t341 ** 2
t347 = t221 * t242 * t168
t354 = t223 * t29
t355 = t180 * s2
t362 = s2 ** 2
t363 = t188 * t362
t372 = (t29 * s2 + 0.24e2 * t180 * t223) ** 2
t377 = t235 ** params_a_task_d
t383 = jnp.where(r1 <= p_a_dens_threshold, 0, -0.3e1 / 0.8e1 * t5 * t218 * t27 * (params_a_task_h0x * t235 + (0.10e1 - (t301 + t336) / t342) * ((0.48e2 * t354 * t355 * t170 - 0.144e3 * t354 * t355 * t176 + 0.576e3 * t347 * t170 + t363 * t170 - 0.576e3 * t347 * t173 + t363 * t173 + 0.576e3 * t347 * t176 + t363 * t176) / t372 - params_a_task_h0x) * t377))
res = t210 + t383
