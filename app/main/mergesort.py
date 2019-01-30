def merge_sort_time(job_list):
    '''
        sorts the list by timestamp
    :return:
        array
    '''
    if len(job_list) > 1:
        mid = len(job_list) // 2
        lefthalf = job_list[:mid]
        righthalf = job_list[mid:]

        merge_sort_time(lefthalf)
        merge_sort_time(righthalf)

        i = 0
        j = 0
        k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i]['time'] > righthalf[j]['time']:
                job_list[k] = lefthalf[i]
                i = i + 1
            else:
                job_list[k] = righthalf[j]
                j = j + 1
            k = k + 1

        while i < len(lefthalf):
            job_list[k] = lefthalf[i]
            i = i + 1
            k = k + 1

        while j < len(righthalf):
            job_list[k] = righthalf[j]
            j = j + 1
            k = k + 1