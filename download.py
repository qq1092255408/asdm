# Import
import requests
import os

print('''
 _______  _______  ______   __   __ 
|   _   ||       ||      | |  |_|  |
|  |_|  ||  _____||  _    ||       |
|       || |_____ | | |   ||       |
|       ||_____  || |_|   ||       |
|   _   | _____| ||       || ||_|| |
|__| |__||_______||______| |_|   |_|
     Auto Scratch-Desktop Mirror
           DOWNLOAD START

''')

# Create 'output'
if not os.path.exists('output'):
    os.mkdir('output')
# Download 'Scratch Setup.exe' for Windows
r = requests.get('https://downloads.scratch.mit.edu/microbit/scratch-microbit.hex.zip', stream=True)

with open(r'./output/scratch-microbit.hex.zip', "wb") as f:
    for chunk in r.iter_content(chunk_size=512):
        f.write(chunk)

print('Download scratch-microbit for windows done.')

# Download 'Scratch Setup.exe' for Windows
r = requests.get('https://downloads.scratch.mit.edu/desktop/Scratch%20Setup.exe', stream=True)

with open(r'./output/scratch-win.exe', "wb") as f:
    for chunk in r.iter_content(chunk_size=512):
        f.write(chunk)

print('Download scratch-desktop for windows done.')

# Download 'Scratch.dmg' for Mac

r = requests.get('https://downloads.scratch.mit.edu/desktop/Scratch.dmg', stream=True)

with open(r'./output/scratch-mac.dmg', "wb") as f:
    for chunk in r.iter_content(chunk_size=512):
        f.write(chunk)

print('Download scratch-desktop for macOS done.')

# Get Scratch Version
try:
    getVersion = requests.get('https://downloads.scratch.mit.edu/desktop/Scratch%20Setup.exe', allow_redirects=False)
    version = getVersion.headers['location'].split('%20')[1]
    os.system('echo "scratch_version='+version+'" >> $GITHUB_ENV')
except:
    print('Get version Error!')
else:
    print('Get version done. version :', version, '. Cost',getVersion.elapsed.total_seconds(),'sec.')
