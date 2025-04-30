if google_t:
    if coord_x >= limit_left:
        left = True
    elif coord_x <= limit_right:
        right = True

elif kb_t or calc_t:
    if coord_x < limit_left and coord_x > limit_right and coord_y < 70 and coord_y > 0:
        center_all = True
    if coord_x >= limit_left:
        left = True
    elif coord_x <= limit_right:
        right = True
    elif coord_y <= limit_top:
        top = True
    elif coord_y >= limit_bot:
        bottom = True
else:
    if coord_x >= limit_left:
        left = True
    elif coord_x <= limit_right:
        right = True
    elif coord_y <= limit_top:
        top = True
    elif coord_y >= limit_bot:
        bottom = True

