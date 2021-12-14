from collections import Counter

from test_input import raw

template, raw_rules = raw
rules = {a: b for a, b in (tuple(rr.split(" -> ")) for rr in raw_rules.split("\n"))}
print(rules)
for i in range(40):
    new_template = ""
    for j in range(len(template)):
        if j + 1 < len(template):
            if (lookup := template[j]+template[j+1]) in rules:
                new_template += template[j] + rules[lookup]
            else:
                new_template += template[j]
        else:
            new_template += template[j]
    template = new_template

print(template)

print(c := [b for a, b in Counter(template).most_common()])
print(c[0] - c[-1])
