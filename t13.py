import numpy as np

lst = []
line = np.genfromtxt('/Users/sourabhjoshi/Desktop/Learning/projects/hycdx_option_quotes_1.txt',  
    dtype=[('floatname', 'float')], skip_header=1)
lst.append(line)

print(lst)