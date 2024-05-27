def hello():
    print("Testing Pipeline for Build Autotrigger via Jenkins file for multi-branch pipeline ...")
    print("\tSuccess\t\t...\n\tHello Krishna\t!!!")
    return 0

if __name__ == '__main__':
    hello()


# triggers {
#         cron('H/5 * * * *')
#     }
