def check_task_tracking(tasklist):
    if tasklist == "":
        raise Exception("Text doesn't include #TODO string")
    return "#TODO" in tasklist