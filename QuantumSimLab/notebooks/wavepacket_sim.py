import numpy as np
from scipy.sparse import diags
from scipy.sparse.linalg import splu

class WavePacket1D:
    def __init__(self, x, dt=0.01, V=None):
        self.x = x
        self.N = len(x)
        self.dx = x[1] - x[0]
        self.dt = dt
        self.hbar = 1
        self.m = 1
        self.V = V if V is not None else np.zeros(self.N)
        self.psi = None
        self.alpha = 1j*self.hbar*self.dt/(2*self.m*self.dx**2)
        self._build_matrices()
        
    def _build_matrices(self):
        N = self.N
        alpha = self.alpha
        main_diag = (1 + 2*alpha + 1j*self.dt*self.V/(2*self.hbar))*np.ones(N)
        off_diag = -alpha*np.ones(N-1)
        self.A = diags([off_diag, main_diag, off_diag], [-1,0,1], format='csc')
        self.B = diags([-off_diag, 2 - main_diag, -off_diag], [-1,0,1], format='csc')
        self.lu = splu(self.A)
        
    def set_initial_wavepacket(self, x0=-5, k0=5, sigma=0.5):
        psi = (1/(sigma*np.sqrt(np.pi)))**0.5 * np.exp(-(self.x-x0)**2/(2*sigma**2)) * np.exp(1j*k0*self.x)
        psi /= np.sqrt(np.sum(np.abs(psi)**2)*self.dx)
        self.psi = psi
        
    def step(self):
        b = self.B @ self.psi
        self.psi = self.lu.solve(b)
        return self.psi

