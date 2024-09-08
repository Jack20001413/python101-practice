def is_valid_walk(walk):
    return len(walk) == 10 and walk.count("w") == walk.count("e") and walk.count("s") == walk.count("n")

walks = ['n','n','n','s','n','s','n','s','n','s']
result = is_valid_walk(walks)
print(result)

