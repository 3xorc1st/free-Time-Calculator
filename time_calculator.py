def add_time(start, duration, day=None):
    # Parse start time
    time_part, period = start.split()
    start_hour, start_minute = map(int, time_part.split(':'))
    
    # Parse duration
    duration_hour, duration_minute = map(int, duration.split(':'))
    
    # Convert start time to 24-hour format for easier calculation
    if period == 'AM':
        if start_hour == 12:
            start_hour = 0
    else:  # PM
        if start_hour != 12:
            start_hour += 12
    
    # Add duration
    total_minutes = start_minute + duration_minute
    total_hours = start_hour + duration_hour
    
    # Handle minute overflow
    if total_minutes >= 60:
        total_hours += total_minutes // 60
        total_minutes = total_minutes % 60
    
    # Calculate days passed
    days_passed = total_hours // 24
    total_hours = total_hours % 24
    
    # Convert back to 12-hour format
    if total_hours == 0:
        display_hour = 12
        display_period = 'AM'
    elif total_hours < 12:
        display_hour = total_hours
        display_period = 'AM'
    elif total_hours == 12:
        display_hour = 12
        display_period = 'PM'
    else:
        display_hour = total_hours - 12
        display_period = 'PM'
    
    # Format the time
    result = f'{display_hour}:{total_minutes:02d} {display_period}'
    
    # Add day of week if provided
    if day is not None:
        days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        
        # Normalize the input day (case insensitive)
        day_lower = day.lower()
        current_day_index = None
        
        for i, d in enumerate(days_of_week):
            if d.lower() == day_lower:
                current_day_index = i
                break
        
        # Calculate new day
        new_day_index = (current_day_index + days_passed) % 7
        new_day = days_of_week[new_day_index]
        
        result += f', {new_day}'
    
    # Add days later information
    if days_passed == 1:
        result += ' (next day)'
    elif days_passed > 1:
        result += f' ({days_passed} days later)'
    
    return result


# Test cases
if __name__ == '__main__':
    print(add_time('3:30 PM', '2:12'))
    print(add_time('11:55 AM', '3:12'))
    print(add_time('2:59 AM', '24:00'))
    print(add_time('11:59 PM', '24:05'))
    print(add_time('8:16 PM', '466:02'))
    print(add_time('3:30 PM', '2:12', 'Monday'))
    print(add_time('2:59 AM', '24:00', 'saturDay'))
    print(add_time('11:59 PM', '24:05', 'Wednesday'))
    print(add_time('8:16 PM', '466:02', 'tuesday'))
    print(add_time('11:43 AM', '00:20'))
    print(add_time('10:10 PM', '3:30'))
    print(add_time('11:43 PM', '24:20', 'tueSday'))
    print(add_time('6:30 PM', '205:12'))
    print(add_time('3:00 PM', '3:10'))
