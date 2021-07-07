def joseph_solution_one(joseph_num_totle, joseph_num_delete):
    if joseph_num_totle == 1:
        return 0
    else:
        return (joseph_solution_one(joseph_num_totle - 1, joseph_num_delete) 
                + joseph_num_delete) % joseph_num_totle

def joseph_solution_two(joseph_num_totle, joseph_num_delete):
    joseph_list = range(joseph_num_totle)

    while True:
        if len(joseph_list) > 1:
            joseph_temporary = (joseph_num_delete 
                                - 1 
                                + joseph_temporary) % len(joseph_list)
            joseph_list.pop(joseph_temporary)
    return joseph_temporary[0]


if __name__ == '__main__':
    result = joseph_solution_one(9, 2)
    print(result + 1)
