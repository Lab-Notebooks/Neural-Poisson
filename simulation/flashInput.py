"""Script to create input files"""

import toml
import argparse
import numpy

def createParfile(inputDict):
    """
    Create flash.par
    """
    with open("flash.par", "w") as parfile:

        # Add comment to the parfile
        parfile.write("# Programmatically generated parfile for flashx\n")

        # Loop over keys
        for key, value in inputDict["Parfile"].items():
            if type(value) == str and value not in [
                ".TRUE.",
                ".FALSE.",
                ".true.",
                ".false.",
            ]:
                parfile.write(f'{key} = "{value}"\n')
            else:
                parfile.write(f"{key} = {value}\n")

        if "Heater" in inputDict.keys():
            parfile.write(f'sim_heaterName = "{inputDict["Heater"]["name"]}"\n')
            parfile.write(
                f'sim_nucSeedRadius = {inputDict["Heater"]["nucSeedRadius"]}\n'
            )
            parfile.write(f"sim_numHeaters = 1")

    print(f"Wrote parameter information to file flash.par")

if __name__ == "__main__":
    # Create an arg parser
    InputParser = argparse.ArgumentParser(description="Parser For Input File")
    InputParser.add_argument("-i", "--input", help="Input File", type=str)
    InputParser.set_defaults(input=None)

    # Load toml dictionary
    inputDict = toml.load(InputParser.parse_args().input)

    # Create input files
    createParfile(inputDict) 
