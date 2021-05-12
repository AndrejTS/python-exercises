def transfuse(from_bucket, to_bucket):
    to_bucket['content'] = to_bucket['content'] + from_bucket['content']
    if to_bucket['content'] > to_bucket['capacity']:
        from_bucket['content'] = to_bucket['content'] - to_bucket['capacity']
        to_bucket['content'] = to_bucket['capacity'] 
    else:
        from_bucket['content'] = 0


def measure(bucket_one, bucket_two, goal, start_bucket):
    b1 = {}
    b2 = {}
    b1['capacity'] = bucket_one
    b2['capacity'] = bucket_two
    if start_bucket == 'one':
        b1['content'] = bucket_one
        b2['content'] = 0
        start_bucket = b1
        non_start_bucket = b2
    else:
        b1['content'] = 0
        b2['content'] = bucket_two
        start_bucket = b2
        non_start_bucket = b1
    moves = 1

    while True:
        if b1['content'] == goal:
            desired = 'one'
            residue = b2['content']
            break
        if b2['content'] == goal:
            desired = 'two'
            residue = b1['content']
            break
        # filling non-start bucket if its capacity is equal to goal
        if non_start_bucket['capacity'] == goal:
           non_start_bucket['content'] = goal 
        # filling the start bucket if it is empty
        elif start_bucket['content'] == 0:
            start_bucket['content'] = start_bucket['capacity']
        # emptying the non-start bucket if it is full
        elif non_start_bucket['content'] == non_start_bucket['capacity']:
            non_start_bucket['content'] = 0
        # otherwise transfer
        else:
            transfuse(start_bucket, non_start_bucket)
        moves += 1
    return (moves, desired, residue)

