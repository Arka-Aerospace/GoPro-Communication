from open_gopro import WiredGoPro

import re

def group_check(s):
    # Regex pattern explained:
    # ^G : Starts with G
    # \d{3} : Exactly three digits (for group ID)
    # \d{4} : Exactly four digits (for group member ID)
    # \. : A literal dot (.)
    # JPG$ : Ends with JPG (for file extension)
    # (?P<name>...) : Creates a named group
    pattern = r"^G(?P<group_id>\d{3})(?P<member_id>\d{4})\.JPG$"

    match = re.match(pattern, s, re.IGNORECASE)

    if match is not None:
        return True, match.group('group_id'), match.group('member_id')
    else:
        return False, None, None

with WiredGoPro(None) as gopro:
    resp = gopro.http_command.get_media_list()
    # print(resp)
    for file in resp.data.get("files", []):
        name = file["n"]
        gopro.http_command.download_file(camera_file=name) 
        # check, group_id, first_member_id = group_check(name)
        # if not check or None in (group_id, first_member_id):
        #     continue
        # # print(name, group_id, first_member_id)
        # first_member_id = int(first_member_id)
        # last_member_id = int(file["l"])
        # print(file)
        # for member_id in range(first_member_id, last_member_id + 1):
        #     if str(member_id) in file["m"]:
        #         continue

        #     name = f"G{group_id}{member_id:04d}.JPG" 
        #     print(name)
        #     gopro.http_command.download_file(camera_file=name) 