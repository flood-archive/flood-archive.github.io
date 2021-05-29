import glob
from os import path, mkdir

floods = glob.glob("floods/*.txt")
count = 0
floodList = ""

for flood in floods:
    floodList += "\t<li><a href='https://raw.githubusercontent.com/flood-archive/flood-archive.github.io/master/{}'>{}</a></li>\n\t".format(flood, open(flood, 'r').readline(50))
    count += 1

with open("base.stub", "r") as index:
    index = index.read().replace('{floodList}', floodList).replace('{count}', str(count))
    try:
        open('docs/index.html', 'w').write(index)
        open("docs/.nojekyll", 'w+').close()
    except FileNotFoundError:
        mkdir('docs')
        open('docs/index.html', 'w').write(index)
        open("docs/.nojekyll", 'w+').close()