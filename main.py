import datetime
import pause
def reserve_court(reservation_location, reservation_day_time):
    if reservation_location == '1':
        print("Stern Grove")
    elif reservation_location == '2':
        print("Presidio Wall")
    elif reservation_location == '3':
        print("Bay Club Gateway")

if __name__ == '__main__':
    reservation_location = input("Press 1 for Stern Grove, 2 for Presidio Wall, 3 for Bay Club Gateway\n")

    reservation_day_time_str = input("When do you want your reservation? Please enter in MM/DD/YY XX:XX\n")
    reservation_day_time = datetime.datetime.strptime(reservation_day_time_str, '%m/%d/%y %H:%M')

    rec_us_intermediate_action_day_time = reservation_day_time - datetime.timedelta(days=7)
    rec_us_action_day_time = rec_us_intermediate_action_day_time.replace(hour=8, minute=0)

    bay_club_action_day_time = reservation_day_time - datetime.timedelta(days=3)

    action_day_time = None
    if reservation_location == '1' or reservation_location == '2':
        action_day_time = rec_us_action_day_time
    elif reservation_location == '3':
        action_day_time = bay_club_action_day_time

    # test only
    test_intermediate_action_day_time = reservation_day_time - datetime.timedelta(days=7)
    test_action_day_time = test_intermediate_action_day_time.replace(hour=9, minute=57)
    action_day_time = test_action_day_time
    # end test

    pause.until(action_day_time)
    reserve_court(reservation_location, reservation_day_time)
