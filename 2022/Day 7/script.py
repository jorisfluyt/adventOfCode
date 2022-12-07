from typing import List

class File :
    def __init__(self, name:str, size:int) -> None:
        self.name = name
        self.size = size

class Directory :
    def __init__(self, name:str, parent) -> None:
        self.parent = parent
        self.name = name
        self.directories = dict()
        self.files = []
    
    def getSize(self) -> int :
        sum = 0
        for f in self.files :
            sum += f.size
        for d in self.getChildren() :
            sum += d.getSize()
        return sum


    def addDir(self, dir:"Directory") :
        self.directories[dir.name] = dir
    
    def getDir(self, name) -> "Directory" :
        return self.directories[name]

    def getChildren(self) -> List["Directory"]:
        return self.directories.values()

    def addFile(self, file:File) :
        self.files.append(file)

def parse(file:str) -> Directory :
    input = open(file)
    lines = input.readlines()
    rootDir = Directory('/', None)
    dirPointer = None
    for line in lines :
        item = line.strip().split(' ')
        if item[1].strip() == 'cd' :
            if item[2].strip() == '/' :
                dirPointer = rootDir
            elif item[2].strip() == '..' :
                dirPointer = dirPointer.parent
            else :
                dirPointer = dirPointer.getDir(item[2])
        elif item[0] == 'dir':
            name = item[1].strip()
            dirPointer.addDir(Directory(name, dirPointer))
        elif item[1] == 'ls' :
            continue
        else :
            size = int(item[0].strip())
            name = item[1].strip()
            dirPointer.addFile(File(name, size))
    return rootDir

def getSumOfDirectoriesLowerThan(directory: Directory, threshhold:int) -> int:
    sumOfDirectories = 0
    if directory.getSize() < threshhold :
        sumOfDirectories += directory.getSize()
    for dir in directory.getChildren() :
        sumOfDirectories += getSumOfDirectoriesLowerThan(dir, threshhold)
    return sumOfDirectories

def getSmallestDirectoryToCleanup(dir: Directory, totalspace: int, freespace: int) -> int:
    cleanup = (dir.getSize() + freespace) - totalspace
    if cleanup < 0 :
        return 0
    return getSmallestDirectoryHigherThan(dir, cleanup)

def getSmallestDirectoryHigherThan(directory:Directory, threshhold:int) -> int:
    if directory.getSize() < threshhold :
        return None
    
    children = []
    for d in directory.getChildren() :
        value = getSmallestDirectoryHigherThan(d, threshhold)
        if value == None :
            continue
        children.append(value)
    
    if children != [] :
        return min(children)
    return directory.getSize()

def main() :
    rootDir = parse('input.txt')
    print('The sum of the total sizes of directories with a total size of at most 100000 is {}'.format(getSumOfDirectoriesLowerThan(rootDir, 100000)))
    print('The total size of the smallest directory that, if deleted, would free up enough space is {}'.format(getSmallestDirectoryToCleanup(rootDir, 70000000, 30000000)))

main()
