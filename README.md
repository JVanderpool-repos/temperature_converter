# Temperature Converter

A simple Python command-line tool to convert temperatures between Celsius, Fahrenheit, and Kelvin.

## Features

- Convert between Celsius (C), Fahrenheit (F), and Kelvin (K)
- Command-line interface
- No external dependencies

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/JVanderpool-repos/temperature_converter.git
   cd temperature_converter
   ```

2. Create a virtual environment:
   ```bash
   python3 -m venv venv
   ```

3. Activate the virtual environment:
   - On Linux/Mac:
     ```bash
     source venv/bin/activate
     ```
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```

4. The tool has no dependencies, so no need to install anything else.

## Usage

Run the script with the temperature value and units:

```bash
python temperature_converter.py <value> <from_unit> <to_unit>
```

### Examples

- Convert 25°C to Fahrenheit:
  ```bash
  python temperature_converter.py 25 C F
  ```
  Output: `25.0 C is 77.00 F`

- Convert 77°F to Celsius:
  ```bash
  python temperature_converter.py 77 F C
  ```
  Output: `77.0 F is 25.00 C`

- Convert 298.15 K to Celsius:
  ```bash
  python temperature_converter.py 298.15 K C
  ```
  Output: `298.15 K is 25.00 C`

### Units

- `C`: Celsius
- `F`: Fahrenheit
- `K`: Kelvin

## Contributing

Feel free to submit issues or pull requests.

## License

This project is open source.