# This is the code used to create the helper functions used in the index route to group cars into chunks of 3.
# This is used to help the index route render the cars in rows of 3.

def group_list(lst, n):
    """
    Yield successive n-sized chunks from lst.

    Parameters:
    lst (list): The list to be divided into chunks.
    n (int): The size of each chunk.

    Yields:
    list: A chunk of the original list with a maximum size of n.
    """
    for i in range(0, len(lst), n):
        yield lst[i:i + n]
