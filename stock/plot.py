import matplotlib.pyplot as plt



def main():
    mean,std = [],[]
    with open('MeanStdData.txt','r') as f:
        for line in f:
            mean.append(float(line.split(',')[1][5:]))
            std.append(float(line.split(',')[2][1:-3]))
            
    plt.plot(mean,std,'ro')
    plt.show()
            
    print(len(mean))


if __name__ =='__main__':main()
