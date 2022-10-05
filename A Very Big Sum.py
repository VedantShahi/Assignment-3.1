

    
def aVeryBigSum(ar):
    bsum=0
    for i in range(0,len(ar)):
        bsum= bsum + ar[i]
    return bsum
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = aVeryBigSum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()

