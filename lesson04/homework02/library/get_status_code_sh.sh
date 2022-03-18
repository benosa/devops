#!/bin/bash
# WANT_JSON

regex='^(https?|ftp|file)://[-A-Za-z0-9\+&@#/%?=~_|!:,.;]*[-A-Za-z0-9\+&@#/%=~_|]\.[-A-Za-z0-9\+&@#/%?=~_|!:,.;]*[-A-Za-z0-9\+&@#/%=~_|]$'

url=$(cat $1 | grep -Po '(?<="url": ")(.*?)(?=")')
result_string=0

if [[ $url =~ $regex ]]
then
    # result_string=$(curl -s -L --head "$url" | grep -oP "(?<=HTTP/[1-3].[0-9] )\d{3}" | tail -1 | tr '\n' '\0')
    result_string=$(curl -LI "$url" -o /dev/null -w '%{http_code}\n' -s)
    if [[ $result_string != 200 ]]
    then
        echo "{\"result_str\": $(($result_string + 0)), \"msg\": \"Not valid status code\", \"rc\": 1, \"failed\": true }"
    else
        echo "{\"result_str\": $result_string, \"msg\": \"Status code is valid\", \"rc\": 0, \"failed\": false }"
    fi
else
    echo "{\"result_str\": 0, \"msg\": \"Url is not valid: $url\", \"rc\": 1, \"failed\": true }"
fi
