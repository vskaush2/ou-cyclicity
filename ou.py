import numpy as np
import pandas as pd
import scipy as sc

class OU:
    def __init__(self, B, Sigma):
        if isinstance(B, np.ndarray) == False:
            raise ValueError("B must be a numpy array")
        if isinstance(Sigma, np.ndarray) == False:
            raise ValueError("Sigma must be a numpy array")
        if Sigma.ndim !=2:
            raise ValueError("Sigma must be a 2-dimensional array")
        if B.shape[0] != B.shape[1]:
            raise ValueError("B must be a square matrix")
        if B.shape[1] != Sigma.shape[0]:
            raise ValueError("The number of columns of B must be equal to the number of rows of Sigma.")
        if np.min(np.real(np.linalg.eig(B)[0])) <= 0:
            raise ValueError("-B must be a stable matrix.")

        self.N = B.shape[0]
        self.M = Sigma.shape[1]
        self.B = B
        self.Sigma = Sigma
        self.D = self.compute_diffusion_matrix()
        self.S = self.compute_stationary_covariance_matrix()
        self.Q = self.compute_lead_matrix()

    def compute_diffusion_matrix(self):
        D = self.Sigma @ self.Sigma.T/2
        return D

    def compute_stationary_covariance_matrix(self):
        S = sc.linalg.solve_continuous_lyapunov(self.B, 2*self.D)
        return S

    def compute_lead_matrix(self):
        A = self.B @self.S
        Q= (A-A.T)/2
        return Q

    def simulate_trajectory_df(self, x0 = None, K=100000, Delta=0.01):
        if x0 is None:
            x0 = np.random.multivariate_normal(np.zeros(self.N), self.S)

        X = np.zeros((K, self.N))
        Xi = np.random.multivariate_normal(np.zeros(self.M), np.eye(self.M), K)
        X[0] = x0.T
        for k in range(1, K):
            prev_x = X[k-1].T
            prev_xi = Xi[k-1].T
            new_x = prev_x - self.B @ prev_x * Delta + np.sqrt(Delta) * self.Sigma @  prev_xi
            X[k] = new_x.T
        trajectory_df = pd.DataFrame(X, columns=[f"{i+1}" for i in range(self.N)])
        trajectory_df.index = np.arange(K)*Delta
        trajectory_df.index.name = r"Time ($t$)"
        return trajectory_df

