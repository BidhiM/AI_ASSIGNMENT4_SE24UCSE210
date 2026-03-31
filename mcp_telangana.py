import matplotlib.pyplot as plt
import matplotlib.patches as patches
import random

# List of Telangana districts (33)
districts = [
    "Adilabad", "Bhadradri_Kothagudem", "Hyderabad", "Jagtial", "Jangaon",
    "Jayashankar_Bhupalpally", "Jogulamba_Gadwal", "Kamareddy", "Karimnagar",
    "Khammam", "Komaram_Bheem", "Mahabubabad", "Mahabubnagar", "Mancherial",
    "Medak", "Medchal_Malkajgiri", "Mulugu", "Nagarkurnool", "Nalgonda",
    "Narayanpet", "Nirmal", "Nizamabad", "Peddapalli", "Rajanna_Sircilla",
    "Ranga_Reddy", "Sangareddy", "Siddipet", "Suryapet", "Vikarabad",
    "Wanaparthy", "Warangal_Rural", "Warangal_Urban", "Yadadri_Bhuvanagiri"
]

# Adjacency list (partial realistic approximation for demo)
neighbors = {

    "Adilabad": ["Komaram_Bheem", "Nirmal"],
    "Komaram_Bheem": ["Adilabad", "Mancherial"],
    "Mancherial": ["Komaram_Bheem", "Peddapalli", "Nirmal"],
    "Nirmal": ["Adilabad", "Mancherial", "Nizamabad"],
    "Nizamabad": ["Nirmal", "Kamareddy"],
    "Kamareddy": ["Nizamabad", "Medak", "Rajanna_Sircilla"],
    
    "Rajanna_Sircilla": ["Kamareddy", "Karimnagar", "Siddipet"],
    "Karimnagar": ["Rajanna_Sircilla", "Peddapalli", "Jagtial"],
    "Peddapalli": ["Karimnagar", "Mancherial", "Jayashankar_Bhupalpally"],
    "Jagtial": ["Karimnagar", "Nizamabad"],
    
    "Jayashankar_Bhupalpally": ["Peddapalli", "Mulugu", "Warangal_Rural"],
    "Mulugu": ["Jayashankar_Bhupalpally", "Warangal_Rural", "Bhadradri_Kothagudem"],
    
    "Bhadradri_Kothagudem": ["Mulugu", "Khammam"],
    "Khammam": ["Bhadradri_Kothagudem", "Mahabubabad", "Suryapet"],
    
    "Mahabubabad": ["Khammam", "Warangal_Rural"],
    "Warangal_Rural": ["Mahabubabad", "Warangal_Urban", "Jangaon", "Mulugu"],
    "Warangal_Urban": ["Warangal_Rural", "Jangaon"],
    
    "Jangaon": ["Warangal_Urban", "Siddipet", "Yadadri_Bhuvanagiri"],
    "Siddipet": ["Jangaon", "Medak", "Rajanna_Sircilla"],
    
    "Medak": ["Kamareddy", "Siddipet", "Sangareddy"],
    "Sangareddy": ["Medak", "Ranga_Reddy", "Vikarabad"],
    
    "Ranga_Reddy": ["Hyderabad", "Sangareddy", "Vikarabad", "Medchal_Malkajgiri"],
    "Hyderabad": ["Ranga_Reddy"], 
    
    "Medchal_Malkajgiri": ["Ranga_Reddy", "Yadadri_Bhuvanagiri"],
    
    "Yadadri_Bhuvanagiri": ["Medchal_Malkajgiri", "Jangaon", "Nalgonda"],
    "Nalgonda": ["Yadadri_Bhuvanagiri", "Suryapet", "Nagarkurnool"],
    
    "Suryapet": ["Nalgonda", "Khammam"],
    
    "Nagarkurnool": ["Nalgonda", "Mahabubnagar", "Wanaparthy"],
    "Mahabubnagar": ["Nagarkurnool", "Wanaparthy", "Narayanpet"],
    "Wanaparthy": ["Nagarkurnool", "Mahabubnagar", "Jogulamba_Gadwal"],
    
    "Jogulamba_Gadwal": ["Wanaparthy", "Narayanpet"],
    "Narayanpet": ["Mahabubnagar", "Jogulamba_Gadwal", "Vikarabad"],
    
    "Vikarabad": ["Sangareddy", "Ranga_Reddy", "Narayanpet"]
}

# Colors
colors = ["Red", "Green", "Blue","Pink"]

# Assignment dictionary
assignment = {}

# Check if assignment is valid
def is_valid(district, color):
    for neighbor in neighbors.get(district, []):
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True

# Backtracking function
def backtrack(index):
    if index == len(districts):
        return True

    district = districts[index]

    for color in colors:
        if is_valid(district, color):
            assignment[district] = color
            if backtrack(index + 1):
                return True
            del assignment[district]

    return False

# Run CSP
if backtrack(0):
    print("District Coloring:\n")
    for d in districts:
        print(f"{d} --> {assignment[d]}")
else:
    print("No solution found")

# Create a grid layout (just for visualization)
cols = 6
rows = 6

fig, ax = plt.subplots(figsize=(8, 8))

# Position districts in grid
positions = {}
i = 0
for r in range(rows):
    for c in range(cols):
        if i < len(districts):
            positions[districts[i]] = (c, rows - r - 1)
            i += 1

# Draw colored blocks
for district, (x, y) in positions.items():
    color = assignment[district].lower()  # match matplotlib colors
    
    rect = patches.Rectangle((x, y), 1, 1, edgecolor='black', facecolor=color)
    ax.add_patch(rect)
    
    # Optional: label (remove if you want only colors)
    ax.text(x + 0.5, y + 0.5, district[:5], 
            ha='center', va='center', fontsize=6, color='white')

# Clean look
ax.set_xlim(0, cols)
ax.set_ylim(0, rows)
ax.axis('off')

plt.title("Telangana District Map Coloring (CSP)")
plt.show()


