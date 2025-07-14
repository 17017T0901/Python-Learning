a = "Today is python first day coding challenge hope this python coding learning goes well  "
split_a = a.strip().split(" ")
non_duplicate_words = set(split_a)
res = " ".join(sorted(non_duplicate_words))
print(res)

#output
#Today challenge coding day first goes hope is learning python this well
