#simple password manager
#store, add/delete/update, and retrieve your password
#desktop application
#windows only

import pyperclip, sys, time

passwordRepo = {'GMAIL': 'samplepw1', 
                'FACEBOOK': 'samplepw2',
                'ACCOUNTX': 'samplepw3', 
                'ACCOUNTY':'samplepw4', 
                'ACCOUNTZ':'samplepw5'}
    

welcomemsg = '  That jurassic password manager you use to retrieve your passwords.  '
print(welcomemsg.center(76, '#'))
print('')
print('Helpful notes:')
print('  Enter nothing below to end program.')
print('  Type "My Accounts" to see list of accounts stored here.')
print('  Type "Update" to update your password/s in the database.')

while True:
    print('')
    print('')
    print ('GET PASSWORD FOR YOUR ACCOUNT (for other actions, see notes above): ')
    account = input()
    account = account.upper()

    if account == 'MY ACCOUNTS':
        dummyDict = []
        for k in passwordRepo.keys():
            dummyDict = dummyDict + [k]
        dummyDict.sort()
        for entry in dummyDict:
            print (' - {}'.format(entry))
    if account == 'UPDATE':
        print ('What account would you want to update?')
        accountUpdate = input()
        if accountUpdate in passwordRepo:
            print ('Important note: The database cannot store old passwords.')
            newPassword = input ('Enter the new password: ')
            passwordRepo[accountUpdate] = newPassword
            print('Database updated.')
        else:
            print('That is not in the repository. Type "My Accounts" to see list of accounts stored here.')
            continue
    if account in passwordRepo:
        pyperclip.copy(passwordRepo[account])
        print('')
        print('Now, CTRL + V that sh*t.')
    if account == '':
        print('User aborted.')
        print('Quitting program.')
        print('...')
        time.sleep(3)
        sys.exit()
    if account not in passwordRepo and account != 'MY ACCOUNTS':
        print('That is not in the repository. Would you like to add it? Y/N')
        action = input()
        action = action.upper()
        while True:
            if action == 'Y':
                print('Enter the password for that account.')
                addpassword = input()
                passwordRepo[account] = addpassword
                print('Password has been added to your ' + account + ' account.')
                break
            if action == 'N':
                print('No action needed then.')
                break
            else:
                print('Type only either Y for yes or N for no. ')
                action = input()
                action = action.upper()
                continue

