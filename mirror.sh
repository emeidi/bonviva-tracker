#!/bin/sh

WGET=$(which wget)

URLBASE="https://rewards.credit-suisse.com/cs/rewards/p/d/commodityRewardDetails.do?source=SP&menuId=n0&id="

IDSTART=1
#IDSTART=4253
IDEND=9999
#IDEND=4254
#IDEND=10

DATE=$(date +"%Y-%m-%d")

ID=4253
URL="$URLBASE$ID"
COOKIEFILE="./cookies-$DATE.txt"
CMD="$WGET --header=\"Accept-Language: de\" --keep-session-cookies --save-cookies $COOKIEFILE -O \"test.html\" \"$URL\""
echo $CMD
eval $CMD

SEQUENCE=$(seq $IDSTART $IDEND)
for I in $SEQUENCE
do
    #echo $i
    
    URL="$URLBASE$I"
    #echo $URL
    
    IREADABLE=$(printf %04d $I)
    
    FOLDER="./cache/$IREADABLE"
    OUTPUTFILE="$FOLDER/$DATE.html"
    
    if [ ! -d $FOLDER ]
    then
        #mkdir "$FOLDER"
        CMD="mkdir -p \"$FOLDER\""
        echo $CMD
        eval $CMD
    fi
    
    CMD="$WGET --header=\"Accept-Language: de\" --load-cookies $COOKIEFILE --referer=\"https://rewards.credit-suisse.com/cs/rewards/p/d/newRewards.do?menuId=n02\" -O \"$OUTPUTFILE\" \"$URL\""
    echo $CMD
    eval $CMD
done

exit 0