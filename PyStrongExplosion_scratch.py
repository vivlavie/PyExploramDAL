
#_strong_explosion_F(ull)
sfx = suffixes[0]
c = case + sfx
f = open(c+'.txt','r')
#read freqeuncy
case_name = f.readline().split(';')[0]
segments_line =  f.readline().split(';')
CategoryNames = segments_line[1:8]
segments = segments_line[8:-1]
NSeg = len(segments)
# Frequency
SF_overall = np.zeros((5,7))
SF_segment = np.zeros((5,NSeg))
for i in range(0,5):
    N = f.readline().split(';')[:-1]
    # N[0] should bene of small, mediu, major, large, or total
    SF_overall[i,:] = [float(x) for x in N[1:8]]
    SF_segment[i,:] = [float(x) for x in N[8:]]
f.readline()
f.readline()
#Probability
case_name = f.readline().split(';')[0]
segments_line =  f.readline().split(';')
# CategoryNames = segments_line[1:8]
# segments = segments_line[8:-1]
# NSeg = len(segments)
#Strong_F
SP_overall = np.zeros((5,7))
SP_segment = np.zeros((5,NSeg))
for i in range(0,5):
    N = f.readline().split(';')[:-1]
    # N[0] should bene of small, mediu, major, large, or total
    SP_overall[i,:] = [float(x) for x in N[1:8]]
    SP_segment[i,:] = [float(x) for x in N[8:]]
f.close()

