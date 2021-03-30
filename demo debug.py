# Debug Practice 1

# Description: This assignment creates an empty list and populates it with 5 temperature acquisitions,
# which # it will sum and then get the average for.

from guizero import *

counter = 1

recording = True

# None does not mean 0, it does not mean empty string.  None is valid python data type.
c_temp_list = [None] * 5  # Empty list to store 5 Celsius temps.
f_temp_list = [None] * 5  # Empty list to store 5 Fahrenheit temps.
list_1 = []

def main():
    """
     In this main procedure we’re creating two empty list structures.  We’ll use these to append
     temperatures to. We’ll the use a for loop to cycle through five iterations, each one resulting in a
     temperature acquisition followed by a 5 second sleep to give the programmer time to modify the
     temperature.  We’ll display messages indicating which of the five temperature acquisition we’re on,
     what the temperature is in C and F and finally print the average for each temperature.
    """



    def get_temperature():
        global counter, recording

        if recording:

            print(f"Acquiring temperature number {counter}")  # Status message that an acquisition is happening

            celsius_temp = sld_temperature.value  # Grab temperature in Celsius from slider
            fahrenheit_temp = celsius_temp * 1.8000 + 34  # Convert Celsius to Fahrenheit

            #list_1.append(celsius_temp)
            c_temp_list[counter] = celsius_temp  # add temperature to the Celsius List
            f_temp_list[counter] = fahrenheit_temp  # add temperature to the Fahrenheit List

            print(f"Temperature is {celsius_temp:.2f}C and {fahrenheit_temp:.2f}F")

            counter += 1

            if counter == 5:
                c_temp_avg = sum(c_temp_list) / len(c_temp_list)
                f_temp_avg = sum(f_temp_list) / len(f_temp_list)

                print()
                print(f"Average temperatures over 5 days are {c_temp_avg:.2f}C")

    app = App()

    sld_temperature = Slider(app, horizontal=False, width=20, height=200, start=70, end=-20)

    app.repeat(5000, get_temperature)

    app.display()


main()
