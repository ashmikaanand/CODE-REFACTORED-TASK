import os

# create test folder and some sample files
os.makedirs("/content/test_folder", exist_ok=True)

with open("/content/test_folder/file1.txt", "w") as f:
    f.write("This is a text file.")

with open("/content/test_folder/photo.jpg", "w") as f:
    f.write("fake image data")

with open("/content/test_folder/video.mp4", "w") as f:
    f.write("fake video data")

print("Test folder and sample files created at /content/test_folder")
