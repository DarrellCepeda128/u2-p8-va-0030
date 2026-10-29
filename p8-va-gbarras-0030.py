# Cepeda Darrell NC = 0030      Fecha 29/10/2026
import numpy as np
import matplotlib.pyplot as plt

diasX=["Lun", "Mar", "Mie", "Jue", "Vie"]
califa_va_y=[5,6,3,8,10]
plt.bar(diasX,califa_va_y)
plt.title("Califas en VA de Cepeda Darrell 0030")
plt.xlabel("dias semana habil")
plt.ylabel("Califaciones en VA")
plt.grid()
plt.show()
