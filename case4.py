#file = open(r"/Users/solovyovame/Downloads/q4_urls.txt")
count_lines = {}
for line in open(r'/Users/solovyovame/Downloads/q4_urls.txt'):
    clean_line = line.rstrip()
    if clean_line not in count_lines:
        count_lines[clean_line] = 0
    count_lines[clean_line] += 1


out = open(r'new.txt', "w")
sorted_lines = dict(sorted(count_lines.items(), key=lambda x: x[1], reverse=True))

for key, value in sorted_lines.items():
    out.write(f"{key}   {value}\n")

out.close()
