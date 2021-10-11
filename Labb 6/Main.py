from timeit import timeit as timeit
from Song import Song as song
import sys

sys.setrecursionlimit(300000)

def loadTracks():
    Tracks = []
    with open("unique_tracks.txt", "r", encoding="utf-8") as tracks:
        for row in tracks:
            trackAttr = row.strip().split('<SEP>')
            Tracks.append(song(trackAttr[0], trackAttr[1], trackAttr[2], trackAttr[3]))
    return Tracks

def binary_search(list, key):
    Found = False
    First = 0
    Last = (len(list) - 1)
    while First <= Last and not Found:
        midpnt = (First + Last) // 2
        if list[midpnt] == key:
            Found = True
            return Found
        else:
            if key > list[midpnt]:
                First = midpnt + 1
            else:
                Last = midpnt - 1
    return Found

#O(n)
def linear_time_test(key, tracks):
    for track in tracks:
        if track == key:
            return True
    return False


def loadHashTable(tracks):
    track_dict = {}
    for track in tracks:
        track_dict[str(track)] = track
    return track_dict

def hashSearch(key, dict):
    return str(key) in dict


def partition(arr, low, high):
    i = (low - 1)  # index of smaller element
    pivot = arr[high]  # pivot

    for j in range(low, high):

        # If current element is smaller than or
        # equal to pivot
        if arr[j] <= pivot:
            # increment index of smaller element
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)


# The main function that implements QuickSort
# arr[] --> Array to be sorted,
# low  --> Starting index,
# high  --> Ending index

# Function to do Quick sort


def quickSort(arr, low, high):
    if len(arr) == 1:
        return arr

    if low < high:
        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(arr, low, high)

        # Separately sort elements before
        # partition and after partition
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)


#https://stackabuse.com/selection-sort-in-python/
def selection_sort(L):
    # i indicates how many items were sorted
    for i in range(len(L)-1):
        # To find the minimum value of the unsorted segment
        # We first assume that the first element is the lowest
        min_index = i
        # We then use j to loop through the remaining elements
        for j in range(i+1, len(L)-1):
            # Update the min_index if the element at j is lower than it
            if L[j] < L[min_index]:
                min_index = j
        # After finding the lowest item of the unsorted regions, swap with the first unsorted item
        L[i], L[min_index] = L[min_index], L[i]


def run_tests(Tracks):
    list_tests = [Tracks[0:250000], Tracks[0:500000], Tracks[0:1000000]]
    results = []
    last_track = Tracks[len(Tracks) - 1]

    for tracks_list in list_tests:
        last_track = tracks_list[len(tracks_list) - 1]
        hash_table = loadHashTable(tracks_list)
        hash_time = timeit(stmt=lambda: hashSearch(last_track, hash_table), setup='', number=1000)
        linear_time = timeit(stmt=lambda: linear_time_test(last_track, tracks_list), setup='', number=1000)

        tracks_list.sort(key=lambda s: s.title)
        binary_time = timeit(stmt=lambda: binary_search(tracks_list, last_track), setup='', number=1000)
        results.append([linear_time, binary_time, hash_time])

    n = [250000, 500000, 1000000]
    for i in range(len(results)):
        print(n[i], 'element:')
        print('Linjär sökning: {0} s| Binärsökning: {1} s| Hashtabell: {2} s'.format(round(results[i][0], 5), round(results[i][1], 5), round(results[i][2], 5)))

def sorting_test(Tracks):
    list_tests = [Tracks[0:1000], Tracks[0:10000], Tracks[0:100000], Tracks[0:1000000]]
    results = []
    for track_list in list_tests:
        quick_sort_time = timeit(stmt=lambda: quickSort(track_list, 0, len(track_list)-1), setup='', number=1)
        #selection_sort_time = timeit(stmt=lambda: selection_sort(track_list), setup='', number=1)
        #print('Quick sort: {0} s| Selection sort: {1} s'.
         #     format(round(quick_sort_time, 8), round(selection_sort_time, 8)))
        print('Quick sort: {0} s'.format(round(quick_sort_time, 8)))


def main():
    Tracks = loadTracks()
    sorting_test(Tracks)
  #  run_tests(Tracks)


main()

""" Vid jämförelse av linjärsökning, binärsökning och sökning i hasthtabell 
är sökning i hashtabell den snabbaste algoritmen oberoende av hur många element som finns
i och med att en hashtabell endast gör ungefär 1 jämförelse kommer 
tidskomplexiteten vara O(1). Binärsökning är nästsnabbast och ökar med 
logaritmiskt ju fler element som söks igenom, tidskomplexiteten är O(log n).
Linjärsökning är den långsammaste algoritmen och växer linjärt med ökning
av antal element O(n). 

Vid jämförelse mellan urvalssortering och quicksort är det tydligt att quicksort 
är den snabbaste algoritmen då urvalssortering är så pass långsam vid 100 000+ 
element att det hade tagit för lång tid att vänta ut ett resultat.
Detta beror på tidskomplexiteten hos de olika sorteringsmetoderna där
quicksort har en tidskomplexitet som är O(n log n) medan urvalssortering
har en tidskomplexitet som är O(n**2)."""
