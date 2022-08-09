import json

buses = json.loads(input())
print("On demand stops test:")
transfer_stops = dict()
starting_stops = set()
ondemand_stops = set()
final_stops = set()
for bus in buses:
    transfer_stops.setdefault(bus['stop_name'], 0)
    transfer_stops[bus['stop_name']] += 1
    if bus['stop_type'] == "S":
        starting_stops.add(bus['stop_name'])
    if bus['stop_type'] == "F":
        final_stops.add(bus['stop_name'])
    if bus['stop_type'] == "O":
        ondemand_stops.add(bus['stop_name'])

transfer_stops_set = set([key for (key, value) in transfer_stops.items() if value > 1])
wrong_stops = ondemand_stops.intersection(starting_stops | final_stops | transfer_stops_set  )

if len(wrong_stops) > 0:
    print("Wrong stop type: {}".format(sorted(wrong_stops)))
else:
    print("OK")