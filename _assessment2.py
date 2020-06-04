from tkinter import Tk, Canvas, PhotoImage, Button, Label, Toplevel
from random import randint
import time


def configure_window():
    global window
    window = Tk()
    window.configure(background="#cafafe")
    window.title("M Y   G A M E")
    ws = window.winfo_screenwidth()
    hs = window.winfo_screenheight()
    window.geometry("%sx%s" % (ws, hs))
    window.lift()
    window.focus_force()
    global canvas, plane_body, plane_wing1, plane_wing2, plane_tail
    canvas = Canvas(window, bg="#cafafe", width=window.winfo_screenwidth(),
                    height=window.winfo_screenheight())
    plane_body = canvas.create_polygon(40, 296, 126, 296, 146, 312,
                                       134, 316, 66, 316, fill="red")
    plane_wing1 = canvas.create_polygon(78, 315, 114, 315, 74, 335,
                                        57, 335, fill="grey")
    plane_wing2 = canvas.create_polygon(81, 296, 68, 284, 84, 284,
                                        110, 296, fill="grey")
    plane_tail = canvas.create_polygon(40, 296, 32, 280, 46, 280,
                                       66, 296, fill="grey")
    canvas.pack()
    global width, height
    width = window.winfo_screenwidth()
    height = window.winfo_screenheight() - 60
    global cloud_1, cloud_2, cloud_3, cloud_4, cloud_5, cloud_6
    cloud_1 = canvas.create_oval(20, 10, 252, 60, fill="white",
                                 outline="white")
    cloud_2 = canvas.create_oval(272, 10, 504, 60, fill="white",
                                 outline="white")
    cloud_3 = canvas.create_oval(524, 10, 756, 60, fill="white",
                                 outline="white")
    cloud_4 = canvas.create_oval(776, 10, 1008, 60, fill="white",
                                 outline="white")
    cloud_5 = canvas.create_oval(1028, 10, 1260, 60, fill="white",
                                 outline="white")
    cloud_6 = canvas.create_oval(1280, 10, 1512, 60, fill="white",
                                 outline="white")
    canvas.pack()
    global obstacle
    obstacle = []
    global width_obstacle, height_obstacle, distance, start_pos_x, start_pos_y
    for i in range(0, 5):
        width_obstacle = randint(20, 30)
        height_obstacle = randint(100, 250)
        distance = randint(270, 300)
        start_pos_x = randint(1700 + i*distance, 1800 + i*distance)
        start_pos_y = randint(40, height - height_obstacle)
        obstacle.append(canvas.create_rectangle(start_pos_x, start_pos_y,
                                                start_pos_x + width_obstacle,
                                                start_pos_y + height_obstacle,
                                                fill="red"))
    global stars
    stars = []
    global width_star, height_star, distance_stars
    global start_pos_star_x, start_pos_star_y
    for i in range(0, 3):
        width_star = 20
        height_star = 20
        distance_stars = randint(400, 500)
        start_pos_star_x = randint(1800 + i*distance_stars,
                                   2000 + i*distance_stars)
        start_pos_star_y = randint(70, height - 70)
        stars.append(canvas.create_oval(start_pos_star_x, start_pos_star_y,
                                        start_pos_star_x + width_star,
                                        start_pos_star_y + height_star,
                                        fill="yellow"))
    global score_text, level_score
    score_text = canvas.create_text(width/2 - 400, 20, text="Score: 0",
                                    font="Times 20 italic bold")
    level_score = canvas.create_text(width/2 + 200, 20, text="Level: 1",
                                     font="Times 20 italic bold")


def keyboard():
    window.bind("<Up>", move_up)
    window.bind("<KeyRelease-Up>", stop_move)
    window.bind("<Down>", move_down)
    window.bind("<KeyRelease-Down>", stop_move)
    window.bind("p", pause)
    window.bind("u", unpause)
    window.bind("b", boss)
    window.bind("cheat", cheat)
    window.bind("harder", harder)
    window.bind("s", plane_increase_speed)
    window.bind("R", restart)
    window.bind("q", quit)
    window.focus_set()


