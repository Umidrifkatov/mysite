import geocoder
g = geocoder.google([37.39008, -122.08139], method='reverse')
print(g.city)
