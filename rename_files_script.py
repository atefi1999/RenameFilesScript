import os


class FileRenamer:
    def __init__(self, folder_path, prefix="", extension=""):
        self.folder_path = folder_path
        self.prefix = prefix
        self.extension = extension
        self.original_names = []

    def list_files(self):
        """Return a list of files in the folder"""
        if not os.path.isdir(self.folder_path):
            print("❌ Folder not found.")
            return []
        return [f for f in os.listdir(self.folder_path) if os.path.isfile(os.path.join(self.folder_path, f))]

    def rename_files(self):
        """Rename all files with the given prefix and extension"""
        files = self.list_files()
        if not files:
            print("⚠️ No files to rename.")
            return

        self.original_names = files.copy()
        for i, filename in enumerate(files, start=1):
            name, ext = os.path.splitext(filename)

            # Create new file name
            new_name = f"{self.prefix}{i}{self.extension if self.extension else ext}"

            old_path = os.path.join(self.folder_path, filename)
            new_path = os.path.join(self.folder_path, new_name)

            os.rename(old_path, new_path)
            print(f"🔄 {filename} → {new_name}")

        print("✅ Renaming completed.")

    def reset_names(self):
        """Reset files to their original names (if stored)"""
        if not self.original_names:
            print("⚠️ No original names stored. Cannot reset.")
            return

        files = self.list_files()
        if len(files) != len(self.original_names):
            print("⚠️ File count mismatch. Reset may not be accurate.")
            return

        for filename, original in zip(files, self.original_names):
            old_path = os.path.join(self.folder_path, filename)
            new_path = os.path.join(self.folder_path, original)
            os.rename(old_path, new_path)
            print(f"⏪ {filename} → {original}")

        print("✅ Reset completed.")

    def show_summary(self):
        """Show summary of the current files in the folder"""
        files = self.list_files()
        print("\n📊 Current files in folder:")
        for f in files:
            print(f"- {f}")


# ---------------- Sample Run ----------------
if __name__ == "__main__":
    # Change the folder path here
    folder = "test_files"

    renamer = FileRenamer(folder, prefix="file_", extension=".txt")

    print("\n📂 Before Renaming:")
    renamer.show_summary()

    renamer.rename_files()

    print("\n📂 After Renaming:")
    renamer.show_summary()
