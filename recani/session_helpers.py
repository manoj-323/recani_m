# session_helpers.py

def initialize_user_history(session, show1, show2, show3, show1_rating, show2_rating, show3_rating):
    if 'user_history_dict' not in session:
        session['round_no'] = 1
        session['previos_arm'] = 0
        session['user_history_dict'] = {
            'already_recommended': [],
            'arm1': {'anime': [], 'rating': [], 't': 1},
            'arm2': {'anime': [], 'rating': [], 't': 1},
            'arm3': {'anime': [], 'rating': [], 't': 1}
        }
        user_history_dict = session['user_history_dict']
        user_history_dict['arm1']['anime'].append(show1)
        user_history_dict['arm2']['anime'].append(show2)
        user_history_dict['arm3']['anime'].append(show3)
        user_history_dict['arm1']['rating'].append(show1_rating)
        user_history_dict['arm2']['rating'].append(show2_rating)
        user_history_dict['arm3']['rating'].append(show3_rating)
        user_history_dict['already_recommended'].extend([show1, show2, show3])

        session['user_history_dict'] = user_history_dict
        print(user_history_dict)
        print('--------------------session created----------------')

def update_user_history(session, show1_rating, show2_rating, show3_rating):
    user_history_dict = session['user_history_dict']
    arm = session['previous_arm']
    user_history_dict[f'arm{arm}']['rating'].extend([show1_rating, show2_rating, show3_rating])

    session['user_history_dict'] = user_history_dict
    print(user_history_dict)
