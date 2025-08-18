import os

# yahan apna base folder path do jahan sare categories (folders) hain
base_folder = "Anime"  

limit = 20 * 1024 * 1024      # 20MB in bytes
warn_limit = 19.9 * 1024 * 1024  # 19.9MB in bytes
report = []

for root, dirs, files in os.walk(base_folder):
    for file in files:
        if file.lower().endswith((".png", ".jpg", ".jpeg")):  # sirf images
            path = os.path.join(root, file)
            size = os.path.getsize(path)
            size_mb = size / (1024 * 1024)

            if size >= limit:
                report.append(f"❌ {path} -- {size_mb:.2f} MB (Too large)")
            elif size >= warn_limit:
                report.append(f"⚠️ {path} -- {size_mb:.2f} MB (Close to limit)")
            else:
                report.append(f"✅ {path} -- {size_mb:.2f} MB")

# report ko file me save karna
with open("wallpaper_size_report.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(report))

print("✅ Report ready! Check wallpaper_size_report.txt")
