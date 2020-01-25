#Write Program To Find The Largest Number In List.
#a=[10,20,30,40,70,60]


def find_max(a):
    max=a[0]
    for element in a[1:]:
        if(max<element):
            max=element
    return max
#print(f'Largest Element In The Array:{max}')