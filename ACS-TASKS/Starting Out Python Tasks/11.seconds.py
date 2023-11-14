#input the time in "hour:minute:seconds" format
time_input = input("Enter time: ")

#splits the input into hours, minutes, and seconds
time_parts = time_input.split(':')

#checks if the input format is correct
if len(time_parts) != 3:
    print("Invalid input format. Please use 'x:x:x' format.")
else:
    try:
        hours = int(time_parts[0])
        minutes = int(time_parts[1])
        seconds = int(time_parts[2])

        #calculates the total number of seconds
        total_seconds = (hours * 3600) + (minutes * 60) + seconds

        #outputs the total number of seconds
        print("Total seconds:", total_seconds)
    except ValueError:
        print("Invalid input. Please enter valid integers for hours, minutes, and seconds.")
