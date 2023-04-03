# normalizeGreyScale will take a list of flattened image arrays and "normalize" them
# In reality, the scaling is from the pixel values from 255 - 0 into values from 1 - 0
def normalizeGreyScale(input):
    for img in input:
        for i in range(len(img)):
            img[i] /= 255

# prepareSquareImg will flatten the raw data collected in data_collect.ipynb -
# - and normalize the values   
def prepareSquareImg(input):
    input = input.reshape(-1, len(input[0])**2)
    input = input.astype(np.float32)
    normalizeGreyScale(input)
    return input

# Very annoying implementation, but getOneShot will give the indec for -
# the slice of the identity array (implemented in convertLabeltoOneshot) -
# - that represents what class it is meant to be given the label
# Important for the categorical cross entropy loss function
def getOneShot(label):
    value = label
    match label:
        case '36':
            value = 0        
        case '53_73':
            value = 1        
        case '4e':
            value = 2        
        case '41':
            value = 3        
        case '4c_6c':
            value = 4        
        case '4d_6d':
            value = 5        
        case '52':
            value = 6        
        case '71':
            value = 7        
        case '37':
            value = 8        
        case '49_69':
            value = 9        
        case '4f_6f':
            value = 10
        case '6e':
            value = 11
        case '38':
            value = 12
        case '39':
            value = 13
        case '50_70':
            value = 14
        case '35':
            value = 15
        case '32':
            value = 16
        case '31':
            value = 17
        case '30':
            value = 18
        case '59_79':
            value = 19
        case '62':
            value = 20
        case '65':
            value = 21
        case '72':
            value = 22
        case '33':
            value = 23
        case '43_63':
            value = 24
        case '4a_6a':
            value = 25
        case '34':
            value = 26
        case '55_75':
            value = 27
        case '5a_7a':
            value = 28
        case '54':
            value = 29
        case '68':
            value = 30
        case '42':
            value = 31
        case '64':
            value = 32
        case '61':
            value = 33
        case '74':
            value = 34
        case '57_77':
            value = 35
        case '47':
            value = 36
        case '51':
            value = 37
        case '46':
            value = 38
        case '4b_6b':
            value = 39
        case '58_78':
            value = 40
        case '45':
            value = 41
        case '44':
            value = 42
        case '56_76':
            value = 43
        case '67':
            value = 44
        case '48':
            value = 45
        case '66':
            value = 46
    return value

# Converts complete lable list into target list with indeces representing slices of I
def convertLabel2Class(labels):
    target = []
    for label in labels:
        target.append(getOneShot(label))
    return target

# Converts labels to one shot hot encoding using getOneShot
def convertLabel2OneShot(labels):
    target = []
    I = np.eye(47)
    for label in labels:
        target.append(I[getOneShot(label)])
    return target
