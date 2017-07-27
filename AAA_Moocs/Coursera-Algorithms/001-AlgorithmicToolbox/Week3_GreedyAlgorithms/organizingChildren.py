import operator

def group_children(children, age_diff=12):
    """
    Accepts a dict of children {Name, Age in month} and groups them given a 
    maximum age difference
    """
    groups = {}

    # Sort children by age
    sorted_children  = sorted(children.items(), key=operator.itemgetter(1), reverse=True)
    # print(sorted_children)

    while sorted_children:
        name, age = sorted_children.pop()
        # print(name, age, 'Is looking for a group')
        # Entering the first child
        if len(groups)==0:
            groups[0] = {name:age}
            # print(groups)
        
        # If there are already children assigned to groups
        for group in groups:
            if (age - min(groups[group].values())) < age_diff:
                # print(age - min(groups[group].values()))
                # The minimum age of this group is within acceptable limits
                groups[group].update({name:age})
                # print('Added child to existing group')asdfasdf
                del name, age
                # print(groups[group])
            else:
                continue
                  
        
        # Check if the child has not yet been added to any existing group
        if 'name' in locals():
            # print(name, age, 'beeing matched to new group')
            groups[len(groups)] = {name:age}
            

    print(groups)



children = {
    'Hans':38,
    'Wustl':44,
    'Nadia':54,
    'Alex': 60, 
    'Marco': 29, 
    'Matthias': 70,
    'Hans2':38,
    'Wustl2':44,
    'Nadia2':54,
    'Alex2': 60, 
    'Marco2': 29, 
    'Matthias2': 70,
    'Hans3':38,
    'Wustl3':44,
    'Nadia3':54,
    'Alex3': 60, 
    'Marco3': 29, 
    'Matthias3': 70,
}

group_children(children)