def global_variables():
    global score, level
    score = 0
    level = 1
    global up, down
    up = False
    down = False
    global level_up
    level_up = False
    global current_speed_plane
    current_speed_plane = 0
    global current_speed_obstacles
    current_speed_obstacles = 0
    global current_speed_stars
    current_speed_stars = 0
    global current_speed_clouds
    current_speed_clouds = 0
    global speed_decrease
    speed_decrease = 3
    global pos_body, pos_wing1, pos_wing2, pos_tail
    pos_body = []
    pos_wing1 = []
    pos_wing2 = []
    pos_tail = []
    global pause_text
    pause_text = None
    global list_of_scores
    list_of_scores = list()
    global speed_change
    speed_change = 3
    global pos_stars, pos_obstacles
    pos_stars = [0, 0, 0]
    pos_obstacles = [0, 0, 0, 0, 0]
    global speed, up_pressed, down_pressed
    speed = 15
    up_pressed = False
    down_pressed = False
    global game_paused, obstacle_speed, star_speed, game_over, game_paused
    game_paused = True
    obstacle_speed = 7
    star_speed = 7
    game_over = False
    global cloud_speed
    cloud_speed = 7
    global pos_cloud_1, pos_cloud_2, pos_cloud_3, pos_cloud_4, pos_cloud_5
    global pos_cloud_6
    pos_cloud_1 = []
    pos_cloud_2 = []
    pos_cloud_3 = []
    pos_cloud_4 = []
    pos_cloud_5 = []
    pos_cloud_6 = []


def restart(event):
    window.destroy()
    init()


def boss(event):
    window1 = Toplevel()
    window1.title("The best mathematician")
    window1.geometry("%sx%s" % (window1.winfo_screenwidth(),
                                window1.winfo_screenheight()))
    canvas1 = Canvas(window1, height=window1.winfo_screenheight(),
                     width=window1.winfo_screenwidth())
    global image_of_sergei
    image_of_sergei = PhotoImage(file="sergei.png")
    pause(event)
    label = Label(window1, image=image_of_sergei, width="1280", height="720")
    label.place(x=0, y=0)
    window1.mainloop()


def plane_increase_speed(event):
    global speed
    if not game_over:
        speed += 3


def quit(event):
    window.destroy()


def pause(event):
    global speed, speed_change, star_speed, cloud_speed
    global obstacle_speed, pause_text, game_over, game_paused
    global current_speed_plane, current_speed_obstacles
    global current_speed_stars, current_speed_clouds
    current_speed_plane = speed
    current_speed_obstacles = obstacle_speed
    current_speed_stars = star_speed
    current_speed_clouds = cloud_speed
    if not game_over and game_paused:
        speed = 0
        speed_change = 0
        star_speed = 0
        cloud_speed = 0
        obstacle_speed = 0
        pause_text = canvas.create_text(width/2, height/2, fill="black",
                                        font="Times 20 italic bold",
                                        text="Paused!")
        game_paused = False


def unpause(event):
    global speed, speed_change, star_speed, cloud_speed, obstacle_speed
    global game_over, game_paused
    global current_speed_plane, current_speed_obstacles
    global current_speed_stars, current_speed_clouds
    if not game_over and not game_paused:
        for i in range(3):
            canvas.itemconfig(pause_text, text=3 - i)
            window.update()
            time.sleep(1)
        canvas.itemconfig(pause_text, text=" ")
        game_paused = True
        # speed = 15
        # speed_change = 3
        # star_speed = 7
        # cloud_speed = 7
        # obstacle_speed = 7
        speed = current_speed_plane
        speed_change = 3
        star_speed = current_speed_stars
        obstacle_speed = current_speed_obstacles
        window.after(30, unpause(event))


def cheat(event):
    global speed, speed_change, star_speed, cloud_speed, obstacle_speed
    global game_over
    if not game_over:
        while speed_change > 0 and cloud_speed > 0 and obstacle_speed > 0:
            speed += 3
            speed_change -= 1
            star_speed += 2
            cloud_speed -= 2
            obstacle_speed -= 2
            break


def harder(event):
    global speed, speed_change, star_speed, cloud_speed, obstacle_speed
    global game_over
    if not game_over:
        speed = 15
        speed_change += 2
        star_speed += 2
        cloud_speed += 2
        obstacle_speed += 2


def move_up(event):
    global up, down
    up = True
    down = False


