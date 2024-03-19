def proizv_chisel(*args):
    произведение = 1
    for число in args:
        произведение *= число
    return произведение

print(proizv_chisel(5, 6, 7))
print(proizv_chisel(2, 9))
print(proizv_chisel(5, 6, 7, 8))
