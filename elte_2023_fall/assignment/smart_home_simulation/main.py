from sensors.DaylightSensor import DaylightSensor


def main() -> None:
    sensor_daylight: DaylightSensor = DaylightSensor(
        123, "Daylight Sensor"
    )
    print(sensor_daylight.device_name)


if __name__ == "__main__":
    main()