def move_down(event):
    global up, down
    up = False
    down = True


def stop_move(event):
    global up, down
    up = False
    down = False


def overlapping(a, b):
    if a[0] < b[2] and a[2] > b[0] and a[1] < b[3] and a[3] > b[1]:
        return True
    return False


def move_plane():
    global game_over
    if up:
        move_by = -speed
    elif down:
        move_by = speed
    else:
        move_by = 0
    global pos_wing1, pos_wing2
    pos_wing1 = canvas.coords(plane_wing1)
    pos_wing2 = canvas.coords(plane_wing2)
    if pos_wing1[5] + move_by > height:
        move_by = 0
        pos_wing1[5] = height
        pos_wing1[7] = height
    if pos_wing2[3] + move_by < 0:
        move_by = 0
        pos_wing2[3] = 0
        pos_wing2[5] = 0
    canvas.move(plane_body, 0, move_by)
    canvas.move(plane_wing1, 0, move_by)
    canvas.move(plane_wing2, 0, move_by)
    canvas.move(plane_tail, 0, move_by)
    pos_body = canvas.coords(plane_body)
    pos_wing1 = canvas.coords(plane_wing1)
    pos_wing2 = canvas.coords(plane_wing2)
    pos_tail = canvas.coords(plane_tail)
    for i in range(0, 5):
        if overlapping(pos_body, canvas.coords(obstacle[i])):
            game_over = True
            canvas.create_text(width/2, height/2, fill="black",
                               font="Times 20 italic bold",
                               text="Game Over!")
        elif overlapping(pos_wing1, canvas.coords(obstacle[i])):
            game_over = True
            canvas.create_text(width/2, height/2, fill="black",
                               font="Times 20 italic bold",
                               text="Game Over!")
        elif overlapping(pos_wing2, canvas.coords(obstacle[i])):
            game_over = True
            canvas.create_text(width/2, height/2, fill="black",
                               font="Times 20 italic bold",
                               text="Game Over!")
        elif overlapping(pos_tail, canvas.coords(obstacle[i])):
            game_over = True
            canvas.create_text(width/2, height/2, fill="black",
                               font="Times 20 italic bold",
                               text="Game Over!")
    global score
    for i in range(0, 3):
        if overlapping(pos_body, canvas.coords(stars[i])):
            score += 10
            canvas.itemconfig(score_text, text="Score: " + str(score))
            width_star = 20
            height_star = 20
            start_pos_star_x = randint(1300 + i*distance_stars,
                                       1500 + i*distance_stars)
            start_pos_star_y = randint(50, height - 70)
            canvas.coords(stars[i], start_pos_star_x, start_pos_star_y,
                          start_pos_star_x + width_star,
                          start_pos_star_y + height_star)
        if overlapping(pos_wing1, canvas.coords(stars[i])):
            score += 10
            canvas.itemconfig(score_text, text="Score: " + str(score))
            width_star = 20
            height_star = 20
            start_pos_star_x = randint(1300 + i*distance_stars,
                                       1500 + i*distance_stars)
            start_pos_star_y = randint(50, 700)
            canvas.coords(stars[i], start_pos_star_x, start_pos_star_y,
                          start_pos_star_x + width_star,
                          start_pos_star_y + height_star)
        if overlapping(pos_wing2, canvas.coords(stars[i])):
            score += 10
            canvas.itemconfig(score_text, text="Score: " + str(score))
            width_star = 20
            height_star = 20
            start_pos_star_x = randint(1300 + i*distance_stars,
                                       1500 + i*distance_stars)
            start_pos_star_y = randint(50, 700)
            canvas.coords(stars[i], start_pos_star_x, start_pos_star_y,
                          start_pos_star_x + width_star,
                          start_pos_star_y + height_star)
        if overlapping(pos_tail, canvas.coords(stars[i])):
            score += 10
            canvas.itemconfig(score_text, text="Score: " + str(score))
            width_star = 20
            height_star = 20
            start_pos_star_x = randint(1300 + i*distance_stars,
                                       1500 + i*distance_stars)
            start_pos_star_y = randint(50, 700)
            canvas.coords(stars[i], start_pos_star_x, start_pos_star_y,
                          start_pos_star_x + width_star,
                          start_pos_star_y + height_star)
    global level
    level = int(score/50) + 1
    canvas.itemconfig(level_score, text="Level: " + str(level))
    global pos_cloud_1, pos_cloud_2, pos_cloud_3, pos_cloud_4
    global pos_cloud_5, pos_cloud_6
    pos_cloud_1 = canvas.coords(cloud_1)
    pos_cloud_2 = canvas.coords(cloud_2)
    pos_cloud_3 = canvas.coords(cloud_3)
    pos_cloud_4 = canvas.coords(cloud_4)
    pos_cloud_5 = canvas.coords(cloud_5)
    pos_cloud_6 = canvas.coords(cloud_6)
    if overlapping(pos_body, pos_cloud_1):
        game_over = True
        canvas.create_text(width/2, height/2, fill="black",
                           font="Times 20 italic bold", text="Game Over!")

    if overlapping(pos_body, pos_cloud_2):
        game_over = True
        canvas.create_text(width/2, height/2, fill="black",
                           font="Times 20 italic bold", text="Game Over!")
    if overlapping(pos_body, pos_cloud_3):
        game_over = True
        canvas.create_text(width/2, height/2, fill="black",
                           font="Times 20 italic bold", text="Game Over!")

    if overlapping(pos_body, pos_cloud_4):
        game_over = True
        canvas.create_text(width/2, height/2, fill="black",
                           font="Times 20 italic bold", text="Game Over!")

    if overlapping(pos_body, pos_cloud_5):
        game_over = True
        canvas.create_text(width/2, height/2, fill="black",
                           font="Times 20 italic bold", text="Game Over!")

    if overlapping(pos_body, pos_cloud_6):
        game_over = True
        canvas.create_text(width/2, height/2, fill="black",
                           font="Times 20 italic bold", text="Game Over!")

    if overlapping(pos_wing2, pos_cloud_1):
        game_over = True
        canvas.create_text(width/2, height/2, fill="black",
                           font="Times 20 italic bold", text="Game Over!")

    if overlapping(pos_wing2, pos_cloud_2):
        game_over = True
        canvas.create_text(width/2, height/2, fill="black",
                           font="Times 20 italic bold", text="Game Over!")

    if overlapping(pos_wing2, pos_cloud_3):
        game_over = True
        canvas.create_text(width/2, height/2, fill="black",
                           font="Times 20 italic bold", text="Game Over!")

    if overlapping(pos_wing2, pos_cloud_4):
        game_over = True
        canvas.create_text(width/2, height/2, fill="black",
                           font="Times 20 italic bold", text="Game Over!")

    if overlapping(pos_wing2, pos_cloud_5):
        game_over = True
        canvas.create_text(width/2, height/2, fill="black",
                           font="Times 20 italic bold", text="Game Over!")

    if overlapping(pos_wing2, pos_cloud_6):
        game_over = True
        canvas.create_text(width/2, height/2, fill="black",
                           font="Times 20 italic bold", text="Game Over!")

    if overlapping(pos_tail, pos_cloud_1):
        game_over = True
        canvas.create_text(width/2, height/2, fill="black",
                           font="Times 20 italic bold", text="Game Over!")

    if overlapping(pos_tail, pos_cloud_2):
        game_over = True
        canvas.create_text(width/2, height/2, fill="black",
                           font="Times 20 italic bold", text="Game Over!")

    if overlapping(pos_tail, pos_cloud_3):
        game_over = True
        canvas.create_text(width/2, height/2, fill="black",
                           font="Times 20 italic bold", text="Game Over!")

    if overlapping(pos_tail, pos_cloud_4):
        game_over = True
        canvas.create_text(width/2, height/2, fill="black",
                           font="Times 20 italic bold", text="Game Over!")

    if overlapping(pos_tail, pos_cloud_5):
        game_over = True
        canvas.create_text(width/2, height/2, fill="black",
                           font="Times 20 italic bold", text="Game Over!")

    if overlapping(pos_tail, pos_cloud_6):
        game_over = True
        canvas.create_text(width/2, height/2, fill="black",
                           font="Times 20 italic bold", text="Game Over!")


