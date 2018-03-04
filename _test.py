from NextBus import NextBusAPI

# ORIGINAL PYTHON CODE
NextBus = NextBusAPI()
route = '14'
stop = 'E 18th St & 12th Av'
direction = 'West Oakland BART Station'
results = NextBus.BartRoutesResponse(route, stop, direction)
print (results)
# minutesUntilArrival = results['West Oakland BART'][0]
print (minutesUntilArrival)
