Welcome to the Sample Size Calculator, a tool designed to help you easily determine the sample size needed for your experiments and analyses. This project aims to simplify the process of sample size calculation, ensuring that you have the right number of samples to achieve reliable and valid results.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Simple and Intuitive:** User-friendly interface to input your parameters and get the sample size instantly.
- **Flexible Inputs:** Supports various types of input parameters such as confidence level, margin of error, and population size.
- **Accurate Calculations:** Uses standard statistical formulas to ensure accurate and reliable sample size calculations.
- **Open Source:** Free to use and modify under the MIT License.

## Installation

To use the Sample Size Calculator, you need to clone the repository and install the required dependencies. Follow the steps below:

1. Clone the repository:
    ```bash
    git clone https://github.com/33sticks/sample-size-calc.git
    cd sample-size-calc
    ```

2. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

The Sample Size Calculator can be used directly from the command line or integrated into your Python scripts. Below is a basic example of how to use the calculator:

```python
from sample_size_calc import calculate_sample_size

# Define your parameters
confidence_level = 0.95
margin_of_error = 0.05
population_size = 1000

# Calculate sample size
sample_size = calculate_sample_size(confidence_level, margin_of_error, population_size)

print(f"Required sample size: {sample_size}")
```

## Examples

Here are a few examples demonstrating how to use the Sample Size Calculator for different scenarios:

### Example 1: Basic Calculation

```python
sample_size = calculate_sample_size(0.95, 0.05, 1000)
print(f"Required sample size: {sample_size}")
```

### Example 2: Custom Parameters

```python
sample_size = calculate_sample_size(0.99, 0.03, 5000)
print(f"Required sample size: {sample_size}")
```

## Contributing

We welcome contributions to the Sample Size Calculator project! If you have any ideas, suggestions, or bug reports, please open an issue or submit a pull request. Make sure to follow our [contributing guidelines](CONTRIBUTING.md) when submitting changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

Thank you for using the Sample Size Calculator! We hope this tool helps you with your statistical analyses and experiments. If you have any questions or need further assistance, feel free to reach out.
