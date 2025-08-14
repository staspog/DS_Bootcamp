#!/bin/sh

# curl -k -H 'User-Agent: school_21_bootcamp_day_1' 'https://api.hh.ru/vacancies' > hh_temp.json
# jq '.' hh_temp.json > hh.json
# rm hh_temp.json

curl -Gs "https://api.hh.ru/vacancies" \
    --data-urlencode 'search_field=name' \
    --data-urlencode "text='$*'" \
    -d "per_page=20" \
    -H 'User-Agent: school_21_bootcamp_day_1' \
    > hh_temp.json

jq '.' hh_temp.json > hh.json
rm hh_temp.json