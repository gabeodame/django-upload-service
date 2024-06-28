def get_user_info(remote_user):
    user_info = {}
    try:
        # Split domain and username
        domain, username = remote_user.split('\\')

        user_info['username'] = username
        user_info['full_name'] = username  # Since full name is not available from REMOTE_USER, use username as placeholder
        user_info['email'] = f'{username}@{domain}.com'  # Placeholder email construction
        user_info['department'] = 'Unknown'  # Placeholder, as department info is not available
    except Exception as e:
        print(f'Error retrieving user info: {e}')
    
    return user_info
