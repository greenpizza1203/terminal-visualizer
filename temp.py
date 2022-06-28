import wget
"""
import wget
import os
for file in [
"e13e4362"
]:
    file = "chunk-" + file + ".js"
    outputDir = "storage.googleapis.com/prod-terminal-assets/prod-manager-static/static/js/"
    if not os.path.exists(outputDir+file):
        url = "https://"+outputDir+file
        print(url)
        wget.download(url, out=outputDir)
    print() """
url = "https://storage.googleapis.com/prod-terminal-assets/prod-manager-static/static/img/frames_firewall_dead/firewall_dead_blue+pink_texture.png"

[dir, file] = url.split("//", 1)[1].rsplit("/",1)

print(dir, file)
wget.download(url, out = dir)