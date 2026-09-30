def power_curve(wind_speed, 
                rated_power=15, 
                cut_in_speed=3, 
                rated_speed=11, 
                cut_out_speed=25,
                interpolation="linear"
):
    """Takes wind speed and returns the power output of a wind turbine based on its power curve."""
    if interpolation not in ("linear", "cubic"):
        raise ValueError("Interpolation must be either 'linear' or 'cubic'")

    # No power is produced if the wind speed is below cut-in speed or above or equal to cut-out speed.
    if wind_speed < cut_in_speed or wind_speed >= cut_out_speed:
        return 0
    
    # Rated power is produced if the wind speed is equal to or above the rated wind speed. 
    elif wind_speed >= rated_speed:
        return rated_power

    # Between cut-in and rated speed, calculate power using the chosen interpolation method
    else:
        if interpolation == "linear":
            return (wind_speed-cut_in_speed)/(rated_speed-cut_in_speed) * rated_power
        
        elif interpolation == "cubic":
            return (wind_speed**3/rated_speed**3)* rated_power

if __name__ == "__main__":
    wind_speed = float(input("Enter wind speed: "))
    power = power_curve(wind_speed)
    print("Produced power:", power)