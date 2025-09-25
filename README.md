# Quantum Experiments & Algorithms (Qiskit)

A personal collection of **quantum computing projects, tutorials, and experiments** implemented with [Qiskit](https://qiskit.org/).  
This repository serves as both a learning archive and a reference for key quantum algorithms, variational methods, and foundational concepts.

---

## Repository Structure

### `Algorithmes`
Core quantum algorithms and variational methods.

- **VQE_single_qubit_qiskit.ipynb**  
  Demonstrates the **Variational Quantum Eigensolver (VQE)** on a simple 1-qubit Hamiltonian.  
  Covers Pauli operator decomposition, TwoLocal ansatz, and hybrid classical-quantum optimization.

- **qaoa.ipynb**  
  Implements the **Quantum Approximate Optimization Algorithm (QAOA)** for solving a combinatorial problem (e.g., MaxCut).  
  Shows QUBO mapping, cost/mixer Hamiltonians, and optimizer performance.

---

### `ApplicationsVQE`
Applications of VQE to more realistic systems.

- **OHQ_VQE.ipynb**  
  Applies VQE to a molecular or oscillator Hamiltonian (example of higher-dimensional or chemical use cases).  
  Includes Hamiltonian construction, variational ansatz, and convergence analysis.

---

### `Bell_states`
Illustrates entanglement and state preparation.

- **bell_states.ipynb**  
  Prepares and measures **Bell states**.  
  Demonstrates entanglement creation, measurement statistics, and quantum correlations.

---

### `CHSh-game`
Quantum nonlocality and the CHSH inequality.

- **CHSh-gamme.ipynb**  
  Simulates the **CHSH game**, showing violation of classical bounds with entangled states.  
  Useful for understanding Bell’s theorem and quantum advantage in nonlocal games.

---

### `Circuit`
Basic and intermediate quantum circuit demonstrations.

- May include:  
  - Circuit creation and visualization  
  - Quantum measurement techniques  
  - Multi-qubit gates and custom subroutines

---

### `Quantum Computing with Qiskit`
Tutorial-style notebooks.

- **Qiskit_Tutorial.ipynb**  
  Introductory walkthrough of Qiskit: from qubit basics and gates to measurement and simulation.

---

### `QuantumSimLab`
Advanced simulations and numerical experiments.

- `notebooks/`  
  - **schrodinger.ipynb** – Solves the time-dependent Schrödinger equation on a discretized grid.  
- `scripts/`  
  - **quantum_circuits.py** – Helper functions to build reusable circuits.  
  - **schrodinger_solver.py** – Numerical solver implementation.  
  - **wavepacket_sim.py** – Gaussian wave packet evolution and visualization.

---
### `Qiskit v2.x Certification`
 - Note for Qiskit Advocates
 - This repository is designed to help Qiskit Advocates and community members
 - prepare for the **Qiskit v2.x Certification**.  
 - It is **not** affiliated with IBM or the official Qiskit certification team.

##  Getting Started

1. **Clone the repository**
   ```bash
   git clone https://github.com/HichanBen/Quantum.git
   cd Quantum
