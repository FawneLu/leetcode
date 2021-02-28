class UndergroundSystem:

    def __init__(self):
        self.checkindict = {}
        self.traveltime = collections.defaultdict(int)
        self.tarvelcount = collections.defaultdict(int)
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkindict[id] = (stationName,t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation, startTime = self.checkindict[id]
        self.traveltime[(startStation,stationName)] += t-startTime
        self.tarvelcount[(startStation,stationName)] += 1
        
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.traveltime[(startStation,endStation)] / self.tarvelcount[(startStation,endStation)]