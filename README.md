# 📂 Rename Files Script

A simple Python tool to **rename all files in a folder** with a custom prefix and extension.  
It also allows you to **reset the files back to their original names**.

---

## 🚀 Features
- 🔄 Rename all files with a prefix (e.g., `file_1.txt`, `file_2.txt`, …)  
- ⏪ Reset renamed files to their original names  
- 📊 Show summary of current files in the folder  
- ⚠️ Handles missing folders and empty directories  

---

## 🛠️ How to Use

1. Clone the repository or copy the script:
   ```bash
   git clone https://github.com/USERNAME/RenameFilesScript.git
   cd RenameFilesScript
   ```

2. Place your files inside a folder (e.g., test_files/).

3. Run the script:
   ```bash
   python file_renamer.py
   ```
---


# 📋 Example Run
```backtick
Before Renaming
📊 Current files in folder:
- img1.jpg
- img2.jpg
- img3.jpg

After Renaming
🔄 img1.jpg → file_1.txt
🔄 img2.jpg → file_2.txt
🔄 img3.jpg → file_3.txt
✅ Renaming completed.

📊 Current files in folder:
- file_1.txt
- file_2.txt
- file_3.txt

Reset Back to Original
⏪ file_1.txt → img1.jpg
⏪ file_2.txt → img2.jpg
⏪ file_3.txt → img3.jpg
✅ Reset completed.
```
---

## 📂 Project Structure
```markdown
.
├── file_renamer.py   # Main script
├── test_files/       # Folder containing files to rename
└── README.md         # Project documentation
```
