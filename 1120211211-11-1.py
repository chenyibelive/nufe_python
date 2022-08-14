def waterCost(waterWeight):
    if waterWeight >= 0 & waterWeight <= 220:
        Cost = 3.45 * waterWeight
    elif waterWeight >= 220 & waterWeight <= 300:
        Cost = 4.83 * waterWeight
    else:
        Cost = 5.83 * waterWeight
    return Cost



a = waterCost(10)
print(a)

