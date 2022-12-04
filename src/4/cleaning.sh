contained=0
overlapping=0

while read line; do
    IFS=','; arrIN=($line); unset IFS;
    IFS='-'; fst=(${arrIN[0]}); snd=(${arrIN[1]}); unset IFS;
    
    if [[ ${fst[0]} -ge ${snd[0]} ]] && [[ ${fst[1]} -le ${snd[1]} ]]; then # fst in snd
      let "contained+=1"
      else
        if [[ ${snd[0]} -ge ${fst[0]} ]] && [[ ${snd[1]} -le ${fst[1]} ]]; then # snd in fst
          let "contained+=1"
        fi
    fi

    if [[ ${snd[0]} -le ${fst[1]} ]] && [[ ${fst[0]} -le ${snd[1]} ]]; then
      let "overlapping+=1"
    fi
done < in.txt

echo $contained
echo $overlapping