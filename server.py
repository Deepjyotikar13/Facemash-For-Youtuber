from flask import Flask,render_template,request, jsonify,make_response
from flask_sqlalchemy import SQLAlchemy
from json import load,dump
import os
from time import ctime
from datetime import datetime
from give_match_of_a_player import give_match_of_a_player_by_ind #using the "give_match_of_a_player_by_ind" function i can get a particular player index and its match
from random import randint
from ranking_algorithm import Expected_probability_win
main_path="/storage/emulated/0/BestYoutuberELO/"

new_yt_not_chacked=True
app=Flask(__name__)
def find_the_highest_time(new_yt_added=1):
	yt_photo_path=main_path+"static/Photos_of_Youtubers/"
	all_time_arr=[]
	all_files_list_in_dir=os.listdir(yt_photo_path)#contains all the photo name of the youtubers
	new_added_yt_names=[]
	for file_name in all_files_list_in_dir:
			time_str=get_time_file_added(yt_photo_path+file_name)
			time=datetime.strptime(time_str, "%a %b %d %H:%M:%S %Y")
			all_time_arr.append(time)
			
	for _ in range(0,new_yt_added):
		highest_time=max(all_time_arr)#so using this i will find the latest file added in the directory 
		ind=all_time_arr.index(highest_time)#finding the index of the time
		yt_name_path=all_files_list_in_dir[ind]#and finally name of the yt_photo using the index
		new_added_yt_names.append(yt_name_path)
		all_files_list_in_dir.remove(yt_name_path)#removing the yt photo name that is newly added 
		all_time_arr.remove(highest_time) #also removing the newly added yt photo time time so that it will notbe thenewly added photo in the dir
		
	return new_added_yt_names
def get_time_file_added(path):
	"""will return the date when the file was added"""
	created_time=os.path.getctime(path)
	time_creation=ctime(created_time)
	return time_creation
def read_a_file(file_name):
	"""this will open a file and depending on that file what it is string or number list etc you can use as it is """
	path=main_path+file_name
	with open(path,"r") as total_player:
		total_player_num=load(total_player)
	return total_player_num

def modify_a_file(file_name,data_to_put):
	"""using this function i will modify the files"""
	path=main_path+file_name
	with open(path,"w") as file_data:
		dump(data_to_put,file_data)
yt_name_db=read_a_file("All_Youtubers_name.py")#this is the array of names of youtubers
name_and_score_dic=read_a_file("name_and_score_db.py")# this is nane ans score db

def check_if_new_yt_added():
	"""this check if a new youtuber his photo was aded or notif added then it will add the all nessasary detail of the youtuber in the database"""
	total_yt=read_a_file("total_num_of_player.py")
	photos_path=main_path+"static/Photos_of_Youtubers/"
	total_yt_photos_in_dir=len(os.listdir(photos_path))
	if total_yt_photos_in_dir>total_yt:
		newly_added_yt_num=total_yt_photos_in_dir-total_yt #this will give you the number of newly added youtubers  so it subtracts the actuall number of youtubers in the directory from previous number of youtubers
		print(newly_added_yt_num,"youtubers where added")
		newly_added_youtubers=find_the_highest_time(newly_added_yt_num)
		yt_name_score_db=read_a_file("name_and_score_db.py")
		index_of_yt=total_yt #so the index for the frist newly added youtuber will be the length of the previous youtubers list 
		for ind,name in enumerate(newly_added_youtubers):
			print(name)
			#updating all youtubers index and total match played by the array of array
			now_total_num_yt=total_yt+newly_added_yt_num #now i am adding the previous number of yputuber with the total number of newly addedyoutuber
			modify_a_file("total_num_of_player.py",now_total_num_yt)#using this functioni will modify the file
			#updating all youtubers name array db
			yt_name_db.append(name)
			modify_a_file("All_Youtubers_name.py",yt_name_db)
			#updating the name and score db
			yt_name_score_db[name]=1200
			modify_a_file("name_and_score_db.py",yt_name_score_db)
			#updating player index and total match played by the player
			yt_name_total_match=read_a_file("player_ind_with_total_game.py")
			yt_name_total_match.append([index_of_yt,0])
			modify_a_file("player_ind_with_total_game.py",yt_name_total_match)
			index_of_yt+=1
	else:
		print("no New youtuber where added")
		

def update_player_total_match(player_index):
	""""it will basically update the file and at what _to_update it will be which file i want to update ither the "name_and_score in short NS" or the "player_total_match in short ptml"""
	player_ind_t_match=main_path+"player_ind_with_total_game.py"
	player_and_t_match=read_a_file("player_ind_with_total_game.py")
	player_and_t_match[player_index][1]+=1#now i am updating the total match of that player by 1 because he had played the match
	with open(player_ind_t_match,"w") as old_player_score_tmatch:
		#now i will write the updated data into my file and then it will change that spacific thing
		dump(player_and_t_match,old_player_score_tmatch)#now it will update the list of list based on which is changed
	

def update_score_of_player(player_key,player_score):
	"""player_key is the key of the player name from which you will acess it and change the score and player score is the updated score of my player"""
	name_score_path=main_path+"name_and_score_db.py"
	player_score_and_match=read_a_file("name_and_score_db.py")
	player_score_and_match[player_key]=player_score #player_score_and_match is a dictionary which stores the there name and its score and using a spacific key i and updating it
	with open(name_score_path,"w") as update_names_with_score:
			dump(player_score_and_match,update_names_with_score)#so here i am updating the score of my player
			
			
