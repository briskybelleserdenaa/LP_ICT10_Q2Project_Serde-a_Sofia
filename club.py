from pyscript import document

def candidate_checker(e):
    club_members = ["ranee de guzman" , "milli meneses" , "angelica del rosario" ,  "belle serdena"]
    f_name = document.getElementById('first_name').value
    l_name = document.getElementById('last_name').value
    candidate = f_name + ' ' + l_name 

    member_checker = candidate.lower() in club_members
    messages = (f'Sorry {candidate}, you are not a member of the club.', f'Congratulations {candidate}, you are a member of the club!')
    
    document.getElementById('result').innerHTML = messages[member_checker]
