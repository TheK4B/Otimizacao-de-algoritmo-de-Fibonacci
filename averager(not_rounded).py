from pathlib import Path
import re

folderList = {
    Path(".\\memoização"),
    Path(".\\Tabulação"),
    Path(".\\não otimizado")
}

def getFileList(filePath):
    fileList = [f.name for f in filePath.iterdir() if f.is_file]
    for each in fileList:
        if "fib_log_" not in each:
            fileList.remove(each)
    return fileList

def readAndAverage(filePath, fileList):
    format = re.compile(r"n: (\d+) \| time elapsed: \[([0-9e\-\.]+)\] \| memory used: \[\(([0-9]+)\, ([0-9]+)\)\]")
    statList = {}
    iterator = 0
    number = 0
    elapsedTime = 0.0
    memUsage = 0
    memPeak = 0

    for fileName in fileList:
        f = open(str(filePath) + "\\" + fileName, "r")
        for line in f:
            match = format.search(line)
            if match:
                number = int(match.group(1))
                elapsedTime = float(match.group(2))
                memUsage = int(match.group(3))
                memPeak = int(match.group(4))
            if number not in statList:
                statList[number] = [elapsedTime, memUsage, memPeak]
            else:
                statList[number][0] += elapsedTime
                statList[number][1] += memUsage
                statList[number][2] += memPeak
        iterator += 1
        f.close()
    for each in statList.keys():
        statList[each][0] /= iterator
        statList[each][1] /= iterator
        statList[each][2] /= iterator
    return statList

def writeStatsToFile():
    f = open("average_performance_log.txt", "w", encoding="utf-8")
    f.write("Averages per algorithm\n\n")
    for folder in folderList:
        fileList = getFileList(folder)
        averageStats = readAndAverage(folder, fileList)
        f.write("\n" + str(folder) + "\n")
        for x in averageStats.keys():
            f.write("[" + str(x) + "] |")
            f.write("[" + str(averageStats[x][0] * 1000) + "] | ")
            f.write("[" + str(averageStats[x][1]) + " / " + str(averageStats[x][2]) + "]")
            f.write("\n")
    f.close()

writeStatsToFile()