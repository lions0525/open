#! /bin/bash
echo -----------------------
echo User Name : Kim gue nam
echo Student Number : 12223700
echo \[ Menu ]
echo 1. Get the data of the movie identified by a specific \'movie id\' from \'u.item\'
echo 2. Get the data of \'action\' genre movies from \'u.item\'
echo 3. Get the average \'rating\' of the movie identified by specific \'movie id\' from \'u.data\'
echo 4. Delete the \'IMDb URL\' from \'u.item\'
echo 5. Get the data about users from \'u.user\'
echo 6. Modify the format of \'release date\' in \'u.iten\'
echo 7. Get the data of movies rated by a specific \'user id\' from \'u.data\'
echo 8. Get the average \'rating\' of movies rated by users with \'age\'between 20 and 29 and \'occupation\' as \'programmer\'
echo 9.exit
echo -----------------------
while true
do
	read -p "Enter your choice [1-9] " number
	
	
	case $number in
		1)
			echo""
			read -p "Please enter 'movie id' (1~1682) : " number1
			echo""
			awk -F '|' -v n="$number1" '$1==n {print $0}' "$1"
			
			echo ""
			;;
			


		2)	
			echo""
			read -p "Do you want to get the data of 'action' genre movies from 'u.item'? (y/n) : " number2
			if [ $number2 = "y" ]; then
			        echo""	
				awk -F '|' 'BEGIN{count=0}($7==1 && count<10) {print $1 " " $2;count++}' "$1" |sort -n  ;
			fi

			echo ""

			;;
			
		3)     
		       	echo""
		       	read -p "Please enter the 'movie id' (1~1682) : " number3
			echo""
			awk -F ' ' -v num3="$number3" 'BEGIN{ sum=0;line=0;} $2==num3 {sum+=$3;line++} END{average=sum/line; printf("average rating of %d : %.5f\n",num3,average)}' "$2";
			
			echo ""

			;;
			


		4)	
			echo""
			read -p "Do you want to delete the 'IMDb URL' from 'u.item'? (y/n) : " number4
			echo""
			if [ $number4 = "y" ];then
				sed -n '1,10p' "$1" | sed 's/http:\/\/[^|]*//g' 
			fi
			
			echo ""

			;;
			


		5)	
			echo""
			read -p "Do you want to get the data about users from 'u.user'? (y/n) : " number5
			echo""
			if [ $number5 = "y" ];then
				sed -n '1,10p' "$3" | sed  's/\([0-9]*\)|\([0-9]*\)|\([M|F]\)|\([a-zA-Z]*\)|\([0-9]*\)/user \1 is \2 years old \3 \4/' | sed  's/M/male/g' | sed  's/F/female/g' 
			fi

			echo ""

			;;

		

		6)	
			echo""
			read -p "Do you want to Modify the format of 'release data' in 'u.item'? (y/n) : " number6
			echo""
			if [ $number6 = "y" ];then
				sed -e 's/\([0-9]\{2\}\)-\([a-zA-Z]\{3\}\)-\([0-9]\{4\}\)/\3\2\1/' "$1" | tail -n 10 | sed 's/Jan/01/g; s/Feb/02/g; s/Mar/03/g; s/Apr/04/g; s/May/05/g; s/Jun/06/g; s/Jul/07/g; s/Aug/08/g; s/Sep/09/g; s/Oct/10/g; s/Nov/11/g; s/Dec/12/g'
				
			fi
			echo ""
			
			;;


		7)	
			echo""
			read -p "Please enter the 'user id' (1~943) : " number7
			echo
			read a<<<$(awk -F ' ' -v id=$number7 '($1==id) {print $2 " | " ;}' "$2"  |sort -n|tr -d '\n')
			echo $a
			echo ""
			IFS='|' read -ra Arr<<<"$a"
			count=0;
			for val in "${Arr[@]}";do
				awk -v id="$val" -F '|' '$1 == id {print $1 "|" $2}' "$1"
				((count++));
				if [[ $count == 10 ]];then
					break;
				fi
			done
			echo ""	
		
			;;


		8) 	
			echo""
			read -p "Do you want to get the average 'rating' of movies rated by users with 'age' between 20 and 29 and 'occupation' as 'programmer'?(y/n) : " number8
			echo""
			read a<<<$(awk -F ' ' '{print $1 "|" $2 "|" $3}' "$2"|sort -n)
			userArray=()
			userArray=( $(echo "$a"|awk -F '|' '($2<30 && $2>19 && $4 == "programmer"){print $1}' "$3"))
			arrayString=$(IFS=" "; echo "${userArray[*]}")
			
			awk -v external="$arrayString" '
			BEGIN{
			split(external, inarr, " ");
			}
			{
				for( i in inarr){
					if(inarr[i]==$1){	
						ratarr[$2]+=$3;
						perarr[$2]++;
						}
					}
			}
			END {
				for (i in ratarr){
				        result = ratarr[i] / perarr[i];
   					 if (result == int(result)) {
       						 printf("%s %d\n", i, result);
   					 } else {
       					 printf("%s %.5f\n", i, result);
   					 }	
				}
			}	' "$2" |sort -n|awk '{printf "%s %s\n",$1,$2+0}'
			echo ""
			;;

		
		9)echo Bye!;break;;
	esac
done
