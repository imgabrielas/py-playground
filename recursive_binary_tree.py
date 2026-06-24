import turtle as t

def draw_tree(branch_len, angle):
    if branch_len < 5:
        return
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

draw_tree(20, 30)

t.done()
