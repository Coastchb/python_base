from matplotlib import pyplot as plt
import numpy as np

# Generating a Gaussion dTset:
# Creating random vectors from the multivaritate normal distribution
# givem mean and covariance

mu_vecl = np.array([0, 0])
cov_matl = np.array([[2, 0], [0, 2]])

x1_samples = np.random.multivariate_normal(mu_vecl, cov_matl, 100)
x2_samples = np.random.multivariate_normal(mu_vecl + 0.2, cov_matl + 0.2, 100)
x3_samples = np.random.multivariate_normal(mu_vecl + 0.4, cov_matl + 0.4, 100)

plt.figure(figsize=(8, 6))

plt.scatter(x1_samples[:, 0], x1_samples[:, 1], marker='x',
            color='blue', alpha=0.7, label='x1 samples')
plt.scatter(x2_samples[:, 0], x1_samples[:, 1], marker='o',
            color='green', alpha=0.7, label='x2 samples')
plt.scatter(x3_samples[:, 0], x1_samples[:, 1], marker='^',
            color='red', alpha=0.7, label='x3 samples')
plt.title('Basic scatter plot')
plt.ylabel('variable X')
plt.xlabel('Variable Y')
plt.legend(loc='upper right')

plt.show()
