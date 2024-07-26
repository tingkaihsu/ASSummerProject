# ASSummerProject
This is the project containing all stuff in AS summer 2024
# To set up Time/counter Device
We use python here, and in order to get permission to the remote device.
Plz use 'sudo' to run the code!
https://github.com/pyserial/pyserial/issues/124

# How to install ROOT
I think the snap method for installing ROOT is the most stable one, plz ref the official website to learn more.

# ROOT drawing
To create a `TTree` file with ROOT in Python where the data format is `1,95;2,4`, you will follow these steps. This example will walk you through creating a `TTree`, filling it with your data, and saving it to a file.

### 1. Import ROOT and Create a TFile

First, make sure you import the `ROOT` module and create an instance of `TFile` where you will save the `TTree`.

```python
import ROOT

# Create a new ROOT file to store the TTree
output_file = ROOT.TFile("channel_data.root", "RECREATE")
```

### 2. Define the TTree and Branches

Next, you need to define the `TTree` structure. For this example, you will create a tree where each entry consists of a list of channel numbers and counts. We'll use a `std::vector` to store the data for each entry.

```python
# Define the TTree and branches
tree = ROOT.TTree("tree", "A Tree with channel data")

# Variables to hold data
channel_numbers = []
counts = []
tree.Branch("channel_numbers", channel_numbers)
tree.Branch("counts", counts)
```

### 3. Parse Your Input Data

Assuming your input data is in the format `1,95;2,4`, you need to parse it and extract the channel numbers and counts.

```python
# Example input data
data = "1,95;2,4"

# Parse the input data
for entry in data.split(";"):
    channel, count = map(int, entry.split(","))
    channel_numbers.append(channel)
    counts.append(count)

    # Fill the TTree
    tree.Fill()

# Clear the data for the next potential fill
channel_numbers.clear()
counts.clear()
```

### 4. Write and Close the File

Finally, write the `TTree` to the file and close the file.

```python
# Write the TTree to the file
output_file.Write()
# Close the file
output_file.Close()
```

### Full Example Code

Here is the full example code that combines all the steps:

```python
import ROOT

# Create a new ROOT file to store the TTree
output_file = ROOT.TFile("channel_data.root", "RECREATE")

# Define the TTree and branches
tree = ROOT.TTree("tree", "A Tree with channel data")

# Variables to hold data
channel_numbers = []
counts = []
tree.Branch("channel_numbers", channel_numbers)
tree.Branch("counts", counts)

# Example input data
data = "1,95;2,4"

# Parse the input data and fill the TTree
for entry in data.split(";"):
    channel, count = map(int, entry.split(","))
    channel_numbers.append(channel)
    counts.append(count)

    # Fill the TTree
    tree.Fill()

# Clear the data for the next potential fill
channel_numbers.clear()
counts.clear()

# Write the TTree to the file
output_file.Write()
# Close the file
output_file.Close()

print("TTree file 'channel_data.root' has been created.")
```

### Reading Back the TTree

To read the `TTree` file you created and check its contents, you can use the following script:

```python
import ROOT

# Open the ROOT file
input_file = ROOT.TFile("channel_data.root", "READ")

# Get the TTree from the file
tree = input_file.Get("tree")

# Set up variables to hold the data
channel_numbers = ROOT.std.vector('int')()
counts = ROOT.std.vector('int')()

# Set up branches
tree.SetBranchAddress("channel_numbers", channel_numbers)
tree.SetBranchAddress("counts", counts)

# Loop over the entries
for entry in tree:
    print(f"Channel numbers: {list(channel_numbers)}")
    print(f"Counts: {list(counts)}")

# Close the file
input_file.Close()
```

### Additional Information

If you have more complex data formats or if you want to store multiple entries in a single TTree, you might need to adjust the way you parse and fill the TTree. This basic example assumes a single string of data for simplicity.

### References

- [ROOT TTree Documentation](https://root.cern/manual/ttree/)
- [ROOT Python Bindings Documentation](https://root.cern/manual/python/)
- [ROOT User Guide](https://root.cern/manual/)

# 7/26/2024
Make sure the version of gcc is correct.
Conda forge may cause problem.
I uninstall conda-forge and renew the version of gcc.
Commend
```
make
```
```
sudo make install
```
and then the CAENVME driver and USB connection package are installed.
Try to demo now.

