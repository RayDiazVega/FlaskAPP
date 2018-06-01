#import matplotlib as mpl
#mpl.use('WebAgg')
import matplotlib.pyplot as plt
from matplotlib import style
import matplotlib.animation as animation
from metodos import Newton, Punto, Euler
tabla, men = Euler().resultado()
#print("\nf'(x)=",df)
print(tabla,men)
plt.show()