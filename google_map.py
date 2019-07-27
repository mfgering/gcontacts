# Mapping for Google contact info

def map_name(name, google_contact, postbox_contact):
  first_name = google_contact['First Name']
  if google_contact['Middle Name']:
    first_name += google_contact['Middle Name']
  postbox_contact['First Name'] = first_name
  postbox_contact['Last Name'] = google_contact['Last Name']

def map_birthday(name, google_contact, postbox_contact):
  if google_contact[name]:
    parts = google_contact[name].split('/')
    if len(parts) >= 1:
      postbox_contact['Birth Month'] = parts[0]
      if len(parts) >= 2:
        postbox_contact['Birth Day'] = parts[1]
        if len(parts) >= 3:
          postbox_contact['Birth Year'] = parts[2]

def map_primary_phone(name, google_contact, postbox_contact):
  if google_contact[name]:
    postbox_contact['Home Phone'] = google_contact[name]
  if google_contact['Home Phone']:
    postbox_contact['Home Phone'] = google_contact['Home Phone']

def map_home_address(name, google_contact, postbox_contact):
  print("field {} is missing".format(name))

def map_business_address(name, google_contact, postbox_contact):
  print("field {} is missing".format(name))


google2postbox_map = {
  'First Name': map_name,
  'Middle Name': None,
  'Last Name': None,
  'Title': None,
  'Suffix': None,
  'Initials': None,
  'Web Page': 'Web Page 1',
  'Gender': None,
  'Birthday': map_birthday,
  'Anniversary': None,
  'Location': None,
  'Language': None,
  'Internet Free Busy': None,
  'Notes': 'Notes',
  'E-mail Address': 'Primary Email',
  'E-mail 2 Address': 'Secondary Email',
  'E-mail 3 Address': None,
  'Primary Phone': map_primary_phone,
  'Home Phone': None,
  'Home Phone 2': None,
  'Mobile Phone': 'Mobile Number',
  'Pager': None,
  'Home Fax': 'Fax Number',
  'Home Address': map_home_address,
  'Home Street': None,
  'Home Street 2': None,
  'Home Street 3': None,
  'Home Address PO Box': None,
  'Home City': 'Home City',
  'Home State': 'Home State',
  'Home Postal Code': 'Home ZipCode',
  'Home Country': 'Home Country',
  'Spouse': None,
  'Children': None,
  'Manager\'s Name': None,
  'Assistant\'s Name': None,
  'Referred By': None,
  'Company Main Phone': None,
  'Business Phone': 'Work Phone',
  'Business Phone 2': None,
  'Business Fax': None,
  'Assistant\'s Phone': None,
  'Company': None,
  'Job Title': 'Job Title',
  'Department': 'Department',
  'Office Location': None,
  'Organizational ID Number': None,
  'Profession': None,
  'Account': None,
  'Business Address': map_business_address,
  'Business Street': None,
  'Business Street 2': None,
  'Business Street 3': None,
  'Business Address PO Box': None,
  'Business City': 'Work City',
  'Business State': 'Work State',
  'Business Postal Code': 'Work ZipCode',
  'Business Country': 'Work Country',
  'Other Phone': None,
  'Other Fax': None,
  'Other Address': None,
  'Other Street': None,
  'Other Street 2': None,
  'Other Street 3': None,
  'Other Address PO Box': None,
  'Other City': None,
  'Other State': None,
  'Other Postal Code': None,
  'Other Country': None,
  'Callback': None,
  'Car Phone': None,
  'ISDN': None,
  'Radio Phone': None,
  'TTY/TDD Phone': None,
  'Telex': None,
  'User 1': None,
  'User 2': None,
  'User 3': None,
  'User 4': None,
  'Keywords': None,
  'Mileage': None,
  'Hobby': None,
  'Billing Information': None,
  'Directory Server': None,
  'Sensitivity': None,
  'Priority': None,
  'Private': None,
  'Categories': None,
  }

def handle_google_field(google_field_name, google_contact, postbox_contact):
  if not google_field_name in google2postbox_map:
    print("Error: missing mapping for "+google_field_name)
    return
  target = google2postbox_map[google_field_name]
  if target is not None:
    if callable(target):
      target(google_field_name, google_contact, postbox_contact)
    elif(type(target) == str):
      postbox_contact[target] = google_contact[google_field_name]
    else:
      print("FAIL")

def handle_google_contact(google_contact):
  postbox_contact = {}
  for field_name in google_contact:
    handle_google_field(field_name, google_contact, postbox_contact)
  return postbox_contact