import re
class File:
    _name = ""
    _size = 0
    def __init__(self, name, size):
        if not isinstance(name, str):
            raise ValueError("name must be str type")
        if not isinstance(size, int):
            raise ValueError("size must be int type")
        self._name = name
        self._size = size

    def name(self):
        return self._name

    def size(self):
        return self._size

class Files(list):
    def find(self, name):
        for file in self:
            if file.name() == name:
                return file
        return None

    def size(self):
        size = 0
        for file in self:
            size += file.size()
        return size
class Directories(list):
    def find(self, name):
        for directory in self:
            if directory.name() == name:
                return directory
        return None
class Directory:
    def __init__(self, name, parent = None):
        if not isinstance(name, str):
            raise ValueError("name must be str type")
        if (not parent is None) and (not isinstance(parent, Directory)):
            raise ValueError("parent must be Directory type")
        self._name = name
        self._files = Files()
        self._directories = Directories()
        self._parent = parent

    def name(self):
        return self._name

    def files(self):
        return self._files

    def directories(self):
        return self._directories

    def parent(self):
        return self._parent

    def size(self):
        size = 0
        for file in self._files:
            size += file.size()
        for directory in self._directories:
            size += directory.size()
        return size

    def move(self, relativePath):
        if not isinstance(relativePath, str):
            raise ValueError("relativePath must be str type")
        target = self
        sep = "/"
        tokens = relativePath.split(sep)
        for token in tokens:
            if token == "..":
                if target.parent() is None:
                    print("Cannot move out beyond {} directory because this is the root".format(target.name()))
                else:
                    target = target.parent()
            else:
                found = target.directories().find(token)
                if found:
                    target = found
                else:
                    print("Cannot find {} under {} directory".format(token, target.name()))
        return target

    def addDir(self, directory):
        if not isinstance(directory, Directory):
            raise ValueError("die must be Directory type")
        self._directories.append(directory)

    def addFile(self, file):
        if not isinstance(file, File):
            raise ValueError("file must be File type")
        self._files.append(file)

    def representation(self, depth = 0):
        result = "{}{} (size = {})\n".format("\t" * depth, self.name(), self.size())
        for directory in self.directories():
            result += directory.representation(depth+1)
        return result

    def __str__(self):
        return self.representation()

    def findSumDirSizeLessThan(self, maxSize):
        result = 0
        for directory in self.directories():
            result += directory.findSumDirSizeLessThan(maxSize)
        if self.size() <= maxSize:
            print("{} less than or equal to size {}, size = {}".format(self.name(), maxSize, self.size()))
            result += self.size()
        return result

    def _findSmallestSizeDirGreaterThan(self, greaterThanSize, currentSmallestSize):
        if self.size() >= greaterThanSize and self.size() < currentSmallestSize:
            currentSmallestSize = self.size()
        for directory in self.directories():
            currentSmallestSize = directory._findSmallestSizeDirGreaterThan(greaterThanSize, currentSmallestSize)
        return currentSmallestSize
    def findSmallestSizeDirGreaterThan(self, greaterThanSize):
        if self.size() >= greaterThanSize:
            return self._findSmallestSizeDirGreaterThan(greaterThanSize, self.size())
        return -1



if __name__ == "__main__":
    overlapPairsCount = 0
    inputFile = open("input.txt", "r")
    try:
        ROOT_DIR_NAME = "/"
        PATH_SEP = "/"
        COMMAND_PREFIX = "$"
        CD_COMMAND = "cd"
        LS_COMMAND = "ls"

        rootDir = Directory(ROOT_DIR_NAME)
        curDir = rootDir
        lines = inputFile.readlines()
        inLs = False
        for line in lines:
            if line.startswith(COMMAND_PREFIX):
                promptIdx = line.index(COMMAND_PREFIX)
                commandLine = line[promptIdx + 1:].strip()
                commandTokens = commandLine.split()
                command = commandTokens[0]
                if command == "cd":
                    path = commandTokens[1]
                    if path.startswith(ROOT_DIR_NAME):
                        curDir = rootDir
                        if path == ROOT_DIR_NAME:
                            continue
                        pathTokens = path[len(ROOT_DIR_NAME) + 1:].split(PATH_SEP) # remove first path delimiter
                        for pathToken in pathTokens:
                            nextDir = curDir.directories().find(pathToken)
                            if not nextDir:
                                nextDir = Directory(pathToken, curDir)
                            curDir = nextDir
                    else:
                        curDir = curDir.move(path)
                    inLs = False
                elif command == "ls":
                    inLs = True
            else:
                if inLs:
                    tokens = line.strip().split()
                    firstToken = tokens[0]
                    if firstToken.isdigit():
                        fileName = tokens[1]
                        fileSize = int(firstToken)
                        file = File(fileName, fileSize)
                        curDir.addFile(file)
                    elif firstToken == "dir":
                        dirName = tokens[1]
                        newDir = Directory(dirName, curDir)
                        curDir.addDir(newDir)
                    else:
                        print("Unknown type of item in file system")
                else:
                    print("Something went wrong")
        neededSize = 30000000 - (70000000 - rootDir.size())
        print(rootDir.findSmallestSizeDirGreaterThan(neededSize))
    finally:
        inputFile.close()