from pathlib import Path

def create_test_folder(base_path="/content/test_folder"):
    base = Path(base_path)
    base.mkdir(parents=True, exist_ok=True)

    files = {
        "file1.txt": "This is a text file.",
        "photo.jpg": "fake image data",
        "video.mp4": "fake video data"
    }

    for name, content in files.items():
        file_path = base / name
        file_path.write_text(content)
        print(f"✅ Created: {file_path}")

    print(f"\nAll sample files successfully created in {base.resolve()}")

if __name__ == "__main__":
    create_test_folder()
