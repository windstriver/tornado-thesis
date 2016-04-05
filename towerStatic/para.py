# Import the 'os' module, which provides a portable way of using
# operating system dependent functionality
import os

workDir = "C:/Users/wy/GitHub/tornado-thesis/towerStatic"

# Specify the Mechanical APDL Input file to be processed
inputFile = AbsUserPathName(workDir + "APDL.MAC")

# Provide a list of bar length (Z) values to solve and write CDB files for.
# Note: We expect '0' to fail.
RValues = [0,100,200,300]

# Open a log file to record script progress
logFile = open(AbsUserPathName(workDir + "para.log"),"w")

# Start a new project and create the Mechanical APDL system
Reset()
template1 = GetTemplate(TemplateName="Mechanical APDL")
system1 = template1.CreateSystem()

# Read the input file into the Mechanical APDL Setup
setup1 = system1.GetContainer(ComponentName="Setup")
mapdlInputFile1 = setup1.AddInputFile(FilePath=inputFile)


# Create Workbench parameters from two of the Mechanical APDL parameters
# in the input file
mapdlInputFile1.PublishMapdlParameter(Name="R")
parameter1 = Parameters.GetParameter(Name="P1")

mapdlInputFile1.PublishMapdlParameter(Name="OUT_U",IsDirectOutput=True)
parameter2 = Parameters.GetParameter(Name="P2")

# Save the initial project definition.
Save(FilePath=AbsUserPathName(workDir + "para.wbpj"),Overwrite=True)

# Loop through all provided bar lengths
for RVal in RValues:
    # Set the Z (length) parameter expression
    parameter1.Expression = str(RVal)
    logFile.write("Updating for R = %s\n" % RVal)
    # Update the project for the new parameter value, and report
    # success or failure to the log file.
    try:
        Update()
    except:
        logFile.write(" Update failed.\n")
    else:
        logFile.write(" Update succeeded. U = %s\n" % parameter2.Value)

# Save the final project state.
Save()
logFile.close()