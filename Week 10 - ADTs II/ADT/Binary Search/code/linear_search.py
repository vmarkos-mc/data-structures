def linear_search_version_1(items, search_item):
       
    # Initialise the variable
    found_index = -1

    # Repeat until the end of the list is reached
    for current in range(len(items)):
                
        # Compare the item at the current index to the search item
        if items[current] == search_item:
            # If the item has been found, store the current index 
            found_index = current 

    # Return the index of the search_item or -1 if not found
    return found_index

def linear_search_version_2(items, search_item):

    found_index = -1    # Initialise the variables
    current = 0
    found = False

    # Repeat while end not reached and search item not found
    while current < len(items) and found == False:
        
        if items[current] == search_item: # If the item has been found
            found_index = current # Store the current index
            found = True # Raise the flag to stop the loop

        current = current + 1 # Go to the next index in the list

    return found_index # Return the index of the search_item or -1 if not found

if __name__ == "__main__":
    items = [1,4,2,6,3,7,10]
    linear_search_version_1(items, 5)
    linear_search_version_1(items, 7)

    linear_search_version_2(items, 5)
    linear_search_version_2(items, 7)