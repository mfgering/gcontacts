import argparse, csv, sys
import google_map, postbox_map

# name_map: name => name|fn
# postbox_contact: name => value
# postbox_order: name => col_num

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('google', help="Google contacts in csv file input")
	parser.add_argument('--postbox', help="Postbox csv file output")
	args = parser.parse_args()
	with open(args.google, newline='', encoding="utf-8") as google_csvfile:
		post_file = sys.stdout
		if args.postbox:
			post_file = open(args.postbox, "w", newline='', encoding="utf-8")
		#wrtr = csv.writer(post_file, delimiter=',', quotechar='"')
		wrtr = csv.DictWriter(post_file, postbox_map.postbox_fields,)
		wrtr.writeheader()
		rdr = csv.reader(google_csvfile, delimiter=',', quotechar='"')
		hdr = next(rdr)
		for row in rdr:
			print(", ".join(row))
			google_contact = {}
			for col_num in range(0, len(hdr)):
				google_contact[hdr[col_num]] = row[col_num]
			postbox_contact = google_map.handle_google_contact(google_contact)
			wrtr.writerow(postbox_contact)

if __name__ == '__main__':
	main()