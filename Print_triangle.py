def print_hollow_triangle(n):
    if n < 1:
        print("邊長必須大於 0")
        return

    for i in range(n):
        # 左側空格，讓三角形居中
        spaces = ' ' * (n - i - 1)

        if i == 0:
            # 最上面一行：一個星星
            print(spaces + '*')
        elif i == n - 1:
            # 最底下一行：2n-1個星星
            print('*' * (2 * n - 1))
        else:
            # 中間行：一個星星 + 空格 + 一個星星
            inside_spaces = ' ' * (2 * i - 1)
            print(spaces + '*' + inside_spaces + '*')


print("輸入")
n = int(input())
print_hollow_triangle(n)

