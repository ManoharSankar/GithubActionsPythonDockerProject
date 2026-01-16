import os

os.makedirs("site", exist_ok=True)

with open("site/index.html", "w") as f:
    f.write("<h1>Docker + GitHub Pages Works 🚀</h1>")

print("site/index.html created")