def move_obstacles():
    global game_over
    global obstacle_speed, obstacle, pos_obstacles
    canvas.pack()
    for i in range(0, 5):
        canvas.move(obstacle[i], -obstacle_speed -
                    int(speed_change*(level - 1)), 0)
        pos_obstacles[i] = canvas.coords(obstacle[i])
        if pos_obstacles[i][2] < 0:
            width_obstacle = randint(20, 30)
            height_obstacle = randint(100, 250)
            start_pos_x = randint(2000, 2100)
            start_pos_y = randint(100, height - height_obstacle)

            canvas.coords(obstacle[i], start_pos_x, start_pos_y,
                          start_pos_x + width_obstacle,
                          start_pos_y + height_obstacle)


def move_stars():
    global game_over
    global star_speed, stars, pos_stars
    canvas.pack()
    for i in range(0, 3):
        canvas.move(stars[i], -star_speed -
                    int(speed_change*(level - 1)), 0)
        pos_stars[i] = canvas.coords(stars[i])
        if pos_stars[i][2] < 0:
            width_star = 20
            height_star = 20
            start_pos_star_x = randint(1800 + i*distance_stars,
                                       2000 + i*distance_stars)
            start_pos_star_y = randint(70, height - 70)
            canvas.coords(stars[i], start_pos_star_x, start_pos_star_y,
                          start_pos_star_x + width_star,
                          start_pos_star_y + height_star)


