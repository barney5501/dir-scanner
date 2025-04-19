## DirScanner 📂🔍

This simple script goes over a given directory and outputs a csv file with each file and folder in it
recursively, including their size.<br>
each record is linked to it's parent by the "parent" column.


### TODO ☑:
- [ ] parent is linked by name - if 2 or more subfolders have the same name that would be a problem.
- [ ] improve data structures - list of objects instead of dict of lists.
- [ ] optimize size calculation - can be moved to the main scan.
- [ ] convert to mb on df - instead of during the scan.
- [ ] use path.join instead of \\ - to support other OSs.
- [ ] use path.parent instead of split by \\
- [x] Add streamlit app - Currently in another branch, needs improvements.