
import win32com.client

def get_user_info(username):
    user_info = {}
    try:
        # Connect to the Active Directory
        ad = win32com.client.Dispatch('ADsNameSpaces')
        ldap = ad.GetObject('', 'LDAP:')
        conn = ldap.OpenDSObject(
            'LDAP://DC=herbertstanley,DC=com',  # Replace with your actual domain
            None,
            None,
            0
        )
        
        # Search for the user in Active Directory
        user = conn.GetObject('', f'LDAP://CN={username},OU=Users,DC=herbertstanley,DC=com')  # Adjust the path based on your AD structure
        user_info['username'] = username
        user_info['full_name'] = user.Get('displayName')
        user_info['email'] = user.Get('mail')
        user_info['department'] = user.Get('department')
    except Exception as e:
        print(f'Error retrieving user info: {e}')
    
    return user_info
