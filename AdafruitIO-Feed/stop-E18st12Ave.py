from NextBus import NextBusAPI

# class BusStatus(object):
	
# 	def __init__(self):
# 		''' 
# 		initiate with values for the current stop 
# 		'''
# 		self.stopInput = "E 18th St & 12th Av"
# 		self.routeInput = "14"
# 		self.directionInput = "West Oakland BART"

# 	def getNextArrival(self, bus):
# 		''' 
# 		generate and return minutes until next arrival
# 		'''
# 		results = bus.BartRoutesResponse(stopInput = stopInput, routeInput = routeInput, directionInput = directionInput)[0]
# 		minutesUntilArrival = results[directionInput][0]
# 		return minutesUntilArrival

# NextBus = NextBusAPI()
# print(BusStatus.getNextArrival(NextBus))

# ORIGINAL PYTHON CODE
NextBus = NextBusAPI()
route = '14'
stop = 'E 18th St & 12th Av'
direction = 'West Oakland BART Station'
results = NextBus.BartRoutesResponse(route, stop, direction)
print (results)
# minutesUntilArrival = results['West Oakland BART'][0]
print (minutesUntilArrival)
