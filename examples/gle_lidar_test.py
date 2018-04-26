def main():
    fd = open('/home/glendal/workspace/BreezySLAM/examples/exp2.dat', 'rt')
    s = fd.readline()
    toks = s.split()[0:-1]
    timestamp = int(toks[0])
    print("timestamp: "+ str(timestamp))
    odometry = timestamp, int(toks[2]), int(toks[3])
    print("odometry: "+ str(odometry))
    
    lidar = [int(tok) for tok in toks[24:]]
    print("lidar: "+ str(lidar))

    fd.close()

main()


