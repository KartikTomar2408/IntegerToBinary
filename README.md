---

# Integer to Binary Converter

This project is a simple integer to binary converter, utilizing a basic user interface to input an integer and display its binary equivalent.

## Files

- `ui.py`: Contains the user interface code for the integer to binary converter.
- `backend.py`: Contains the backend code responsible for converting integers to binary.

## Usage

### Running the Application

1. Ensure you have Python installed.
2. Install the required dependencies by running:
    ```
    pip install -r requirements.txt
    ```
3. Run the application using:
    ```
    streamlit run ui.py
    ```

### How to Use

1. Upon launching the application, a user interface will appear.
2. Enter any integer value into the designated input field.
3. Click the "Convert to binary" button.
4. The application will display the binary equivalent of the entered integer.

## Code Overview

### Backend (`backend.py`)

```python
def IntBinary(int1):
    return bin(int1)
```

The `IntBinary` function in the backend takes an integer as input and returns its binary representation using Python's `bin` function.

### User Interface (`ui.py`)

```python
import streamlit
from backend import IntBinary

streamlit.title("Integer to Binary Converter")
intvalue = int(streamlit.number_input("Input any integer value"))

if streamlit.button('Convert to binary'):
    streamlit.text(f"Your converted value is: {IntBinary(intvalue)}")
```

The user interface is created using Streamlit. It prompts the user to input an integer value and displays its binary equivalent upon clicking the conversion button.

---
