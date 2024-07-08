import matplotlib.pyplot as plt
def ploting(filepath, fig):
    with open(filepath, 'r') as Input:
        lines = Input.readlines()
    time = []
    ch1 = []
    ch2 = []
    ch3 = []
    string = []
    enable = False
    for line in lines:
        if (enable):
            data = line.split(',')
            #print(data)
            time.append(float(data[0])*100000000)
            ch1.append((float(data[1])))
            ch2.append((float(data[2])))
            data[3] = data[3][:-1]
            ch3.append(float(data[3]))
        if line.startswith('TIME'):
            enable = True
    #debug
    #print(string)
    # print(time)
    print(ch1)
    # print(len(ch2))
    # print(len(ch3))

    plt.plot(time,ch1, alpha=0.75,c='y')
    plt.plot(time,ch2, alpha=0.5,c='b')
    plt.plot(time,ch3, alpha=0.25, c='r')
    plt.savefig(fig)

ploting('tek0000.csv', 'test.png')
