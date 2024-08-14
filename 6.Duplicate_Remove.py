def dup_remove():
    with_dup = input().split(" ")
    print(with_dup)
    without_dup = []
    for i in with_dup:
        if i not in without_dup:
            without_dup.append(i)
    print(without_dup)


dup_remove()
