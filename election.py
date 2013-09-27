import csv, json, urllib2
f = urllib2.urlopen('ftp://User:Pass@ftp://election_ftp.calgary.ca/FILENAME.XXX', 'rU')
reader = csv.DictReader( f, fieldnames = ( "WARD", "ACCLAIMED", "INCUMBENT", "CANDIDATE_NAME", "TOTAL_VOTES", "LEADING_BY", "PERCENTAGE_OF_VOTES", "WARD_STATIONS_REPORTING", "TOTAL_WARD_STATIONS", "CITY_WIDE_STATIONS_REPORTING", "TOTAL_CITY_WIDE_STATIONS", "OFFICE_TYPE" ), delimiter='|')
out = json.dumps([ row for row in reader ])
with open('data.json', 'w') as outfile:
  outfile.write(out)