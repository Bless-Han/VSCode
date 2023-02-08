from decimal import Decimal
from decimal import ROUND_HALF_UP

print(Decimal(0.5).quantize(Decimal("0"), ROUND_HALF_UP))
print(Decimal(0.145).quantize(Decimal("0.00"), ROUND_HALF_UP))