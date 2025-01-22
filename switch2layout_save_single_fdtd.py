## author Ramesh Kudalippalliyalil, LPS, UMD
import sys
import os
sys.path.append("C:\\Program Files\\Lumerical\\v232\\api\\python\\")
sys.path.append(os.path.dirname(__file__)) #Current directory
import lumopt
import numpy as np
import lumapi  # Import the Lumerical API

directory = "./"  # Replace with your target directory (e.g., "/path/to/files")

lms_files = [f for f in os.listdir(directory) if f.endswith(".fsp")]
print(lms_files)

for lms_file in lms_files:
    if not lms_files:
        print("No .fdtd files found in the specified directory.")
    else:
        input_file = os.path.join(directory, lms_file)  # Use the first detected .lms file

        mode = lumapi.open("fdtd")

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