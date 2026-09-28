#!/bin/bash
# usage: ./randomize_names.sh /path/to/folder

folder="$1"

if [ -z "$folder" ] || [ ! -d "$folder" ]; then
    echo "Usage: $0 <folder>"
    exit 1
fi

for file in "$folder"/*; do
    [ -f "$file" ] || continue   # skip directories

    ext="${file##*.}"
    base=$(basename -- "$file")

    # if there's no real extension, don't force one
    if [ "$ext" = "$base" ]; then
        newname="$(uuidgen | tr 'A-Z' 'a-z')"
    else
        newname="$(uuidgen | tr 'A-Z' 'a-z').$ext"
    fi

    mv -- "$file" "$folder/$newname"
done

echo "Done."
