def bundleup(n,s):
    temp = int(s.replace('*C', ''))
    inside_temp=(temp*1.1)*1.1
    return f"{round(inside_temp, 1)}*"
print(bundleup(1, "2*C"))


