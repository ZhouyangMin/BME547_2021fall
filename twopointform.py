def twopointform(x1, y1, x2, y2, input_x):
    slope = (y1 - y2)/(x1 - x2)
    return_y = round(slope * (input_x - x1) + y1, 2)
    return return_y
                    

if __name__ == "__main__":
    y = twopointform(1, 2, 3, 4, 5)
    print(y)