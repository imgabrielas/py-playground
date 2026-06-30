import turtle as t

def draw_tree(branch_len, angle):
    if branch_len < 5:
        return

    # Brown trunk and main branches
    if branch_len > 15:
        t.pencolor("saddlebrown")
    else:
        t.pencolor("forestgreen")

    # Thicker trunk, thinner branches
    t.pensize(max(1, branch_len / 4))

    t.forward(branch_len)

    t.right(angle)
    draw_tree(branch_len * 0.75, angle)

    t.left(angle * 2)
    draw_tree(branch_len * 0.75, angle)

    t.right(angle)
    t.backward(branch_len)

t.speed("fastest")
t.left(90)

t.penup()
t.backward(200)
t.pendown()

draw_tree(30, 30)

t.done()