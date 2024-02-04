
***OpenCB Engine*** is an open-source code analysis tool designed to provide comprehensive insights into Python code. It supports various engine types, each tailored for specific analysis techniques, making it a versatile tool for software developers.




   ____                    _____ ____  
  
## Features

- **Basic Code Analysis**: Provides insights into the code structure, including the number of functions and classes.
- **Complexity Analysis**: Calculates a custom complexity metric, offering a deeper understanding of code intricacies.
- **Bug Detection**: Identifies potential bugs, such as non-alphanumeric strings and missing semicolons.
- **Predictive Analysis**: Detects potential issues, like unused variables, using advanced predictive analysis techniques.

## Advantages

- **Versatility**: Choose from multiple engine types based on your analysis needs.
- **Comprehensive Analysis**: Utilize a range of tools for in-depth code understanding and issue detection.
- **Ease of Use**: Simple command-line interface for effortless code analysis.

## Supported Engine Types

| Engine Type        | Analysis Tools                                   |
|--------------------|--------------------------------------------------|
| opencv-1           | Basic Code Analysis                              |
| opencv-2           | Basic Code Analysis, Complexity Analysis        |
| opencv-3           | Basic Code Analysis, Complexity Analysis, Bug Detection |
| opencv4-5turbo     | All Analysis Tools (Basic, Complexity, Bug Detection, Predictive Analysis) |

## Usage
```python
from opencb_engine import OpenCBEngine

# Example usage
engine_type = "opencv-1"
code_path = "/path/to/your/code.py"

opencb_engine = OpenCBEngine(engine_type)
result = opencb_engine.analyze_code(code_path)

print(result)
```

## Installation

```bash
pip install -r requirements.txt
```


## Contributing

Feel free to contribute to the project by opening issues or pull requests. We welcome any improvements or additional features.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
