"""utilities for testing."""

import numpy as np
import jax.numpy as jnp
import scipy.special

_r50 = np.arange(50)
perm_2n_n = scipy.special.perm(2 * _r50, _r50)


def gto(center, exponent, angular):
  """Gaussian type orbital.
  Args:
    center: shape = (3,)
    exponent: shape = (,)
    angular: shape = (3,)
  Returns:
    gaussian type wave function
  """
  normalization = (2 * exponent / np.pi)**(3 / 4) * jnp.sqrt(
    (8 * exponent)**(jnp.sum(angular)) / jnp.prod(perm_2n_n[angular])
  )

  def _gto(r):
    r = r - center
    xyz = jnp.prod(jnp.power(r, angular))
    return xyz * jnp.exp(-exponent * jnp.linalg.norm(r)**2) * normalization

  return _gto
