def main() -> None:
    hour = int(input("Starting time (hours): "))
    mins = int(input("Starting time (minutes): "))
    dura = int(input("Event duration (minutes): "))

    curr_time_in_mins: int = (hour * 60) + mins
    event_finish_in_mins: int = curr_time_in_mins + dura

    event_finish_mins: int = event_finish_in_mins % 60
    event_finish_hours: int = (event_finish_in_mins // 60) % 24

    print(f"{event_finish_hours}:{event_finish_mins}")


if __name__ == "__main__":
    main()