def give_match():
	yt_ind_t_match_arr=read_a_file("player_ind_with_total_game.py")
	total_yt=read_a_file("total_num_of_player.py")
	while True:
		random_player_ind=randint(0,total_yt-1) #this will genarate a random index of player from 0 to total_youtuber-2 because total youtuber will be total length of youtubers -2 because by doing-1 it will give me the last index amd by another -1 to give the 2nd last player cause the last player wpuldent have amy match
		player_ind_t_match=yt_ind_t_match_arr[random_player_ind] #cosding the list of list player index and its total match
		remeaning_match=len(yt_ind_t_match_arr[random_player_ind+1:total_yt])-player_ind_t_match[1] #remeaning matches of the player 
		if remeaning_match==0:
			pass
		else:
			two_player_ind=give_match_of_a_player_by_ind(yt_ind_t_match_arr,player_ind_t_match)#so this will return index of the 2 players that will have a match 
			print(two_player_ind,player_ind_t_match,"remaning matches",remeaning_match)
			return two_player_ind
			break
@app.route('/image_clicked', methods=['POST'])
def image_clicked():
    data = request.get_json()
    message = data.get('message')
    won_img_name=data.get("win_img_name")
    lost_img_name=data.get("lost_img_name")
    yt_ind_at_left=data.get("left_player_ind")#this the player index of left side
    yt_ind_at_right=data.get("right_player_ind")#this is the player index who is at right side
    player_ind_to_increment=data.get("player_ind_to_add_total_match")
    if message=="Lefttimg":
    	left_yt_won_current_score=name_and_score_dic[won_img_name]#this will be the score of youtuber at left side and it has won cause the user clicked on him
    	right_yt_loss_current_score=name_and_score_dic[lost_img_name]#this is the youtuber that has lost and this is his score
    	left_won_yt_new_score=Expected_probability_win(right_yt_loss_current_score,left_yt_won_current_score,1) #this will give methe current score of left youtuber who has won
    	right_loss_yt_new_score=Expected_probability_win(left_yt_won_current_score,right_yt_loss_current_score,0)#this will give me thescore of player at right who has lost
    	update_score_of_player(won_img_name,left_won_yt_new_score[1])#updating the score of left player
    	update_player_total_match(int(player_ind_to_increment))
    	update_score_of_player(lost_img_name,right_loss_yt_new_score[1])#udating score of right side player
    	print(f" so {message} is clicked and {won_img_name} has won and index is {yt_ind_at_left} new score {left_won_yt_new_score}. {lost_img_name} has lost index is {yt_ind_at_right} now current score {right_loss_yt_new_score}")
    	return make_response('', 204)
    elif message=="Rightimg":
    	right_yt_won_current_score=name_and_score_dic[won_img_name] #current score of player at right who has won
    	left_yt_loss_current_score=name_and_score_dic[lost_img_name] #current score of player at left who has lost
    	right_won_yt_new_score=Expected_probability_win(left_yt_loss_current_score,right_yt_won_current_score,1) #this will give methe current score of right side youtuber who has won
    	left_loss_yt_new_score=Expected_probability_win(right_yt_won_current_score,left_yt_loss_current_score,0)#this will give me thescore of player at right who has lost
    	update_score_of_player(won_img_name,right_won_yt_new_score[1])#updating score of player at right
    	update_player_total_match(int(player_ind_to_increment))
    	update_score_of_player(lost_img_name,left_loss_yt_new_score[1])#updating player score at left
    	print(f" so {message} is clicked and {won_img_name} has won index is {yt_ind_at_right} new score {right_won_yt_new_score}. {lost_img_name} has lost index is {yt_ind_at_left} 0now current score {left_loss_yt_new_score}")
    	return make_response('', 204)
    else:
    	return jsonify(success=True)

@app.route("/")
def browser_search_page():
	two_player_ind=give_match()
	player_img_at_left=yt_name_db[two_player_ind[0]]#this is the youtuber imgae who will be placed at the left side
	player_img_at_right=yt_name_db[two_player_ind[1]]#this is the youtuber image who will be palced at the right side
	left_yt_name=player_img_at_left.split(".")[0]# this is the youtubers whowill be placed at the left side
	right_yt_name=player_img_at_right.split(".")[0] #this is the name of the youtubers who will be placed at the right side 
	youtuber_name_and_img_url=[[player_img_at_left,left_yt_name],[player_img_at_right,right_yt_name],two_player_ind[0],two_player_ind[1],two_player_ind[0]]#so the two_player_ind[0] is main player whso match is 
	
	return render_template("index.html",yt_name_and_url=youtuber_name_and_img_url)
@app.route("/top")
def top_ranking_performer():
	#dic={'A': 8, 'B': 15, 'C': 3, 'D': 12, 'E': 5, 'F': 18, 'G': 7, 'H': 10, 'I': 2, 'J': 34}
	total_ind=read_a_file("total_num_of_player.py")
	name= [key for key, value in sorted(name_and_score_dic.items(), key=lambda item: item[1], reverse=True)]
	#print(name)
	return render_template("TopRanks.html",name_score=name,total_ind=total_ind)
	
if __name__=="__main__":
	if new_yt_not_chacked:
		check_if_new_yt_added()
		print("checking Done!")
		new_yt_not_chacked=False
	app.run(port=8000)