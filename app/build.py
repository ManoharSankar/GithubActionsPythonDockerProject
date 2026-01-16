import os

os.makedirs("site", exist_ok=True)

html = """<!DOCTYPE html>
<html>
<head>
    <title>GitHub Pages Deployment</title>
</head>
<body>
    <h1>✅ Deployment Successful</h1>
    <p>This site was built using Python, Docker, and GitHub Actions.</p>
</body>
</html>
"""

with open("site/index.html", "w") as f:
    f.write(html)

print("site/index.html created")
