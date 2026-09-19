from rembg import remove
from PIL import Image
import io
import os

files = [
    "assets/lego/scouttrek-trail.png",
    "assets/lego/chefshat-fridge.png",
    "assets/lego/ai-content-scene.png",
    "assets/lego/lego-arrow.png",
    "assets/lego/computer-screen.png",
    "assets/lego/minifig-desk.png",
]

base = os.path.dirname(os.path.abspath(__file__))

for rel_path in files:
    path = os.path.join(base, rel_path)
    if not os.path.exists(path):
        print(f"SKIP (not found): {rel_path}")
        continue
    print(f"Processing: {rel_path} ...", end=" ", flush=True)
    with open(path, "rb") as f:
        input_data = f.read()
    output_data = remove(input_data)
    img = Image.open(io.BytesIO(output_data)).convert("RGBA")
    img.save(path, "PNG")
    print("done")

print("All done.")
