import tkinter as tk

sampleMap = [["-1","-1","-1","-1","-1","-1","-1","-1","-1","-1","-1","-1","-1","-1","-1","-1","-1","-1","-1","-1"],
["-1","SEAFOOD","SEAFOOD","SEAFOOD","0","MEAT","MEAT","MEAT","MEAT","MEAT","MEAT","0","DAIRY","DAIRY","DAIRY","0","ALCOHOL","ALCOHOL","0","-1"],
["-1","SEAFOOD","SEAFOOD","SEAFOOD","0","MEAT","MEAT","MEAT","MEAT","MEAT","MEAT","0","DAIRY","DAIRY","DAIRY","0","ALCOHOL","ALCOHOL","0","-1"],
["-1","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","-1"],
["-1","BULK","0","0","1","0","2","0","3","0","4","0","5","0","6","0","ALCOHOL","ALCOHOL","0","-1"],
["-1","BULK","0","0","1","0","2","0","3","0","4","0","5","0","6","0","ALCOHOL","ALCOHOL","0","-1"],
["-1","BULK","0","0","1","0","2","0","3","0","4","0","5","0","6","0","0","0","0","-1"],
["-1","0","0","0","1","0","2","0","3","0","4","0","5","0","6","0","BAKERY","BAKERY","0","-1"],
["-1","PRODUCE","0","0","1","0","2","0","3","0","4","0","5","0","6","0","BAKERY","BAKERY","0","-1"],
["-1","PRODUCE","0","0","1","0","2","0","3","0","4","0","5","0","6","0","BAKERY","BAKERY","0","-1"],
["-1","PRODUCE","0","0","1","0","2","0","3","0","0","0","0","0","0","0","0","0","0","-1"],
["-1","PRODUCE","0","0","1","0","2","0","3","0","FROZEN","FROZEN","FROZEN","FROZEN","0","DELI","DELI","DELI","0","-1"],
["-1","PRODUCE","0","0","1","0","2","0","3","0","FROZEN","FROZEN","FROZEN","FROZEN","0","DELI","DELI","DELI","0","-1"],
["-1","PRODUCE","0","0","1","0","2","0","3","0","FROZEN","FROZEN","FROZEN","FROZEN","0","DELI","DELI","DELI","0","-1"],
["-1","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","-1"],
["-1","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","-1"],
["-1","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","-1"],
["-1","FLORIST","FLORIST","FLORIST","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","-1"],
["-1","FLORIST","FLORIST","FLORIST","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","-1"],
["-1","DOOR","DOOR","DOOR","-1","-1","-1","-1","-1","-1","-1","-1","-1","-1","-1","-1","-1","-1","-1","-1"],
["-1","DOOR","DOOR","DOOR","-1","-1","-1","-1","-1","-1","-1","-1","-1","-1","-1","-1","-1","-1","-1","-1"]]




class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def distance(self, other):
        return ((self.x - other.x)**2 + (self.y - other.y)**2)**(1/2)
    
    def __str__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"
    
    
    
class DepartmentStore:
    def __init__(self, name, point1, point2):
        self.name = name
        self.point1 = point1
        self.point2 = point2
    
    def findDistance(self, other):
        distance_1 = self.point1.distance(other.point1)
        distance_2 = self.point1.distance(other.point2)
        distance_3 = self.point2.distance(other.point1)
        distance_4 = self.point2.distance(other.point2)
        min_distance =  min(distance_1, distance_2, distance_3, distance_4)
        if min_distance == distance_1:
            return (min_distance, self.point1, other.point1)
        if min_distance == distance_2:
            return (min_distance, self.point1, other.point2)
        if min_distance == distance_3:
            return (min_distance, self.point2, other.point1)
        if min_distance == distance_4:
            return (min_distance, self.point2, other.point2)

    def draw(self, canvas, scale=1, fill='red'):
        canvas.create_rectangle(self.point1.x * scale, self.point1.y * scale, self.point2.x * scale, self.point2.y * scale, fill=fill)

    def __str__(self):
        return self.name + ": {" + str(self.point1) + ", " + str(self.point2) + "}"

class GroceryMap:
    def __init__(self, gMap):
        self.map = gMap
        self.deptList = []
        self.gotoList = []
        self.door = ""
        self.done = {}
        self.serialize()
        
    def getRows(self):
        return len(self.map)

    def getCols(self):
        if(self.getRows() == 0):
            return 0
        return len(self.map[0])

    def getMap(self):
        return self.map

    def getDeptList(self):
        return self.deptList

    def setMap(self, m):
        self.map = m

    def serialize(self):
        for i in range(0, self.getRows()):
            for j in range(0, self.getCols()):
                if(self.map[i][j] != "0" and self.map[i][j] != "-1" and not(self.map[i][j] in self.done)):
                    dept = self.map[i][j]
                    start = Point(i, j)
                    k = i
                    l = j
                    while(k < self.getRows() and self.map[k][l] == dept):
                        k += 1
                    k -= 1
                    while(j < self.getCols() and self.map[i][l] == dept):
                        l += 1
                    l -= 1
                    end = Point(k, l)
                    if(dept == "DOOR"):
                        self.door = DepartmentStore(dept, start, end)
                    else:
                        self.deptList.append(DepartmentStore(dept, start, end))
                    self.done[dept] = 0

#deptList is list of all DepartmentStore objects
    def getPath(self, canvas):
        path = []
        cur = self.door
        cur.draw(canvas, 25, fill='red')
        path.append(cur)
        mini = 999999999
        while(len(self.deptList) > 0):
            for i in range(0, len(self.gotoList)):
                dist = cur.findDistance(self.gotoList[i])
                if(dist[0] < mini):
                   mini = dist[0]
                   pointA = dist[1]
                   pointB = dist[2]
                   goto = self.gotoList[i]
                   index = i
            path.append(goto)
            goto.draw(canvas, 25, fill='blue')
            cur = goto
            self.gotoList.pop(index)
            mini = 999999999
            draw(pointA, pointB, canvas, 25)
        path.append(self.door)
        return path

def draw(point1, point2, canvas, scale = 1):
    canvas.create_line(point1.x * scale, point1.y * scale, point2.x * scale, point2.y * scale, fill="#476042", arrow = tk.LAST)

G = GroceryMap(sampleMap)
window = tk.Tk()
canvas = tk.Canvas(window, width=1200, height=1200)
canvas.pack()
G.getPath(canvas)
window.mainloop()




