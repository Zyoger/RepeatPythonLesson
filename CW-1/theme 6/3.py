s = b"\xe6\x88\x81\xa3@\x89\xa2@\xa8\x96\xa4\x99@\x86\x81\xa5\x96\xa4\x99\x89\xa3\x85@\x97\x99\x96\x87\x99\x81\x94\x94" \
    b"\x89\x95\x87@\x93\x81\x95\x87\xa4\x81\x87\x85o"
message = s.decode("cp037", errors="replace")
print(message)
my_message = "Python"
my_message = my_message.encode("cp037")
print(my_message)