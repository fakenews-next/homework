filename = 'demo.py'
with open(filename, 'r', encoding='UTF-8') as fp:
    lines = fp.readlines()                             #将demo.py每一行内容记入lines中
    maxLength = len(max(lines, key=len))               #统计最长的行的长度，方便填充空格以致对齐

lines = [line.rstrip().ljust(maxLength)+'#'+str(index)+'\n' #rstrip() 删除 string 字符串末尾的指定字符（默认为空格）
    for index, line in enumerate(lines)]                    # ljust() 方法返回一个原字符串左对齐,并使用空格填充至指定长度的新字符串
with open(filename[:-3]+'_new.py', 'w') as fp:
    fp.writelines(lines)