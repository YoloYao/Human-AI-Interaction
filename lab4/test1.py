print('These are your booking details : You have booked ' + str(assigned) +
      ' seat(s). \ nIf you are happy to proceed with your booking click enter or type \'cancel \' to cancel your booking ')
while True:
    reply = input()
    if reply == '':
        # assigns a random booking reference for the user
        booking_reference = random.randint(1000, 9999)
        print('Booking confirmed ! Booking reference : ' + str(booking_reference))