def move_clouds():
    global game_over, level
    global cloud_1, cloud_2, cloud_3, cloud_4, cloud_5, cloud_speed
    canvas.pack()
    canvas.move(cloud_1, -cloud_speed - int(speed_change*(level - 1)), 0)
    canvas.move(cloud_2, -cloud_speed - int(speed_change*(level - 1)), 0)
    canvas.move(cloud_3, -cloud_speed - int(speed_change*(level - 1)), 0)
    canvas.move(cloud_4, -cloud_speed - int(speed_change*(level - 1)), 0)
    canvas.move(cloud_5, -cloud_speed - int(speed_change*(level - 1)), 0)
    canvas.move(cloud_6, -cloud_speed - int(speed_change*(level - 1)), 0)
    pos_cloud_1 = canvas.coords(cloud_1)
    pos_cloud_2 = canvas.coords(cloud_2)
    pos_cloud_3 = canvas.coords(cloud_3)
    pos_cloud_4 = canvas.coords(cloud_4)
    pos_cloud_5 = canvas.coords(cloud_5)
    pos_cloud_6 = canvas.coords(cloud_6)
    if pos_cloud_1[2] < 0:
        canvas.coords(cloud_1, width, 10, width + 232, 60)
    if pos_cloud_2[2] < 0:
        canvas.coords(cloud_2, width, 10, width + 232, 60)
    if pos_cloud_3[2] < 0:
        canvas.coords(cloud_3, width, 10, width + 232, 60)
    if pos_cloud_4[2] < 0:
        canvas.coords(cloud_4, width, 10, width + 232, 60)
    if pos_cloud_5[2] < 0:
        canvas.coords(cloud_5, width, 10, width + 232, 60)
    if pos_cloud_6[2] < 0:
        canvas.coords(cloud_6, width, 10, width + 232, 60)


def leaderboard():
    global score, list_of_scores
    with open("leader_board.txt", "a") as file:
        file.write(str(score) + "\n")

    # global list_of_scores
    # array = []
    # with open ("leader_board.txt", "r") as file:
    # 	list_of_scores = file.readlines()
    # 	array.append(list_of_scores)
    # array.sort()
    # array_1 = array.read()
    # with open ("leader_board.txt", "w") as file:
    # 	file.write((int(line) + "\n") for line in array_1)

    with open("leader_board.txt", "r") as file:

        for line in file.readlines():
            list_of_scores.append(int(line))
        list_of_scores.sort()
        list_of_scores = list_of_scores[::-1]

    with open("leader_board.txt", "w") as file:
        counter = 0
        for number in list_of_scores:
            if counter == 5:
                break
            else:
                file.write(str(number) + '\n')
                counter += 1


def movement():
    global game_over
    move_plane()
    move_obstacles()
    move_stars()
    move_clouds()
    if not game_over:
        window.after(60, movement)
    else:
        leaderboard()


def init():
    global_variables()
    configure_window()
    keyboard()
    movement()
    window.mainloop()

# init()
