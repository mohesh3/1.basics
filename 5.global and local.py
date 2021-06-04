total = 100
def func():
    global total
    if total > 99:
        total = 15
print('Total = ', total)
func()
print('Total = ', total)