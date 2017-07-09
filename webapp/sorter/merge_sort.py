
class MergeSort():
    @staticmethod
    def merge_with_array(array,ansArray):

        arraycp = [i for i in array]
        
        
        ansLen = len(ansArray)
        ct = 0
        arrayLen = len(arraycp)
        powArray = []
        tmp = [0 for i in range(0,arrayLen)]
        k = 1
        while(True):
            powArray.append(k)
            if k*2 < arrayLen:
                k = k * 2
            else:
                break
        for div in powArray:
            segArray = []
            l = 0
            while(True):
                segArray.append(l)
                if l+div*2 < arrayLen:
                    l = l+div*2
                else:
                    break
            for seg in segArray:
                fb = n = seg
                sb = fe = min(fb + div, arrayLen)
                se = min(sb + div, arrayLen)
                i = fb
                j = sb
                while (i < fe and j < se):
                    if ct >= ansLen:
                        return [arraycp[i],arraycp[j]]
                    if ansArray[ct] == 1:
                        tmp[n] = arraycp[i]
                        n = n + 1
                        i = i + 1
                    else:
                        tmp[n] = arraycp[j]
                        n = n + 1
                        j = j + 1
                    ct = ct + 1
    
                while ( i < fe ):
                    tmp[n] = arraycp[i]
                    n = n + 1
                    i = i + 1
                while ( j < se ):
                    tmp[n] = arraycp[j]
                    n = n + 1
                    j = j + 1
                for p in range(seg,n):
                    arraycp[p] = tmp[p]
        return arraycp
