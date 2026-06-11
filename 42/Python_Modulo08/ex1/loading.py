# pip install numpy pandas matplotlib
# python /home/dalopez3/python08/ex1/loading.py
# txt
# pip install -r /home/dalopez3/python08/ex1/requirements.txt
# toml
# curl -sSL https://install.python-poetry.org | python3 -
# poetry install
# poetry run python loading.py

print("LOADING STATUS: Loading programs...")
print("Checking dependencies:")
print()

checknumpy = False
checkpandas = False
checkmat = False

try:
    import numpy as np
    checknumpy = True
    print(f"[OK] numpy ({np.__version__}) - Numerical computation ready")
except ImportError:
    print("[MISSING] numpy - install with pip install numpy")

try:
    import pandas as pd  # type: ignore
    checkpandas = True
    print(f"[OK] pandas ({pd.__version__}) - Data manipulation ready")
except ImportError:
    print("[MISSING] pandas - install with pip install pandas")

try:
    import matplotlib.pyplot as plt  # type: ignore
    checkmat = True
    print(
        f"[OK] matplotlib ({plt.matplotlib.__version__})"
        "- Visualization ready"
    )
except ImportError:
    print("[MISSING] matplotlib - install with pip install matplotlib")

if (checknumpy and checkpandas and checkmat):
    print("Dependency manager: pip (requirements.txt)")
    print("Alternative: Poetry (pyproject.toml)")
    print()
    print("Analyzing Matrix data...")
    print("Processing 1000 data points...")
    print()
    data = np.random.randint(1, 100, 1000)
    df = pd.DataFrame(data, columns=['randoms_numbers'])
    print()
    print("Generating visualization...")
    print()
    plt.plot(df["randoms_numbers"])
    plt.title("Matrix Analysis")
    plt.savefig("matrix_analysis.png")
    plt.close()
    print("Analysis complete!")
    print("Results saved to: matrix_analysis.png")
