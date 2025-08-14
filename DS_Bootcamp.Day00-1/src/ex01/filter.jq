# filter.jq
["id", "created_at", "name", "has_test", "alternate_url"],
(.items[] | [(.id | tonumber), .created_at, .name, .has_test, .alternate_url])
| @csv