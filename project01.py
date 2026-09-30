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

    if wind_speed < cut_in_speed or wind_speed >= cut_out_speed:
        return 0
    
    elif wind_speed >= rated_speed:
        return rated_power

    else:
        if interpolation == "linear":
            return (wind_speed-cut_in_speed)/(rated_speed-cut_in_speed) * rated_power
        
        elif interpolation == "cubic":
            return (wind_speed**3/rated_speed**3)* rated_power

