from qiskit import QuantumCircuit, Aer, transpile, execute
from qiskit.visualization import plot_histogram

def bell_state_circuit():
    """Create a Bell state circuit (|Φ+> state)"""
    qc = QuantumCircuit(2, 2)
    qc.h(0)        # Apply Hadamard to qubit 0
    qc.cx(0, 1)    # Apply CNOT (control=0, target=1)
    qc.measure([0, 1], [0, 1])  # Measure both qubits
    return qc

def simulate_bell_state(qc):
    """Simulate the circuit and return counts and histogram"""
    simulator = Aer.get_backend('qasm_simulator')
    transpiled_circuit = transpile(qc, simulator)
    job = simulator.run(transpiled_circuit, shots=1024)
    result = job.result()
    counts = result.get_counts()
    
    # Plot histogram
    plot_histogram(counts)
    
    return counts

# Example usage
if __name__ == "__main__":
    qc = bell_state_circuit()
    counts = simulate_bell_state(qc)
    print("Measurement results:", counts)

