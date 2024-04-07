import streamlit as st
import sys
from io import StringIO

st.title('Python IDE')

# Define initial code
initial_code = '''\
# Welcome to the Python IDE!
def greet(name):
    return "Hello, " + name

print(greet("World"))
'''

# Display the code editor
code = st.text_area('Write your Python code here:', value=initial_code, height=300)

# Button to execute the code
if st.button('Run'):
    # Redirect stdout to capture output
    output_area = st.empty()
    stdout = sys.stdout
    sys.stdout = StringIO()
    
    # Execute the code
    try:
        exec(code)
        output_value = sys.stdout.getvalue()
        output_area.write(output_value)
    except Exception as e:
        st.error(f"An error occurred: {e}")
    
    # Restore stdout
    sys.stdout = stdout
