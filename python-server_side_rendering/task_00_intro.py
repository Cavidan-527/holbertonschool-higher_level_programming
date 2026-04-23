import os

def generate_invitations(template, attendees):
    # 1. Giriş tiplərinin yoxlanılması
    if not isinstance(template, str):
        print("Error: Template is not a string.")
        return
        
    if not isinstance(attendees, list) or not all(isinstance(item, dict) for item in attendees):
        print("Error: Attendees is not a list of dictionaries.")
        return

    # 2. Boş girişlərin yoxlanılması
    if template.strip() == "":
        print("Template is empty, no output files generated.")
        return
        
    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return

    # 3. İştirakçı siyahısını dövrə salıb faylları yaratmaq
    for index, attendee in enumerate(attendees, start=1):
        invitation = template
        placeholders = ["name", "event_title", "event_date", "event_location"]
        
        for key in placeholders:
            # Əgər məlumat yoxdursa və ya None-dırsa, "N/A" yazırıq
            value = attendee.get(key)
            if value is None:
                value = "N/A"
                
            # Şablondakı dəyərləri əvəzləyirik
            invitation = invitation.replace(f"{{{key}}}", str(value))
            
        # 4. Faylı yaratmaq və yazmaq
        file_name = f"output_{index}.txt"
        try:
            with open(file_name, 'w', encoding='utf-8') as file:
                file.write(invitation)
        except Exception as e:
            print(f"Error writing to {file_name}: {e}")
