import os

os.makedirs("site", exist_ok=True)

html = """
<!DOCTYPE html>
<html>
<head>
  <title>Docker + GitHub Pages</title>
</head>
<body>
  <h1>🚀 Python + Docker + GitHub Pages</h1>
  <p>This site was built inside a Docker container.</p>
</body>
</html>
"""

with open("site/index.html", "w") as f:
    f.write(html)

print("Static site generated in /site")
