color = dict(apple='red', banana='yellow')
color['cherry'] = 'red'
color['apple'] = 'green'

for k,v in color.items():
    print(k,v)

del color['cherry']
print(color)

color.clear()
print(color)