# Mapping for Google contact info

def google_map_name(name, google_contact, postbox_contact):
	postbox_contact['Display Name'] = google_contact['Name']
	postbox_contact['First Name'] = google_contact['Given Name']
	postbox_contact['Last Name'] = google_contact['Family Name']

def google_outlook_map_birthday(name, google_contact, postbox_contact):
	if google_contact[name]:
		parts = google_contact[name].split('/')
		if len(parts) >= 1:
			postbox_contact['Birth Month'] = parts[0]
			if len(parts) >= 2:
				postbox_contact['Birth Day'] = parts[1]
				if len(parts) >= 3:
					postbox_contact['Birth Year'] = parts[2]

# This map is for the Google export to Google format
google_google2postbox_map = {
	'Name': google_map_name,
	'Given Name': None,
	'Additional Name': None,
	'Family Name': None,
	'Yomi Name': None,
	'Given Name Yomi': None,
	'Additional Name Yomi': None,
	'Family Name Yomi': None,
	'Name Prefix': None,
	'Name Suffix': None,
	'Initials': None,
	'Nickname': None,
	'Short Name': None,
	'Maiden Name': None,
	'Birthday': google_outlook_map_birthday,
	'Gender': None,
	'Location': None,
	'Billing Information': None,
	'Directory Server': None,
	'Mileage': None,
	'Occupation': None,
	'Hobby': None,
	'Sensitivity': None,
	'Priority': None,
	'Subject': None,
	'Notes': 'Notes',
	'Language': None,
	'Photo': None,
	'Group Membership': None,
	'E-mail 1 - Type': None,
	'E-mail 1 - Value': 'Primary Email',
	'Phone 1 - Type': None,
	'Phone 1 - Value': None,
	'Phone 2 - Type': None,
	'Phone 2 - Value': None,
	'Address 1 - Type': None,
	'Address 1 - Formatted': None,
	'Address 1 - Street': None,
	'Address 1 - City': None,
	'Address 1 - PO Box': None,
	'Address 1 - Region': None,
	'Address 1 - Postal Code': None,
	'Address 1 - Country': None,
	'Address 1 - Extended Address': None,
	'Address 2 - Type': None,
	'Address 2 - Formatted': None,
	'Address 2 - Street': None,
	'Address 2 - City': None,
	'Address 2 - PO Box': None,
	'Address 2 - Region': None,
	'Address 2 - Postal Code': None,
	'Address 2 - Country': None,
	'Address 2 - Extended Address': None,
	'Organization 1 - Type': None,
	'Organization 1 - Name': None,
	'Organization 1 - Yomi Name': None,
	'Organization 1 - Title': None,
	'Organization 1 - Department': None,
	'Organization 1 - Symbol': None,
	'Organization 1 - Location': None,
	'Organization 1 - Job Description': None,
}

def outlook_map_name(name, google_contact, postbox_contact):
	first_name = google_contact['First Name']
	if google_contact['Middle Name']:
		first_name += ' '+google_contact['Middle Name']
	postbox_contact['Display Name'] = first_name+' '+google_contact['Last Name']
	postbox_contact['First Name'] = first_name
	postbox_contact['Last Name'] = google_contact['Last Name']

def outlook_map_primary_phone(name, google_contact, postbox_contact):
	if google_contact[name]:
		postbox_contact['Home Phone'] = google_contact[name]
	if google_contact['Home Phone']:
		postbox_contact['Home Phone'] = google_contact['Home Phone']

