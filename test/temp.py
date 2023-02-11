from decimal import Decimal
from decimal import ROUND_HALF_UP
a = [1.4, 0.5, 2.5]

for i in a:
	print(round(i + 0.00001))

print("-" * 20)
for i in a:
	print(Decimal(i).quantize(Decimal("0"), ROUND_HALF_UP))