import numpy as np
from scipy.linalg import eigh

def solve_schrodinger_1D(V, x, hbar=1, m=1):
    dx = x[1] - x[0]
    N = len(x)
    
    # Kinetic energy (finite difference)
    T = np.zeros((N,N))
    for i in range(N):
        if i > 0: T[i,i-1] = -1
        T[i,i] = 2
        if i < N-1: T[i,i+1] = -1
    T *= -(hbar**2)/(2*m*dx**2)
    
    # Hamiltonian
    H = T + np.diag(V)
    
    # Eigenvalues and eigenvectors
    energies, wavefunctions = eigh(H)
    for n in range(min(3,N)):
        wavefunctions[:,n] /= np.sqrt(np.sum(np.abs(wavefunctions[:,n])**2)*dx)
    return energies, wavefunctions
