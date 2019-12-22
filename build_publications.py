import frontmatter
import os
import json

# WHere to look
here = "/Users/uum209/GitHub/thredgroup.github.io/_posts"
directory = os.listdir(here)

# Build the list
publications = []
names = []
for file in directory:
    if file.endswith(".md"):
        print(file)
        with open(here + "/" + file) as f:
            publications.append(frontmatter.load(f).metadata)
            names.extend(publications[-1]['authors'])


# build files for export
names = list(set(names))
for name in names:
    temp = []
    for file in publications:
        if name in file['authors']:
            temp.append(file)

    with open("/Users/uum209/GitHub/thredgroup.github.io/assets/"+name.split(" ")[-1]+'.json', 'w') as outfile:
        json.dump(temp, outfile)
