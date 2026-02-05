# Quantum Route Optimiser

A research / prototype project that explores using quantum algorithms and hybrid quantum-classical strategies to solve vehicle routing and route optimisation problems (VRP / TSP variants). The repository provides reference implementations, simulators, and tooling to compare classical heuristics with quantum approaches.

Status
- Prototype / experimental. This repository contains research code and examples intended for experimentation and benchmarking. Not production-ready.

Features
- Reference problem formulations: TSP, VRP variants
- Classical solvers: baseline heuristics and local search
- Quantum approaches: QAOA and hybrid variational methods (simulators)
- End-to-end experiment scripts and benchmarking utilities

Quick links
- Usage and examples: ./examples
- Experiments and benchmarks: ./experiments
- Notebooks: ./notebooks

Requirements
- Python 3.9+
- Recommended: conda or venv for environment management
- Suggested quantum SDKs (optional, for real quantum backends): Qiskit or Pennylane

Installation
1. Clone the repository:

   git clone https://github.com/harix10/quantum-route-optimiser.git
   cd quantum-route-optimiser

2. Create and activate a virtual environment (example with venv):

   python -m venv .venv
   source .venv/bin/activate   # macOS / Linux
   .\.venv\Scripts\activate  # Windows

3. Install dependencies:

   pip install -r requirements.txt

Running examples
- Classical baseline (example):

   python -m examples.run_baseline --problem examples/data/sample_tsp.csv

- Quantum simulation (QAOA) example:

   python -m examples.run_qaoa --problem examples/data/sample_tsp.csv --p 1 --shots 1024

Configuration
- Check ./config/default.yaml for configurable experiment parameters such as solver choices, seeds, dataset paths, and quantum backend settings.

Project structure (high level)
- src/ - implementation code (solvers, encodings, utilities)
- examples/ - runnable example scripts
- experiments/ - experiment orchestration and benchmarking code
- notebooks/ - Jupyter notebooks for analysis and visualization
- data/ or examples/data - sample problem instances

How to add a new solver
1. Add your implementation to src/solvers/ and follow the Solver interface (see src/solvers/base.py).
2. Add a small unit test in tests/ to cover basic behaviour.
3. Update examples/ to include an example run.

Testing
- Run unit tests with pytest:

   pytest -q

Contributing
Contributions, issues, and feature requests are welcome. Please follow these guidelines:
- Open an issue to discuss significant changes or new features before implementation.
- Send a pull request with a clear description and tests where applicable.
- Follow the repository's coding style and include type hints where possible.

License
- Add the appropriate license (e.g., MIT) in the LICENSE file.

Contact
- Maintainer: harix10 (GitHub)

Acknowledgements
- Research inspired by work in quantum optimisation, QAOA, and hybrid quantum-classical algorithms.

Notes / Next steps
- Consider adding CI to run tests and basic examples on push.
- Add more detailed notebooks demonstrating how to encode VRP instances into QUBO/Ising form and benchmark on small hardware/simulators.