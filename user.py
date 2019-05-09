# user.py

def turn(*inputs):
    """
    This function is called at every frame of the simulation.
    It defines the behaviour of your two ovnis.

    {inputs} is a tuple containing the inputs sent from the game.
    The first element is an integer representing the number of the current
    frame. The first frame is 0.
    The second element is the position of your flag, represented as a 2-tuple.
    The third element is the position of the enemy flag, represented as a
    2-tuple.
    The position of the flag is (-1,-1) if it is taken.
    The fourth and fifth elements are 5-tuples containing datas of your two
    ovnis, such as the position in x and y, the velocity vector in x and y and
    a boolean value turned to true when the ovni is carrying a flag.
    The sixth and seventh elements are also 5-tuples containing the same datas
    for the two enemy ovnis.

    The two outputs are 3-tuples. They concern the behaviour of your ovnis. They
    must contain the aimed position (i.e., the direction vector of the
    acceleration force) in x and y, and the power of the motors. The power is an
    integer value from 0 to 100 or "BOOST". "BOOST" is equal to a value of
    350. You have 0.75 second of boost available and 4 seconds to reload it when
    you empty it. If the "BOOST" is not ready but you try it, the power value
    will be automatically set to 100.

    The field has a width of 10,000 and a height of 8,000. The origin is the
    bottom left corner of the field. To score points you need to capture the
    enemy flag and to bring it to your base. The team with the most points wins
    the game. The carrier of the flag can be taccled by getting hit from an ovni
    with more velocity.
    """

    # ---
    ii = inputs[0]
    flag_x, flag_y = inputs[1]
    enemy_flag_x, enemy_flag_y = inputs[2]
    ovni_1_x, ovni_1_y, ovni_1_vx, ovni_1_vy, ovni_1_flag = inputs[3]
    ovni_2_x, ovni_2_y, ovni_2_vx, ovni_2_vy, ovni_2_flag = inputs[4]
    enemy_ovni_1_x, enemy_ovni_1_y, enemy_ovni_1_vx, enemy_ovni_1_vy, enemy_ovni_1_flag = inputs[5]
    enemy_ovni_2_x, enemy_ovni_2_y, enemy_ovni_2_vx, enemy_ovni_2_vy, enemy_ovni_2_flag = inputs[6]
    # ---
    

    aimx_1, aimy_1, mag_1 = 0, 0, 0
    aimx_2, aimy_2, mag_2 = 0, 0, 0


    # ---
    return (aimx_1, aimy_1, mag_1), (aimx_2, aimy_2, mag_2)
