import matplotlib.pyplot as pp
import numpy as np

grey_hounds= 500
labs= 500

grey_height= 28 + 4* np.random.randn(grey_hounds)
labs_height= 24 + 4* np.random.randn(labs)

pp.hist([grey_height,labs_height], stacked= True, color=['r','b'])
pp.show()