def weight_on_planets():
    earth = input("What do you weigh on earth? \n")
    earth = float(earth)
    mars = earth * 0.38
    jupiter = earth * 2.34
    print("On Mars you would weigh", mars, "pounds.\nOn Jupiter you would weigh", jupiter, "pounds.")


if __name__ == '__main__':
    weight_on_planets()