import sys
print(sys.argv)
if not sys.argv:
    sys.exit(0)
args = tuple(map(lambda x: x.strip(), sys.argv[1:]))
if args[0].endswith('.html') and not args[0].startswith('index'):
    title = ' '.join(args[1:])
    base_list_item = '<li class="list-group-item">...새 산책로들도 기대해주세요</li>'
    new_list_item = f'<li class="list-group-item">{title}</li>\n'
    lines = []
    with open('index.html', 'r', encoding='utf-8') as index:
        lines = index.readlines()
        cur = lines.index(base_list_item)
        lines.insert(cur+1, new_list_item)
    with open('index.html', 'w', encoding='utf-8') as index:
        index.writelines(lines)