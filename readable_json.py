import json

# Explore the structure of the data
filename = '/path/to/file.json'

# Store all data in json file, a giant dictionary
with open(filename) as f:
    all_data = json.load(f)
    
readable_file = '/path/to/readableFile.json'

# A file to write the same data into a more readable format
with open(readable_file, 'w') as f:
    json.dump(all_data,f,indent=4)