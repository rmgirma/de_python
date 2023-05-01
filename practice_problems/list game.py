def transformer(target, sample):
    for i in sample:
        if i not in target:
            target.append(i)
    i = 0
    while i < len(target):
        if target[i] not in sample:
            target.remove(target[i])
        else:
            i+= 1
    return target

sample = ["apple", "pear", "pineapple", "blue", "red", "pink"]
target = ["apple", "orange", "ananas", "pear"]   

result = transformer(sample, target)
print(sorted(result))

