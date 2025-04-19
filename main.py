import os
import pandas as pd
from tqdm import tqdm

struct = {"path": [], "filename": [], "type": [], "size": []}

for root, dirs, files in tqdm(os.walk(r"C:\Users\user\Desktop", topdown=False)):
    path = root
    foldername = path.split("\\")[-1]
    filetype = "folder"
    foldersize = os.path.getsize(path) / 1024**2
    for filename in files:
        filepath = f"{path}\\{filename}"
        filesize = os.path.getsize(filepath) / 1024**2

        struct["path"].append(filepath)
        struct["filename"].append(filename)
        struct["type"].append("file")
        struct["size"].append(filesize)
        foldersize += filesize
    for subfolder in dirs:
        subfolder_path = f"{path}\\{subfolder}"
        if subfolder_path in struct["path"]:
            subfolder_index = struct["path"].index(subfolder_path)
            subfolder_size = struct["size"][subfolder_index]
            foldersize += subfolder_size
    struct["path"].append(path)
    struct["filename"].append(foldername)
    struct["type"].append(filetype)
    struct["size"].append(foldersize)

file_tree = pd.DataFrame(struct)
file_tree["parent"] = file_tree["path"].str.split("\\")
file_tree["parent"] = file_tree["parent"].apply(lambda a: a[-2])


rootdir = file_tree.iloc[-1]["filename"]
file_tree.to_csv(f"{rootdir}.csv", index=False)
