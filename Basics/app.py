# One of the ways to use packages
import ecommerce.shipping
ecommerce.shipping.calc_shipping()

# Another way to use packages
from ecommerce.shipping import calc_shipping
calc_shipping()

# Another way to use packages
import ecommerce.shipping as shipping
shipping.calc_shipping() 