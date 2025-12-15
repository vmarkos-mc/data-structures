def binary_search(items, search_item):
  
    # Initialise the variables
    found = False
    found_index = -1
    first = 0
    last = len(items) - 1

    # Repeat while there are still items between first and last 
    # and the search item has not been found
    while first <= last and found == False:
        
        # Find the midpoint position (in the middle of the range)
        midpoint = (first + last) // 2

        # Compare the item at the midpoint to the search item
        if items[midpoint] == search_item:
            # If the item has been found, store the midpoint position
            found_index = midpoint
            found = True # Raise the flag to stop the loop

        # Check if the item at the midpoint is less than the search item    
        elif items[midpoint] < search_item:
            # Focus on the items after the midpoint
            first = midpoint + 1

        # Otherwise the item at the midpoint is greater than the search item  
        else:
            # Focus on the items before the midpoint
            last = midpoint - 1

    # Return the position of the search_item or -1 if not found
    return found_index

# We can also implement this with first 
def binary_search_recursive(items, search_item, first, last):

    # Base case for recursion: The recursion will stop when the
    # index of the first item is greater than the index of last
    if first > last:
        return -1 # Return -1 if the search item is not found

    # Recursively call the function
    else:
        # Find the midpoint position (in the middle of the range)
        midpoint = (first + last) // 2
        
        # Compare the item at the midpoint to the search item
        if items[midpoint] == search_item:
            # If the item has been found, return the midpoint position
            return midpoint
     
        # Check if the item at the midpoint is less than the search item 
        elif items[midpoint] < search_item:
            # Focus on the items after the midpoint
            first = midpoint + 1
            return binary_search_recursive(items, search_item, first, last)

        # Otherwise the item at the midpoint is greater than the search item
        else:
            # Focus on the items before the midpoint
            last = midpoint - 1 
            return binary_search_recursive(items, search_item, first, last)

if __name__ == "__main__":
    items = [1,4,2,6,3,7,10]
    search_index = binary_search(items, 5)
    print(search_index)
    search_index = binary_search(items, 7)
    print(search_index)

    search_index = binary_search_recursive(items, 5, 0, len(items))
    print(search_index)
    search_index = binary_search_recursive(items, 7, 0, len(items))
    print(search_index)

    