# This map is for the Google export to Outlook format
google_outlook2postbox_map = {
	'First Name': outlook_map_name,
	'Middle Name': None,
	'Last Name': None,
	'Title': None,
	'Suffix': None,
	'Initials': None,
	'Web Page': 'Web Page 1',
	'Gender': None,
	'Birthday': google_outlook_map_birthday,
	'Anniversary': None,
	'Location': None,
	'Language': None,
	'Internet Free Busy': None,
	'Notes': 'Notes',
	'E-mail Address': 'Primary Email',
	'E-mail 2 Address': 'Secondary Email',
	'E-mail 3 Address': None,
	'Primary Phone': outlook_map_primary_phone,
	'Home Phone': None,
	'Home Phone 2': None,
	'Mobile Phone': 'Mobile Number',
	'Pager': None,
	'Home Fax': 'Fax Number',
	'Home Address': 'Home Address',
	'Home Street': None,
	'Home Street 2': 'Home Address 2',
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
	'Business Address': 'Work Address',
	'Business Street': None,
	'Business Street 2': 'Work Address 2',
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
	'Name': None,
	'Given Name': None,
	'Additional Name': None,
	'Family Name': None,
	'Yomi Name': None,
	'Given Name Yomi': None,
	'Additional Name Yomi': None,
	'Family Name Yomi': None,
	'Name Prefix': None,
	'Name Suffix': None,
	'Initials': None,
	'Nickname': None,
	'Short Name': None,
	'Maiden Name': None,
	'Birthday': None,
	'Gender': None,
	'Location': None,
	'Billing Information': None,
	'Directory Server': None,
	'Mileage': None,
	'Occupation': None,
	'Hobby': None,
	'Sensitivity': None,
	'Priority': None,
	'Subject': None,
	'Notes': None,
	'Language': None,
	'Photo': None,
	'Group Membership': None,
	'E-mail 1 - Type': None,
	'E-mail 1 - Value': None,
	'E-mail 2 - Type': None,
	'E-mail 2 - Value': None,
	'E-mail 3 - Type': None,
	'E-mail 3 - Value': None,
	'E-mail 4 - Type': None,
	'E-mail 4 - Value': None,
	'Phone 1 - Type': None,
	'Phone 1 - Value': None,
	'Phone 2 - Type': None,
	'Phone 2 - Value': None,
	'Phone 3 - Type': None,
	'Phone 3 - Value': None,
	'Address 1 - Type': None,
	'Address 1 - Formatted': None,
	'Address 1 - Street': None,
	'Address 1 - City': None,
	'Address 1 - PO Box': None,
	'Address 1 - Region': None,
	'Address 1 - Postal Code': None,
	'Address 1 - Country': None,
	'Address 1 - Extended Address': None,
	'Address 2 - Type': None,
	'Address 2 - Formatted': None,
	'Address 2 - Street': None,
	'Address 2 - City': None,
	'Address 2 - PO Box': None,
	'Address 2 - Region': None,
	'Address 2 - Postal Code': None,
	'Address 2 - Country': None,
	'Address 2 - Extended Address': None,
	'Address 3 - Type': None,
	'Address 3 - Formatted': None,
	'Address 3 - Street': None,
	'Address 3 - City': None,
	'Address 3 - PO Box': None,
	'Address 3 - Region': None,
	'Address 3 - Postal Code': None,
	'Address 3 - Country': None,
	'Address 3 - Extended Address': None,
	'Organization 1 - Type': None,
	'Organization 1 - Name': None,
	'Organization 1 - Yomi Name': None,
	'Organization 1 - Title': None,
	'Organization 1 - Department': None,
	'Organization 1 - Symbol': None,
	'Organization 1 - Location': None,
	'Organization 1 - Job Description': None,
	'Website 1 - Type': None,
	'Website 1 - Value': None,
	'Custom Field 1 - Type': None,
	'Custom Field 1 - Value': None,
def handle_google_field(csv_format, google_field_name, google_contact, postbox_contact):
	if csv_format == 'google':
		google_map = google_google2postbox_map
	else:
		google_map = google_outlook2postbox_map
	if not google_field_name in google_map:
		print("Error: missing mapping for "+google_field_name)
		return
	target = google_map[google_field_name]
	if target is not None:
		if callable(target):
			target(google_field_name, google_contact, postbox_contact)
		elif(type(target) == str):
			postbox_contact[target] = google_contact[google_field_name]
		else:
			print("FAIL")

def handle_google_contact(csv_format, google_contact):
	postbox_contact = {}
	for field_name in google_contact:
		handle_google_field(csv_format, field_name, google_contact, postbox_contact)
	return postbox_contact