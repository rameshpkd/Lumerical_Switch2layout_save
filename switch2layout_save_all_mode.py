## author Ramesh Kudalippalliyalil, LPS, UMD
import sys
import os
sys.path.append("C:\\Program Files\\Lumerical\\v232\\api\\python\\")
sys.path.append(os.path.dirname(__file__)) #Current directory
import lumopt
import numpy as np
import lumapi  # Import the Lumerical API


root_directory = "./"  # Replace with your target directory (e.g., "/path/to/root")
print(root_directory)

# Walk through the directory structure
for dirpath, dirnames, filenames in os.walk(root_directory):
    for file in filenames:
        if file.endswith(".lms"):
            input_file = os.path.abspath(os.path.join(dirpath, file))
            print(f"Found file: {input_file}")

            # Launch Lumerical MODE
            mode = lumapi.open("mode")

            # Open the detected .lms file
            mode.switchtolayout()  # Ensure the software starts in layout mode
            mode.eval(f'load("{input_file}");')
            print(f"File '{input_file}' opened successfully.")

            # Switch to Layout Mode
            mode.switchtolayout()
            print("Switched to Layout Mode.")

            # Save the file (overwrite)
            mode.eval(f'save("{input_file}");')
            print(f"File '{input_file}' overwritten successfully.")

            # Close the MODE instance
            mode.close()
