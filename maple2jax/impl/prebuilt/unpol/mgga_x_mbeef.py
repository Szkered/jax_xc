t3 = 3 ** (0.1e1 / 0.3e1)
t4 = math.pi ** (0.1e1 / 0.3e1)
t7 = 0.1e1 <= p_a_zeta_threshold
t8 = p_a_zeta_threshold - 0.1e1
t10 = jnp.where(t7, -t8, 0)
t11 = jnp.where(t7, t8, t10)
t12 = t11 + 0.1e1
t14 = p_a_zeta_threshold ** (0.1e1 / 0.3e1)
t16 = t12 ** (0.1e1 / 0.3e1)
t18 = jnp.where(t12 <= p_a_zeta_threshold, t14 * p_a_zeta_threshold, t16 * t12)
t19 = r0 ** (0.1e1 / 0.3e1)
t21 = 6 ** (0.1e1 / 0.3e1)
t22 = math.pi ** 2
t23 = t22 ** (0.1e1 / 0.3e1)
t24 = t23 ** 2
t25 = 0.1e1 / t24
t26 = t21 * t25
t28 = 2 ** (0.1e1 / 0.3e1)
t29 = t28 ** 2
t30 = r0 ** 2
t31 = t19 ** 2
t33 = 0.1e1 / t31 / t30
t36 = s0 * t29 * t33
t42 = t26 * s0 * t29 * t33 / (0.65124e1 + t26 * t36 / 0.24e2)
t44 = t42 / 0.12e2 - 0.1e1
t45 = t44 ** 2
t47 = t45 ** 2
t48 = t47 * t45
t59 = 0.5e1 / 0.9e1 * (tau0 * t29 / t31 / r0 - t36 / 0.8e1) * t21 * t25
t61 = 0.1e5 < t59
t62 = jnp.where(t61, t59, 0.1e5)
t63 = t62 ** 2
t68 = t63 ** 2
t72 = jnp.where(t61, 0.1e5, t59)
t73 = t72 ** 2
t74 = 0.1e1 - t73
t75 = t74 ** 2
t77 = t73 * t72
t83 = jnp.where(0.1e5 <= t59, 0.1e1 - 0.3e1 / t63 - 0.1e1 / t63 / t62 + 0.3e1 / t68, -t75 * t74 / (0.1e1 + t77 * (0.1e1 + t77)))
t84 = t83 ** 2
t85 = t84 ** 2
t86 = t85 * t84
t91 = t85 * t83
t93 = t84 * t83
t95 = t85 * t93
t97 = t45 * t44
t99 = t47 * t44
t101 = t47 * t97
t106 = 0.63e2 / 0.8e1 * t91 - 0.35e2 / 0.4e1 * t93 + 0.15e2 / 0.8e1 * t83
t110 = -0.1e1 / 0.2e1 + 0.3e1 / 0.2e1 * t45
t112 = -0.1e1 / 0.2e1 + 0.3e1 / 0.2e1 * t84
t117 = 0.5e1 / 0.2e1 * t93 - 0.3e1 / 0.2e1 * t83
t120 = -0.92294814328125000000e-1 * t45 + 0.80024660533125000000e-1 * t48 - 0.13805618397812500000e0 * t47 - 0.80008813355625000000e-4 * t86 + 0.30207156698031250000e-2 * t85 + 0.70318268775656250000e-2 * t84 - 0.43736526393718750000e-2 * t83 - 0.94588310356312500000e-3 * t91 + 0.46461028218468750000e-2 * t93 + 0.19735677658125000000e-4 * t95 + 0.49794463840937500000e0 * t97 - 0.39506119958812500000e0 * t99 + 0.10602581552062500000e0 * t101 + 0.822139896e-3 * t44 * t106 - 0.150103636e-1 * t110 * t112 + 0.293253041e-2 * t110 * t117
t123 = 0.3e1 / 0.8e1 + 0.35e2 / 0.8e1 * t85 - 0.15e2 / 0.4e1 * t84
t131 = -0.5e1 / 0.16e2 + 0.231e3 / 0.16e2 * t86 - 0.315e3 / 0.16e2 * t85 + 0.105e3 / 0.16e2 * t84
t138 = 0.429e3 / 0.16e2 * t95 - 0.693e3 / 0.16e2 * t91 + 0.315e3 / 0.16e2 * t93 - 0.35e2 / 0.16e2 * t83
t143 = 0.5e1 / 0.2e1 * t97 - t42 / 0.8e1 + 0.3e1 / 0.2e1
t162 = 0.3e1 / 0.8e1 + 0.35e2 / 0.8e1 * t47 - 0.15e2 / 0.4e1 * t45
t171 = 0.182906057e-2 * t110 * t123 - 0.351041030e-3 * t110 * t106 + 0.668980219e-8 * t110 * t131 - 0.223014657e-8 * t110 * t138 - 0.182177954e-1 * t143 * t83 + 0.280678872e-1 * t143 * t112 - 0.845508103e-2 * t143 * t117 + 0.339308972e-2 * t143 * t123 + 0.100339208e0 * t44 * t83 - 0.879090772e-2 * t44 * t112 - 0.303347141e-2 * t44 * t117 + 0.119130546e-2 * t44 * t123 + 0.912223751e-8 * t162 * t131 + 0.209603871e-7 * t162 * t106 + 0.631891628e-2 * t162 * t117 - 0.790811707e-7 * t162 * t123
t192 = -0.5e1 / 0.16e2 + 0.231e3 / 0.16e2 * t48 - 0.315e3 / 0.16e2 * t47 + 0.105e3 / 0.16e2 * t45
t198 = 0.63e2 / 0.8e1 * t99 - 0.35e2 / 0.4e1 * t97 + 0.5e1 / 0.32e2 * t42 - 0.15e2 / 0.8e1
t213 = -0.182911291e-1 * t162 * t112 + 0.162638575e-1 * t162 * t83 - 0.216860568e-7 * t143 * t131 + 0.674910119e-8 * t143 * t138 + 0.896739466e-3 * t143 * t106 - 0.514204676e-4 * t44 * t131 - 0.940351563e-5 * t44 * t138 - 0.434643460e-1 * t110 * t83 - 0.957417512e-2 * t192 * t83 + 0.850272392e-8 * t198 * t138 - 0.376702959e-7 * t198 * t106 - 0.138472194e-7 * t198 * t131 + 0.162238741e-6 * t198 * t123 - 0.896771404e-2 * t198 * t117 - 0.188495102e-1 * t198 * t112 - 0.884148272e-2 * t198 * t83
t220 = 0.429e3 / 0.16e2 * t101 - 0.693e3 / 0.16e2 * t99 + 0.315e3 / 0.16e2 * t97 - 0.35e2 / 0.192e3 * t42 + 0.35e2 / 0.16e2
t248 = 0.13805672252189968750e1 - 0.493824365e-8 * t162 * t138 - 0.276524680e-6 * t220 * t112 + 0.940675747e-2 * t220 * t83 - 0.691592964e-8 * t192 * t138 + 0.694482484e-8 * t192 * t131 + 0.236391411e-7 * t192 * t106 - 0.416393106e-7 * t192 * t123 + 0.169805915e-6 * t192 * t112 - 0.265114646e-7 * t192 * t117 + 0.888525527e-8 * t220 * t138 - 0.338128188e-7 * t220 * t106 - 0.774224962e-8 * t220 * t131 + 0.554588743e-7 * t220 * t123 + 0.505920757e-7 * t220 * t117 - 0.13022208355989583333e-1 * t42
t254 = jnp.where(r0 / 0.2e1 <= p_a_dens_threshold, 0, -0.3e1 / 0.8e1 * t3 / t4 * t18 * t19 * (t120 + t171 + t213 + t248))
res = 0.2e1 * t254
