import os


SRC_DIR = "path/to/source"
DEST_DIR = "path/to/dest"

IMAGE_EXTS = {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".webp"}


def get_images(base_dir):
    images = {}
    for root, _, files in os.walk(base_dir):
        for f in files:
            ext = os.path.splitext(f)[1].lower()
            if ext in IMAGE_EXTS:
                rel_path = os.path.relpath(root, base_dir)  # relative folder
                # store folder details and full path
                images[f] = {
                    "folder": rel_path if rel_path != "." else "",
                    "full_path": os.path.join(root, f)
                }
    return images


def main():
    src_imgs = get_images(SRC_DIR)
    dest_imgs = get_images(DEST_DIR)

    missing = []
    for fname, details in src_imgs.items():
        if fname not in dest_imgs:
            missing.append(details)

    if not missing:
        print("All images from source were copied to destination.")
    else:
        print("Missing images:")
        for m in missing:
            print(f"- {m['full_path']} (lowest folder: {m['folder']})")


if __name__ == "__main__":
    main()