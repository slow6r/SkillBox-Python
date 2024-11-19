def tpl_sort(tpl):
    if all(isinstance(x, int) for x in tpl):
        return tuple(sorted(tpl))
    return tpl

# Пример вызова
tpl = (6, 3, -1, 8, 4, 10, -5)
print(tpl_sort(tpl))
tpl_invalid = (6, "a", -1)
print(tpl_sort(tpl_invalid))
