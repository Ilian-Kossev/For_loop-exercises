number_transports = int(input())
transport_bus = 0
transport_truck = 0
transport_train = 0
total_tons_transport = 0
total_price_transport = 0
for number in range(1, number_transports + 1):
    weight_transport = int(input())
    total_tons_transport += weight_transport
    if weight_transport <= 3:
        price_per_ton = 200
        transport_bus += weight_transport
    elif 3 < weight_transport <= 11:
        price_per_ton = 175
        transport_truck += weight_transport
    else:
        price_per_ton = 120
        transport_train += weight_transport
    price_transport = price_per_ton * weight_transport
    total_price_transport += price_transport
average_price_per_ton = total_price_transport / total_tons_transport
percent_transport_bus = transport_bus / total_tons_transport * 100
percent_transport_truck = transport_truck / total_tons_transport * 100
percent_transport_train = transport_train / total_tons_transport * 100
print(f"{average_price_per_ton:.2f}")
print(f"{percent_transport_bus:.2f}%")
print(f"{percent_transport_truck:.2f}%")
print(f"{percent_transport_train:.2f}%")
