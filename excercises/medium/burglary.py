def burglary(key):
    items = {"tv": 30,"timmy": 20,"stereo": 50,}
    if key in items:
        print(key.capitalize(),"is gone...")
    else:
        print(key.capitalize(), "is here...")
burglary('tv')