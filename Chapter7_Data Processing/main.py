import fund_cal # import module we've been created
def main():
    t = int(input("Enter the total number of people who participate in the hospital donation event: "))
    total = fund_cal.fund(t)

    print("Total Donation Amount: ",total)

main()