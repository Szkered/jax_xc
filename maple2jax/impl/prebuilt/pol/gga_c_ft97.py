t1 = math.log(0.2e1)
t2 = 0.1e1 - t1
t3 = math.pi ** 2
t5 = t2 / t3
t6 = 3 ** (0.1e1 / 0.3e1)
t7 = 0.1e1 / math.pi
t8 = t7 ** (0.1e1 / 0.3e1)
t9 = t6 * t8
t10 = t5 * t9
t11 = 4 ** (0.1e1 / 0.3e1)
t12 = t11 ** 2
t13 = r0 + r1
t14 = t13 ** (0.1e1 / 0.3e1)
t15 = 0.1e1 / t14
t16 = t12 * t15
t17 = 2 ** (0.1e1 / 0.3e1)
t20 = (r0 - r1) / t13
t21 = 0.1e1 + t20
t23 = (0.1e1 / t21) ** (0.1e1 / 0.3e1)
t24 = t17 * t23
t25 = 4 ** (0.1e1 / 0.5e1)
t26 = t9 * t12
t27 = t15 * t17
t28 = t27 * t23
t29 = t26 * t28
t30 = t29 ** (0.1e1 / 0.5e1)
t31 = t30 ** 2
t32 = t31 ** 2
t35 = math.exp(-0.20818970000000000000e-1 * t25 * t32)
t38 = (0.942486901e0 + 0.349064173e0 * t35) ** 2
t39 = t6 ** 2
t40 = t8 ** 2
t41 = t39 * t40
t43 = r0 ** 2
t44 = r0 ** (0.1e1 / 0.3e1)
t45 = t44 ** 2
t47 = 0.1e1 / t45 / t43
t52 = t6 * t8 * t7
t53 = s0 ** 2
t55 = t43 ** 2
t60 = t52 * t12 * t53 / t44 / t55 / r0
t61 = 0.55569193573523559258e-3 * t60
t63 = (0.1e1 + 0.45058854638888888889e-1 * t41 * t11 * s0 * t47 + t61) ** 2
t65 = math.exp(-t61)
t66 = t65 ** 2
t70 = t17 ** 2
t74 = t9 * t12 * s0 * t47 * t14 * t70 / t23
t79 = t38 * t63 * t66 / (0.1e1 + 0.19153082513888888889e-1 * t74)
t81 = jnp.where(0.1e-59 < t79, t79, 0.1e-59)
t82 = 0.1e1 / t81
t85 = t10 * t16 * t24 * t82
t86 = t85 / 0.6e1
t88 = xc_E1_scaled(t86)
t89 = t5 * t26
t90 = math.sqrt(0.6e1)
t91 = t90 * t7
t94 = t2 * t6 * t8 * t12
t98 = math.sqrt(t94 * t27 * t23 * t82)
t99 = t91 * t98
t102 = 0.3e1 + t99 / 0.3e1 + t85 / 0.3e1
t105 = 0.1e1 / (0.3e1 + t99 + t85)
t115 = 0.1e1 - t20
t119 = jnp.where(0.10e8 <= t86, 0, t5 * (-t88 * (0.1e1 + t89 * t28 * t82 * t102 * t105 / 0.3e1) + 0.2e1 * t102 * t105) * t115 / 0.4e1)
t120 = math.sqrt(t29)
t122 = math.exp(-0.54466942400000000000e0 * t120)
t124 = t25 ** 2
t125 = t124 * t25
t128 = math.exp(-0.16390970575000000000e0 * t125 * t31)
t131 = (0.1247511874e1 - 0.859614445e0 * t122 + 0.812904345e0 * t128) ** 2
t132 = 0.56633563016285904186e-1 * t60
t134 = (0.1e1 + t132) ** 2
t136 = math.exp(-t132)
t137 = t136 ** 2
t142 = t131 * t134 * t137 / (0.1e1 + 0.50008500819444444447e-1 * t74)
t144 = jnp.where(0.1e-59 < t142, t142, 0.1e-59)
t145 = 0.1e1 / t144
t148 = t10 * t16 * t24 * t145
t149 = t148 / 0.6e1
t151 = xc_E1_scaled(t149)
t155 = math.sqrt(t94 * t27 * t23 * t145)
t156 = t91 * t155
t159 = 0.3e1 + t156 / 0.3e1 + t148 / 0.3e1
t162 = 0.1e1 / (0.3e1 + t156 + t148)
t172 = t41 * t11
t173 = t14 ** 2
t175 = 0.1e1 / t173 * t70
t176 = t23 ** 2
t180 = (0.46950800000000000000e0 * t120 + 0.43329250000000000000e0 * t29) ** 2
t186 = math.exp(-t172 * t175 * t176 / t180 / 0.4e1)
t191 = jnp.where(0.10e8 <= t149, 0, t5 * (-t151 * (0.1e1 + t89 * t28 * t145 * t159 * t162 / 0.3e1) + 0.2e1 * t159 * t162) * t186 * t21 / 0.4e1)
t193 = (0.1e1 / t115) ** (0.1e1 / 0.3e1)
t194 = t17 * t193
t195 = t27 * t193
t196 = t26 * t195
t197 = t196 ** (0.1e1 / 0.5e1)
t198 = t197 ** 2
t199 = t198 ** 2
t202 = math.exp(-0.20818970000000000000e-1 * t25 * t199)
t205 = (0.942486901e0 + 0.349064173e0 * t202) ** 2
t207 = r1 ** 2
t208 = r1 ** (0.1e1 / 0.3e1)
t209 = t208 ** 2
t211 = 0.1e1 / t209 / t207
t215 = s2 ** 2
t217 = t207 ** 2
t222 = t52 * t12 * t215 / t208 / t217 / r1
t223 = 0.55569193573523559258e-3 * t222
t225 = (0.1e1 + 0.45058854638888888889e-1 * t41 * t11 * s2 * t211 + t223) ** 2
t227 = math.exp(-t223)
t228 = t227 ** 2
t235 = t9 * t12 * s2 * t211 * t14 * t70 / t193
t240 = t205 * t225 * t228 / (0.1e1 + 0.19153082513888888889e-1 * t235)
t242 = jnp.where(0.1e-59 < t240, t240, 0.1e-59)
t243 = 0.1e1 / t242
t246 = t10 * t16 * t194 * t243
t247 = t246 / 0.6e1
t249 = xc_E1_scaled(t247)
t253 = math.sqrt(t94 * t27 * t193 * t243)
t254 = t91 * t253
t257 = 0.3e1 + t254 / 0.3e1 + t246 / 0.3e1
t260 = 0.1e1 / (0.3e1 + t254 + t246)
t273 = jnp.where(0.10e8 <= t247, 0, t5 * (-t249 * (0.1e1 + t89 * t195 * t243 * t257 * t260 / 0.3e1) + 0.2e1 * t257 * t260) * t21 / 0.4e1)
t274 = math.sqrt(t196)
t276 = math.exp(-0.54466942400000000000e0 * t274)
t280 = math.exp(-0.16390970575000000000e0 * t125 * t198)
t283 = (0.1247511874e1 - 0.859614445e0 * t276 + 0.812904345e0 * t280) ** 2
t284 = 0.56633563016285904186e-1 * t222
t286 = (0.1e1 + t284) ** 2
t288 = math.exp(-t284)
t289 = t288 ** 2
t294 = t283 * t286 * t289 / (0.1e1 + 0.50008500819444444447e-1 * t235)
t296 = jnp.where(0.1e-59 < t294, t294, 0.1e-59)
t297 = 0.1e1 / t296
t300 = t10 * t16 * t194 * t297
t301 = t300 / 0.6e1
t303 = xc_E1_scaled(t301)
t307 = math.sqrt(t94 * t27 * t193 * t297)
t308 = t91 * t307
t311 = 0.3e1 + t308 / 0.3e1 + t300 / 0.3e1
t314 = 0.1e1 / (0.3e1 + t308 + t300)
t324 = t193 ** 2
t328 = (0.46950800000000000000e0 * t274 + 0.43329250000000000000e0 * t196) ** 2
t334 = math.exp(-t172 * t175 * t324 / t328 / 0.4e1)
t339 = jnp.where(0.10e8 <= t301, 0, t5 * (-t303 * (0.1e1 + t89 * t195 * t297 * t311 * t314 / 0.3e1) + 0.2e1 * t311 * t314) * t334 * t115 / 0.4e1)
res = t119 + t191 + t273 + t339
