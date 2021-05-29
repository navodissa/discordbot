
def buildJSON(keys, values):
    output_dic = {}
    # Itereate through passed keys and values; Assign values to corresponding keys
    for keyInx in range(0, len(keys)):
        output_dic[keys[keyInx]] = values[keyInx]
    return output_dic


def parseJSON():
    return
