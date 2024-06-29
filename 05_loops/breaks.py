while True:
    line = input('> ')
    if line[0] == '#':
        continue # ends current iteration and jumd to the top of the loop and starts the next iteration
        # continue is skipping TO THE TOP of the loop
    if line == "done":
        break # break escapes the block, get out of that loop
        # break is skipping to the OUT of the loop
    print(line)
print('done') 