from plyer import notification
import datetime
from playsound import playsound


def get_patient_name():
    return input("Please enter your name: ")

def calculate_BMI(kg,meters):
    bmi=kg/(meters*meters)
    return bmi

#One of the features we wanted to add in our program
def get_patient_weight_and_height():
    info=[]
    kg=float(input("what is your weight(kg):"))
    meters=float(input("what is your height(meter):"))
    info.append({
        'weight':kg,
        'height':meters
    })
    bmi=calculate_BMI(kg,meters)
    format_bmi = "{:.2f}".format(bmi)
    return format_bmi


def get_medicine_schedule():
    medicines = []
    while True:
        #The program will continue to loop until the user types "done" in the medicine_name input
        medicine_name = input("Please enter the name of your medicine (or type 'done' if you're finished): ")
        if medicine_name.lower() == 'done':
            break
        dosage = input("Please enter the dosage for this medicine: ")
        frequency = int(input("How many times will you drink this medicine for a day (in hours): "))
        start_time = input("When will you start drinking this medicine (in format YYYY-MM-DD HH:MM): ")
        start_time = datetime.datetime.strptime(start_time, '%Y-%m-%d %H:%M')
        medicines.append({
            'name': medicine_name,
            'dosage': dosage,
            'frequency': frequency,
            'start_time': start_time
        })
    return medicines

def get_next_checkup_date():
    next_checkup_date = input("When is the day of your next checkup (in format YYYY-MM-DD): ")
    next_checkup_date = datetime.datetime.strptime(next_checkup_date, '%Y-%m-%d')
    return next_checkup_date

def play_sound(Announcement):
    playsound(Announcement)

def main():
    patient_name = get_patient_name()
    body_weight_tracker=get_patient_weight_and_height()
    medicine_schedule = get_medicine_schedule()
    next_checkup_date = get_next_checkup_date()
    #All the inputs made typed by the user is printed after answering all the required questions for this program to run
    print("Your name is " +str(patient_name))
    print("your BMI is"+str(body_weight_tracker))
    print(medicine_schedule)
    print("Your next checkup is on "+str(next_checkup_date))
    
   

    while True:
        current_time = datetime.datetime.now()
        if current_time>= next_checkup_date:
            notification.notify(
                title="Time to consult your Doctor!",
                message=f"{patient_name}, today is the day of your next checkup.",
                timeout=10
                )
            play_sound(r'C:\Users\Anton\Music\Announcement.wav')

        for medicine in medicine_schedule:
            while current_time < medicine['start_time']:
                # Wait until it's time to start
                current_time = datetime.datetime.now()
            
            while current_time >= medicine['start_time']:
                # Generate notification
                notification.notify(
                    title=f"Its Time to take {medicine['name']}!",
                    message=f"{patient_name}, please take {medicine['dosage']} of {medicine['name']} now.",
                    timeout=10
                )
                play_sound(r'C:\Users\Anton\Music\Announcement.wav')
                medicine['start_time'] += datetime.timedelta(hours=medicine['frequency'])  # Schedule the next dose

                # Update current time to avoid looping too fast
                current_time = datetime.datetime.now()
            

if __name__ == '__main__':
    main()

