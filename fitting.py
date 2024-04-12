import numpy as np
# how we tested all that 
# or fitting...
# Suppose we have the following sample of values
values = [0.007, 0.008, 0.009, 0.015, 0.007, 0.009, 0.007, 0.007]


# The average of values (mean)
mean_sample = np.mean(values)

#  (std_dev) 
std_dev_sample = np.std(values, ddof=1)

# size
size_sample = len(values)

# The estimated average value of the general population (mu)
mu_population = 0.007  # The real data

# Calculating the t-statistics (t_score)
t_score = (mean_sample - mu_population) / (std_dev_sample / np.sqrt(size_sample))

# print t-statistics
print('t = ' +str(t_score))


e = 72*(10**9) # Young's coefficient from GOST(russian standart sistem) for optical fiber
s = 3.14159265358979 *(125*10**-6)**2 # the cross-sectional area of the fiber

l = 0.1 # lenth

k = s*e/l
print('k = ' +str(k))
ld = 0.007 #fiber extension
f = k*ld
print('f = ' +str(f))
f = e*s*ld/l
print('f = ' +str(f))
p = f/s
print('p = ' +str(p))