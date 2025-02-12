# 方式1
import shape.circle
print(shape.circle.radius)

# 方式2
import shape.circle as sc
print(sc.radius)

# 方式3
from shape import circle
print(circle.radius)

# 方式4
from shape import circle as sc
print(sc.radius)